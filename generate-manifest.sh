#!/bin/sh
set -eu
# Generate manifest.json from packages/*/.meta files
# Usage: sh generate-manifest.sh
#   Always overwrites manifest.json

OUTPUT="manifest.json"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# --- helpers ---

csv_to_json_array() {
    val="$1"
    if [ -z "$val" ]; then
        printf '[]'
        return
    fi
    result='['
    first=true
    oldifs="$IFS"
    IFS=','
    for item in $val; do
        item="$(printf '%s' "$item" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
        [ -z "$item" ] && continue
        if $first; then first=false; else result="$result, "; fi
        result="$result\"$item\""
    done
    IFS="$oldifs"
    result="$result]"
    printf '%s' "$result"
}

json_escape() {
    printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'
}

# --- write header ---
{
    printf '{\n'
    printf '  "schema_version": "1",\n'
    printf '  "repo": {\n'
    printf '    "id": "ZenLabs",\n'
    printf '    "name": "ZenLabs",\n'
    printf '    "url": "https://xzenlabs.github.io/repo/",\n'
    printf '    "icon_url": "https://xzenlabs.github.io/repo/favicon.svg"\n'
    printf '  },\n'
    printf '  "packages": [\n'
} > "$OUTPUT"

# --- collect .meta files ---
meta_files="$(find packages -name '.meta' | sort)"
count=$(printf '%s\n' "$meta_files" | wc -l | tr -d ' ')

i=0
for meta_file in $meta_files; do
    i=$((i + 1))

    # Parse .meta into temp file (filter comments/blank lines)
    tmp="$(mktemp)"
    while IFS= read -r line; do
        case "$line" in
            ''|\#*) continue ;;
        esac
        case "$line" in
            *=*) printf '%s\n' "$line" >> "$tmp" ;;
        esac
    done < "$meta_file"

    # Read fields (cut preserves everything after first =, handles = in URLs)
    id=$(grep '^id=' "$tmp" 2>/dev/null | sed 's/^id=//' | head -1)
    name=$(grep '^name=' "$tmp" 2>/dev/null | sed 's/^name=//' | head -1)
    version=$(grep '^version=' "$tmp" 2>/dev/null | sed 's/^version=//' | head -1)
    description=$(grep '^description=' "$tmp" 2>/dev/null | sed 's/^description=//' | head -1)
    author=$(grep '^author=' "$tmp" 2>/dev/null | sed 's/^author=//' | head -1)
    category=$(grep '^category=' "$tmp" 2>/dev/null | sed 's/^category=//' | head -1)
    platforms=$(grep '^platforms=' "$tmp" 2>/dev/null | sed 's/^platforms=//' | head -1)
    dependencies=$(grep '^dependencies=' "$tmp" 2>/dev/null | sed 's/^dependencies=//' | head -1)
    install_url=$(grep '^install_url=' "$tmp" 2>/dev/null | sed 's/^install_url=//' | head -1)
    uninstall_url=$(grep '^uninstall_url=' "$tmp" 2>/dev/null | sed 's/^uninstall_url=//' | head -1)
    size=$(grep '^size=' "$tmp" 2>/dev/null | sed 's/^size=//' | head -1)
    featured=$(grep '^featured=' "$tmp" 2>/dev/null | sed 's/^featured=//' | head -1)
    icon_url=$(grep '^icon_url=' "$tmp" 2>/dev/null | sed 's/^icon_url=//' | head -1)
    featured_image=$(grep '^featured_image=' "$tmp" 2>/dev/null | sed 's/^featured_image=//' | head -1)
    source=$(grep '^source=' "$tmp" 2>/dev/null | sed 's/^source=//' | head -1)
    source_asset=$(grep '^source_asset=' "$tmp" 2>/dev/null | sed 's/^source_asset=//' | head -1)

    case "$category" in
        utility|games|productivity|media) ;;
        *)
            echo "Invalid or missing category in $meta_file: $category" >&2
            rm -f "$tmp"
            exit 1
            ;;
    esac

    # Build package JSON
    {
        printf '    {\n'
        printf '      "id": "%s",\n' "$(json_escape "$id")"
        printf '      "name": "%s",\n' "$(json_escape "$name")"
        printf '      "version": "%s",\n' "$(json_escape "$version")"
        printf '      "description": "%s",\n' "$(json_escape "$description")"
        printf '      "author": "%s",\n' "$(json_escape "$author")"
        printf '      "category": "%s",\n' "$(json_escape "$category")"
        printf '      "platforms": %s,\n' "$(csv_to_json_array "$platforms")"
        printf '      "dependencies": %s' "$(csv_to_json_array "$dependencies")"
    } >> "$OUTPUT"

    # Optional string fields
    [ -n "$install_url" ]    && printf ',\n      "install_url": "%s"' "$(json_escape "$install_url")" >> "$OUTPUT"
    [ -n "$uninstall_url" ]  && printf ',\n      "uninstall_url": "%s"' "$(json_escape "$uninstall_url")" >> "$OUTPUT"
    [ -n "$icon_url" ]       && printf ',\n      "icon_url": "%s"' "$(json_escape "$icon_url")" >> "$OUTPUT"
    [ -n "$featured_image" ] && printf ',\n      "featured_image": "%s"' "$(json_escape "$featured_image")" >> "$OUTPUT"

    # Optional boolean: featured
    if [ "$featured" = "true" ]; then
        printf ',\n      "featured": true' >> "$OUTPUT"
    fi

    # Size
    [ -n "$size" ] && printf ',\n      "size": "%s"' "$size" >> "$OUTPUT"

    # Source fields
    [ -n "$source" ]       && printf ',\n      "source": "%s"' "$(json_escape "$source")" >> "$OUTPUT"
    [ -n "$source_asset" ] && printf ',\n      "source_asset": "%s"' "$(json_escape "$source_asset")" >> "$OUTPUT"

    # Constraints (dot notation: constraints.abi)
    constraint_abis=$(grep '^constraints\.abi=' "$tmp" 2>/dev/null | sed 's/^constraints\.abi=//' | head -1 || true)
    if [ -n "$constraint_abis" ]; then
        printf ',\n      "constraints": {\n' >> "$OUTPUT"
        printf '        "abi": %s\n' "$(csv_to_json_array "$constraint_abis")" >> "$OUTPUT"
        printf '      }' >> "$OUTPUT"
    fi

    # Launcher (dot notation: launcher.platform.key)
    launcher_lines=$(grep '^launcher\.' "$tmp" 2>/dev/null || true)
    if [ -n "$launcher_lines" ]; then
        printf ',\n      "launcher": {' >> "$OUTPUT"

        launcher_tmp="$(mktemp)"
        printf '%s\n' "$launcher_lines" | sort > "$launcher_tmp"

        prev_platform=""
        lpf_first=true

        while IFS='=' read -r lkey lval; do
            lkey_no_prefix="${lkey#launcher.}"
            platform="${lkey_no_prefix%%.*}"
            subkey="${lkey_no_prefix#$platform.}"

            if [ "$platform" != "$prev_platform" ]; then
                if [ -n "$prev_platform" ]; then
                    printf '\n        }' >> "$OUTPUT"
                fi
                if $lpf_first; then
                    lpf_first=false
                else
                    printf ',' >> "$OUTPUT"
                fi
                printf '\n        "%s": {\n' "$platform" >> "$OUTPUT"
                prev_platform="$platform"
            else
                printf ',\n' >> "$OUTPUT"
            fi
            printf '          "%s": "%s"' "$subkey" "$(json_escape "$lval")" >> "$OUTPUT"
        done < "$launcher_tmp"

        if [ -n "$prev_platform" ]; then
            printf '\n        }' >> "$OUTPUT"
        fi
        printf '\n      }' >> "$OUTPUT"

        rm -f "$launcher_tmp"
    fi

    printf '\n    }' >> "$OUTPUT"

    if [ "$i" -lt "$count" ]; then
        printf ',' >> "$OUTPUT"
    fi
    printf '\n' >> "$OUTPUT"

    rm -f "$tmp"
done

# --- footer ---
printf '  ]\n}\n' >> "$OUTPUT"

echo "Generated $OUTPUT with $i packages"

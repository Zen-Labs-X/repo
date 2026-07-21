#!/bin/sh
set -eu
# Generate manifest.json from all packages/**/.meta files
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
    printf '    "name": "ZenLabs Repo",\n'
    printf '    "url": "https://repo.zen-labs.org/",\n'
    printf '    "icon_url": "https://repo.zen-labs.org/favicon.svg"\n'
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
    incompatible_platforms=$(grep '^incompatible_platforms=' "$tmp" 2>/dev/null | sed 's/^incompatible_platforms=//' | head -1)
    dependencies=$(grep '^dependencies=' "$tmp" 2>/dev/null | sed 's/^dependencies=//' | head -1)
    conflicts=$(grep '^conflicts=' "$tmp" 2>/dev/null | sed 's/^conflicts=//' | head -1)
    install_url=$(grep '^install_url=' "$tmp" 2>/dev/null | sed 's/^install_url=//' | head -1)
    uninstall_url=$(grep '^uninstall_url=' "$tmp" 2>/dev/null | sed 's/^uninstall_url=//' | head -1)
    size=$(grep '^size=' "$tmp" 2>/dev/null | sed 's/^size=//' | head -1)
    featured=$(grep '^featured=' "$tmp" 2>/dev/null | sed 's/^featured=//' | head -1)
    featured_order=$(grep '^featured_order=' "$tmp" 2>/dev/null | sed 's/^featured_order=//' | head -1)
    icon_url=$(grep '^icon_url=' "$tmp" 2>/dev/null | sed 's/^icon_url=//' | head -1)
    featured_image=$(grep '^featured_image=' "$tmp" 2>/dev/null | sed 's/^featured_image=//' | head -1)
    source=$(grep '^source=' "$tmp" 2>/dev/null | sed 's/^source=//' | head -1)
    source_asset=$(grep '^source_asset=' "$tmp" 2>/dev/null | sed 's/^source_asset=//' | head -1)
    source_type=$(grep '^source_type=' "$tmp" 2>/dev/null | sed 's/^source_type=//' | head -1)
    source_url=$(grep '^source_url=' "$tmp" 2>/dev/null | sed 's/^source_url=//' | head -1)
    stars=$(grep '^stars=' "$tmp" 2>/dev/null | sed 's/^stars=//' | head -1)
    updated_at=$(grep '^updated_at=' "$tmp" 2>/dev/null | sed 's/^updated_at=//' | head -1)
    readme_url=$(grep '^readme_url=' "$tmp" 2>/dev/null | sed 's/^readme_url=//' | head -1)
    readme_hash=$(grep '^readme_hash=' "$tmp" 2>/dev/null | sed 's/^readme_hash=//' | head -1)

    case "$category" in
        utility|games|productivity|media|theme|patches) ;;
        *)
            echo "Invalid or missing category in $meta_file: $category" >&2
            rm -f "$tmp"
            exit 1
            ;;
    esac

    if [ -n "$featured_order" ]; then
        case "$featured_order" in
            *[!0-9]*)
                echo "Invalid featured_order in $meta_file: $featured_order" >&2
                rm -f "$tmp"
                exit 1
                ;;
        esac
        if [ "$featured" != "true" ]; then
            echo "featured_order requires featured=true in $meta_file" >&2
            rm -f "$tmp"
            exit 1
        fi
        featured_order=$(printf '%s' "$featured_order" | sed 's/^0*//;s/^$/0/')
    fi

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

    [ -n "$conflicts" ] && printf ',\n      "conflicts": %s' "$(csv_to_json_array "$conflicts")" >> "$OUTPUT"
    [ -n "$incompatible_platforms" ] && printf ',\n      "incompatible_platforms": %s' "$(csv_to_json_array "$incompatible_platforms")" >> "$OUTPUT"

    # Optional string fields
    [ -n "$install_url" ] && printf ',\n      "install_url": "%s"' "$(json_escape "$install_url")" >> "$OUTPUT"
    [ -n "$uninstall_url" ] && printf ',\n      "uninstall_url": "%s"' "$(json_escape "$uninstall_url")" >> "$OUTPUT"
    [ -n "$icon_url" ]       && printf ',\n      "icon_url": "%s"' "$(json_escape "$icon_url")" >> "$OUTPUT"
    [ -n "$featured_image" ] && printf ',\n      "featured_image": "%s"' "$(json_escape "$featured_image")" >> "$OUTPUT"

    # Optional boolean: featured
    if [ "$featured" = "true" ]; then
        printf ',\n      "featured": true' >> "$OUTPUT"
    fi
    [ -n "$featured_order" ] && printf ',\n      "featured_order": %s' "$featured_order" >> "$OUTPUT"

    # Size
    [ -n "$size" ] && printf ',\n      "size": "%s"' "$size" >> "$OUTPUT"

    # Source fields
    [ -n "$source" ]       && printf ',\n      "source": "%s"' "$(json_escape "$source")" >> "$OUTPUT"
    [ -n "$source_asset" ] && printf ',\n      "source_asset": "%s"' "$(json_escape "$source_asset")" >> "$OUTPUT"
    [ -n "$source_type" ]  && printf ',\n      "source_type": "%s"' "$(json_escape "$source_type")" >> "$OUTPUT"
    [ -n "$source_url" ]   && printf ',\n      "source_url": "%s"' "$(json_escape "$source_url")" >> "$OUTPUT"
    [ -n "$stars" ]        && printf ',\n      "stars": "%s"' "$stars" >> "$OUTPUT"
    [ -n "$updated_at" ]   && printf ',\n      "updated_at": "%s"' "$(json_escape "$updated_at")" >> "$OUTPUT"
    [ -n "$readme_url" ]   && printf ',\n      "readme_url": "%s"' "$(json_escape "$readme_url")" >> "$OUTPUT"
    [ -n "$readme_hash" ]  && printf ',\n      "readme_hash": "%s"' "$(json_escape "$readme_hash")" >> "$OUTPUT"

    # Assets array (dot notation: assets.N.key)
    asset_indices=$(grep '^assets\.' "$tmp" 2>/dev/null \
        | sed 's/^assets\.\([0-9][0-9]*\)\..*/\1/' \
        | sort -n | uniq || true)
    if [ -n "$asset_indices" ]; then
        printf ',\n      "assets": [' >> "$OUTPUT"
        af_first=true
        for idx in $asset_indices; do
            a_arch=$(grep "^assets\.$idx\.arch=" "$tmp" 2>/dev/null | sed "s/^assets\.$idx\.arch=//" | head -1)
            a_asset=$(grep "^assets\.$idx\.asset=" "$tmp" 2>/dev/null | sed "s/^assets\.$idx\.asset=//" | head -1)
            a_url=$(grep "^assets\.$idx\.url=" "$tmp" 2>/dev/null | sed "s/^assets\.$idx\.url=//" | head -1)
            a_size=$(grep "^assets\.$idx\.size=" "$tmp" 2>/dev/null | sed "s/^assets\.$idx\.size=//" | head -1)

            if $af_first; then af_first=false; else printf ',' >> "$OUTPUT"; fi
            printf '\n        {\n' >> "$OUTPUT"
            printf '          "arch": "%s",\n' "$(json_escape "$a_arch")" >> "$OUTPUT"
            printf '          "asset": "%s",\n' "$(json_escape "$a_asset")" >> "$OUTPUT"
            printf '          "url": "%s"' "$(json_escape "$a_url")" >> "$OUTPUT"
            [ -n "$a_size" ] && printf ',\n          "size": "%s"' "$a_size" >> "$OUTPUT"
            printf '\n        }' >> "$OUTPUT"
        done
        printf '\n      ]' >> "$OUTPUT"
    fi

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

# v1.0.1

- Fix all-day events leaking into the next day in DST-observing zones

    ICS.parseDateTime and the RRULE UNTIL parser forced isdst=false when
    building timestamps for date-only and floating date-time values. In a
    DST-observing timezone (e.g. Europe/Lisbon in August), this shifts the
    resulting epoch by the DST offset, pushing an all-day DTEND an hour
    past the following midnight and causing it to overlap that next day's
    bucket in groupByDay. Leave isdst unset so mktime auto-detects DST,
    matching the convention already used in calendar_view.lua's midnight()/
    addDays().

# v1.0.0

 - initial release

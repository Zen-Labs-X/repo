# ReadingCompanion.koplugin-
Reading Companion 📚

A reading dashboard for KOReader — because apparently reading books wasn’t nerdy enough, so now we have statistics.

Reading Companion turns your KOReader history into something a little more fun. Track your reading, look back at finished books, earn achievements, see ridiculous amounts of statistics, and—when you inevitably reopen a book after three days and remember absolutely nothing—use Previously On… to get back into the story.

* Tested and developed on a jailbroken Kindle Paperwhite Signature Edition
 
✨ Features

📖 Previously On…

Forgot what happened?

Same.

Previously On gives you a quick view of where you are in your current book and can generate a spoiler-free Story Recap with Google Gemini.

The recap is generated only through your current reading position, focusing on the major characters, events, relationships, conflicts, and where things currently stand.

No intentionally peeking ahead. No “helpful” reminder about the character who dies 80 pages from now.

📊 Reading Stats

See far more information about your reading habits than any reasonable person needs:

* Reading time
* Pages read
* Sessions
* Reading days
* Streaks
* Book progress
* Reading heat map
* Historical stats

Basically, if KOReader recorded it, Reading Companion probably wants to make a number out of it.

🗓️ Reading Recap

Look back at your reading by:

* Month
* Year
* All Time

See books completed, pages, reading time, reading days, and other highlights from your reading history.

🏆 Achievements

Because finishing a book apparently wasn’t enough motivation.

Reading Companion includes 70 achievements covering reading habits, milestones, strange hours of the night, annotations, consistency, and other things you’ll probably start doing specifically because there’s now an achievement for them.

Some achievements are secret.

Good luck with that.

🏅 Awards

Reading Companion can also hand out reading awards based on your activity.

Is this necessary?

Absolutely not.

Is it fun?

Yes.

📚 Bookshelf

Your finished books live in the Bookshelf, along with available ratings and reviews.

It’s your little history of literary conquests—or the books you somehow finished at 2:37 AM when you absolutely should have been sleeping.

🏠 SimpleUI Integration

Using SimpleUI?

Reading Companion includes an optional customizable mini-dashboard showing things like:

* Book cover
* Title and author
* Current progress
* Previously On status
* Three configurable reading stats

You can customize the layout, visible information, stats, scale, and background style.

🤖 Gemini Story Recaps

Story Recaps require your own Google Gemini API key.

Add your key in:

Reading Companion → Settings → Story Recaps

Then open Previously On… and choose Generate Recap.

Reading Companion sends extracted book text through your current reading position to the Gemini API when you explicitly generate or update a recap.

Your API key stays in Reading Companion’s local plugin data.

Google’s handling of API requests is governed by the terms and policies applicable to your Gemini API account.

### Requirements

- KOReader v2026.7.02(or above)
- Google Gemini API key *(optional — only required for Story Recaps)*
- Internet connection *(only when generating or updating a Story Recap)*
  
📦 Installation

1. Download the latest Reading Companion release.
2. Extract readingcompanion.koplugin.(It’s inside the file extracted from the .zip) 
3. Copy the folder into your KOReader plugins directory.
4. Restart KOReader.
5. Open Reading Companion from the KOReader menu.
6. Immediately spend ten minutes looking at your reading statistics instead of actually reading.

For updates, replace the previous readingcompanion.koplugin folder with the new one.

Your Reading Companion data is stored separately from the plugin code.

🔒 Data & Privacy

Reading Companion treats KOReader’s reading statistics as read-only.

It does not erase or modify your KOReader statistics.

Reading Companion maintains its own plugin data for features such as achievements and Story Recaps.

Book text is sent externally only when you explicitly ask Reading Companion to generate or update a Gemini Story Recap.

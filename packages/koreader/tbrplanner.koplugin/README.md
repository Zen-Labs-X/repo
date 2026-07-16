## TBR Planner

TBR Planner is a KOReader plugin to help you organize and schedule your **To Be Read** list.

- Separate books into **Wishlist** (no dates yet) and **Planned** (with dates).
- See your plans on a monthly **Calendar** view.
- Let the plugin calculate an end date from your **daily pages** target.
- Shift a plan forward or backward while keeping the same reading duration with **Keep duration**.

---

## 1. Opening the plugin

TBR Planner lives in KOReader’s main menu.

1. From KOReader’s main screen, open the main menu.
2. Go to the tools menu.
3. Tap **TBR Planner** (Probably on the second page)
4. At the top of the screen you will see three tabs:
   - **Wishlist**
   - **Planned**
   - **Calendar**
5. In the header you will also see a **+ New** button. It creates a new item for the currently active tab.

You can also add books to TBR Planner directly from the **File Manager** (see section 3.2).

---

## 2. Core concepts

- **Wishlist** – Books you want to read someday, but without dates yet.
- **Planned** – Books that have a start date and/or end date and appear on the calendar.
- **Calendar** – A monthly grid that shows your planned books as colored spans.
- **Priority** – A numeric importance value (for example 0, 1, 2…). Higher numbers usually mean higher priority.
- **Tags** – Free‑form labels to group books. They are shown as `#tag` in lists.

---

## 3. Ways to add books

### 3.1 From inside TBR Planner

#### Adding a book to the Wishlist tab

1. Switch to the **Wishlist** tab.
2. Tap **+ New**.
3. Fill in the fields:
   - **Title** – Book title (required).
   - **Author** – Author (optional).
   - **Priority (number)** – Any number you like.
   - **Tags (comma-separated)** – Example: `classic, sci-fi`.
4. Tap **Add** to save.

Wishlist items do not have dates. They are ideas and candidates for future planning.

#### Adding a planned book directly in the Planned tab

1. Switch to the **Planned** tab.
2. Tap **+ New**.
3. Fill in:
   - **Title**
   - **Author**
   - **Start date (YYYY-MM-DD)**
   - **End date (YYYY-MM-DD)** – required
   - **Priority (number)**
   - **Tags (comma-separated)**
4. Tap **Add**.

> **Note on date format**
>
> Internally the plugin uses `YYYY-MM-DD`, but you can type any non‑digit separator:
>
> - `2025-11-25`
> - `2025.11.25`
> - `2025/11/25`
> - `2025 11 25`
>
> All of these will be accepted and normalized to `2025-11-25`.

### 3.2 From the File Manager

You can attach an existing book file to TBR Planner:

1. In KOReader’s **File Manager**, long‑press a book.
2. Choose **TBR Planner** from the context menu.
3. A dialog opens where you can, depending on the current state:
   - Add the book to **Wishlist**.
   - Turn it into a **Planned** item with dates.
   - View or update an existing TBR Planner entry for this file.

This is usually the fastest way to plan a book you have just found in your library.

---

## 4. Working with Wishlist

In the **Wishlist** tab:

- Each row shows:
  - **First line** – Title.
  - **Second line** – Author, status (if needed), and priority.
- The **Options** menu at the top lets you:
  - Change sorting (Priority, Title A–Z, Added newest/oldest).
  - Filter by text or tags.

When you tap a Wishlist item you get an action menu:

- **Open** – Opens the book in KOReader (only if the file path is known).
- **Edit** – Edit title, author, priority, tags.
- **Delete** – Remove the entry.
- **Plan** – Move the book into **Planned** with dates (see section 6 for details).

---

## 5. Working with Planned

The **Planned** tab lists all books that have at least one planned date.

### 5.1 List view and visual highlights

- Each row shows:
  - **First line** – Title.
  - **Second line** – Author, start or end date, and priority.
- Visual cues help you see what matters today:
  - **Overdue items** (their end date is in the past):
    - `⚠` symbol at the beginning of the title.
    - Title and second line text are shown in gray.
  - **Items active today** (today is between start and end):
    - Row background is shaded light gray.

This makes it easy to see what you should focus on first.

### 5.2 Planned item actions

Tap a row in the Planned list to open its action menu:

- **Open** – Open the book (if the file path is known).
- **Edit** – Edit the plan details.
- **Delete** – Delete the entry.
- **Move to wishlist** – Remove the dates and return the book to Wishlist.

### 5.3 Editing a planned item and Keep duration

When you choose **Edit** for a planned item, the dialog includes:

- Title
- Author
- Start date (YYYY-MM-DD)
- End date (YYYY-MM-DD)
- Priority
- Tags

Buttons:

- **Cancel** – Close without saving.
- **Save** – Save the changes.
- **Keep duration** – Only shown when the item status is `planned`, `started`, or `paused`.

#### What does Keep duration do?

- It keeps the original reading duration (number of days between Start and End).
- You type a new **Start date**.
- When you press **Keep duration**:
  - The plugin computes the original duration.
  - It applies the same duration starting from your new Start date.
  - The **End date** field is updated automatically.
- You then press **Save** to store the new dates.

This is useful when you want to postpone or bring forward a plan but keep the same overall reading window.

The same behavior is available when you edit a planned item from the **Calendar** view (section 7.3).

---

## 6. Planning from Wishlist and Calc. end date

When you plan a book from Wishlist, and the plugin knows its page count, you get extra options.

### 6.1 Planning dialog

From a Wishlist item, choose **Plan**. The dialog includes:

- Title
- Author
- Start date
- End date
- Priority
- Tags
- **Daily pages (number)** – only shown when page count is available.
- **Calc. end date** button – also only shown when page count is available.

### 6.2 How Calc. end date works

1. Enter a **Start date**.
2. Enter how many pages you want to read per day in **Daily pages**.
3. Press **Calc. end date**. The plugin will:
   - Read the total page count and, if available, your current reading progress.
   - Compute how many pages remain.
   - Calculate how many days are needed at your daily pace.
   - Fill in the **End date** field automatically.

> **Tips**
>
> - Page count is usually available after you have opened the book at least once in KOReader.
> - If page information is missing, the plugin cannot show or use **Calc. end date**.

---

## 7. Calendar view

The **Calendar** tab shows your plans on a monthly grid.

- The header shows the month and year (for example `November 2025`).
- You can move between months with the left/right arrows or swipe gestures.
- Each day cell shows:
  - The day number.
  - Colored bars for planned items that cover that day.
  - A `+N` badge when there are more items than can be shown.

### 7.1 Tapping a day

Tap a day cell to open a small menu for that date:

- First row: **+ New** – Add a new planned item starting on that day.
- Below: A list of books that are active on that day (title and author).

Tap one of the listed books to open its item menu.

### 7.2 Single item menu from the calendar

For a book selected from a day:

- **Open** – Open the book (if the file path is known).
- **Edit** – Edit the plan.
- **Delete** – Delete the entry.
- **Move to wishlist** – Move the item back to Wishlist.

The popup dialog title shows the **book title** (not just the date), so you always know which book you are editing.

### 7.3 Editing from Calendar and Keep duration

When you choose **Edit** from the Calendar menu, the dialog is similar to the Planned edit dialog:

- Title
- Author
- Start date
- End date

Buttons:

- Cancel
- Save
- **Keep duration** – again available for `planned`, `started`, or `paused` items.

Keep duration here behaves exactly like in the Planned tab: you choose a new Start date and let the plugin adjust End date while preserving the same duration.

---

## 8. Daily start notification ("today" prompt)

When you start KOReader, TBR Planner checks if any books are scheduled to **start today**.

- If there are, it shows a short info message listing them.
- Each line uses a `➤` symbol followed by the book title (and author when available).
- The message is shown **only once per day**.

This helps you quickly see which books you planned to start on the current day.

---

## 9. Filters and search

Both **Wishlist** and **Planned** tabs have an **Options** menu in the header.

From there you can:

- Change **sorting** (options depend on the tab).
- **Filter by text** – finds items where the text appears in the title, author, or note.
- **Filter by tags** – filter by a comma‑separated list of tags.
- **Clear filters** – reset all filters to show the full list again.

---

## 10. Date input behavior

- Internally all dates are stored as `YYYY-MM-DD`.
- You may type dates with any separator between year, month, and day, such as:
  - `2025-01-02`
  - `2025.01.02`
  - `2025/01/02`
  - `2025 01 02`
- The plugin normalizes them and shows clear error messages when a date cannot be understood.

---

## 11. Known limitations

- **Calc. end date** cannot be used when the plugin cannot determine the book’s page count.
- Some actions (for example Keep duration and certain date edits) only apply to items with status `planned`, `started`, or `paused`, not pure Wishlist entries.

---

## 12. Credits

- TBR Planner is designed and implemented with the assistance of **Windsurf (AI)**.
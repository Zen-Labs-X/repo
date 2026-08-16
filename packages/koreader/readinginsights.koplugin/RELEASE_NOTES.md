**Fixed**

- The insights cache no longer grows without bound — yearly/monthly stale entries were kept per day and never pruned, slowly bloating the on-disk cache (slower startup over time). Now only the latest entry per year/mode is kept.
---
alias: ['Journal', 'Journal Dashboard']
banner_icon: 📔
banner: "https://images.unsplash.com/photo-1488722796624-0aa6f1bb6399?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.5
---

# 300 ⌯ Journal

```button
name 🌱 Open Daily Note
type command
action Periodic Notes: Open daily note
```
---
## Daily notes
```dataview
table without ID file.link as Day, achievement as Achievement, gratitude as Gratitude
from -"900 ⌯ Supporting Files"
where fileClass = "day-note"
and date <= date(today)
sort date DESC
limit 7
```
---
## Tasks

### ⚠️ Overdue tasks
```tasks
not done
due before today
sort by due
hide recurrence rule 
```
### This week
```tasks
not done 
happens before in 1 week
sort by due
sort by scheduled
group by happens
hide recurrence rule 
hide task count
```
---

## Recent meetings
```dataview
table without ID file.link as Meeting, category-meeting as Category, summary as Summary
from -"900 ⌯ Supporting Files"
where fileClass = "meeting-minute"
sort date DESC
limit 8
```
---
≤
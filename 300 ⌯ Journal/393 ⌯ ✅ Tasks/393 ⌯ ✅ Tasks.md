```button
name 📥 New task
type command
action QuickAdd: Add to task list
``` 
^button-add-task

---
[[393 ⌯ ✅ Tasks|✅ Dashboard]] ⌯ [[⏳ Upcoming tasks|⏳ Upcoming]] ⌯ [[✓ Completed]] ⌯ [[✻ All tasks|✻ All]]

---
## ⚠️ Overdue tasks
```tasks
not done
happens before today
sort by due
hide recurrence rule 
```
---
## Today
```tasks
not done 
happens today
sort by due
sort by scheduled
sort by done
hide recurrence rule 
```
---
## This week
```tasks
not done 
happens after yesterday
happens before in 1 week
sort by due
sort by scheduled
group by happens
hide recurrence rule 
```
---
## Needs scheduling
```tasks
(not done) AND ((no due date) AND (no scheduled date)) AND NOT (path includes Supporting Files)
sort by path
hide recurrence rule 
```
---
## Invalid data
```tasks
(done date is invalid) OR (due date is invalid) OR (scheduled date is invalid) OR (start date is invalid)

# Optionally, uncomment this line and exclude your templates location
# path does not include _templates

group by path
```
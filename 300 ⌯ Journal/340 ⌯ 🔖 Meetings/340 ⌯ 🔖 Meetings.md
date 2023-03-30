---
alias: ['🔖 Meetings']
banner_icon: 🔖
banner: "https://images.unsplash.com/photo-1509785307050-d4066910ec1e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1928&q=80"
banner_y: 0.692
---

# 340 ⌯ 🔖 Meetings

```button
name 🔖 New Meeting
type command
action QuickAdd: 🔖 New Meeting
```
^button-new-meeting

---
## To be reviewed
```dataview
table without ID file.link as Meeting, category-meeting as Category
from -"900 ⌯ Supporting Files"
where fileClass = "meeting-minute"
and reviewed = "n"
Sort date DESC
limit 5
```
---
## Meetings, last two weeks

```dataview
table without ID file.link as Meeting, category-meeting as Category
from -"900 ⌯ Supporting Files"
where fileClass = "meeting-minute"
and reviewed = "y"
and date >= date(today)-dur(2 weeks) 
and date <=date(today)
Sort date DESC
```
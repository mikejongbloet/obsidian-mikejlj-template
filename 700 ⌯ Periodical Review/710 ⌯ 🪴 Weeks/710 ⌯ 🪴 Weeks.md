---
alias: ['🪴 Weeks', '🪴 Weeks Dashboard']
banner: "https://images.unsplash.com/photo-1553078954-b5770add7a4e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.652
banner_icon: 🪴
---

# 710 ⌯ 🪴 Weeks

```button
name 🪴 Open week
type command
action Periodic Notes: Open weekly note
```
---
### Achievements & areas of improvement
```dataview
table
	weekly-highlight as "🏆 Highlight",
	area-to-improve as "🎯 To improve"
from -"900 ⌯ Supporting Files"
where
	date >= date(today)-dur(4 weeks) and
	date <=date(today) and
	fileClass = "week-note"
sort date
```
---
### Reflection
```dataview
table
	weekly-reflection as "🧘 Reflection"
from -"900 ⌯ Supporting Files"
where
	date >= date(today)-dur(4 weeks) and
	date <=date(today) and
	fileClass = "week-note"
sort date
```
---
alias: ['🗓️ Months', '🗓️ Months Dashboard']
banner: "https://images.unsplash.com/photo-1519681393784-d120267933ba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.628
banner_icon: 🗓️
---

# 730 ⌯ 🗓️ Months

```button
name 🗓️ Open Month
type command
action Periodic Notes: Open monthly note
```
---
### Achievements
```dataview
table 
	monthly-highlight as "🏆 Highlight"
from -"900 ⌯ Supporting Files"
where date >= date(today)-dur(6 months) and date <=date(today) and fileClass = "month-note"
sort date desc
```
---
### Reflection
```dataview
table 
	monthly-reflection as "🧘 Reflection"
from -"900 ⌯ Supporting Files"
where date >= date(today)-dur(6 months) and date <=date(today) and fileClass = "month-note"
sort date desc
```

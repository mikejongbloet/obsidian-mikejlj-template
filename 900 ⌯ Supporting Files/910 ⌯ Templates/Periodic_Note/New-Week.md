---
fileClass: week-note
date: {{ date:YYYY-MM-DD }}
banner: "https://images.unsplash.com/photo-1553078954-b5770add7a4e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.724
banner_icon: 🪴
---
← [[{{date-7d:gggg-[W]ww}}]] ••• [[710 ⌯ 🪴 Weeks|🪴 Weeks Dashboard]] ••• [[{{date+7d:gggg-[W]ww}}]] →

# <% tp.file.title %>
<small>*{{ date:Do MMM }} - {{ date+6d:Do MMM }}, {{ date:YYYY }}*</small>
Days: [[{{date:YYYY-MM-DD}}|{{date:Do MMM}}]] ⌯ [[{{date+1d:YYYY-MM-DD}}|{{date+1d:Do MMM}}]] ⌯ [[{{date+2d:YYYY-MM-DD}}|{{date+2d:Do MMM}}]] ⌯ [[{{date+3d:YYYY-MM-DD}}|{{date+3d:Do MMM}}]] ⌯ [[{{date+4d:YYYY-MM-DD}}|{{date+4d:Do MMM}}]] ⌯ [[{{date+5d:YYYY-MM-DD}}|{{date+5d:Do MMM}}]] ⌯ [[{{date+6d:YYYY-MM-DD}}|{{date+6d:Do MMM}}]]
Month:: [[{{date:YYYY-MM}}|{{date: MMM YYYY}}]]

---

# 🧹 Cleanup tasks

- [ ] #task Process email inbox ⏳ {{date+4d:YYYY-MM-DD}}
- [ ] #task Convert physical notes to digital notes ⏳ {{date+4d:YYYY-MM-DD}}
- [ ] #task Process [[340 ⌯ 🔖 Meetings|meeting notes]] ⏳ {{date+4d:YYYY-MM-DD}}
- [ ] #task Review [[393 ⌯ ✅ Tasks|tasks]] ⏳ {{date+4d:YYYY-MM-DD}}
- [ ] #task Review [[392 ⌯ 📨 Projects|📨Projects]] ⏳ {{date+4d:YYYY-MM-DD}}
- [ ] #task Create next week and set next weeks goal ⏳ {{date+4d:YYYY-MM-DD}}

---

# ✍🏻 Journal

## Week notes

-

## Reflections
- 🪴🏆 **Weekly highlight**:: 
- 🪴🎯 **Area to improve**:: 
- 🪴🧘 **Weekly reflection**:: 

```dataview
table
	Feeling as "🫥",
	week-day as "🌱 Day",
	Achievement as "😄 Achievement",
	Learned as "🎓 Learned",
	Gratitude as "🤗 Gratitude"
where
	date >= date({{date:YYYY-MM-DD}}) and
	date <= date({{date+6d:YYYY-MM-DD}}) and
	fileClass = "day-note"
sort date
```

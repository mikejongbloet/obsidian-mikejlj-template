---
fileClass: day-note
date: {{ date:YYYY-MM-DD }}
week-day: {{ date:dddd }}
banner: "https://images.unsplash.com/photo-1500382017468-9049fed747ef?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2532&q=80"
banner_icon: 🌱
banner_y: 0.664
---

← [[{{date-1d:YYYY-MM-DD}}]] ••• [[310 ⌯ 🌱 Daily|🌱 Journal Notes]] ••• [[{{date+1d:YYYY-MM-DD}}]] →

# <% tp.file.title %>

<small>_{{ date:dddd MMMM Do, YYYY }}_</small>

Month:: [[{{date:YYYY-MM}}|{{date: MMM YYYY}}]]
Week:: [[{{date:gggg-[W]ww}}]]

---

# 🎯 Task(s)

#### 🎯 Todays goal

>

#### ⚠️ Overdue

```tasks
not done
due before {{ date:YYYY-MM-DD }}
sort by due
hide recurrence rule
```

#### Today

**Todo**

```tasks
not done
happens on {{ date:YYYY-MM-DD }}
sort by due
sort by scheduled
sort by done
hide recurrence rule
```

**Done**

```tasks
done on {{ date:YYYY-MM-DD }}
sort by done
hide recurrence rule
```

---

# 💭 Daily log

<% tp.file.cursor() %>
`button-tb-capture-thought` `button-tb-capture-idea` `button-tb-capture-reflection` `button-tb-add-to-watch` `button-tb-add-book` `button-tb-add-article`

---

# 🔖 Meetings

```dataview
TABLE WITHOUT ID
time AS "Time",
file.link AS "Title",
choice(reviewed = "y", "👍🏻", "No") AS "Processed?"
from -"900 ⌯ Supporting Files"
where (
	fileClass = "meeting-minute" and
	date = date({{ date:YYYY-MM-DD }})
)
sort file.ctime asc
```

```button
name 🔖 New Meeting
type command
action QuickAdd: 🔖 New Meeting
```

---

# 🧘 Reflections

**[[{{date:YYYY-MM-DD}}|{{date: dddd Do MMM, YYYY}}]]**

- 🫥 **Feeling**::
- 😄 **Achievement**::
- 🎓 **Learned**::
- 🤗 **Gratitude**::

---

# 🧠 Knowledge Management

```dataview
list
from -"900 ⌯ Supporting Files"
where (
	fileClass = "literature-note" or
	fileClass = "atomic-note"  or
	fileClass = "resource" and
	date = date({{ date:YYYY-MM-DD }})
)
sort file.ctime asc
```

---

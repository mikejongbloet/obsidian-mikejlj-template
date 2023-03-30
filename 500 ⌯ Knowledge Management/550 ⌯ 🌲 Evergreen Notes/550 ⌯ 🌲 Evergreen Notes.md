---
alias: ['🌲 Evergreen Notes', '🌲 Evergreen Note Dashboard']
exclude_from_graph: true
banner: "https://images.unsplash.com/photo-1488330890490-c291ecf62571?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0
banner_icon: 🌲
---

# 550 ⌯ 🌲 Evergreen Notes

```button
name 🌲 New Evergreen Note
type command
action QuickAdd: 🌲 New Evergreen
```
---
## Overview
```dataviewjs
let notesRO = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="evergreen-note"
		&& p["reviewed"] == "n"
	);
let n1 = notesRO.length
let pb1 = n1
let p1 = "Inbox"

let notes2 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="evergreen-note"
		&& p["reviewed"] == "y"
	);
let n2 = notes2.length
let pb2 = n2
let p2 = "Reviewed"


const table = dv.markdownTable(
	["Note status","Count"],[[p1,pb1],[p2,pb2]],)
dv.paragraph(table)
```

---

## Inbox
```dataview
list
from -"900 ⌯ Supporting Files"
where fileClass = "evergreen-note" and reviewed = "n"
```
---
## Reviewed
```dataview
list
from -"900 ⌯ Supporting Files"
where fileClass = "evergreen-note" and reviewed = "y"
sort score desc
limit 20
```

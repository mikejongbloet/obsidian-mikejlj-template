---
alias: ['📝 Atomic Notes', '📝 Atomic Note Dashboard']
exclude_from_graph: true
banner: "https://images.unsplash.com/photo-1678008630409-1608b48e7ff7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_icon: 📝
banner_y: 0.756
---

# 530 ⌯ 📝 Atomic Notes

```button
name 📝 New Atomic Note
type command
action QuickAdd: 📝 New Atomic note
```
---
## Overview
```dataviewjs
let notesRO = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="atomic-note"
		&& p["reviewed"] == "n"
	);
let n1 = notesRO.length
let pb1 = n1
let p1 = "Inbox"

let notes2 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="atomic-note"
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
where fileClass = "atomic-note" and reviewed = "n"
```
---
## Reviewed

```dataview
list
from -"900 ⌯ Supporting Files"
where fileClass = "atomic-note" and reviewed = "y"
sort score desc
limit 20
```

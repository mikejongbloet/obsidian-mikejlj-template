---
alias: ['📚 Literature Notes', '📚 Literature Note Dashboard']
exclude_from_graph: true
banner: "https://images.unsplash.com/photo-1495446815901-a7297e633e8d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.396
banner_icon: 📚
---

# 510 ⌯ 📚 Literature Notes

```button
name 📚 New Literature Note
type command
action QuickAdd: 📚 New Literature
```
---
## Overview
```dataviewjs
let notesI = dv.pages('-"900 ⌯ Supporting Files"')
	.where(p => p["fileClass"]=="literature-note" && p["reviewed"] == "n");
let n3 = notesI.length
let pb3 = n3
let p3 = "Inbox"

let notesRO = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="literature-note"
		&& p["reviewed"] == "y"
	);
let n1 = notesRO.length
let pb1 = n1
let p1 = "Reviewed"

const table = dv.markdownTable(
	["Note status","Count"],[[p3,pb3],[p1,pb1]],)
dv.paragraph(table)
```
---

## Inbox
```dataview
list
from -"900 ⌯ Supporting Files"
where fileClass = "literature-note" and reviewed = "n"
sort date desc
```

## Reviewed
```dataview
list
from -"900 ⌯ Supporting Files"
where fileClass = "literature-note" and reviewed = "y"
sort score desc
limit 20
```
---
alias: ['🛠️ Resources', '🛠️ Resources Dashboard']
exclude_from_graph: true
banner: "https://images.unsplash.com/photo-1512758017271-d7b84c2113f1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.304
banner_icon: 🛠️
---

# 520 ⌯ 🛠️ Resources

```button
name 🛠️ New Resource
type command
action QuickAdd: 🛠️ New Resource
```
---
## Overview

```dataviewjs
let notesRO = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="resource"
		&& p["reviewed"] == "n"
	);
let n1 = notesRO.length
let pb1 = n1
let p1 = "Inbox"

let notes2 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["fileClass"]=="resource"
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
where fileClass = "resource" and reviewed = "n"
sort date desc
```

## Reviewed
```dataview
list
from -"900 ⌯ Supporting Files"
where fileClass = "resource" and reviewed = "y"
sort score desc
limit 20
```
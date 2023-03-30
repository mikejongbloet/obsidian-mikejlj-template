---
alias: ['Knowledge Management', 'Knowledge Management Dashboard']
exclude_from_graph: true
banner: "https://images.unsplash.com/photo-1644088379091-d574269d422f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2593&q=80"
banner_y: 0.628
banner_icon: 🧠
---

# 500 ⌯ Knowledge Management

```dataviewjs
let notes1 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(p => p["fileClass"]=="literature-note");
let n1 = notes1.length
let pb1 = "<progress value='" + n1+ "' max='1000'></progress>" +n1
let p1 = dv.page("510 ⌯ 📚 Literature Notes").file.link

let notes2 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(p => p["fileClass"]=="atomic-note");
let n2 = notes2.length
let pb2 = "<progress value='" + n2+ "' max='1000'></progress>" + n2
let p2 = dv.page("530 ⌯ 📝 Atomic Notes").file.link

let notes6 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(p => p["fileClass"]=="resource");
let n6 = notes6.length
let pb6 = "<progress value='" + n6+ "' max='1000'></progress>" + n6
let p6 = dv.page("520 ⌯ 🛠️ Resources").file.link

let notes3 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(p => p["fileClass"]=="evergreen-note");
let n3 = notes3.length
let pb3 = "<progress value='" + n3+ "' max='1000'></progress>" + n3
let p3 = dv.page("550 ⌯ 🌲 Evergreen Notes").file.link

let notes4 = dv.pages('-"900 ⌯ Supporting Files"')
	.where(p => p["fileClass"]=="topic");
let n4 = notes4.length
let pb4 = "<progress value='" + n4+ "' max='1000'></progress>" + n4
let p4 = dv.page("570 ⌯ 🧵 Topics").file.link

const table = dv.markdownTable(["Note Type","Note Number"],[[p1,pb1],[p2,pb2],[p6,pb6],[p3,pb3],[p4,pb4]],)
dv.paragraph(table)
```

# Needs review
```dataview
table
from -"900 ⌯ Supporting Files"
where reviewed = "n"
sort date asc
```

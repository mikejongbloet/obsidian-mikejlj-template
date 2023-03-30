---
alias: ['🧵 Topics', '🧵 Topic Dashboard']
exclude_from_graph: true
banner: "https://images.unsplash.com/photo-1529957018945-07aed3538ad5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
banner_y: 0.184
banner_icon: 🧵
---

# 570 ⌯ 🧵 Topics

```button
name 🧵 New Topic
type command
action QuickAdd: 🧵 New Topic
```
---
## Recent topics
```dataviewjs
let topics = dv.pages('-"900 ⌯ Supporting Files"')
	.sort(p => p.file.mtime, "desc")
	.where(p => p["fileClass"]=="topic")
	.limit(20);
dv.table(
    ["Topic"],
    topics.map(p =>[
        p.file.link
    ]
    )
);
```
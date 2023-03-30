---
alias: ['📨 Projects', '📨 Projects Dashboard']
banner_icon: 📥
banner: "https://images.unsplash.com/photo-1572177812156-58036aae439c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.44
---

# 392 ⌯ 📨 Projects

```button
name 📨 New Project
type command
action QuickAdd: 📨 New Project
```
---
## Active projects
```dataviewjs
let projects = dv.pages('-"900 ⌯ Supporting Files"')
    .where(p => (p["status"] == "🟢 Active"||p["status"] == "🟠 On-hold") && p["fileClass"]=="project").sort(p => p.type);
dv.table(
    ["Project", "Type", "Status", "Progress"],
    projects.map(p => [
        p.file.link + " (" + p["projectClass"] + ")",
        p["projectClass"],
        p["status"],
        "![pb|100](https://progress-bar.dev/"  + Math.round(p["totalCompletion"]) + "/)",
    ])
);
```
---

## Queued projects
```dataview
table WITHOUT ID file.link as "Project", projectClass as "Type", status as Status
from -"900 ⌯ Supporting Files"
where fileClass="project"
and status="✨ Future"
```

---
fileClass: project
projectClass: work
status: 🟢 Active
date: <% tp.date.now("YYYY-MM-DD") %>
total: 0
completed: 0
totalCompletion: 40
---

# <% tp.file.title %>

[[392 ⌯ 📨 Projects|Projects Dashboard]]


---
## Notepad

* <% tp.file.cursor() %>

### Created notes
```dataviewjs
let project = dv.current().file.path;
let noteProject = [];
let projectMatch = 0;
let notes = [];
let query = dv.pages('-"900 ⌯ Supporting Files"').where(p => p["fileClass"]== "basic-note");

for (q of query)
{
	projectMatch = 0;
	noteProject = q.Project;
	if(noteProject != null) { projectMatch = (noteProject.path === project) ? 1 : 0; }

	if (projectMatch > 0) notes.push(q);
}

dv.table(["Note", "Date"], notes.sort(m => m.date).map(m => ["[[" + m.file.name + "]]", m.date.toFormat("yyyy-MM-dd")]))

// dv.list(meetings);
```
---
## Tasks

---
## Meetings
```dataviewjs
let project = dv.current().file.path;
let meetingProject = [];
let projectMatch = 0;
let meetings = [];
let query = dv.pages('-"900 ⌯ Supporting Files"').where(p => p["fileClass"]== "meeting-minute");

for (q of query)
{
	projectMatch = 0;
	meetingProject = q.Project;

	console.log(meetingProject);

	if(meetingProject != null) { projectMatch = (meetingProject.path === project) ? 1 : 0; }

	console.log(projectMatch);

	if (projectMatch > 0) meetings.push(q);
}

dv.table(["Meeting", "Date", "Summary"], meetings.sort(m => m.date).map(m => ["[[" + m.file.name + "]]", m.date.toFormat("yyyy-MM-dd") + " (" + m.time + ")", m.summary ]))

```

---
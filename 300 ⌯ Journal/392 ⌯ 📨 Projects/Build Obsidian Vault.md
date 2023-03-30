---
fileClass: project
projectClass: personal
status: 🟢 Active
date: 2023-03-30
total: 7
completed: 6
totalCompletion: 40
---

# Build Obsidian Vault

[[392 ⌯ 📨 Projects|Projects Dashboard]]


---
## Notepad

* Imported ChenLMS repo as a base for the repo
* Added new theme - Things
* Made a bunch of styling tweks
* Thinking of adding 'Meetings' as a type
* etc
* etc

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
- [x] #task Fork existing repo from community ✅ 2023-03-30
- [x] #task Rebuild People dashboard ✅ 2023-03-30
- [x] #task Rebuild Projects section ✅ 2023-03-30
- [x] #task Add emojis for each type of note as a visual cue ✅ 2023-03-30
- [x] #task Look into CSS styling the menu in Obsidian ✅ 2023-03-30
- [x] #task Break out Resources as it's own section ✅ 2023-03-30
- [ ] #task Create dummy vault to share back to the community 📅 2023-04-06

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
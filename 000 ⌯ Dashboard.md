---
cssclass: dashboard
obsidianUIMode: preview
banner: "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2413&q=80"
banner_y: 0.964
banner_icon: 🌎
---
*Today is `="[[" + dateformat(date(today), "yyyy-MM-dd") + "|"+ dateformat(date(today), "cccc dd") +"]]"` `="[[" + dateformat(date(today), "yyyy/yyyy-MM") + "|"+ dateformat(date(today), "MMMM") +"]]"`, in `="[[" + dateformat(date(today), "yyyy") + "-W" + dateformat(date(today), "W") + "|Week "+ dateformat(date(today), "W") +"]]"`*
`button-daily`   `button-add-task` `button-new-meeting`

`button-tb-capture-thought` `button-tb-capture-idea` `button-tb-capture-reflection` `button-tb-add-to-watch` `button-tb-add-book` `button-tb-add-article`

---

# Tasks today <small style="font-size: 0.5em">[[393 ⌯ ✅ Tasks|✅]]</small>
```tasks
not done 
happens today
sort by due
sort by scheduled
sort by done
hide recurrence rule 
```

---
# Meetings today
```dataview
TABLE WITHOUT ID
time AS "Time",
file.link AS "Title",
choice(reviewed = "y", "👍🏻", "No") AS "Processed?"
from -"900 ⌯ Supporting Files"
where (
	fileClass = "meeting-minute" and
	date = date(dateformat(date(today), "yyyy-MM-dd"))
)
sort file.ctime asc
```
---
# Projects
```dataviewjs
let type = "work";
let projects = [];
let number = 3;
let n = 0;

let query = dv.pages('"300 ⌯ Journal/392 ⌯ 📨 Projects"')
	.where(
		p => p["projectClass"]== type
		&& p["status"]== "🟢 Active"
	).sort(
		p => p['date'], 'desc'
	);

let numResults = query.length;

if(numResults > 0) {

	dv.header(2, "Active " + type + " projects (" + numResults + ")");

	for (q of query) {
		projects.push("[[" + query[n].file.name + "]]")
	}

	dv.list(projects);
}
```
```dataviewjs
let type = "personal";
let projects = [];
let number = 3;
let n = 0;

let query = dv.pages('"300 ⌯ Journal/392 ⌯ 📨 Projects"')
	.where(
		p => p["projectClass"]== type
		&& p["status"]== "🟢 Active"
	).sort(
		p => p['date'], 'desc'
	);

let numResults = query.length;

if(numResults > 0) {

	dv.header(2, "Active " + type + " projects (" + numResults + ")");

	for (q of query) {
		projects.push("[[" + query[n].file.name + "]]")
	}

	dv.list(projects);
}
```
---
# Knowledge
```dataviewjs
let notes = [];
let numNotes = 6;
let excess = "banana";
let query = dv.pages('"500 ⌯ Knowledge Management"')
	.where(
		p => p["reviewed"]== "n"
	).sort(
		p => p['date'], 'desc'
	);

console.log(query)

dv.header(2, "To be reviewed (" + query.length + ")");

excess = (numNotes < query.length) ? true : false;

numNotes = (numNotes < query.length) ? numNotes : query.length;

console.log(excess)

console.log("numNotes: " + numNotes)

for (let i = 0; i <= numNotes - 1; i++) {
console.log(i + ":" + numNotes)

	notes.push("[[" + query[i].file.name + "]]")
}

if(excess) notes.push("[[592 ⌯ 🔭 To be reviewed|And " + (query.length - numNotes) + " more...]]")

dv.list(notes);
```
---
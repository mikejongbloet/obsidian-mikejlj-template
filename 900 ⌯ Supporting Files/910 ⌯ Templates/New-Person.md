---
alias:
fileClass: person
category-person:
source-person:
relationship:
---
# <% tp.file.title %>
**Profession**:: <% tp.file.cursor(1) %>
**Organisation**::
**Email**::
**Located**::

---
## Notes
*

---
## Meetings
```dataviewjs
let person = dv.current().file.path;
let attendees = [];
let attendeeMatch = 0;
let meetings = [];
let query = dv.pages('-"900 ⌯ Supporting Files"').where(p => p["fileClass"]== "meeting-minute");

for (q of query)
{
	attendeeMatch = 0;
	attendees = q.Attendees;

	if (attendees != null) {
		if (attendees.length > 1)
		{
			for (x of attendees)
			{
				// console.log(x.path +" & "+ person);

				attendeeMatch = (x.path === person) ? attendeeMatch + 1 : attendeeMatch;
				// console.log("First:" + attendeeMatch);
			}
		}
		else
		{
			attendeeMatch = (attendees.path === person) ? attendeeMatch + 1 : attendeeMatch;
		}
	}

	// console.log("Second:" + attendeeMatch);

	if (attendeeMatch > 0) meetings.push(q);

}

// console.log(meetings)

dv.table(["Meeting", "Date", "Summary", "Project"], meetings.sort(m => m.date).map(m => ["[[" + m.file.name + "]]", m.date.toFormat("yyyy-MM-dd") + " (" + m.time + ")", m.summary, m.project ]))

// dv.list(meetings);
```
---
## Notes as author
```dataviewjs
let author = dv.current().file.name;
let authorNotes = [];
let query = dv.pages('-"900 ⌯ Supporting Files"')
	.where(
		p => p["author"]== author
	);

for (q of query) {
    authorNotes.push("[[" + q.file.name + "]]");
};

dv.list(authorNotes);
```
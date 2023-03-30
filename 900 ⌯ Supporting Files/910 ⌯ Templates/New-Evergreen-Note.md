---
excerpt:
fileClass: evergreen-note
score: x
category-evergreen-note:
reviewed: n
date: <% tp.date.now("YYYY-MM-DD") %>
last-review: <% tp.date.now("YYYY-MM-DD") %>
---
Tags::
# <% tp.file.title %>

<% tp.file.cursor(1) %>

---
#### 🏷️ Related by tag
~~~dataviewjs
let tags = this.current().file.tags
let notes = tags
	.map(t => dv.pages(t + ' and !"' + this.current().file.path + '"'));
dv.list(notes.file.link);
~~~
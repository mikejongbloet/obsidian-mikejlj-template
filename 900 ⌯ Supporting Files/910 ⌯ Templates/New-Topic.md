---
alias: []
excerpt:
fileClass: topic
score: x
category-topic:
reviewed: n
cover:
date: <% tp.date.now("YYYY-MM-DD") %>
last-review: <% tp.date.now("YYYY-MM-DD") %>
---
Related-Tag:: #

---
**Notes that haven't been processed**
~~~dataviewjs
let currentPage = this.current()
let tagRel = currentPage["Related-Tag"].split(" ").map(item => item.trim());

console.log(tagRel)

let notes = dv.pages('!"' + this.current().file.path + '"' )
			.where(p => !p.file.inlinks.includes(currentPage.file.link) & p.file.etags.some(r=> tagRel.includes(r)));
if (tagRel != "#dummytopic") {
	dv.list(notes.file.link);
}
~~~
---
# <% tp.file.title %>

<% tp.file.cursor(1) %>
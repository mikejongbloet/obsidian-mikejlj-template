---
alias: []
excerpt:
fileClass: topic
score: x
category-topic:
reviewed: n
cover:
date: 2023-03-30
last-review: 2023-03-30
---
Related tags:: #design-thinking #business 

---
**Notes that haven't been processed**
~~~dataviewjs
let currentPage = this.current()
let tagRel = currentPage["related-tags"].split(" ").map(item => item.trim());

console.log(tagRel)

let notes = dv.pages('!"' + this.current().file.path + '"' )
			.where(p => !p.file.inlinks.includes(currentPage.file.link) & tagRel.every(r=> p.file.etags.includes(r)));
if (tagRel != "#dummytopic") {
	dv.list(notes.file.link);
}
~~~
---
# Design Thinking and Business
* Add topic notes here
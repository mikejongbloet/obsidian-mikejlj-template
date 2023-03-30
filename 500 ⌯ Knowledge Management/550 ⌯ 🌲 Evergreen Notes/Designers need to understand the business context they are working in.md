---
excerpt:
fileClass: evergreen-note
score: x
category-evergreen-note:
reviewed: n
date: 2023-03-30
last-review: 2023-03-30
---
Tags:: #business #design #design-thinking 
# Designers need to understand the business context they are working in

As designers, we have a critical role in creating products, services, and experiences that align with the goals and objectives of the businesses we work for.

To achieve this, it's essential for us to understand the business context we're designing for. This involves researching and comprehending the [[target audience]], analyzing the [[competitive landscape]], understanding the company's [[brand values]] and [[positioning]], and its long-term strategic goals. 

By having this understanding, we can create designs that not only look visually appealing but also effectively communicate the company's messaging and objectives. This, in turn, results in more successful outcomes for the business. 

Understanding the business context also allows us to make informed decisions about design choices and prioritize our work effectively. 

Ultimately, as designers who understand the business context we're working in, we can create more impactful and effective designs that contribute to the success of the businesses we work for.

---
#### 🏷️ Related by tag
~~~dataviewjs
let tags = this.current().file.tags
let notes = tags
	.map(t => dv.pages(t + ' and !"' + this.current().file.path + '"'));
dv.list(notes.file.link);
~~~
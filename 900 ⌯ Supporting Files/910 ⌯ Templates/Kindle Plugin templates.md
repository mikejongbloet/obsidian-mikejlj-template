```
📙 {{title}} ({{firstAuthorLastName}})
```

---

```
---
fileClass: literature-note
score: xx
category-literature-note: kindle
reviewed: n
date: {{lastAnnotatedDate}}
last-review: {{lastAnnotatedDate}}
---
Tags:: 
# {{longTitle}}
**Author**:: {{author}}
**Rating**:: ⭐️⭐️⭐️⭐️⭐️

## Summary

---
## My thoughts


---

## Highlights
{{highlights}}

---

## Review

---

#### Related by tag

~~~dataviewjs
let tags = this.current().file.tags
let notes = tags
	.map(t => dv.pages(t + ' and !"' + this.current().file.path + '"'));
dv.list(notes.file.link);
~~~
```

---

```
> {{ text }}

{% if note %}
\```ad-note
{{note}}
\```

{% endif %}

⌯
```
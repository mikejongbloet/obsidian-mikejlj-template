---
banner: "https://images.unsplash.com/photo-1526779259212-939e64788e3c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2374&q=80"
banner_y: 0.172
banner_icon: 🍃
---
# 302 ⌯ Reflections log

```dataview
list 🍃-reflection
where 
	🍃-reflection and
	date >= date(today)-dur(1 month) and date <=date(today)
	sort date DESC
```
---
banner: "https://images.unsplash.com/photo-1507494924047-60b8ee826ca9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1973&q=80"
banner_y: 0.648
banner_icon: 💭
---
# 301 ⌯ Thoughts and ideas
## 💭 Recent thoughts
```dataview
list 💭-thought
where 
	💭-thought and
	date >= date(today)-dur(1 month) and date <=date(today)
	sort date DESC
```
## 💡Recent ideas
```dataview
list 💡-idea
where 
	💡-idea and
	date >= date(today)-dur(1 month) and date <=date(today)
sort date DESC
```
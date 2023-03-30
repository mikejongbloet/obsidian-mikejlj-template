---
banner: "https://images.unsplash.com/photo-1630852722667-ef9764a76b3e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2370&q=80"
banner_y: 0.78
---
# Reading list

`button-add-book` `button-add-article`

## Articles
```dataview 
TASK 
WHERE !completed 
AND contains(tags, "#to-read")
AND contains(tags, "#📝")
```
## Books
```dataview 
TASK 
WHERE !completed 
AND contains(tags, "#to-read")
AND contains(tags, "#📙")
```
---
alias: ['🕺 People', '🕺 People Dashboard']
banner_icon: 🕺
banner: "https://images.unsplash.com/20/bw-room.JPG?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1480&q=80"
banner_y: 0.62
---

# 391 ⌯ 🕺 People

```button
name 🕺 New Person
type command
action QuickAdd: 🕺 New Person
```
```dataviewjs
let i = 0;
let letter = "a";
let query = dv.pages('"300 ⌯ Journal/391 ⌯ 🕺 People"').where(p => p["relationship"]!= "none");
let name = "";
let lastName = "";
let people = [];

// generate each letter of the alphabet
for (i = 0; i < 26; i++) {
	people = [];
	letter = (i+10).toString(36).toUpperCase();

	for (q of query)
	{
		let name = q.file.name;
		let lastName = name.substr(name.indexOf(" ") + 1);
		let firstName = name.substr(0, name.length - lastName.length);

		if(lastName.charAt(0) === letter) people.push("[[" + q.file.name + "|" + lastName + ", " + firstName + "]]");
	}

	if(people.length > 0) {
		//document.write("## " + letter);
		dv.header(4, letter)
		dv.list(people);
	}
}


```
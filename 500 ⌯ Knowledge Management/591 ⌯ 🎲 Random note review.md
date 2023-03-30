---
banner: "https://images.unsplash.com/photo-1597591406871-b57baac13802?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1037&q=80"
banner_y: 0.548
exclude_from_graph: true
---
# 591 ⌯ 🎲 Random note review
```dataviewjs
let fileList = [];
let randomIndexes = [];
let itemsToPick = [];
let numItems = 5;

let query = dv.pages('-"900 ⌯ Supporting Files"').where(
	p => p["fileClass"] == "literature-note" ||
	p["fileClass"] == "evergreen-note" ||
	p["fileClass"] == "atomic-note" ||
	p["fileClass"] == "topic"
);

if(query.length > 0) {

  numItems = (numItems <= query.length) ? numItems : query.length;

  for (q of query) {
      fileList.push(q.file.name);
  };

  while (randomIndexes.length < numItems) {
    let randomIndex = Math.round(Math.random() * (fileList.length - 1));
    if(!randomIndexes.includes(randomIndex)) {
      randomIndexes.push(randomIndex)
    }
  }

  itemsToPick = randomIndexes.map(indexOfItem =>"[[" + fileList[indexOfItem] + "]]")

  dv.list(itemsToPick);

} else {
  dv.el("em","No notes to display.");
}
```
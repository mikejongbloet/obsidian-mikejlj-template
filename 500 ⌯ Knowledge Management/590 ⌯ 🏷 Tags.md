---
alias:
  - 🏷_Tags
  - 🏷_Tags Dashboard
tags:
  - dashboard
exclude_from_graph: true
---

# 590 ⌯ 🏷 Tags

```dataviewjs
let tags = dv.pages('-"900 ⌯ Supporting Files"').file.etags
	.distinct()
		.sort(t => dv.pages(t).length, "desc");
let tags_no_fileClassTag = tags
	.where(t => t!="#dashboard" && t!="#dummytopic" && t!="#task")
dv.table(
    ["Tag","Occurance"],
    tags_no_fileClassTag.map(t =>[
        t,
        dv.pages(t).length,
    ]
    )
);
```

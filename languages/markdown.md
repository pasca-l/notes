## [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

### Basic Syntax
Elements supported by all markdown applications

| Syntax | Code | View |
| ----------- | ----------- | ----------- |
| Header | #TEXT, ##TEXT, ###TEXT | <h1>TEXT</h1> <h2>TEXT</h2> <h3>TEXT</h3> |
| Bold | \*\*TEXT\*\* | <b>TEXT</b> |
| Italic | \*TEXT\* | <i>TEXT</i> |
| Blockquote| \>TEXT | <blockquote>TEXT</blockquote> |
| Ordered List | 1\.TEXT<br>2\.TEXT<br>3\.TEXT | <ol><li>TEXT</li><li>TEXT</li><li>TEXT</li></ol> |
| Unordered List | \-TEXT<br>\-TEXT<br>\-TEXT | <ul><li>TEXT</li><li>TEXT</li><li>TEXT</li></ul> |
| Code | \'TEXT\' | <code>TEXT</code> |
| Horizontal Rule | \--- | <hr> |
| Link | \[TEXT\]\(https://www.markdownguide.org\) | [TEXT](https://www.markdownguide.org) |
| Image | !\[TEXT\]\(https://www.markdownguide.org\) | ![TEXT](https://www.markdownguide.org/assets/images/tux.png) |


## Extended Syntax
Elements extended from basic syntax, not supported by all markdown applications


### Code

`code`

### Horizontal Rule

---

### Link

[Markdown Guide](https://www.markdownguide.org)

### Image

![alt text](https://www.markdownguide.org/assets/images/tux.png)

## Extended Syntax

These elements extend the basic syntax by adding additional features. Not all Markdown applications support these elements.

### Table

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

### Fenced Code Block

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

### Footnote

Here's a sentence with a footnote. [^1]

[^1]: This is the footnote.

### Heading ID

### My Great Heading {#custom-id}

### Definition List

term
: definition

### Strikethrough

~~The world is flat.~~

### Task List

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

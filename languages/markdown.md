## [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

### [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
Elements supported by all markdown applications

| Syntax | Code | View |
| --- | --- | --- |
| Header | # TEXT -> ###### TEXT | <h1>TEXT</h1> <h6>TEXT</h6> |
| Bold | \*\*TEXT\*\* | <b>TEXT</b> |
| Italic | \*TEXT\* | <i>TEXT</i> |
| Blockquote | \>TEXT | <blockquote>TEXT</blockquote> |
| Ordered List | 1\.TEXT<br>2\.TEXT<br>3\.TEXT | <ol><li>TEXT</li><li>TEXT</li><li>TEXT</li></ol> |
| Unordered List | \-TEXT<br>\-TEXT<br>\-TEXT | <ul><li>TEXT</li><li>TEXT</li><li>TEXT</li></ul> |
| Code | \'TEXT\' | <code>TEXT</code> |
| Horizontal Rule | \--- | <hr> |
| Link | \[TEXT\]\(https://www.markdownguide.org\) | [TEXT](https://www.markdownguide.org) |
| Image | !\[TEXT\]\(https://www.markdownguide.org\) | ![TEXT](https://www.markdownguide.org/assets/images/tux.png) |


## [Extended Syntax](https://www.markdownguide.org/extended-syntax/)
Elements extended from basic syntax, not supported by all markdown applications

| Syntax | Code | View |
| --- | --- | --- |
| Table | \| TEXT \|<br>\| --- \|<br>\| TEXT \| | |
| Fenced Code Block | \'''\{LANGUAGE_NAME} TEXT \''' | <codeblock>TEXT</codeblock> |
| Footnote | TEXT \[^1] | TEXT [^1] |
| Heading ID | \# TEXT \{#CUSTOM-ID} | <h1 id="custom-id">TEXT</h1> |
| Linking to Heading ID | \[TEXT]\(#CUSTOM-ID) | <a href="#custom-id">TEXT</a> |

[^1]: Footnote


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

# [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/) <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Basic Syntax](#basic-syntax)
- [Extended Syntax](#extended-syntax)
- [Highlighted codes](#highlighted-codes)
- [Math equations](#math-equations)
- [Preview on VSCode](#preview-on-vscode)

## [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
Elements supported by all markdown applications.

| Syntax | Code | View |
| --- | --- | --- |
| Header | # TEXT <br> ###### TEXT | <h1>TEXT</h1> <h6>TEXT</h6> |
| Bold | \*\*TEXT\*\* | <b>TEXT</b> |
| Italic | \*TEXT\* | <i>TEXT</i> |
| Blockquote | \>TEXT | <blockquote>TEXT</blockquote> |
| Ordered List | 1\.TEXT<br>2\.TEXT<br>3\.TEXT | <ol><li>TEXT</li><li>TEXT</li><li>TEXT</li></ol> |
| Unordered List | \-TEXT<br>\-TEXT<br>\-TEXT | <ul><li>TEXT</li><li>TEXT</li><li>TEXT</li></ul> |
| Code | \`TEXT\` | <code>TEXT</code> |
| Horizontal Rule | \--- | <hr> |
| Link | \[TEXT\]\(https://www.markdownguide.org\) | [TEXT](https://www.markdownguide.org) |
| Image | !\[TEXT\]\(https://www.markdownguide.org\) | ![TEXT](https://www.markdownguide.org/assets/images/tux.png) |

## [Extended Syntax](https://www.markdownguide.org/extended-syntax/)
Elements extended from basic syntax, not supported by all markdown applications.

| Syntax | Code | View |
| --- | --- | --- |
| Table | \| TEXT \|<br>\| --- \|<br>\| TEXT \| | |
| Fenced Code Block | \```\{LANGUAGE_NAME}<br>TEXT \``` | ```TEXT``` |
| Footnote | TEXT \[^1] | TEXT [^1] |
| Heading ID | \# TEXT \{#CUSTOM-ID} | <h1 id="custom-id">TEXT</h1> |
| Linking to Heading ID | \[TEXT]\(#CUSTOM-ID) | <a href="#custom-id">TEXT</a> |
| Definition | TEXT<br>\: TEXT | <dl><dt>TEXT</dt><dd>TEXT</dd></dl> |
| Strikethrough | \~\~TEXT\~\~ | <strike>TEXT</strike> |
| Task List | \- \[x] TEXT<br>\- \[ ] TEXT | <ul><li>[x] TEXT</li><li>[ ] TEXT</li></ul> |

[^1]: Footnote

## Highlighted codes
python code
```python
print("hello, world!")
```

javascript code
```javascript
console.log("hello, world!");
```

## Math equations
Written equivalent to TeX notation.

| Syntax | Code | View |
| --- | --- | --- |
| Equation | \```math<br>\e^{i\pi}=-1 \``` | ![e^{i\pi}=-1](https://latex.codecogs.com/gif.latex?e^{i\pi}=-1) [^eqongithub] |

[^eqongithub]: As GitHub does not render equations within code blocks, image from [CODECOGS](https://www.codecogs.com/latex/eqneditor.php) used instead.

## Preview on VSCode
`command` + `shift` + `V`
opens the preview on VSCode.

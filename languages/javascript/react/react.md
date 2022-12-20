# React Cheat Sheet

## Using React
To use React, the following scripts are used (loaded externally from unpkg.com):
- react: core React library
- react-dom: provides DOM-specific methods
```html
<!-- index.html -->
<html>
  <body>
    <div id="app"></div>

    <script src="https://unpkg.com/react@17/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@17/umd/react-dom.development.js"></script>

  </body>
</html>
```

With React, the code can be written declaratively, instead of imperative JavaScript code.
```html
<!-- index.html -->
<!-- in <body> -->
<script type="text/jsx">
  const app = document.getElementById("app")
  ReactDOM.render(<h1>Hello World!</h1>, app)
</script>

<!-- instead of -->
<script type="text/javascript">
  const app = document.getElementById('app');
  const header = document.createElement('h1');
  const headerContent = document.createTextNode('Hello World!');
  header.appendChild(headerContent);
  app.appendChild(header);
</script>
```
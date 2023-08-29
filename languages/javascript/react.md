# React.js Cheat Sheet <!-- omit in toc -->

## Table of Content <!-- omit in toc -->
- [Using React](#using-react)
  - [Components](#components)
  - [Props](#props)
  - [State](#state)
- [Creating project](#creating-project)

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

With React, the code can be written declaratively, instead of imperative JavaScript code. Note that, `<h1>...</h1>` inside `ReactDOM` method would give a syntax error, due to the code being JSX and not valid JavaScript. Therefore, for the browser to understand JSX, JavaScript compiler, such as Babel, needs to transform the JSX script.
```html
<!-- index.html, in <body> -->

<!-- loading Babel -->
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<script type="text/jsx">
  const app = document.getElementById("app");
  ReactDOM.render(<h1>Hello World!</h1>, app);
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

### Components
User interfaces can be broken into small building blocks called components. By using this modularity, the project becomes more maintainable. React components should be capitalized to distinguish them from plain HTML and JavaScript, and used with angle brackets.
```html
<!-- index.html, in <body> -->
<script type="text/jsx">
  const app = document.getElementById("app");

  // React component
  function Header() {
    return <h1>Hello World!</h1>;
  }

  ReactDOM.render(<Header />, app);
</script>
```

### Props
React components can have properties passed to it. Like HTML attributes, the props are accepted as the component's first function parameter as an object.
```html
<!-- index.html, in <body> -->
<script type="text/jsx">
  const app = document.getElementById("app");

  // React component
  function Header({ title }) {
    return <h1>{title}</h1>;
  }

  ReactDOM.render(<Header title="Hello World!"/>, app);
</script>
```
- If the component is used as a regular HTML tag, the text appears in between the tags. This text can be accessed by `children`.

### State
User interfaces can change according to the state of the React component. Hooks can be used to add additional logic of state to the component without writing a class.
```html
<!-- index.html, in <body> -->
<script type="text/jsx">
  const app = document.getElementById("app");

  // React component
  function Header({ title }) {
    const [num, setNum] = React.useState(0);

    function handleClick() {
      setNum(num + 1);
    }

    return (
      <h1>`${title} ${num}`</h1>
      <div>
        <button onClick={handleClick}>Add</button>
      </div>
    );
  }

  ReactDOM.render(<Header title="Hello World!"/>, app);
</script>
```
- Because changing state triggers re-rendering of the component, conflicting interactions between functions can take place. To skip unnecessary processes, `useEffect(()=>{}, [])` can be used.

## Creating project
Create a template React project.
```
$ npx create-react-app PROJECT_DIRECTORY
```
Under PROJECT_DIRECTORY, files are set up automatically.
```
PROJECT_DIRECTORY
  |- src/
  |- public/
  |- package.json
  |- node_modules/
  |- ...
```
- `src` directory, holds files in the unit of pages.
- `public` directory, stores static assets including images, fonts and etc.
- `package.json` file, is for recording dependencies.
- `node_modules` directory, holds all dependencies.

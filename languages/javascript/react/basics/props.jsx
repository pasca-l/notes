// referenced "Passing Props to a Component" (https://react.dev/learn/passing-props-to-a-component)

// components can receive props by the `props` variable, or by destructuring
// receiving props directly
function Component(props) {
  let arg1 = props.arg1;
  let arg2 = props.arg2;
  // ...
}
// receiving props with destructuring
// default value can be given, for missing or undefined props
function Component({ arg1, arg2 = 1 }) {
  // ...
}

// all props received by the component can be forwarded using a spread syntax
function Component(props) {
  return (
    <>
      {/* use of spread sytax */}
      <ChildComponent {...props} />
    </>
  );
}

// JSX itself can also be passed through by the `children` prop
function Component({ children }) {
  return <>{children}</>;
}
// which is then used by some parent component
// for example, <Component><ChildComponent /></Component>

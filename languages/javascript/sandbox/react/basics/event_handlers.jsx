// referenced "Responding to Events" (https://react.dev/learn/responding-to-events)

// event handlers are passed in as props to an appropriate JSX tag,
// which are usually defined inside the component,
// with naming convention of `handle` + event name
function Button() {
  function handleClick() {
    alert("Clicked!");
  }

  return (
    // handlers can also be defined inline, such as using arrow functions
    // note that the handler function in not called, and just passed
    <button onClick={handleClick}>button</button>
  );
}

// events get propagated ("bubbles") up the tree,
// meaning that event handlers attach to the tags above fires as well
function ButtonWithNoPropagation({ onClick, children }) {
  return (
    <>
      <button
        onClick={(e) => {
          // event handlers receive event objects, conventionally named as `e`
          // event objects allows to stop propagation
          e.stopPropagation();
          onClick();
        }}
      >
        {children}
      </button>

      <form
        onSubmit={(e) => {
          // some browser events have default behaviors, which can be stopped
          e.preventDefault();
          alert("submit!");
        }}
      ></form>
    </>
  );
}

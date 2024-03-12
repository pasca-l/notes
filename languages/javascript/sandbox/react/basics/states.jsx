// referenced "Adding interactivity" (https://react.dev/learn/adding-interactivity)
// - "State: A Component's Memory"
// - "State as a Snapshot"
// - "Queueing a Series of State Updates"
// - "Updating Objects in State"
// - "Updating Arrays in State"

// event handlers are able to change something,
// however 2 things prevent these changes to be visible
// - local variables are not persistent between renders
// - changes to local variables does not trigger renders

// using the `useState` Hook, data can be retained, and trigger render on change
import { useState } from "react";

function Component() {
  // `useState` gives back an array of a state variable and a setter function
  // states are private to the component
  const [index, setIndex] = useState(0);

  // as state can hold any kind of JavaScript value, such as objects and lists,
  // but needs to be treated as read-only (as immutable value)
  const [position, setPosition] = useState({
    x: 0,
    y: 0,
    other: "other",
  });
  const [todos, setTodos] = useState([]);

  return (
    <>
      <button
        onClick={() => {
          // React stores states outside of the component,
          // thus giving a snapshot of the state of the current render
          // (a state variable's value does not change within a render)
          setIndex(index + 1);

          // even if another increment code is implemented as below,
          // within the same render, "index" has the same value as above,
          // resulting in only a single incrementation (eg. setIndex(0 + 1);)
          setIndex(index + 1);

          // React also waits until all code is ran before state update,
          // therefore, updating multiple state is also possible (batching)
          // giving updater functions queues the process of states
          setIndex((idx) => idx + 1);
        }}
      >
        increment
      </button>

      <div
        // objects are updated by passing a new object into the setter function
        onPointerMove={(e) => {
          setPosition({ ...position, x: e.clientX, y: e.clientY });
          // if a property can be set dynamically, [] can be used
          // eg. setPosition({ ...position, [e.target.name]: e.target.value })
        }}
      >
        ...
      </div>

      <div
        onClick={(e) => {
          // common array operations and methods are in the table below:
          //           | mutating methods         | non-mutating methods
          // --------- | ------------------------ | --------------------
          // adding    | `push`, `unshift`        | `concat`, `[...arr]`
          // removing  | `pop`, `shift`, `splice` | `filter`, `slice`
          // replacing | `splice`, `arr[i] = ...` | `map`
          // sorting   | `reverse`, `sort`        | copy array first

          // non-mutating methods should be used on arrays
          setTodos([...todos, "clicked!"]);
        }}
      ></div>
    </>
  );
}

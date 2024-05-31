// referenced "Referencing Values with Refs" (https://react.dev/learn/referencing-values-with-refs)
// referenced "Manipulating the DOM with Refs" (https://react.dev/learn/manipulating-the-dom-with-refs)

// for a component to remember information without triggering new renders,
// `useRef` Hook can be used
import { useRef } from "react";

function Component() {
  const ref = useRef(0);
  const domRef = useRef(null);

  function handler() {
    // ref value is accessed by `ref.current`, which is mutable
    ref.current = ref.current++;
  }

  return (
    <>
      {/* to access a DOM node, pass the ref to the `ref` attribute */}
      {/* this will allow the use of built-in browser APIs, */}
      {/* eg. domRef.current.focus(), domRef.current.scrollIntoView() */}
      <div ref={domRef}></div>
      {/* it is recommended to avoid changing DOM mangaed by React */}
    </>
  );
}

// React components does not let access to the DOM node,
// therefore a component needs to opt in this behavior by forwarding the ref
import { forwardRef } from "react";
const InputComponent = forwardRef((props, ref) => {
  return <input {...props} ref={ref} />;
});

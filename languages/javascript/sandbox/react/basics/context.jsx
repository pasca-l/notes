// referenced "Passing Data Deeply with Context" (https://react.dev/learn/passing-data-deeply-with-context)

// context allows parent components to provide data to the entire tree below,
// in contrast to explicitly piping data by passing props

// context is firstly created in a file and exported
import { createContext } from "react";
export const LevelContext = createContext(1);

// context is then used in the components
import { useContext } from "react";
import { LevelContext } from "./LevelContext.jsx";

function Heading({ children }) {
  // the `level` prop is moved inside of the component, reading the context
  const level = useContext(LevelContext);
  // ...
}

// context needs to be provided in some other component
function Section({ level, children }) {
  return (
    <section>
      {/* this tells if any component inside asks for the context, */}
      {/* the value is given from the nearest provider */}
      <LevelContext.Provider value={level}>{children}</LevelContext.Provider>
    </section>
  );
}

// for the `Section` component can also figure its `level` automatically
function Section({ level, children }) {
  const level = useContext(LevelContext);
  return (
    <section>
      {/* `level` is incremented for `Section` components inside */}
      <LevelContext.Provider value={level + 1}>
        {children}
      </LevelContext.Provider>
    </section>
  );
}

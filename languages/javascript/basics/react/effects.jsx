// referenced "Synchronizing with Effects" (https://react.dev/learn/synchronizing-with-effects)

// Effects lets some code run after rendering (end of a commit) to synchronize
// components with external system outside of React
import { useEffect } from "react";

function VideoPlayer({ src, isPlaying }) {
  const ref = useRef(null);

  // with `useEffect`, lets React update the screen first, and then the Effect
  useEffect(
    () => {
      // without `useEffect`, the logic below causes side effect during render,
      // therefore needs to be moved out of the rendering calculation
      if (isPlaying) {
        ref.current.play();
      } else {
        ref.current.pause();
      }

      // cleanup functions are called each time before Effect runs again,
      // and a final time when the component gets unmounted (removed)
      return () => {
        // ... eg. disconnecting an established connection
      };
    },

    // unnecessary re-running can be skipped by giving an array of dependencies,
    // if the dependency value is the same as the previous render, no re-run
    [isPlaying]
    // empty dependency array [], runs only on mount (when components appear)
  );

  return <video ref={ref} src={src} loop playsInline />;
}

// referenced "Reusing Logic with Custom Hooks" (https://react.dev/learn/reusing-logic-with-custom-hooks)

import { useState, useEffect } from "react";

// custom Hooks can be used to extract repetetive component logics,
// especially details of how external systems or browsers are dealt
function useOnlineStatus() {
  const [isOnline, setIsOnline] = useState(true);

  useEffect(() => {
    function handleOnline() {
      setIsOnline(true);
    }
    function handleOffline() {
      setIsOnline(false);
    }

    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);

  return isOnline;
}

// components read values given back from custom Hooks,
// which allows synchronization with some shared external value
function StatusBar() {
  const isOnline = useOnlineStatus();
  return <h1>{isOnline ? "Online!!!" : "Disconnected ..."}</h1>;
}

function StatusButton() {
  const isOnline = useOnlineStatus();
  return (
    <button
      disabled={!isOnline}
      onClick={() => {
        console.log("clicked");
      }}
    >
      {isOnline ? "Press while online!!!" : "Offline ..."}
    </button>
  );
}

function App() {
  return (
    <>
      {/* both of the components will synchronize according to online status */}
      <StatusBar />
      <Statusbutton />
    </>
  );
}

// referenced "Extracting State Logic into a Reducer" (https://react.dev/learn/extracting-state-logic-into-a-reducer)

// state update logic can be moved out of the component in a reducer function
// instead of setting state, action objects are dispatched on events
import { useReducer } from "react";

function TaskApp() {
  const [tasks, dispatch] = useReducer(taskReducer, initialTasks);
  const initialTasks = [];
  let taskId = 1;

  function handleAddTask() {
    // action object is dispatched, instead of raw logics
    dispatch({
      type: "added",
      id: taskId++,
    });
  }

  function handleChangeTask(task) {
    dispatch({
      type: "changed",
      task: task,
    });
  }

  function handleDeleteTask(targetId) {
    dispatch({
      type: "deleted",
      id: targetId,
    });
  }

  return (
    <>
      {/* example components that uses the event handlers */}
      <AddTask onAddTask={handleAddTask} />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

// reducer function, takes in the current state and the action object,
// and returns the next state
function taskReducer(tasks, action) {
  switch (action.type) {
    case "added": {
      return [
        ...tasks,
        {
          id: action.id,
          // ...
        },
      ];
    }
    case "changed": {
      return tasks.map((t) => {
        if (t.id === action.task.id) {
          return action.task;
        } else {
          return t;
        }
      });
    }
    case "deleted": {
      return tasks.filter((t) => t.id !== action.id);
    }
    default: {
      throw Error("unknown action: " + action.type);
    }
  }
}

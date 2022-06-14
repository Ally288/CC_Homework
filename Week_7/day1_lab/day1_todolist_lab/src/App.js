import './App.css';
import React, {useState} from 'react';

function App() {

  const [task, setTask] = useState([
    {name: "Feed Dog", priority: "High"},
    {name: "Clean Kitchen", priority: "Low"},
    {name: "Wash Car", priority: "High"},
  ]);

  const [newTask, setNewTask] = useState("");
  const [newPriority, setNewPriority] = useState("")

  const taskLists = task.map((task, index) => {
    return(
      <li key={index} className={task.priority === "High" ? "high-priority" : "low-priority"}><span>{task.name}</span>{}
      </li>
    )
  })

  const handleTaskInput = (event) => {
    setNewTask(event.target.value);
  }

  const saveNewTask = (event) => {
    event.preventDefault();
    const copyTasks = [...task, {name: newTask, priority: newPriority}];
    copyTasks.push({name: newTask})
    setTask(copyTasks)
    setNewTask("")
    setNewPriority("")
    event.target.reset();
  }

  const handleTaskPriority = (event) => {
    setNewPriority(event.target.value);
  }


  return (
    <div className="App">

      <h1>ToDo's Task List</h1>
      <hr></hr>

      <form onSubmit={saveNewTask}>
        <label htmlFor="new-task">Add a new ToDo task:</label>
        <input id="new-task" type="text" value={newTask} onChange={handleTaskInput} />
        <input type="radio" id="high" value="High" name="priority" onChange={handleTaskPriority}/>High
        <input type="radio" id="low" value="Low" name="priority" onChange={handleTaskPriority}/>Low
        <input type="submit" value="Save New Task" className={"button"} />
      </form>

      <ul>
        {taskLists}
      </ul>

    </div>
  );
}

export default App;

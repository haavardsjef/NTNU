// Event listener, when user clicks sumbit, run addTask function
document.addEventListener("submit", addTask);

// Document selectors
input = document.getElementById("todo");
ul = document.getElementById("todo-list");

// Task list
const tasks = [
  { id: 0, name: "Todo1", completed: false, timestamp: Date() },
  { id: 1, name: "Todo2", completed: false, timestamp: Date() },
];

// IDCOUNTER
let idCounter = 2;

function addTask(event) {
  event.preventDefault(); // Prevent page from reloading
  if (input.value != "") {
    tasks.unshift({
      // The unshift method adds to begining of array, keeping the order we wanted
      id: idCounter,
      name: input.value,
      completed: false,
      timestamp: Date(),
    });
    idCounter++;
    drawList();
    console.log(tasks);
  } else {
    console.error("Cant add empty todo");
  }
}

function drawList() {
  ul.innerHTML = ""; // Clear list
  let completed = 0; // Keep track of how many are completed
  tasks.forEach((task) => {
    // Create checkbox
    const checkbox = document.createElement("input");
    checkbox.setAttribute("type", "checkbox");
    checkbox.setAttribute("id", task.id);
    checkbox.addEventListener("click", taskChecked(tasks.indexOf(task)));

    // Create label for checkbox
    const label = document.createElement("label");
    label.setAttribute("for", task.id);
    label.innerText = task.name;

    // If the task is checked
    if (task.completed) {
      completed++; // Keep track of how many are completed
      checkbox.setAttribute("checked", true);
      label.style.textDecoration = "line-through";
    }

    // Create LI and add checkbox and label, then add to list
    const li = document.createElement("li");
    li.appendChild(checkbox);
    li.appendChild(label);
    ul.appendChild(li);
  });
}

function taskChecked(event) {
  const index = event.target.id;
  tasks[index].completed = !tasks[index].completed;
  redrawList();
}

drawList();

// Event listener, when user clicks sumbit, run addTask function
document.addEventListener("submit", addTask);

// Document selectors
input = document.getElementById("todo");
ul = document.getElementById("todo-list");

// Task list
const tasks = [
  { id: 0, name: "Clean the dishes", completed: false, timestamp: Date() },
  { id: 1, name: "Walk the dog", completed: false, timestamp: Date() },
];

// IDCOUNTER
let idCounter = 2; // Starts at 2 since we have 0,1 as example todos

function addTask(event) {
  // Add task to tasklist
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
    checkbox.addEventListener("change", function () {
      if (this.checked) {
        // If checkbox is checked
        tasks[tasks.indexOf(task)].completed = true;
        drawList();
      } else {
        // If checkbox is not checked
        tasks[tasks.indexOf(task)].completed = false;
        drawList();
      }
    });

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
  // Updated completed and total counter
  document.getElementById("completed-count").innerHTML = completed;
  document.getElementById("task-count").innerHTML = tasks.length;
}

drawList();

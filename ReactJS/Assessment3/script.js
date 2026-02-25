const form = document.getElementById("todoForm");
const input = document.getElementById("todoInput");
const list = document.getElementById("todoList");
const error = document.getElementById("error");

// Load todos from localStorage
let todos = JSON.parse(localStorage.getItem("todos")) || [];
renderTodos();

// ADD TODO
form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (input.value.trim() === "") {
    error.textContent = "Task can not be empty!";
    return;
  }

  error.textContent = "";

  const todo = {
    text: input.value,
    completed: false
  };

  todos.push(todo);
  saveTodos();
  renderTodos();
  input.value = "";
});

// EVENT DELEGATION (delete / complete)
list.addEventListener("click", function (e) {

  // MARK COMPLETE
  if (e.target.classList.contains("todo-text")) {
    const index = e.target.dataset.index;
    todos[index].completed = !todos[index].completed;
  }

  // DELETE
  if (e.target.classList.contains("delete")) {
    const index = e.target.dataset.index;
    todos.splice(index, 1);
  }

  saveTodos();
  renderTodos();
});

// SAVE TO LOCALSTORAGE
function saveTodos() {
  localStorage.setItem("todos", JSON.stringify(todos));
}

// DISPLAY TODOS
function renderTodos() {
  list.innerHTML = "";

  todos.forEach((todo, index) => {
    const li = document.createElement("li");

    li.innerHTML = `
      <span class="todo-text ${todo.completed ? "completed" : ""}" data-index="${index}">
        ${todo.text}
      </span>
      <button class="delete" data-index="${index}">X</button>
    `;

    list.appendChild(li);
  });
}

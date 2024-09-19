document.addEventListener("DOMContentLoaded", () => {
  // User registration flow
  const registerForm = document.getElementById("register-form");
  if (registerForm)
    registerForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const username = document.getElementById("username").value,
        password = document.getElementById("password").value;

      try {
        const res = await fetch("http://127.0.0.1:8000/cadastro/create", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, password }),
        });

        const msgEl = document.getElementById("message");
        if (res.ok) {
          msgEl.textContent =
            "User registered successfully! Redirecting to the to-do list...";
          setTimeout(() => (window.location.href = "todo.html"), 2000);
        } else {
          const errData = await res.json();
          msgEl.textContent = errData.detail || "Failed to register user.";
        }
      } catch (error) {
        console.error("Error:", error);
        document.getElementById("message").textContent = "An error occurred.";
      }
    });

  // Task submission flow
  const taskForm = document.getElementById("task-form");
  if (taskForm)
    taskForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const taskDesc = document.getElementById("task-desc").value,
        taskStart = document.getElementById("task-start").value,
        taskEnd = document.getElementById("task-end").value;

      if (!taskDesc || !taskStart || !taskEnd) {
        alert("All fields are required");
        return;
      }

      // Create task object
      const task = {
        description: taskDesc,
        start: taskStart,
        end: taskEnd,
        completed: false,
      };

      // Add task to the list
      addTaskToList(task);

      // Clear form fields
      taskForm.reset();
    });
});

function addTaskToList(task) {
  const taskList = document.getElementById("task-list");

  // Create task container
  const taskItem = document.createElement("div");
  taskItem.classList.add("task-item");

  // Create checkbox
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.addEventListener("change", function () {
    task.completed = checkbox.checked;
    taskItem.classList.toggle("completed", task.completed);
  });

  // Create task description
  const taskDescription = document.createElement("span");
  taskDescription.textContent = `${task.description} (from: ${task.start} to: ${task.end})`;

  // Append checkbox and description to task item
  taskItem.appendChild(checkbox);
  taskItem.appendChild(taskDescription);

  // Append task item to task list
  taskList.appendChild(taskItem);
}

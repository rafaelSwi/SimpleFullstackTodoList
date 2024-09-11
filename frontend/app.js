document.addEventListener("DOMContentLoaded", function () {
  // Check if we're on the registration page and if the registration form exists
  const registerForm = document.getElementById("register-form");
  if (registerForm) {
    registerForm.addEventListener("submit", async function (event) {
      event.preventDefault(); // Prevent the form from refreshing the page

      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;

      try {
        // API request to register the user
        const response = await fetch("http://127.0.0.1:8000/cadastro/create", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
          const data = await response.json();
          document.getElementById("message").textContent =
            "User registered successfully!";

          console.log("User registered, creating button...");

          // to-do list
          const todoButton = document.createElement("button");
          todoButton.textContent = "Go to To-Do List";
          todoButton.onclick = () => {
            window.location.href = "todo.html";
          };

          document.getElementById("message").appendChild(todoButton);
          console.log("Button created and appended.");
        } else if (response.status === 400) {
          const errorData = await response.json();
          document.getElementById("message").textContent = errorData.detail;
        } else {
          document.getElementById("message").textContent =
            "Failed to register user.";
        }
      } catch (error) {
        console.error("Error:", error);
        document.getElementById("message").textContent = "An error occurred.";
      }
    });
  }

  // Check if we're on the to-do list page and if the task form exists
  const taskForm = document.getElementById("task-form");
  if (taskForm) {
    taskForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const taskDesc = document.getElementById("task-desc").value;
      const taskStart = document.getElementById("task-start").value;
      const taskEnd = document.getElementById("task-end").value;

      console.log("Task Description:", taskDesc);
      console.log("Task Start Date:", taskStart);
      console.log("Task End Date:", taskEnd);

      const taskList = document.getElementById("task-list");
      const taskItem = document.createElement("div");
      taskItem.textContent = `${taskDesc} (From: ${taskStart} To: ${taskEnd})`;
      taskList.appendChild(taskItem);
    });
  }
});

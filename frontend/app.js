document.addEventListener("DOMContentLoaded", () => {
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
            "User registered successfully! Redirecting to the To-Do List...";
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

  const taskForm = document.getElementById("task-form");
  if (taskForm)
    taskForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const taskDesc = document.getElementById("task-desc").value,
        taskStart = document.getElementById("task-start").value,
        taskEnd = document.getElementById("task-end").value;
      console.log("Task:", taskDesc, taskStart, taskEnd);
      const taskItem = document.createElement("div");
      taskItem.textContent = `${taskDesc} (From: ${taskStart} To: ${taskEnd})`;
      document.getElementById("task-list").appendChild(taskItem);
    });
});

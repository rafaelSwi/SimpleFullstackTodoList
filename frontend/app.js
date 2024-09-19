document.addEventListener("DOMContentLoaded", () => {
  // seleciona o formulário de registro quando o documento é carregado
  const registerForm = document.getElementById("register-form");
  if (registerForm)
    // adiciona um evento de "submit" ao formulário de registro
    registerForm.addEventListener("submit", async (e) => {
      e.preventDefault(); // impede o comportamento padrão de recarregar a página
      // obtém os valores dos campos de nome de usuário e senha
      const username = document.getElementById("username").value,
        password = document.getElementById("password").value;
      try {
        // envia uma requisição POST para o backend para criar um novo usuário
        const res = await fetch("http://127.0.0.1:8000/cadastro/create", {
          method: "POST",
          headers: { "Content-Type": "application/json" }, // define o tipo de conteúdo como JSON
          body: JSON.stringify({ username, password }), // envia os dados do formulário no corpo da requisição
        });
        // seleciona o elemento de mensagem para exibir o resultado da requisição
        const msgEl = document.getElementById("message");
        if (res.ok) {
          // se a resposta for bem-sucedida, exibe uma mensagem de sucesso
          msgEl.textContent =
            "user registered successfully! redirecting to the to-do list...";
          // redireciona para a página da lista de tarefas após 2 segundos
          setTimeout(() => (window.location.href = "todo.html"), 2000);
        } else {
          // se a resposta falhar, exibe a mensagem de erro do backend ou uma mensagem padrão
          const errData = await res.json();
          msgEl.textContent = errData.detail || "failed to register user.";
        }
      } catch (error) {
        // em caso de erro, exibe uma mensagem de erro no console e na página
        console.error("error:", error);
        document.getElementById("message").textContent = "an error occurred.";
      }
    });

  // seleciona o formulário de tarefas
  const taskForm = document.getElementById("task-form");
  if (taskForm)
    // adiciona um evento de "submit" ao formulário de tarefas
    taskForm.addEventListener("submit", (e) => {
      e.preventDefault(); // impede o comportamento padrão de recarregar a página
      // obtém os valores dos campos de descrição, data de início e data de término da tarefa
      const taskDesc = document.getElementById("task-desc").value,
        taskStart = document.getElementById("task-start").value,
        taskEnd = document.getElementById("task-end").value;
      // exibe os valores no console para depuração
      console.log("task:", taskDesc, taskStart, taskEnd);
      // cria um novo elemento de div para exibir a tarefa
      const taskItem = document.createElement("div");
      // define o texto do novo elemento como a descrição e datas da tarefa
      taskItem.textContent = `${taskDesc} (from: ${taskStart} to: ${taskEnd})`;
      // adiciona o novo elemento de tarefa à lista de tarefas
      document.getElementById("task-list").appendChild(taskItem);
    });
});

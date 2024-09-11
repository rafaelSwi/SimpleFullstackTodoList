document
  .getElementById("register-form")
  .addEventListener("submit", async function (event) {
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
        console.log(data);
      } else if (response.status === 400) {
        // Handle the "Username already taken" case
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

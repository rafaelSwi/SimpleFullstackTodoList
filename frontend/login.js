const API_URL = 'http://localhost:8000';  // Altere para a URL da sua API FastAPI

// Função para autenticar o usuário e obter o token
async function login(username, password) {
    const response = await fetch(`${API_URL}/get`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            username: username,
            password: password
        })
    });

    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('access_token', data.access_token);
        alert('Login bem-sucedido!');
        // Redirecionar ou carregar a página principal após login
    } else {
        alert('Erro ao fazer login. Verifique suas credenciais.');
    }
}

// Evento de envio do formulário de login
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    await login(username, password);
});

<template>
  <div class="login-container">
    <div class="login-box">
      <img src="/logo-infl.png" alt="Logo" class="login-logo">
      <h2>Iniciar sesión</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" placeholder="Nombre de usuario" />
        <input type="password" v-model="password" placeholder="Contraseña" />
        <button type="submit">Iniciar sesión</button>
      </form>

      <!-- Mostrar mensaje de error si el login falla -->
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '' 
    };
  },
  methods: {
    async handleLogin() {
      this.errorMessage = ''; 
      try {
        const response = await axios.post('http://192.168.1.2:5000/logedbd', {
          nombre_usuario: this.username,
          password: this.password
        });

        if (response.data.status === 'success') {
          localStorage.setItem('isAuthenticated', 'true');
          this.$router.push('/dashboard');
        } else {
          this.errorMessage = 'Usuario o contraseña incorrectos'; 
        }
      } catch (error) {
        console.error("Hubo un error en el login:", error);
        this.errorMessage = 'Usuario o Contraseña Incorrectos. .'; 
      } finally {
        this.username = '';
        this.password = '';
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #2c2c2c;
}

.login-box {
  background-color: #000;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  width: 300px;
  text-align: center;
}

.login-logo {
  width: 200px;
  margin-bottom: 20px;
}

.login-box h2 {
  color: #ff4c4c;
  text-align: center;
  margin-bottom: 20px;
}

.login-box input {
  width: 90%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ff4c4c;
  border-radius: 4px;
  background-color: #333;
  color: #fff;
}

.login-box button {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 4px;
  background-color: #ff4c4c;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.login-box button:hover {
  background-color: #e03a3a;
}


.error-message {
  color: #ff4c4c;
  margin-top: 10px;
}
</style>

<style>
  html, body {
    margin: 0;
    padding: 0;
    height: 100%;
    background-color: #2c2c2c; 
  }

  #app {
    height: 100%;
  }
</style>

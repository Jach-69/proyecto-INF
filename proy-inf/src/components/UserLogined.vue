<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Iniciar sesión</h2>
      <form @submit.prevent="handleLogin">
        <input v-model="username" placeholder="Nombre de usuario" />
        <input type="password" v-model="password" placeholder="Contraseña" />
        <button type="submit">Iniciar sesión</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('http://192.168.0.109:5000/logedbd', {
          nombre_usuario: this.username,
          password: this.password
        });

        if (response.data.status === 'success') {
          console.log(response.data.message);
          this.$router.push('/dashboard');
        } else {
          console.log(response.data.message);
        }
      } catch (error) {
        console.error("Hubo un error en el login:", error);
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
</style>

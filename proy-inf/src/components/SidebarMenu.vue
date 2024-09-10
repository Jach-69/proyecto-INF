<template>
  <div class="sidebar-menu">
    <div class="logo-container">
      <img src="/logo-infl.png" alt="Logo" class="logo" />
    </div>
    <ul>
      <li @click="navigateTo('create')">Crear Acceso</li>
      <li @click="navigateTo('list')">Lista de Accesos</li>
      <li @click="logout">Cerrar Sesión</li>
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    navigateTo(route) {
      this.$router.push(`/dashboard/${route}`);
    },
    logout() {
      // Limpiar la sesión o token y redirigir a la pantalla de login
      localStorage.removeItem('token');
      this.$router.push('/');
    }
  }
};
</script>


<style scoped>
.sidebar-menu {
  width: 250px;
  background-color: #1e1e1e;
  height: 100vh;
  padding: 20px;
  color: white;
}

.logo-container {
  text-align: center;
  margin-bottom: 30px;
}

.logo {
  width: 150px;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  padding: 15px;
  cursor: pointer;
  background-color: #ff4c4c;
  margin-bottom: 10px;
  text-align: center;
}

ul li:hover {
  background-color: #e03a3a;
}
</style>

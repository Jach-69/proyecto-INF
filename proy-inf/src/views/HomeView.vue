<template>
  <div>
    <h1>Accesos</h1>
    
    <!-- Formulario para agregar acceso -->
    <div>
      <h2>Agregar acceso</h2>
      <form @submit.prevent="createAccess">
        <label>Clave:</label>
        <input v-model="newAccess.clave" type="text" required />

        <label>Tarjeta RFID:</label>
        <input v-model="newAccess.tarjeta_rfid" type="text" required />

        <label>Nombre Usuario:</label>
        <input v-model="newAccess.nombre_usuario" type="text" required />

        <button type="submit">Agregar</button>
      </form>
    </div>

    <!-- Mostrar accesos -->
    <div>
      <h2>Lista de accesos</h2>
      <ul>
        <li v-for="acceso in accesos" :key="acceso.id">
          {{ acceso.nombre_usuario }} (Clave: {{ acceso.clave }}, RFID: {{ acceso.tarjeta_rfid }})
          <button @click="deleteAccess(acceso.id)">Eliminar</button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      accesos: [],
      newAccess: {
        clave: '',
        tarjeta_rfid: '',
        nombre_usuario: ''
      }
    }
  },
  methods: {
    // Obtener todos los accesos
    getAccesses() {
      axios.get('http://localhost:5000/accesos')
        .then(response => {
          this.accesos = response.data;
        })
        .catch(error => {
          console.error("Error obteniendo accesos:", error);
        });
    },
    // Crear nuevo acceso
    createAccess() {
      axios.post('http://localhost:5000/accesos', this.newAccess)
        .then(response => {
          this.accesos.push(response.data); // Agregar nuevo acceso a la lista
          this.newAccess = { clave: '', tarjeta_rfid: '', nombre_usuario: '' }; // Limpiar formulario
        })
        .catch(error => {
          console.error("Error creando acceso:", error);
        });
    },
    // Eliminar un acceso
    deleteAccess(id) {
      axios.delete(`http://localhost:5000/accesos/${id}`)
        .then(() => {
          this.accesos = this.accesos.filter(acceso => acceso.id !== id); // Filtrar lista de accesos
        })
        .catch(error => {
          console.error("Error eliminando acceso:", error);
        });
    }
  },
  mounted() {
    this.getAccesses(); // Llamar al cargar la página para obtener los accesos
  }
}
</script>

<style scoped>
h1 {
  color: #42b983;
}
form {
  margin-bottom: 20px;
}
</style>

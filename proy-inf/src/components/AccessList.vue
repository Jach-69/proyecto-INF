<template>
  <div class="access-list">
    <h2>Lista de Accesos</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Clave</th>
          <th>Tarjeta RFID</th>
          <th>Nombre Usuario</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="acceso in accesos" :key="acceso.id">
          <td>{{ acceso.id }}</td>
          <td>{{ acceso.clave }}</td>
          <td>{{ acceso.tarjeta_rfid }}</td>
          <td>{{ acceso.nombre_usuario }}</td>
          <td>
            <button class="edit-button" @click="editAccess(acceso.id)">Modificar</button>
            <button class="delete-button" @click="confirmDelete(acceso.id)">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      accesos: []
    };
  },
  async created() {
    try {
      const response = await axios.get('http://192.168.1.2:5000/accesos');
      this.accesos = response.data;
    } catch (error) {
      console.error(error);
    }
  },
  methods: {
    async confirmDelete(id) {
      const confirmed = window.confirm('¿Está seguro de que desea eliminar este acceso?');
      if (confirmed) {
        try {
          await axios.delete(`http://192.168.1.2:5000/accesos/${id}`);
          this.accesos = this.accesos.filter(acceso => acceso.id !== id);
          alert('Acceso eliminado con éxito');
        } catch (error) {
          console.error(error);
          alert('Error eliminando acceso');
        }
      }
    },
    editAccess(id) {
      this.$router.push(`/dashboard/edit/${id}`);
    }
  }
};
</script>

<style scoped>
.access-list {
  padding: 20px;
}

table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0 10px; 
}

th, td {
  padding: 10px;
  text-align: left;
}

th {
  background-color: #333;
  color: #fff;
}

td {
  background-color: #444;
  color: #fff;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  margin-right: 10px;
}

.edit-button {
  background-color: #007bff;
  color: #fff;
}

.delete-button {
  background-color: #dc3545;
  color: #fff;
}
</style>

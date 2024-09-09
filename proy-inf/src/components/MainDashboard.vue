<template>
  <div class="access-management">
    <h1>Gestión de Accesos</h1>
    
    <!-- Formulario para añadir nuevo acceso -->
    <form @submit.prevent="addAccess" class="form">
      <input v-model="newAccess.clave" placeholder="Clave" required />
      <input v-model="newAccess.tarjeta_rfid" placeholder="Tarjeta RFID" required />
      <input v-model="newAccess.nombre_usuario" placeholder="Nombre de Usuario" required />
      <input v-model="newAccess.usuario_id" placeholder="ID de Usuario" required />
      <button type="submit">Añadir Acceso</button>
    </form>
    
    <!-- Lista de accesos -->
    <div class="access-list">
      <div class="access-item" v-for="access in accesses" :key="access.id">
        <div class="access-info">
          <p><strong>Clave:</strong> {{ access.clave }}</p>
          <p><strong>RFID:</strong> {{ access.tarjeta_rfid }}</p>
          <p><strong>Nombre de Usuario:</strong> {{ access.nombre_usuario }}</p>
          <p><strong>Fecha y Hora:</strong> {{ access.fecha_hora }}</p>
        </div>
        <div class="access-actions">
          <button @click="editAccess(access.id)">Editar</button>
          <button @click="deleteAccess(access.id)">Eliminar</button>
        </div>
      </div>
    </div>
    
    <!-- Formulario para editar acceso -->
    <div v-if="editingAccess" class="edit-form">
      <h2>Editar Acceso</h2>
      <form @submit.prevent="updateAccess" class="form">
        <input v-model="editingAccess.clave" placeholder="Clave" required />
        <input v-model="editingAccess.tarjeta_rfid" placeholder="Tarjeta RFID" required />
        <input v-model="editingAccess.nombre_usuario" placeholder="Nombre de Usuario" required />
        <input v-model="editingAccess.usuario_id" placeholder="ID de Usuario" required />
        <button type="submit">Actualizar Acceso</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      accesses: [],
      newAccess: {
        clave: '',
        tarjeta_rfid: '',
        nombre_usuario: '',
        usuario_id: ''
      },
      editingAccess: null
    };
  },
  mounted() {
    this.fetchAccesses();
  },
  methods: {
    async fetchAccesses() {
      try {
        const response = await axios.get('http://192.168.0.109:5000/accesos');
        this.accesses = response.data;
      } catch (error) {
        console.error("Error fetching accesses:", error);
      }
    },
    async addAccess() {
      try {
        const response = await axios.post('http://192.168.0.109:5000/accesos', this.newAccess);
        this.accesses.push(response.data);
        this.newAccess = { clave: '', tarjeta_rfid: '', nombre_usuario: '', usuario_id: '' };
      } catch (error) {
        console.error("Error adding access:", error);
      }
    },
    async editAccess(id) {
      try {
        const access = this.accesses.find(a => a.id === id);
        this.editingAccess = { ...access };
      } catch (error) {
        console.error("Error editing access:", error);
      }
    },
    async updateAccess() {
      try {
        await axios.put(`http://192.168.0.109:5000/accesos/${this.editingAccess.id}`, this.editingAccess);
        this.fetchAccesses();
        this.editingAccess = null;
      } catch (error) {
        console.error("Error updating access:", error);
      }
    },
    async deleteAccess(id) {
      try {
        await axios.delete(`http://192.168.0.109:5000/accesos/${id}`);
        this.fetchAccesses();
      } catch (error) {
        console.error("Error deleting access:", error);
      }
    }
  }
};
</script>

<style scoped>
.access-management {
  padding: 20px;
  background-color: #2c2c2c; /* Plomo oscuro */
  color: #fff;
}

.access-management h1 {
  color: #ff4c4c; /* Rojo dark */
  text-align: center;
  margin-bottom: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.form input {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ff4c4c; /* Rojo dark */
  border-radius: 4px;
  background-color: #333;
  color: #fff;
}

.form button {
  padding: 10px;
  border: none;
  border-radius: 4px;
  background-color: #ff4c4c; /* Rojo dark */
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.form button:hover {
  background-color: #e03a3a; /* Rojo oscuro */
}

.access-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.access-item {
  background-color: #000; /* Negro */
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.access-info {
  flex: 1;
}

.access-actions {
  display: flex;
  gap: 10px;
}

.access-actions button {
  padding: 5px 10px;
  border: none;
  border-radius: 4px;
  background-color: #ff4c4c; /* Rojo dark */
  color: #fff;
  cursor: pointer;
}

.access-actions button:hover {
  background-color: #e03a3a; /* Rojo oscuro */
}

.edit-form {
  margin-top: 20px;
}

.edit-form h2 {
  color: #ff4c4c; /* Rojo dark */
  margin-bottom: 20px;
}
</style>

<template>
  <div class="access-edit-container">
    <div class="form-container">
      <h1>Editar Acceso</h1>
      <form @submit.prevent="updateAccess">
        <div class="form-group">
          <label for="clave">Clave:</label>
          <input type="text" id="clave" v-model="editable.clave" />
          <!--  <p>Valor Actual: {{ original.clave || 'No disponible' }}</p>  -->
        </div>
        <div class="form-group">
          <label for="tarjeta_rfid">Tarjeta RFID:</label>
          <input type="text" id="tarjeta_rfid" v-model="editable.tarjeta_rfid" />
          <!-- <p>Valor Actual: {{ original.tarjeta_rfid || 'No disponible' }}</p> -->
        </div>
        <div class="form-group">
          <label for="nombre_usuario">Nombre de Usuario:</label>
          <input type="text" id="nombre_usuario" v-model="editable.nombre_usuario" />
          <!--  <p>Valor Actual: {{ original.nombre_usuario || 'No disponible' }}</p> -->
        </div>
        <div class="button-group">
          <button type="submit" class="btn-update">Actualizar</button>
          <button type="button" @click="goBack" class="btn-cancel">Volver a la lista</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  data() {
    return {
      original: {
        clave: '',
        tarjeta_rfid: '',
        nombre_usuario: ''
      },
      editable: {
        clave: '',
        tarjeta_rfid: '',
        nombre_usuario: ''
      }
    }
  },
  methods: {
    async updateAccess() {
      try {
        const id = this.$route.params.id;
        await axios.put(`http://192.168.1.2:5000/accesos/${id}`, this.editable);
        this.$router.push('/dashboard/list'); 
      } catch (error) {
        console.error("Error al actualizar acceso:", error);
      }
    },
    goBack() {
      this.$router.push('/dashboard/list'); 
    }
  },
  async created() {
    try {
      const id = this.$route.params.id;
      const response = await axios.get(`http://192.168.1.2:5000/accesos/${id}`);
      const acceso = response.data;

      this.original.clave = acceso.clave || 'No disponible';
      this.original.tarjeta_rfid = acceso.tarjeta_rfid || 'No disponible';
      this.original.nombre_usuario = acceso.nombre_usuario || 'No disponible';

      this.editable.clave = acceso.clave || '';
      this.editable.tarjeta_rfid = acceso.tarjeta_rfid || '';
      this.editable.nombre_usuario = acceso.nombre_usuario || '';
    } catch (error) {
      console.error("Error al cargar datos de acceso:", error);
    }
  }
}
</script>

<style scoped>
.access-edit-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.form-container {
  background-color: #333; 
  color: #fff; 
  padding: 20px;
  border-radius: 8px;
  width: 100%;
  max-width: 600px;
}

.form-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 5px;
}

.form-group input {
  padding: 8px;
  border: 1px solid #444;
  border-radius: 4px;
  background-color: #555;
  color: #fff;
}

.button-group {
  display: flex;
  gap: 10px;
}

.btn-update, .btn-cancel {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-update {
  background-color: #28a745; 
  color: #fff;
}

.btn-cancel {
  background-color: #dc3545; 
  color: #fff;
}
</style>

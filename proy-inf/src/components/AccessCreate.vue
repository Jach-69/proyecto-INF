<template>
  <div class="form-container">
    <h2>Crear Nuevo Acceso</h2>
    <form @submit.prevent="createAccess">
      <div class="form-group">
        <input v-model="clave" placeholder="Clave" />
      </div>
      <div class="form-group">
        <input v-model="tarjeta_rfid" placeholder="Tarjeta RFID" />
      </div>
      <div class="form-group">
        <input v-model="nombre_usuario" placeholder="Nombre de Usuario" />
      </div>
      <button type="submit">Crear</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AccessCreate',
  data() {
    return {
      clave: '',
      tarjeta_rfid: '',
      nombre_usuario: '',
    };
  },
  methods: {
    async createAccess() {
      try {
        await axios.post('http://192.168.1.2:5000/accesos', {
          clave: this.clave,
          tarjeta_rfid: this.tarjeta_rfid,
          nombre_usuario: this.nombre_usuario,
        });
        alert('Acceso creado con éxito');
        this.clave = '';
        this.tarjeta_rfid = '';
        this.nombre_usuario = '';
      } catch (error) {
        console.error("Error al crear acceso:", error);
        alert('Error al crear acceso');
      }
    },
  },
};
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 20px;
}

form {
  width: 100%;
  max-width: 600px;
}

.form-group {
  margin-bottom: 15px;
  width: 100%;
  
}

input {
  padding: 8px;
  border: 2px solid #555;
  border-radius: 4px;
  background-color: #444;
  color: #e0e0e0; 
  width: 150%;
  max-width: 400px;
}


button {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  font-size: 16px;
   background-color: #28a745;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>

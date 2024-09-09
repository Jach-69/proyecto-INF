from flask import Blueprint

# Crear un Blueprint para las rutas de acceso
access_bp = Blueprint('access', __name__)

# Importar las rutas específicas para accesos
from . import access_routes

# Crear otro Blueprint para las rutas de autenticación
auth_bp = Blueprint('auth', __name__)

# Importar las rutas específicas para autenticación
from . import auth_routes

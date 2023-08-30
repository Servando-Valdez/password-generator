#!/bin/bash

# Navegar a la carpeta del backend y activar el entorno
cd backend
source .\\venv\\Scripts\\activate

# Ejecutar el servidor FastAPI
uvicorn main:app --reload


# Navegar a la carpeta del frontend y ejecutar el servidor de desarrollo
cd ../frontend
npm run dev
# Explorando FastAPI

El objetivo de este proyecto es explorar y experimentar con las funcionalidades del framework.  
Este documento describe los pasos necesarios para descargar, configurar y ejecutar el proyecto localmente utilizando FastAPI.

---

## Requisitos Previos

1. **Python**: Asegúrate de tener instalado Python 3.8 o superior.
2. **Git**: Necesitarás Git para clonar el repositorio.
3. **pip**: Para instalar las dependencias del proyecto.

---

## Pasos para Configurar y Ejecutar la API

### 1. Clonar el Repositorio

Descarga el código fuente desde el repositorio de GitHub:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Luego, navega al directorio del proyecto:

```bash
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crear un Entorno Virtual

Crea un entorno virtual para evitar conflictos de dependencias:

```bash
python -m venv venv
```

Activa el entorno virtual:

- En **Windows** mediante **cmd**:
  ```bash
  venv\Scripts\activate
  ```
- En **Windows** mediante bash:
  ```bash
  source venv/Scripts/activate
  ```
- En **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependencias

Instala las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el Servidor Local

Inicia el servidor local con el siguiente comando:

```bash
fastapi dev main.py
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

Para explorar la documentación interactiva de la API, accede a:

```
http://127.0.0.1:8000/docs
```

---

## Notas Adicionales

- Para desactivar el entorno virtual:

  ```bash
  deactivate
  ```

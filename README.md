# Ejemplo de una aplicación con Flask

## Introducción

Este es un pequeño ejemplo de un servidor web desarrollado con Flask.

## Objetivos

---

Los objetivos de este ejemplo son los siguientes:

- Aprender a clonar un repositorio de GitHub
- Crear un entorno virtual e instalar las dependencias necesarias
- Levantar un servidor en _localhost_

## Requerimientos previos

---

Para correr este ejemplo será necesario tener instalados los siguientes programas:

- Git
- Python
- Virtualenv

## Instrucciones

---

1. Abre una terminal.
2. Cambia a la carpeta donde deseas guardar el código
3. Clona este repositorio con el siguiente comando: `git clone https://github.com/TavoJG/flask-example.git`
4. Cambia a la carpeta utilizando `cd flask-example`
5. Crea un entorno virtual con `virtualenv venv`
6. Activa tu entorno virtual: `source venv/bin/activate` (VSCode lo hace en automático)
7. Ejecuta el servidor con los siguientes comandos

```
export FLASK_ENV=development
flask run
```

8. Visita [localhost:5000](http://localhost:5000)
9. Explora las rutas definidas en el archivo [app.py](./app.py)

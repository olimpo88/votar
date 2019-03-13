# Proyecto base django 2.1 con docker

Este proyecto tiene como finalidad desplegar *nuevos proyectos django 2.1* de forma veloz.
Genera un entorno inicial el cual despliega un ambiente con tres servicios.

1. Django 2.1
2. Postgres 9.6
3. Nginx 1.15

## La propuesta arquitectónica es la siguiente:

# ![Arquitectura django base](https://i.imgur.com/FfRsX1L.jpg)

## Procedimiento de uso

### 1. Descargar proyecto inicial
```
$ git clone https://git.altec.com.ar/desarrollo/django-base.git

```
### 2. Preparar entorno
Editar el archivo docker-compose.yml adecuando las variables de entorno a las deseadas. El archivo propone valores de ejemplo

#### 2.1 Base de datos
Por defecto el proyecto inicial esta preparado para trabajar usando postgres. Si se cambia estas variables de ambiente no son necesarias

*DB_HOST:* nombre del servicio
*DB_NAME:* nombre del esquema
*DB_USER:* usuario
*DB_PASSWORD:* contraseña

#### 2.2 SuperUsuario
Usuario administrador inicial del proyecto, necesario para acceder al panel de administración de django

*DJANGO_SU_NAME:* nombre de super-usuario
*DJANGO_SU_EMAIL:* email del super-usuario
*DJANGO_SU_PASSWORD:* contraseña del super-usuario

#### 2.3 Ocultar directorio admin (opcional)
Descomentar la variable y poner el path deseado

*DJANGO_ADMIN_URL:* admin

### 3 Quitar referencia al git inicial
Como este repositorio esta pensado para un nuevo proyecto, este proyecto tendrá sus propios repositorios de código. Desde la raíz del proyecto hacer:
```
$ sudo rm -rf .git/
```
### 4. Personalizar imagen base (opcional)
En futuras versiones cambiaremos este método por extender la imagen base. Por ahora se explica como modificarla.

#### 4.1 Renombrar la carpeta docker/base-image a docker/mi-proyecto
```
$ mv docker/base-image docker/mi-proyecto
```

#### 4.2 Personalizar la imagen inicial
Editar el archivo docker/mi-proyecto/Dockerfile. Se pueden agregar archivos necesarios para embeber configuraciones, etc. Siempre dentro de la carpeta de la imagen, respetando la documentación oficial de docker. No agregar requerimientos python de desarrollo mediante el Dockerfile, hacerlo como explica el próximo paso.

Referencia: [link to Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

#### 4.3 Requerimientos de desarrollo en python

Editar el archivo requirements.txt que esta junto al Dockerfile

#### 4.4 Construir la nueva imagen
```
$ cd docker/mi-proyecto
$ docker build -t mi-proyecto:version .
```
#### 4.5 Editar el archivo docker-compose.yml del proyecto
Respetando el nombre y versión de la imagen generada en el paso anterior.

```
services:
  django:
    image: mi-proyecto:version
```

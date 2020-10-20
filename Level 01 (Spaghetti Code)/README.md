# Level 01 (Spaghetti Code)

En este nivel se creara un script para definir el esquema de la base de datos. Se creara un archivo `app.py` donde correra el servidor de nuestra API REST y donde se crearan 4 endpoints para hacer un par de funcionalidades.

La clave de este nivel es observar lo dificil que es programar de esta manera, sin una arquitectura definida y con un monton de logicas diferentes en el mismo archivo `app.py` haciendo de este archivo largo e inestablemente incomodo.

Muy Importante dominar conceptos como: REST, API, Endpoints, HTTP, Servicios.

## Creación de la Base de Datos

Usaremos una base de datos relacional en MySQL. Necesitamos tener un archivo para crear la base de datos y sus respectivas tablas y relaciones.

`generate_db.py` será el archivo que al ser ejecutado revisará si la base de datos existe y en caso contrario la creará junto con sus tablas. Será necesario que edites por lo menos las constantes `USER` y `PASSWORD` como en él se indica para que se ejecute exitosamente.

## Creación de Servicios

Los servicios los crearemos definiendo endpoints.

Crearemos un archivo llamado `api.py` en el cual implementaremos los servicios para la creación de usuarios, artículos, sus comentarios y sus aplausos.

Implementaremos estados HTTP como 202, 200, 404 para diferentes escenarios de los endpoints.

Tambien te tendra en cuenta el uso semantico de los metodos HTTP. [Info](https://tools.ietf.org/html/rfc7231#section-4)

## Servicios a implementar

* Creacion de Usuario (Registro)

* Obtener usuario por su ID

* Obtener todos los usuarios

* Crear Articulos

## Habilidades adquiridas al dominar este nivel

- Comprensión de cómo evolucionan la Web y los estándares

- Paradigmas de bases de datos e implementaciones

- Protocolos de transferencia de datos

## Enlaces Externos

CRUD: https://es.wikipedia.org/wiki/CRUD

Cómo hacer una API En Flask: https://www.youtube.com/watch?v=Esdj9wlBOaI

REST: https://en.wikipedia.org/wiki/Representational_state_transfer

Tesis que introduce el concepto de REST: https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf

Artículo de la IETF que define HTTP (sección sobre los métodos): https://tools.ietf.org/html/rfc7231#section-4

Tutorial que ilustra cómo instalar MySQL: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-es

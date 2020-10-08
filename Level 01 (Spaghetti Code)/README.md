# Level 01 (Spaghetti Code)

Para empezar a construir la API tendremos en cuenta los siguientes términos:

* API:

Interfaz que conecta un Software con Otro. Por ejemplo: una aplicación móvil se puede conectar a este Backend mediante la API que estaremos creando.

* Servicios:

Usualmente los servicios se refieren a cada parte de la API que cumple un rol espefício, en nuestro caso tendremos un servicio para Crear Artículos, otro para Crear Comentarios, otro para Registrar un Usuario, y así sucesivamente.

* REST:

La transferencia de estado representacional es el quinto capítulo de la [tesis](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) escrita por Roy Fielding, que plantea cómo conectar diferentes sistemas a nivel de protocolos de transferencia de datos. Actualmente REST se asocia con APIs y HTTP para la creacion de arquitecturas orientadas a servicios, como la nuestra.

* Endpoints:

Los endpoints son las URLs a las cuales apuntan los servicios en nuestra API REST.

* CRUD:

En informática, CRUD es el acrónimo de "Crear, Leer, Actualizar y Borrar" (del original en inglés: Create, Read, Update and Delete), que se usa para referirse a las funciones básicas en bases de datos o la capa de persistencia en un software.


## Creación de la Base de Datos

Usaremos una base de datos relacional en MySQL. Necesitamos tener un archivo para crear la base de datos y sus respectivas tablas y relaciones.

`generate_db.py` será el archivo que al ser ejecutado revisará si la base de datos existe y en caso contrario la creará junto con sus tablas.

## Creación de Servicios

Los servicios los crearemos definiendo endpoints.

Crearemos un archivo llamado `api.py` en el cual implementaremos los servicios para la creación de usuarios, artículos, sus comentarios y sus aplausos.

## Servicios a implementar

* Creacion de Usuario (Registro)

* CRUD Articulos

* CRUD Comentarios en Articulos

## Enlaces Externos

CRUD: https://es.wikipedia.org/wiki/CRUD

Como hacer una API En Flask https://www.youtube.com/watch?v=Esdj9wlBOaI

REST: https://en.wikipedia.org/wiki/Representational_state_transfer

REST Paper: https://www.ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf

IETF Paper de HTTP: https://tools.ietf.org/html/rfc7231#section-4

Install MySQL: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-es

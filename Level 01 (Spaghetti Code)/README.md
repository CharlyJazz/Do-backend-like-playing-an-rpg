# Level 01 (Spaghetti Code)

Para empezar a construir la API tendremos en cuenta los siguientes terminos

* API:

Interface que conecta un Software con Otro. Ejemplo, una aplicacion movil se puede conectar a este Back-end mediante la API que estaremos creando.

* Servicios:

Usualmente los servicios se refieren a cada parte de la API que cumple un rol espeficio, en nuestro caso tendremos un servicio para Crear Artículos, otro para Crear Comentarios, otro para Registrar un Usuario, y así sucesivamente.

* REST:

La transferencia de estado representacional es el quinto capitulo de la [tesis](https://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) escrita por Roy Fielding que plantea como conectar diferentes sistemas a nivel de protocolos de transferencia de datos. Actualmente REST se asocia con APIS y HTTP para la creacion de arquitecturas orientadas a servicios, como la nuestra.

* Endpoints:

Los `endpoints` son las URL's a las cuales apuntan los servicios en nuestra API REST

## Creación de la Base de Datos

Usaremos una base de dato relacional usando MySQL, necesitamos tener un archivo para crear la base de datos y sus respectivas tablas y relaciones.


`generate_db.py` Sera el archivo que al ejecutar creara la base de datos si no existe y sus tablas

## Creación de Servicios

Los servicios los crearemos definiendo `endpoints`.

Crearemos un archivo llamado a`pi.py` en el cual implementaremos los servicios para la creacion de usuarios, articulos, sus comentarios y sus aplaudos.

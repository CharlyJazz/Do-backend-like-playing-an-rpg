# Level 02 (Modularization)

En este nivel empezamos a modularizar el proyecto, porque seria inviable agregar nuevas caracteristicas a nuestra API si
solo tenemos un archivo `app.py`. Caracteristicas como autenticacion, validacion de entradas, guardado de imagenes, 
separacion de competencias serian imposibles de agregar todas es un solo archivo.


## Reduccion de la cohesion entre endpoints y la base de dato

Crearemos una carpeta para guardar las consultas a la base de datos

```
/data
    /dal
        mysql.py
    /dto
        /users.py
        /articles.py
        /....
    /dta
        /users.py
        /articles.py
        /....
    /....
    
```

De esta manera separaremos la manipulacion de la base de datos creando clases de programacion orientada objeto siguiendo las restricciones necesarias para crear 
DAL, DTO y DAO Clases, conceptos creados hace mas de una decadas pero muy vigentes para crear software limpio. 

En la carpeta DAL guardaremos una clase para aislar nuestra RDBMS (MySQL) y alli guardar la apertura de una conexion y su cierre. 
Esta clase se usara en la carpeta DTA.

En la carpeta DTA guardaremos consultas a la base de dato que se usaran en los endpoints guardados en la carpeta `/api`, cada metodo de las clases DTA retornan una
instancia de la clase DTO que viene siendo la serializacion necesaria de los datos que la base de datos no da.

En la carpeta DTO se guardan clases con metodos que mapean datos, quizas una clase DTO Users mapea un usuario y le crea un atributo full_name o edita la fecha en otor formato diferente 
que el que la base de dato nos ha dado


## Descomponer `app.py`

Para modularizar mas el proyecto haremos una carpeta `/api` en la cual agruparemos endpoints por dominio, para esto usaremos una caracteristica de Flask llamada
blueprint que nos permite crear diferentes archivos con endpoints y evitar tenerlos todos en un solo archivo.

```
/api
    /users.py
    /articles.py
    /....
```

## Aislar logica de creacion de la base datos

Crearemos una carpeta `/schema` para guardar el archivo que crea la base de datos sql.

## Nuevos Endpoints por agregar:

Creamos endpoints para los articulos y implementaremos un mecanismo para autenticacion usando PASETO

- PUT /articles/:id
- DELETE /articles/:id
- GET /articles/:id
- POST /auth/login
- POST /auth/register

## Seguridad: Proteger endpoints.

Cada socilitud de creacion, edicion o de eliminar algo debe llevar en el Header un Bearer Token. De esta manera empezamos a implementar OAuth2 poco a poco


## Enlaces Externos

DAL, DTO Y DAO Clases: https://stackoverflow.com/questions/37644957/what-is-the-difference-between-dal-dto-and-dao-in-a-3-tier-architecture-style-i

DTO y DAL: https://stackoverflow.com/questions/46091178/what-is-dto-equivalent-term-for-objects-returned-from-dal

OAuth2: https://tools.ietf.org/html/rfc6749

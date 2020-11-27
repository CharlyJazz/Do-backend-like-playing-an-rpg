# Level 02 (Modularization)

En este nivel empezamos a modularizar el proyecto, porque sería inviable agregar nuevas características a nuestra API si
sólo tenemos un archivo `api.py`. Caracteristicas como autenticación, validación de entradas, guardado de imágenes,
separación de competencias serían imposibles de agregar todas en un solo archivo.

## Reducción de la cohesión entre endpoints y la base de datos

Crearemos una carpeta para guardar las consultas a la base de datos.

```
data/
├── dal
│   └── mysql.py
├── dao
│   ├── articles.py
│   ├── auth.py
│   ├── comments.py
│   ├── topics.py
│   └── users.py
└── dto
    ├── articles.py
    ├── auth.py
    ├── comments.py
    ├── topics.py
    └── users.py
```

De esta manera separaremos la manipulación de la base de datos creando clases de programación orientada a objetos siguiendo las restricciones necesarias para crear
clases DAL, DTO y DAO, conceptos creados hace más de una década pero muy vigentes para crear software limpio.

En la carpeta `dal/` guardaremos una clase para aislar nuestra RDBMS (MySQL) y allí guardar la apertura de una conexión y su cierre.
Esta clase se usará en la carpeta `dao/`.

En la carpeta `dao/` guardaremos consultas a la base de datos que se usarán en los endpoints guardados en la carpeta `api/`, cada método de las clases DTA retornan una
instancia de la clase DTO que viene siendo la serialización necesaria de los datos que la base de datos no da.

En la carpeta `dto/` se guardán clases con métodos que mapean datos, quizás una clase DTO Users mapea un usuario y le crea un atributo full_name o edita la fecha en otro formato diferente
al que la base de datos nos ha dado.

## Descomponer `api.py`

Para modularizar mas el proyecto haremos una carpeta `api/` en la cual agruparemos endpoints por dominio, para esto usaremos una caracteristica de Flask llamada
blueprint, que nos permite crear diferentes archivos con endpoints y evitar tenerlos todos en un solo archivo.

```
api/
├── articles.py
├── auth.py
├── comments.py
├── __init__.py
├── topics.py
└── users.py
```

## Aislar lógica de creación de la base de datos

Crearemos una carpeta `schema/` para guardar el archivo que crea la base de datos SQL.

Archivos de `schema/`:

-   create_database.sql - Creará la base de datos.
-   create_topics.sql - Creará topics, son necesarios para crear articles.
-   create_users.sql - Creará dos usuarios necesario para testear los endpoints como claps, comments, etc.

## Nuevos Endpoints por agregar:

Creamos endpoints para los artículos e implementaremos un mecanismo para autenticacion usando PASETO.

-   PUT /users/:id
-   GET /users/:id
-   POST /auth/login
-   POST /auth/register
-   POST /articles
-   PUT /articles/:id
-   DELETE /articles/:id
-   GET /articles/:id
-   PUT /comments/:id
-   DELETE /comments/:id
-   GET /comments/:id
-   POST /comments/
-   POST /articles/:id/claps - Creation of claps for a article

Nótese que no vamos a implementar GET LIST ni un CRUD completo de usuarios. Solamente PUT y GET de un usuario.
Tampoco tendremos un CRUD de topics, solamente el GET LIST.

El endpoint que era POST /users/ ahora sera /auth/register.

## Enlaces Externos

DAL, DTO Y DAO Clases: https://stackoverflow.com/questions/37644957/what-is-the-difference-between-dal-dto-and-dao-in-a-3-tier-architecture-style-i

DTO y DAL: https://stackoverflow.com/questions/46091178/what-is-dto-equivalent-term-for-objects-returned-from-dal

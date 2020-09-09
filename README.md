# Do backend, like playing an rpg game

(Illustracion)

## Que es esto?

(Illustracion)

Este repositorio esta destinado a mostrar las diferentes maneras de codificar software del lado del backend. Tomando en cuenta la cantidad de conocimientos implementados en el. Segmente en 10 niveles, de manera progresiva mientras la persona adquiere conocimientos de diferentes areas que conciernen al desarrollo de software en general.

Hay un nivel 0. Este nivel es cuando una persona escribe en Google "Como programar" y las semanas posiblemente busco "Como hacer una API" , posteriormente esa persona aprende que existen palabras claves como REST, HTTP, Autenticacions, Bases de Datos y un par mas que se te podran ocurrir. Con estos conocimientos recien adquiridos nuestro "jugador" empieza una aventura: Crear una API y mejorarla mediante el aumenta sus habilidades

## Negocio (De que trata nuestro software)

(Illustracion)

Nuestro inexistente cliente quiere una API para clonar el funcionamiento de Medium, Creaciones de Articulos, Busqueda, Aplausos a Articulos, Comentarios, Login, Registro, Notificaciones por Correo Electronico.

Esta API esta pensada para ser consumida por las aplicaciones mobiles y la aplicacion web que esta en desarrollo actualmente por otros desarrolladores, la tarea de nuestro querido jugador es crear esta API y que el cliente logre crear su propio Medium Clone y ser feliz.

A continuacion se detallan todas las reglas de negocio de la API:

### Creacion de Usuario, Registro y Actualizacion de Contrasena:

(Illustracion)

Cuando el usuario se registra o quiere cambiar su contrasena se le envia un correo con un token.

### Usuario:

(Illustracion)

Necesita un endpoint para obtener los articulos de un usuarios usando su identificador unico.

Cuando un usuario es etiquetado en un comentario se le envia un correo.

Un usuario puede crear articulos, eliminarlos y editarlos

El usuario puede editar sus datos personales

La imagen de perfil del usuario debe ser guardada

Un Usuario puede collecionar N Articulos y agruparlos por un titulo

Un Usuario puede agregar a Bookmark un articulo

### Articulos:

(Illustracion)

Se pueden comentar

Se debe poder obtener un articulo, sus aplausos y sus comentarios.

Cuando se crea el primer comentario en un articulo se le envia un correo al creador

Los articulos son en formato README

Un articulo tiene titulo, una imagen opcional que se debe guardar y palabras claves asociadas

### Comentarios:

(Illustracion)

Un comentario puede tener comentarios relacionados si el no tiene un comentario padre relacionado

Se pueden etiquetar usuarios en comentarios

### Topicos:

(Illustracion)

Habra una serie de Topicos para relacionar Articulos a ellos, ejemplo (Salud, Economia)

Estos topicos deben estar definidos y el usuario no puede modificarlos

### Tags

(Illustracion)

Habra una serie de Etiquetas para relacionar Articulos a ellos, ejemplo (Javascript, Excel)

El usuario puede crear nuevos topicos si no existen

### Search Engine

(Illustracion)

Se debe poder buscar por Tag, Topic, Titulo y Username con su debida paginacion

### User Feed

(Illustracion)

Debe haber una manera de adquirir los articulos que posiblemente el usuario quiere leer, como tambien
articulos mas nuevos de las personas que el sigue o relacionados con topics que a el le guste

## Habilidades intelectuales y practicas que el jugador debe mejorara y aprendera en cada nivel:

(Desglozar cada uno) (Illustraciones)

- Protocolos de transferencia de datos
- Arquitectura de Software
- Patrones de arquitectura de software
- Paradigmas de bases de datos e implementaciones
- Practicas de software
- Patrones de disenos
- The Twelve Factor y su implementacion
- Descomposicion de software
- Sistemas Informaticos Distribuidos
- Comprension de como evoluciona la Web y los estandares

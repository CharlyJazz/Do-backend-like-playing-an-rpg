# Do backend, like playing an rpg game

(Ilustración)

## ¿Qué es esto?

(Ilustración)

Este repositorio esta destinado a mostrar las diferentes maneras de codificar software del lado del backend. Tomando en cuenta la cantidad de conocimientos implementados en el. Segmente en 10 niveles, de manera progresiva mientras la persona adquiere conocimientos de diferentes áreas que conciernen al desarrollo de software en general.

Hay un nivel 0. Este nivel es cuando una persona escribe en Google "Cómo programar" y las semanas posiblemente busco "Cómo hacer una API" , posteriormente esa persona aprende que existen palabras claves como REST, HTTP, Authentications, Bases de Datos y un par más que se te podrán ocurrir. Con estos conocimientos recién adquiridos nuestro "jugador" empieza una aventura: Crear una API y mejorarla mediante el aumento de sus habilidades

## Negocio (¿De qué trata nuestro software?)

(Ilustración)

Nuestro inexistente cliente quiere una API para clonar el funcionamiento de Medium: Creación de Artículos, Búsqueda, Aplausos a Artículos, Comentarios, Inicio de Sesión, Registro, Notificaciones por Correo Electrónico.

Esta API está pensada para ser consumida por las aplicaciones móviles y la aplicación web que están en desarrollo actualmente por otros desarrolladores, la tarea de nuestro querido jugador es crear esta API y que el cliente logre crear su propio Medium Clone y ser feliz.

A continuación se detallan todas las reglas de negocio de la API:

### Creación de Usuario, Registro y Actualización de Contraseña:

(Ilustración)

Cuando el usuario se registra o quiere cambiar su contraseña se le envía un correo con un token.

### Usuario:

(Ilustración)

Necesita un endpoint para obtener los artículos de un usuarios usando su identificador único.

Cuando un usuario es etiquetado en un comentario se le envía un correo.

Un usuario puede crear, eliminar y editar artículos

El usuario puede editar sus datos personales

La imagen de perfil del usuario debe ser guardada

Un Usuario puede coleccionar N Artículos y agruparlos por un título

Un Usuario puede agregar un Bookmark a un artículo

### Articulos:

(Ilustración)

Se pueden comentar

Se debe poder obtener un artículo, sus aplausos y sus comentarios.

Cuando se crea el primer comentario en un artículo se le envía un correo al creador

Los artículos son en formato Markdown

Un articulo tiene título, una imagen opcional que se debe guardar y palabras claves asociadas

### Comentarios:

(Ilustración)

Un comentario puede tener comentarios relacionados si él no tiene un comentario padre relacionado

Se pueden etiquetar usuarios en comentarios

### Tópicos:

(Ilustración)

Habrá una serie de Tópicos para relacionar Artículos a ellos, ejemplo (Salud, Economía)

Estos tópicos deben estar definidos y el usuario no puede modificarlos

### Etiquetas

(Ilustración)

Habrá una serie de Etiquetas para relacionar Artículos a ellos, ejemplo (Javascript, Excel)

El usuario puede crear nuevas Etiquetas si no existen

### Motor de Búsqueda

(Ilustración)

Se debe poder buscar por Etiqueta, Tópico, Título y Nombre de usuario, con su debida paginación

### User Feed

(Ilustración)

Debe haber una manera de adquirir los artículos que posiblemente el usuario quiere leer, como también artículos más nuevos de las personas que él sigue o relacionados con tópicos que le gusten.

## Habilidades intelectuales y prácticas que el jugador mejorará y aprenderá en cada nivel:

(Desglozar cada uno) (Ilustraciones)

- Protocolos de transferencia de datos
- Arquitectura de Software
- Patrones de arquitectura de software
- Paradigmas de bases de datos e implementaciones
- Prácticas de software
- Patrones de diseño
- The Twelve Factor y su implementacion
- Descomposición de software
- Sistemas Informáticos Distribuidos
- Comprensión de cómo evolucionan la Web y los estándares

## Diagrama entendidad-relacion (ERD)


![medium-clone](https://user-images.githubusercontent.com/55514234/94639437-c7cca580-02a1-11eb-8630-cca4ec2ac92f.png)

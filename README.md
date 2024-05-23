# Crushed
Adventure game 

Antes que nada, es un proyecto que invito a cualqueira pueda usar ya que creo que en los codigos libres y las colaboraciones! Espero lo disfruten tanto como yo!


Juego de Laberinto Crushed

¡Bienvenido al Juego de Laberinto! Este es un juego simple pero entretenido que enseña habilidades básicas de programación en Python utilizando la biblioteca Pygame. El objetivo del juego es guiar a un personaje a través de un laberinto para llegar a la salida. A medida que avanzas, se generan nuevos laberintos aleatorios.

Tabla de Contenidos

    Instalación
    Uso
    Estructura del Proyecto
    Contribuir
    Créditos

Instalación:

Para jugar a este juego, necesitarás tener Python y Pygame instalados en tu sistema.
Requisitos

    Python 3.8 o superior
    Pygame

Instrucciones de Instalación:

Clona este repositorio en tu máquina local:

    https://github.com/fergodie/Crushed
    

Crea un entorno virtual:

    python -m venv venv



Activa el entorno virtual:

En Windows:

    .\venv\Scripts\activate



En macOS/Linux:

    source venv/bin/activate


Instala las dependencias:


    pip install -r requirements.txt

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Uso

Para iniciar el juego, ejecuta el archivo main.py:

    python main.py
    

Controles del Juego:


*Flechas del teclado: Mover el personaje (arriba, abajo, izquierda, derecha)


Pantallas del Juego


-Pantalla Principal: Opción para iniciar el juego o salir

-Pantalla de Juego: Navega a través del laberinto

-Pantalla Final: Agradecimiento por jugar y opción para salir

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Estructura del Proyecto

css

      juego-de-laberinto/
      │
      ├── README.md
      ├── main.py
      ├── maze_generator.py
      ├── levels.py
      ├── requirements.txt
      └── textures/
          ├── wall.png
          └── player.png
    

    main.py: Archivo principal que gestiona las pantallas y el bucle del juego.
    maze_generator.py: Genera laberintos aleatorios.
    levels.py: Administra los niveles del juego.
    textures/: Carpeta que contiene las imágenes de las texturas para las paredes y el jugador.
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    

Contribuir

¡Las contribuciones son bienvenidas! Para contribuir, sigue estos pasos:

    Haz un fork del repositorio.
    Crea una rama nueva (git checkout -b feature-nueva).
    Realiza tus cambios y haz commit (git commit -m 'Agregar nueva característica').
    Empuja tus cambios a la rama (git push origin feature-nueva).
    Abre un Pull Request.

Por favor, asegúrate de que tus cambios pasan las pruebas existentes y añade nuevas pruebas para cualquier nueva funcionalidad.


    Pygame: https://www.pygame.org/
    Generador de Laberintos Aleatorios: Basado en algoritmos clásicos de generación de laberintos.

¡Gracias por jugar y contribuir a este proyecto!

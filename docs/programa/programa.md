# Programa

El programa consiste en 4 capas:

1. Comunicación serial bidireccional con el respirador.
    - Así por un USB puedes comunicarte con lo que sea por ahora.
    - Mas adelante podemos ampliarlo para más interfaces, como MQTT, Websockets, etc, si hiciese falta.
2. Traductores de los mensajes de entrada y generador de los de salida.
    - En principio podemos tomar como ejemplo el de las tramas que tenemos.
    - Está abierto a ser ampliado.
3. Operaciones con los datos de entrada y de salida.
    - Esto ya sería una capa que tendría que modificarse para cada respirador.
4. Interfaz visual para mostrar datos y obtener modificaciones de parámetros.

!!! tip
    Dentro de cada fichero python, se ha añadido (y debes de añadir) la siguiente cabecera para ayudar a cumplir las normas del [PEP8](https://pep8.org/).

    Por un lado tienes el orden en el que deben de ir los imports.
    
    Por otro tienes una referencia de como de larga puedes ser las líneas. Recuerda que **cada línea no puede contener más de 80 caracteres**.

    ```python
    # Built-in --------------------------------------------------------------------
    # Installed -------------------------------------------------------------------
    # Coded -----------------------------------------------------------------------
    # Program ---------------------------------------------------------------------
    ```

    Cada import que hagas, mételo debajo de cada comentario correspondiente, como en el siguiente ejemplo:

    ```python
    # Built-in --------------------------------------------------------------------
    import logging
    from time import time, sleep
    # Installed -------------------------------------------------------------------
    import serial
    from serial.tools.list_ports import comports
    # Coded -----------------------------------------------------------------------
    import mimodulo
    from mimodulo import miscript
    # Program ---------------------------------------------------------------------
    ```

## Estructura del programa

El código fuente se ha puesto dentro de la carpeta `src`. Así es directo saber donde está codigo fuente a nivel de repo, no generando ansias de estar cambiando el nombre del programa y evitando tener problemas con los imports (no hace falta refactorizar los imports).

| Función | Fichero-Carpeta| Explicación |
| :-: | :-: | :- |
| Configuración | `configurarion.ini` | Fichero con la configuración |
|  | `settings.py` | Lee la configuración del fichero anterior.<br>Genera las constantes - objectos globales para cada parte del proyecto |
| Comunicación Serie | `sercomm` | Módulo encargado de la comunicación serie |
| Interfaz Gráfica | `gui` | Módulo con el frontend del programa |
| TODO: | *ir añadiendo lo que falte* |  |

## Logs

Para poder tener un control de lo que ocurre en el programa se usan los llamados logs. Son mensajes que se pueden ver por la consola o ir almacenando en ficheros. En este caso se ha optado en que se autogenere una carpeta `log` a nivel de repositorio, es decir, fuera de la carpeta `src`.

Los objetos dentro del programa encargados de generar estos logs se llaman *loggers*, y se encuentran definidos en el `settings.py`. Se han creado 2:

1. `logapp`:
    - Este es el logger principal que se usa para el programa.
    - Manda su información, tanto por consola, como a un fichero de logs.
2. `logmcu`:
    - Este logger es secundario, y sirve para poder controlar que ocurre en el respirador.
    - Hay MCUs que poseen varios puertos serial, como la placa Arduino Mega que tiene tres.
    - Así, si se quiere, se puede tener un control de lo que ocurre en el respirador a nivel interno.

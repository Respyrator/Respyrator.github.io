# Comunicación Serie con el respirador

La comunicación serie se ha implementado en el módulo `sercomm`.

## Capa de comunicación serie

Su configuración está en la sección `[SERIAL]` del fichero `configuration.ini`.

El fichero `comm.py` contiene la clase `Comm` encargada de:

- Abrir / cerrar y mantener una conexión serie estable.
- Si la comunicación no se puede establecer, lanza una excepción.
- Permite leer / mandar una linea / trama (conjunto de bytes) de bytes.
- Permite leer / mandar una linea de strings (se ha puesto como opcional).

La opción de obtener la trama como strings, es porque es más cómoda quizás en futuras soluciones y también para debuggear / cacharrear.

## Capa de Traducción de tramas

Dentro del módulo `sercomm` podría ir también los traductores de tramas. La idea de los traductores es la siguiente:

- Las tramas puede ser que vayan en campos definidos por bytes.
- Un traductor de recepción por ejemplo:
    - Se le pasa la trama en bytes recibida por el serial.
    - A través de una función con un parámetro o varios, le indicas que bytes quieres que te devuelva y en que tipo (solo devuelve un campo).
        - Por ejemplo, le pasas `'1B'` y `'int'` y te devuelve el byte 0x1B convertido en entero.
        - Otro ejemplo, le pasas `[1C, 1D]` y `float` y te devuelve el valor de esos bytes juntos convertidos en un flotante.
    - Así puedes obtener los campos de la trama que te sean necesarios y sirve para cada trama que se le ocurra a cualquiera.
- Un traductor de transmisión por ejemplo:
    - Se le pasa un diccionario con todos los campos de la trama.
    - Su **clave**-**valor** podría ser `'1B': campo_n`.
    - El traductor te devuelve la trama de envio completa, convirtiendo a byte cada **valor**, siendo su posición en la trama la **clave**.

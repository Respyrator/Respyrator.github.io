# Ayuda para documentar

## Documentación:

- Está hecha con [MKDocs](https://www.mkdocs.org/).
- Se ha usado la [plantilla para talleres](https://github.com/lajaqueria/plantilla-taller) de [La Jaquería](https://lajaqueria.org)
- Esa plantilla no es más que una customización del tema [mkdocs-material (Material Design)](https://squidfunk.github.io/mkdocs-material/) (el repo [aquí](https://github.com/squidfunk/mkdocs-material)) hecho por [Martin Donath, aka @squidfunk](https://github.com/squidfunk)

Se compone de 2 elementos básicos:

1. Fichero `mkdocs.yml`
    - Contiene la configuración de la documentación.
    - En principio solo deberías de tocar la sección `nav` para añadir páginas nuevas.
    - La referencia a un fichero de texto se hace pensando que estas dentro de la carpeta `doc`.
2. Directorio `docs`:
    - Contiene todos los recursos de la documentación: ficheros de texto (markdown), imagenes, js, etc.
    - Aquí es donde se deben añadir en ficheros o ficheros dentro de sub carpetas la documentación.

## Trabajar con la documentación

Lo primero arranca el servidor para poder ver la documentación desde un navegador. Para usa el siguiente comando

```bash
pipenv run serve
```

Ahora abre en tu navegador la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Recuerda dejar la terminal abierta con el servidor funcionando, si no, no podras ver los cambios ver los cambios en tiempo real en el navegador. Si quisieras apagar el servidor, pulsa `Ctrl-C` o cierra la terminal.

Para escribir sigue estos pasos:

1. Comprueba si existe o no la sección donde quieras escribir.
2. Si no existe, genera tu el fichero markdown dentro de docs y luego referencialo en la sección `nav` del fichero `mkdocs.yml`.
3. Comprueba que lo que escribes se ve bien.
4. Los documentos largos son pesados de leer, divide en documentos el texto si es muy largo.
5. Si no se te ve bien algo, prueba a recargar la página en el navegador o a parar y volver arrancar el servidor.

Si no sabes escribir en Markdown, no te preocupes porque es sencillisimo. Además este tema que usa la documentación tiene plugins para hacer más visual todo. Tienes una ayuda básica para desenvolverte con Markdown. Y otra para poder sacarle más partido al tema Material Design:

- [Escribir Markdown](markdown.md)
- [Sacarle jugo al tema Material Design](material.md)

## Despliegue de la documentación

La documentación se va a ver [aquí](https://respyrator.github.io/respirador/). Tiene los ficheros de despliegue `.travis.yml` para Travis-CI, y también el `.readthedocs.yml` para ReadTheDocs.

En principio la documentación se actualizará sola una vez los cambios se suban a la rama `master`.

Aun así, si quieres ver la documentación que has hecho en una web real, puedes usar el comando

```bash
pipenv run deploy
```

Esto generará la web, la meterá en la rama `gh-pages` de tu repositorio y podrás ver la docu en https://<tu-usuario-de-github>.io/respirador/.

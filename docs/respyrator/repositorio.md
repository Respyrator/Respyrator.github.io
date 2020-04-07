# Repositorio

El proyecto está dentro de un repositorio, así que es necesario que sepas como está estructurado antes de que sigas.

| Función | Fichero - Carpeta | Explicación |
| :- | :-: | :- |
| Programa | `src/` | Código fuente |
|  | `test/` | Tests del programa |
|  | `.travis.yml` | Para el CI del programa y también generar la documentación en la rama `gh-pages` |
|  | `log` | Esta carpeta se autogenera para almacenar los logs del programa |
| Documentación | `mkdocs.yml` | Configuración e índice |
|  | `docs/` | Ficheros y recursos de la documentación |
|  | `readthedocs.yml` | Fichero para despliegue de documentación en [readthedocs.org](https://readthedocs.org/) |
| Respirador HW | `firmware/` | Código para hacer pruebas con el HW |
| Entorno virtual | `Pipfile` | Fichero para instalar el programa |
|  | `Pipfile.lock` | Fichero de seguridad |
|  | `requirements.txt` | No usar (deprecado) |
|  | `requirements-dev.txt` | No usar (deprecado) |
| Repositorio | `README.md` | Información e instrucciones del repositorio |
|  | `LICENSE` | Licencia del programa |
|  | `CONTRIBUTING.md` | Información sobre como colaborar |
|  | `.gitignore` | Fichero para indicar que ficheros-carpertas no incluir en el repo |

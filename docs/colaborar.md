# Como colaborar

Toda ayuda es bien recibida, pero hay que seguir unas normas por el bien del proyecto. Antes incluso de que leas más sobre el proyecto, es importante que sepas como colaborar. Este es un proyecto software, donde sus contribudores están deslocalizados.

## Requisitos

Los requisitos para trabajar son tener instalado:

- Python 3.8
- Gestor de paquetes pip
- Paquete pipenv

## Metodología

La metodología de trabajo es la siguiente:

1. Haz un fork del [repositorio](https://github.com/Respyrator/respirador) en tu cuenta de Github.
2. Cambia a la rama `dev` y trabaja sobre ella.

    !!! info
        Te recomendamos que añadas también el repo oficial en el remote de git, para que puedas tener los cambios del repositorio oficial en tu local.

        ```bash
        git remote add oficial https://github.com/Respyrator/respirador
        ```

3. Mira los [issues del proyecto](https://github.com/Respyrator/respirador/issues) así como el [tablero de tareas](https://github.com/Respyrator/respirador/projects/1).
4. Antes de hacer avances por tu cuenta, mira si puedes desarrollar algún issue que ya esté abierto.

    !!! tip
        Es más **importante ir cerrando issues**, que tener muchas abiertas.

5. Para cualquier desarrollo que quieras hacer: abre primero un issue, ponle las etiquetas correspondientes y justifícalo.
6. Los desarrollos o cambios que hagas en el programa y que necesiten explicación, **ponlo en la documentación**.

    !!! warning
        **Si no documentas**, estas dificultando la labor de tus compañer@s presentes y futuros.  
        Con ese comportamiento **estás haciendo más daño que bien al proyecto**.

7. Haz tests unitarios de todos tus cambios / mejoras y comprueba que pasas tanto los tuyos como los que ya hay.

    !!! failure
        Para los tests se está usando la suite [Pytest](https://docs.pytest.org/en/latest/).  
        Ejecutando el siguiente comando se ejecutan todos los tests

        ```bash
        pipenv run test
        ```

        Esto no es un proyecto de juguete, **la vida de personas van a depender de él**.  
        **Tu código debe de pasar todos los tests** ya hechos, y tu **debes de preocuparte de hacer tests exhaustivos para tus mejoras**.  
        **Si no** mantenemos esto, a parte de entorpecer a tus compañer@s, **podrían perderse vidas humanas**.

8. Comprueba en tu servidor local que la documentación haya quedado bien (para más información, ve a la [sección de la documentación](ayuda/ayuda.md))
9. Una vez has pasados los tests y la documentación esté bien, guarda los cambios en **commits atómicos**.

    !!! info
        Esto quiere decir que para cada mejora hagas debe de ir en un pequeño commit que pueda ser revisable luego.  
        Los **commits con muchos ficheros y cambios distintos dificultan el trabajo**.

10. Comprueba que tengas tu rama `dev` actualizada respecto a la del repo oficial

    !!! danger
        Si no haces esto, puedes generar conflictos entre ficheros, con su correspondiente carga de trabajo extra.  
        Descarga primero los cambios de la rama `dev` a tu repo local con

        ```bash
        git pull oficial dev
        ```

        Ahora haz lo siguiente:
        
        1. Resuelve conflictos en los ficheros si los hubiere.
        2. Vuelve a pasar los tests.
        3. Comprueba la documentación.
        4. Si está todo OK, ya puedes seguir

11. Sube los cambios a tu repo, siempre en la rama `dev`.
12. Haz un pull request desde tu rama `dev` a la rama `dev`.
13. Los pull requests deben de pasar los tests automatizados del sistema de CI configurado.
14. Una vez pasen los tests, los administradores los revisarán y los aceptarán.

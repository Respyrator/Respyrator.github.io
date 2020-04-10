# Configuraciones

En cada modo hay que hacer una configuración que consiste en:

- Control: Parámetros de control y sus valores.
- Alarmas: Parámetros de alarma y sus valores.

???+ summary "Modalidades Controladas o Mandatorias"

    ???+ info "Controlado por Presión"
        Control: PEEP + FR + T$_{insp}$ + I:E + FiO$_2$ + **P$_{insp}$**

        Alarmas: V$_T$

    ???+ info "Controlado por Volumen"
        Control: PEEP + FR + T$_{insp}$ + I:E + FiO$_2$ + **V$_T$**

        Alarmas: P$_{pk}$ + P$_{plt}$ + Csr

???+ summary "Modalidades Asistidas o Sincronizadas"

    ???+ info "Controlado por Presión"
        Control: PEEP + FR + T$_{insp}$ + I:E + FiO$_2$ + **P$_{insp}$** + **trigger (presión)** + **ramp**

        Alarmas: V$_T$

    ???+ info "Controlado por Volumen"
        Control: PEEP + FR + T$_{insp}$ + I:E + FiO$_2$ + **V$_T$** + **trigger (flujo)** + **ramp**

        Alarmas: P$_{pk}$ + P$_{plt}$ + Csr

???+ info "Modalidad Soporte Controlada por Presión"
    Control: PEEP + **Presión soporte**

    Alarmas: FR + F$_{insp}$

???+ info "Modalidad Espontánea"
    Control: PEEP + FiO$_2$

    Alarmas: **falta**

# Sobre los informes
Aqui estan las respuestas de las preguntas de abajo 
[Resumen Examen Ingeniería Sanitaria - Google Gemini](https://gemini.google.com/app/e3434283b313f196)
## 1. Dinamica y Dotaciones
**Para un diseño de un proyecto de abastecimiento de agua potable, como información básica, detallar:** 
-  **Dinámica poblacional, factores que la determinan y métodos para determinar el crecimiento poblacional.** 
-  **Criterios para determinar las dotaciones**
### Ans
Se determinan por el **crecimiento vegetativo** (natalidad vs. mortalidad), **saldos migratorios**, **población flotante** (turismo/estudios) y **límites de saturación espacial** (capacidad de carga del territorio).

Los metodos de crecimiento poblacional son los siguientes
- **Aritmético:** Crecimiento lineal constante. Ideal para zonas consolidadas o cascos históricos.$$
P_f = P_u + r \cdot \Delta t
$$
- **Geométrico:** Crecimiento porcentual (interés compuesto). Aplicable a ciudades en plena expansión (conos de Lima).$$
P_f = P_u \times (1 + r)^{\Delta t}
$$
- **Wappaus:** Método híbrido que amortigua crecimientos extremos; es el estándar para proyectos del MVCS en poblaciones medianas.

Mientras que los criterios para determinar dotaciones se basan en normativas y tambien dependen del clima, nivel socioeconómico y tipo de sistema de alcantarillado.
- **Urbano (OS.100):** **180** (clima frío) a **220** (clima cálido).
- **Rural (RM 192-2018):** Varía según la tecnología. Con arrastre hidráulico es **80-100** (selva) o **100** (costa/sierra). Sin arrastre (letrinas) baja a **30-50**.
## 2. Determinacion de caudal equipos
**Para la determinación de caudales de la fuente para abastecimiento de agua, es necesarios equipos para cada caso, en tal sentido, detallar** 
-  **Métodos, modalidades y equipos de medición de flujos**
### Ans
- **Métodos en Cauces Abiertos:**
    - **Volumétrico:** Precisión absoluta para caudales menores a 1 L/s ($Q = V/t$).
    - **Área-Velocidad:** Uso de molinetes para integrar velocidades en la sección ($Q = A \cdot V$). Se mide al 60% de la profundidad o promedio de 20% y 80%.
    - **Tecnologías:** **ADCP** (perfiladores acústicos Doppler) para batimetría instantánea y **trazadores químicos** (dilución) para ríos turbulentos o de alta montaña.

- **Estructuras de Control:** Vertederos (triangulares/rectangulares) y canaletas **Parshall** que generan régimen crítico para independizar el caudal del remanso.

## 3. Elementos Planta de tratamiento
**Detallar elementos que en general conforman una planta de tratamiento de agua para consumo humano, desde la bocatoma hasta el almacenamiento, desde donde se inicia la distribución.**
### Ans
- **Ley de Recursos Hídricos (29338):** Gestiona el agua en la fuente natural. Establece prioridades de uso: 1. Primario (humano directo), 2. Poblacional (red pública), 3. Productivo.

- **DS 031-2010-SA:** Reglamento de calidad para consumo humano (el agua en el grifo). Define los **LMP** (Límites Máximos Permisibles) y exige el Plan de Control de Calidad (**PCC**).

- **Diferencia ECA vs. LMP:** El **ECA** mide la calidad del cuerpo receptor (río/lago) y el **LMP** mide la calidad del efluente o descarga puntual.

- **Clasificación para Diseño (OS.020):**
    - **Tipo I:** Desinfección obligatoria.
    - **Tipo II-A:** Tratamiento convencional simple (decantación/filtración lenta).
    - **Tipo II-B:** Requiere **coagulación obligatoria** y tratamiento completo (mezcla rápida, floculación, sedimentación, filtración rápida y desinfección).
## 4. Elementos sistema de distribucion
**Detallar elementos que conforman un sistema de distribución, sistema de conducción, sistema de impulsión, sistema de aducción, red mallada y abierta.**
### Ans
- **Criterios de Producción:** Físicos (turbiedad < 5 UNT), Químicos (metales, dureza) y Biológicos (ausencia de coliformes).
- **Elementos de la PTAP:** Bocatoma $\rightarrow$ Desarenador $\rightarrow$ Mezcla Rápida (Coagulación) $\rightarrow$ Floculador $\rightarrow$ Sedimentador $\rightarrow$ Filtro $\rightarrow$ Desinfección $\rightarrow$ Reservorio.
![[Pasted image 20260514124007.png]]

- **Caudales de Diseño:**
    - **Qmd (Máximo Diario):** $Q_p \times K_1$ ($K_1 = 1.30$). Diseña la **captación, conducción y PTAP**.
    - **Qmh (Máximo Horario):** $Q_p \times K_2$ ($K_2 = 1.80$ a $2.50$). Diseña la **aducción y redes de distribución**.

- **Sistemas de Distribución:**
    - **Conducción:** Agua cruda de fuente a PTAP.
    - **Aducción:** Agua tratada de reservorio a red.
    - **Impulsión:** Bombeo de cotas bajas a altas.
    - **Red Mallada vs. Abierta:** La mallada (anillos cerrados) permite mayor continuidad y presión uniforme; la abierta es tipo árbol y es más susceptible a cortes de servicio.
# Practico
## Tubos con Chezy
**Para la información mostrada en la figura, determinar el caudal que debe suministrar la bomba y el caudal en cada una de las tuberías de tal manera que el caudal de la tubería N° 4 sea el 50% del caudal de la tubería N° 2.**
- **Dibujar la línea de alturas piezométricas si la presión antes de la bomba seria de 0.1 kg./cm².**
- **C es coeficiente de CHEZY**
![[Pasted image 20260416173804.png|575]]
### Sol

## Reservorio - Tuberia
Determinar el caudal que conduce cada una de las tuberías, del sistema mostrado en la figura Nº 1 y la presión en el punto "P", teniendo en cuenta que el valor de "Z" es igual a las dos últimas cifras de su código de alumno.
Si $L_{1} = 1500\ m$, $L_{2} = 2000\ m$, $L_3 = 1800.0\ m$, $L_{4} = 1000\ m$, $f_{1} = 0.02$, $f_{2} = 0.018$, $f_3 = f_4=0.025$ y si, $D_{1} = D_{2} = D_4 = 0.3048\ m$, $D_3 = 0.254\ m$ y además $q = 0.01\ l/s$
![[Pasted image 20260416175327.png|307]]
### Sol



## Flujo Tramos
Diseñar el sistema de conducción mostrado en la figura, si a las tuberías le corresponde un coeficiente de Hazen y Williams de 120, de tal manera que en operación conduzca 250 It./s de agua de viscosidad 10-6 m²/s y cumpla con las siguientes condiciones: Pmax = 50.00 mca, Pmin = 3.0 mca, Vmax 4.0 m/s y Vmin de 0.6 m/s
![[Pasted image 20260514125535.png|602]]

## Tubos con Bomba
Para la información mostrada en la figura N° 2, determinar las alturas piezométricas en los puntos "A" y "D", dibujar la línea de alturas piezométricas cuando la bomba impulsa 140 It's de agua y la potencia de la bomba si se considera la presión antes de la bomba cero.- considerar el coeficiente de CHEZY para la tubería C = 100
![[Pasted image 20260514125453.png|592]]


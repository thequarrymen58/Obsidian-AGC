# Enunciado 1 (Golpe)
En un sistema Reservorio-Tubería-Válvula: 
1. ¿Cómo se determina la máxima presión (maxima carga piezometrica) en la válvula que ocurre durante un cierre instantáneo de la válvula? Deducir la expresión que permite el cálculo. 
2. ¿Cuánto tiempo demora para que toda la tubería esté perturbada por el cierre instantáneo?
## Solucion
1. 
Para determinar la sobrepresión máxima debida a un cierre instantáneo (tiempo de cierre $t_{cierre}=0$), se utiliza la ecuación de Joukowsky. 
La deducción se realiza a partir de un análisis macroscópico con la Segunda Ley de Newton:

- **Fuerza de presión:** Se define como la variación de presión en el área de la tubería, es decir, $F_{presion} = \Delta P \cdot A_0$.
- **Masa del fluido:** La masa en la tubería de longitud $L$ es $m = \rho \cdot A_0 \cdot L$.
- **Aceleración:** La aceleración macroscópica es $a = \frac{\Delta v}{\Delta t}$.
- Igualando la fuerza al producto de la masa por la aceleración ($F = m \cdot a$), obtenemos:
$$
\Delta P \cdot A_0 = (\rho \cdot A_0 \cdot L) \cdot \frac{\Delta v}{\Delta t}
$$
- Sabemos que la distancia que recorre la onda está relacionada con la celeridad y el tiempo mediante $L = C \cdot \Delta t$.
- Reemplazando $L$ en la ecuación anterior y simplificando el área y el tiempo, llegamos a $\Delta P = \rho \cdot C \cdot \Delta v$.
- Finalmente, para expresar esto en términos de carga piezométrica (metros), se divide la ecuación entre el peso específico ($\gamma = \rho \cdot g$):
$$
\Delta H = \frac{C \cdot \Delta v}{g}
$$
2. 
- A partir de la relación de la propagación de la onda, sabemos que la distancia es igual a la celeridad por el tiempo, $L = C \cdot \Delta t$.
    
- Despejando el tiempo, se concluye que el tiempo que demora la onda en viajar desde la válvula hasta el reservorio (perturbando así toda la tubería) es $\Delta t = \frac{L}{C}$.
# Enunciado 2 (Golpe)
En un sistema Reservorio-Tubería-Válvula: 
1. ¿Cuando se dice que el tiempo de cierre de válvula es lento? 
2. Cuando el flujo circula en estado permanente en la tubería de longitud $L$ del sistema Reservorio-Tubería-Válvula, ¿Cómo se determina la carga piezométrica en la posición $L/2$?
## Solucion
1. 
- El documento define explícitamente que el tiempo que demora la onda de presión en ir y volver a la válvula es $T_R = 2L/a$.
- También indica que el tiempo de cierre de la válvula modificará la respuesta según su duración en relación a este tiempo $T_R$.
- Por lo tanto, puedes responder con total seguridad basándote en su material: **Un cierre se considera lento cuando su tiempo de cierre ($T_c$) es mayor al tiempo de retorno de la onda ($T_c > 2L/a$).**
2. 
- En estado permanente (antes del cierre), no hay variación en el tiempo ($\frac{\partial Q}{\partial t} = 0$), por lo que la altura solo decae linealmente debido a la pendiente de fricción $S_f$.
- Sigue siendo correcto afirmar que a la mitad del tramo la carga es: $h_{L/2} = H - S_f \cdot \left(\frac{L}{2}\right)$.
o $h_{l/2}=H-\frac{fLV^2}{4gD}$
# Enunciado 3 (Canales)
A partir de las ecuaciones de movimiento y continuidad en un canal unidimensional sin fricción.
$$
\frac{\partial v}{\partial t} + v \frac{\partial v}{\partial x} + g \frac{\partial h}{\partial x} = 0 \quad (1)
$$
$$
\frac{\partial h}{\partial t} + h \frac{\partial v}{\partial x} + v \frac{\partial h}{\partial x} = 0 \quad (2)
$$
Nota: 
$v$ es la velocidad 
$h$ es la profundidad total de agua
$x$ es el eje a lo largo del canal
$g$ es la aceleración de la gravedad.
1. Obtener las ecuaciones características. 
## Solucion
Basándonos en el método de las características para canales unidimensionales:
- Se define la celeridad de la onda de gravedad como $c = \sqrt{gh}$.
- Al sumar y restar las ecuaciones de movimiento y continuidad (incorporando el término $2c \frac{\partial c}{\partial x}$), el sistema se transforma en derivadas totales.
- La forma característica general resulta en $\frac{d}{dt}(v \pm 2c) = E$.
- Dado que el canal no tiene fricción ni pendiente, el término de energía o fuerzas externas se anula, es decir, $E = 0$.
- Por lo tanto, las ecuaciones características quedan definidas por cantidades constantes a lo largo de sus respectivas líneas:$$
v \pm 2c = \text{constante}
$$- Estas ecuaciones son válidas a lo largo de las curvas características definidas por $\frac{dx}{dt} = v \pm c$

# Enunciado 4 (Canales)
A partir de las ecuaciones de movimiento y continuidad en un canal unidimensional con friccion.
$$
\frac{\partial v}{\partial t} + v \frac{\partial v}{\partial x} + g \frac{\partial h}{\partial x} + g S_f - g S_o = 0 \quad (1)
$$
$$
\frac{dh}{dt} + h \frac{\partial v}{\partial x} + v \frac{\partial h}{\partial x} = 0 \quad (2)
$$
Donde: 
$v$ es la velocidad
$h$ la carga total de agua
$x$ el eje a lo largo del canal
$g$ la aceleración de la gravedad
$S_f, S_o$ las pendientes de energía (por fricción) y de fondo respectivamente.

1. Obtener las ecuaciones características. 
## Solucion

# Enunciado 5 (Canales)
Para un punto "P" de un canal de agua con velocidad $v_p = 4 \text{ m/s}$, y profundidad $h_p = 1 \text{ m}$ en un instante dado: 
1. ¿Cómo se determina las líneas características que pasan por el punto P en base a los datos $v_p$  y $h_p = 1 \text{ m}$? 
2. Grafique las características. 
3. ¿Qué tipo de flujo reflejan las características?
## Solucion
### 1. Determinación de las líneas características

Primero, calculamos la celeridad de la onda de gravedad ($c$) usando la profundidad dada ($h_P = 1 \text{ m}$) y asumiendo la gravedad estándar ($g = 9.81 \text{ m/s}^2$):
$$
c = \sqrt{g \cdot h_P}
$$
$$
c = \sqrt{9.81 \cdot 1} = 3.132 \text{ m/s}
$$
Las líneas características están definidas por las ecuaciones de sus pendientes en el plano espacio-tiempo ($dx/dt = v \pm c$). Evaluamos ambas con la velocidad del punto ($v_P = 4 \text{ m/s}$):

- **Característica Positiva ($C_+$):**
$$
C_+ = v_P + c = 4 + 3.132 = 7.132 \text{ m/s}
$$ 
- **Característica Negativa ($C_-$):**
$$
C_- = v_P - c = 4 - 3.132 = 0.868 \text{ m/s}
$$
Esto significa que, desde el punto $P$, cualquier onda viaja hacia aguas abajo. La onda frontal viaja a **7.132 m/s** y la onda trasera (que normalmente iría contra la corriente) es "arrastrada" por la velocidad del río y también viaja hacia aguas abajo a **0.868 m/s**.

### 2. Gráfico de las características
=Se trata de un flujo supercritico=
![[Pasted image 20260713102053.png|408]]
### 3. ¿Qué tipo de flujo reflejan las características?

Las características reflejan un **Flujo Supercrítico**.

# Enunciado 6 (Canales)
Se trata de un canal de $400 \text{ m}$ con profundidad de $5 \text{ m}$ sin movimiento. 
En el extremo izquierdo se inicia la descarga de agua por metro de ancho, igual a $-1 \text{ m}^2\text{s}^{-1}$ al cabo de $10$ segundos. 
1. Determinar la velocidad y la profundidad en el punto de descarga en ese instante.
## Solucion
### 1. Identificar el estado inicial (Zona no perturbada)

El enunciado nos dice que inicialmente el canal de 400 m de longitud se encuentra "sin movimiento" y con una profundidad constante.

A partir de esto, extraemos las variables de la zona no perturbada (índice "o"):

- Velocidad inicial: $u_o = 0 \text{ m/s}$.
    
- Profundidad inicial: $h_o = 5 \text{ m}$.
    

Calculamos el Invariante de Riemann para esta zona no perturbada, usando la gravedad $g = 9.81 \text{ m/s}^2$:

$$
I_o = u_o - 2\sqrt{g \cdot h_o}
$$

$$
I_o = 0 - 2\sqrt{9.81 \cdot 5}
$$

$$
I_o = -2\sqrt{49.05} = -2(7.0036) = -14.007 \text{ m/s}
$$

### 2. Aplicar la Ecuación Característica en el extremo

En el extremo izquierdo (el punto de descarga, índice "d"), solo existe la curva característica negativa ($C_-$) que viene desde el interior del canal hacia la frontera.

A lo largo de esta característica negativa, la cantidad $u - 2\sqrt{gh}$ se conserva constante, por lo que podemos igualar las condiciones del punto de descarga con las de la zona no perturbada:

$$
u_d - 2\sqrt{g \cdot h_d} = u_o - 2\sqrt{g \cdot h_o}
$$

Sustituyendo el valor que ya calculamos en el paso 1:

$$
u_d - 2\sqrt{9.81 \cdot h_d} = -14.007
$$

$$
u_d - 6.264 \sqrt{h_d} = -14.007 \quad \text{(Ecuación A)}
$$

### 3. Usar la Condición de Frontera (Caudal)

El problema nos indica que la descarga inicia con un caudal unitario $q = -1 \text{ m}^2/\text{s}$ (el signo negativo indica que el agua sale del dominio hacia la izquierda).

Sabemos por continuidad que el caudal por metro de ancho es el producto de la velocidad por la profundidad, por lo que podemos despejar la velocidad en el punto de descarga:

$$
q = u_d \cdot h_d
$$

$$
-1 = u_d \cdot h_d \implies u_d = \frac{-1}{h_d} \quad \text{(Ecuación B)}
$$

### 4. Resolver el sistema de ecuaciones

Ahora sustituimos la Ecuación B dentro de la Ecuación A para dejar todo en función de una sola incógnita (la profundidad $h_d$):

$$
\left( \frac{-1}{h_d} \right) - 6.264 \sqrt{h_d} = -14.007
$$

Para resolverla, la reordenamos multiplicando por $-1$:

$$
\frac{1}{h_d} + 6.264 \sqrt{h_d} = 14.007
$$

Esta es una ecuación no lineal. En un examen, lo normal es resolverla por tanteo (iteración) o usando la función "Solve" de tu calculadora científica:

- Si probamos con $h_d = 5 \text{ m}$: $\frac{1}{5} + 6.264\sqrt{5} = 0.2 + 14.006 = 14.206$ (Nos pasamos de 14.007).
    
- Si probamos con $h_d = 4.8 \text{ m}$: $\frac{1}{4.8} + 6.264\sqrt{4.8} = 0.208 + 13.723 = 13.931$ (Falta un poco).
    
- Resolviendo de forma exacta llegamos a:
    
    $$
h_d \approx 4.854 \text{ m}
$$
    

### 5. Hallar la velocidad final

Conociendo la profundidad de descarga, regresamos a la Ecuación B para calcular la velocidad en ese mismo instante:

$$
u_d = \frac{-1}{4.854}
$$

$$
u_d \approx -0.206 \text{ m/s}
$$

_(Nota sobre el tiempo $t=10$ s: El tiempo no entra directamente en la ecuación porque la celeridad de la onda es $c = \sqrt{9.81 \cdot 5} \approx 7 \text{ m/s}$. Para recorrer los 400 m del canal, la onda tardaría unos 57 segundos. Como solo han pasado 10 segundos, nos aseguramos de que el extremo derecho del canal aún no se ha enterado de la descarga y la onda no ha rebotado, validando que seguimos utilizando los datos de la "zona no perturbada" inicial)_.


Este es un excelente momento para consolidar todo el bloque de canales (flujo a superficie libre). El Método de las Características en canales unidimensionales suele ser uno de los temas filtro en hidráulica avanzada, porque exige combinar el análisis del comportamiento físico del agua con métodos de resolución numérica.

Aquí tienes un resumen estructurado de las preguntas de canales, expandiendo la teoría y añadiendo variaciones prácticas para que domines cualquier escenario que se presente en tu examen.

## 1. Fundamentos Teóricos: Las Ecuaciones Características (Enunciados 3 y 4)

El objetivo de las preguntas teóricas es demostrar cómo un sistema de derivadas parciales complejas se transforma en un sistema de derivadas totales resolubles a lo largo de líneas específicas. Todo parte de definir la celeridad de la onda de gravedad como $c = \sqrt{gh}$.

### A. Canal ideal (Sin fricción ni pendiente)

- **Físicamente:** El canal es horizontal y liso. No hay fuerzas externas que agreguen o quiten energía al flujo.
    
- **Matemáticamente:** Al sumar y restar las ecuaciones de continuidad y movimiento, el término de fuerzas es nulo ($E=0$).
    
- **Resultado:**
    
    $$
\frac{d}{dt}(v \pm 2c) = 0
$$
    
- **Interpretación:** Como la derivada en el tiempo es cero, las cantidades $(v + 2c)$ y $(v - 2c)$ se mantienen **estrictamente constantes** a lo largo de las curvas características $dx/dt = v \pm c$. A estos valores constantes se les llama **Invariantes de Riemann**.
    

### B. Canal real (Con fricción y pendiente)

- **Físicamente:** El canal tiene inclinación ($S_o$) y rugosidad que genera pérdida de carga ($S_f$).
    
- **Matemáticamente:** Aparece el término de fuerzas externas $E = g(S_o - S_f)$.
    
- **Resultado:**
    
    $$
\frac{d}{dt}(v \pm 2c) = g(S_o - S_f)
$$
    
- **Interpretación:** Las cantidades $(v \pm 2c)$ ya no son constantes. Se vuelven **cuasi-invariantes**, lo que significa que su valor cambia gradualmente a medida que la onda avanza, y para calcular ese cambio debes integrar el término de fuerzas a lo largo del tiempo de propagación.
    

## 2. Comportamiento Local y Tipos de Flujo (Enunciado 5)

Esta sección evalúa tu capacidad para interpretar hacia dónde viajan las perturbaciones en el río basándote en un solo punto conocido.

### El caso original: Flujo Supercrítico

Tenías $v_p = 4 \text{ m/s}$ y $h_p = 1 \text{ m}$.

- **Celeridad:** $c = \sqrt{9.81 \cdot 1} = 3.132 \text{ m/s}$.
    
- **Características:** $C_+ = +7.132 \text{ m/s}$ y $C_- = +0.868 \text{ m/s}$.
    
- **Interpretación:** Al ser $v > c$, ambas ondas son arrastradas hacia la derecha (aguas abajo). El flujo supercrítico significa que ninguna señal de lo que ocurre aguas abajo puede viajar en contra de la corriente para avisar a las partículas que vienen.
    

### Variaciones de Estudio

Para entenderlo completamente, visualiza qué pasaría si cambiamos los datos del punto P:

**Variación 1: Flujo Subcrítico (El río tranquilo)**

- Supongamos que el canal es profundo y lento: $v_p = 1.5 \text{ m/s}$ y $h_p = 2 \text{ m}$.
    
- **Celeridad:** $c = \sqrt{9.81 \cdot 2} = 4.429 \text{ m/s}$.
    
- **Características:**
    
    - $C_+ = v + c = 1.5 + 4.429 = +5.929 \text{ m/s}$ (Viaja rápido aguas abajo).
        
    - $C_- = v - c = 1.5 - 4.429 = \mathbf{-2.929 \text{ m/s}}$ (¡Atención al signo negativo!).
        
- **Gráfico:** En el plano $x-t$, la curva $C_+$ se inclina hacia la derecha (`/`), pero la curva $C_-$ se inclina hacia la izquierda (`\`).
    
- **Impacto físico:** Una perturbación en este río sí puede viajar aguas arriba en contra de la corriente (por ejemplo, si cierras una compuerta aguas abajo, el nivel del agua empezará a subir hacia atrás).
    

**Variación 2: Flujo Crítico (El límite exacto)**

- Supongamos que $v_p = 3 \text{ m/s}$ y calculas que $c = 3 \text{ m/s}$.
    
- **Características:** $C_+ = +6 \text{ m/s}$ y $C_- = 0 \text{ m/s}$.
    
- **Gráfico:** La curva $C_-$ se vuelve una línea perfectamente vertical en el plano $x-t$. La onda negativa se queda estacionaria, tratando de nadar contra la corriente a la misma velocidad a la que el río la empuja.
    

## 3. Aplicación en Fronteras y Resolución Numérica (Enunciado 6)

Aquí es donde la teoría se convierte en algoritmos. Se evalúa un extremo del canal para determinar cómo reacciona la velocidad y la profundidad ante un cambio (una descarga).

### El caso original: Descarga en el Extremo Izquierdo

Se planteó un canal de 400 m con $h_o = 5 \text{ m}$, sin movimiento inicial, al que se le impone un caudal de salida de $q = -1 \text{ m}^2\text{/s}$.

- **El método:** Te paras en el punto de descarga y "miras" hacia adentro del canal. La única curva que llega a ti es la $C_-$ que trae la información del estado original del agua (el invariante de Riemann).
    
- **El ensamble:** Se acopla la ecuación de la característica ($u_d - 2\sqrt{gh_d} = u_o - 2\sqrt{gh_o}$) con la ecuación geométrica de la frontera ($q = u_d \cdot h_d$).
    
- **El obstáculo numérico:** Queda una función no lineal de la forma $F(h_d) = \frac{-q}{h_d} - 2\sqrt{gh_d} - \text{Constante} = 0$.
    

### La Variación: Programación Computacional (La mente iterativa)

En tu examen, resuelves $F(h_d) = 0$ con la función Solve de la calculadora. Sin embargo, para dominar verdaderamente esta sección, es útil verla desde la perspectiva de la programación de métodos numéricos, como cuando se automatizan resolutores de ecuaciones diferenciales ordinarias mediante bucles de predicción y corrección.

Cuando te enfrentas a $\frac{1}{h_d} + 6.264\sqrt{h_d} = 14.007$, estás programando mentalmente un bucle de búsqueda de raíces (como el método de Newton-Raphson o bisección).

1. **Valor Semilla (Initial Guess):** Todo método iterativo requiere un punto de partida. En canales, la semilla perfecta siempre es la profundidad original antes de la perturbación ($h_0 = 5 \text{ m}$).
    
2. **Iteración (The Loop):**
    
    - Inicias el bucle.
        
    - Evalúas la ecuación. Si el error respecto a 14.007 es grande, el algoritmo ajusta $h_d$ reduciéndolo.
        
    - Las iteraciones continúan hasta que el paso de convergencia sea menor a la tolerancia deseada, logrando el resultado de $h_d \approx 4.854 \text{ m}$.
        
3. **Post-proceso:** Con la raíz hallada, el script calcula el resto de variables dependientes, como la velocidad $u_d = q / h_d \approx -0.206 \text{ m/s}$.
    

### Variación Práctica: ¿Y si evaluamos el Extremo Derecho?

Si en tu examen el punto de descarga ocurre en el **extremo derecho** del canal (en $s=L$):

- No usarás la curva $C_-$. Te pararás en el extremo derecho y observarás que la onda de información viene desde la izquierda. Utilizarás la característica positiva **$C_+$**.
    
- El invariante a conservar será: $u_d + 2\sqrt{gh_d} = u_o + 2\sqrt{gh_o}$.
    
- El caudal de salida será positivo (el agua fluye en el sentido positivo del eje $x$), por lo que $q = +1 \text{ m}^2\text{/s}$.
    
- Al ensamblar y resolver el bucle numérico, la lógica geométrica dictará que, si sacas agua por la derecha, el nivel $h_d$ también disminuirá respecto a sus 5 metros originales, y el agua acelerará hacia la derecha.
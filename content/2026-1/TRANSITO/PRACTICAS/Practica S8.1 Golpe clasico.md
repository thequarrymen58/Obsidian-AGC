# Enunciado
En un sistema hidraulico reservorio - tuberia - valvula
$L=1000\ m$ 
$D=0.5\ m$
$C=1000\ m/s$ 
$f=0.02$
Carga de agua constante en el reservorio de $H=100\ m$. 
El caudal de $Q_0=1\ m^3/s$ es interrumpido en el extremo aguas abajo en $5\ s$. 

1. Calcular las variaciones de la altura de presión en el extremo aguas abajo de la tuberia.

**Datos del problema:**
*   Área $A = \frac{\pi \cdot 1^2}{4} = 0.7854$ m²
*   Velocidad inicial $v_0 = \frac{Q_0}{A} = \frac{2.0}{0.7854} = 2.546$ m/s

**a) Calcular la carga piezométrica (Estado Permanente):**
Se calcula la pérdida de carga por fricción de Darcy-Weisbach:
$$
h_f = f \frac{L}{D} \frac{v_0^2}{2g} = 0.01976 \cdot \frac{10000}{1} \cdot \frac{2.546^2}{2 \cdot 9.81} \approx 65.3 \text{ m}
$$
La línea piezométrica empieza en 400 m en el reservorio y baja linealmente hasta:
$$
H_{valvula\_inicial} = 400 - 65.3 = \mathbf{334.7 \text{ m}}
$$

**b) Máxima presión posible por cierre instantáneo:**
Calculamos la sobrepresión de Allievi por parar súbitamente el agua ($\Delta v = v_0 = 2.546$ m/s):
$$
\Delta H = \frac{a \cdot \Delta v}{g} = \frac{1000 \cdot 2.546}{9.81} \approx \mathbf{259.6 \text{ m}}
$$
La presión máxima absoluta en la válvula será la suma de la presión estática más el golpe de ariete:
$$
H_{max} = H_{valvula\_inicial} + \Delta H = 334.7 + 259.6 = \mathbf{594.3 \text{ m}}
$$

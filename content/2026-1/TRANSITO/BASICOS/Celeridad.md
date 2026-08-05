Se dice que la celeridad es la velocidad a la cual viaja un onda a travez de un medio.
# [[Golpe de Ariete (Tuberias)]]
Aqui la celeridad dependera del fluido como el material que lo contiene, ya que a mas elastico el material, menor sera la propagacion, asi como la manera en la que este anclada la tuberia.

La celeridad en el golpe de ariete se calcula como.
$$
C=\sqrt{\frac{1}{\rho \cdot (\frac{1}{K_W}+\frac{D \cdot k}{E \cdot e})}}\ [m/s] \tag{1}
$$
 Donde: 
$𝐾_W$: Modulo de Bulk o Modulo de compresibilidad del fluido, en $[Pa]$. 
$k$: Anclaje de la tuberia.
$𝐸$: Modulo de Young o Modulo de elasticidad de la tuberia, en $[Pa]$.
𝑒: Espesor de la tuberia, en $[m]$.
$𝐷$: Diámetro interno de la tuberia, en $[m]$. 
$\rho$: Densidad media, en $[kg/m3]$. Es media debido a que puede variar con la temperatura, asi que esa media seria en condiciones normales.

Podriamos tomar la ecuacion (1), y simplicar el termino en el denominador de la siguiente manera.
$$
\frac{1}{K_C}=\frac{1}{K_W}+\frac{D \cdot k}{E \cdot e} \tag{2}
$$
Donde
$K_C$: Modulo de compresibilidad efectivo del agua en una tuberia elastica, en $[Pa]$.

Entonces, reemplazando (2) en (1).
$$
C=\sqrt{\frac{K_c}{\rho}} \tag{3}
$$
## Anclaje
Para este valor se tiene distintos valores, dependiendo del tipo de anclaje de la tuberia, por ejemplo.
- Tuberias libres de moverse longitudinalmente
$$
k=\frac{5}{4}-\nu
$$
- Tuberias ancladas a ambos extremos
$$
k=1-\nu^2
$$
- Tuberias con juntas de dilataacion.
$$
1-0.5 \cdot \nu
$$

Donde.
$\nu$: Relacion o coeficiente de Poisson, adimensional.

## Forma simplificada
Tomando la eq. (1) y haciendo reemplazos en el sistema tecnico de unidades, ==solo para agua==
1. Densidad: $\rho = \frac{1000 \text{ kg/m}^3}{9.81 \text{ m/s}^2} = \mathbf{101.94 \text{ UTM/m}^3}$
2. Módulo de compresibilidad: $K_W = \mathbf{2.07 \times 10^8 \text{ kgf/m}^2}$
3. Coeficiente de anclaje, se usara un anclaje estándar, $\mathbf{k = 1}$.

Reemplazando estos tres valores fijos en tu ecuación teórica:

$$
\begin{align*}
C &= \frac{1}{\sqrt{\frac{101.94}{2.07 \times 10^8} + \frac{101.94 \times 1}{E} \cdot \frac{D}{e}}} \\ \\

C &= \frac{1}{\sqrt{4.924 \times 10^{-7} + \frac{101.94}{E} \cdot \frac{D}{e}}}
\end{align*}
$$
Multiplicando el numerador y el denominador por 9900, operando y simplificando, se tiene.
$$
C = \frac{9900}{\sqrt{48.3 + \frac{10^{10}}{E} \cdot \frac{D}{e}}}\ [m/s] \tag{4}
$$
Donde la celeridad en este caso tiene un sistema tecnico, ya no es internacional, por lo que el modulo de elasticidad ya no esta en pascalaes $[Pa]$, sino en $[\text{kgf/m}^2]$.  
Para ello debemos recordar que
$$
\begin{align*}
Pa&=\frac{N}{m^2} \\ \\
1\ \text{kgf}&=9.8067\ N \\
\end{align*}
$$
Por ejemplo, para el acero.
$$
\begin{align*}
E_{acero}&=2 \cdot 10^{11}\ Pa =2 \cdot 10^{11}\ \frac{\cancel{N}}{m^2} \cdot \frac{1\ \text{kgf}}{9.8067\ \cancel{N}} \\ \\
E_{acero}&=2.03 \cdot 10^{10}\ \frac{\text{kgf}}{m^2}
\end{align*}
$$


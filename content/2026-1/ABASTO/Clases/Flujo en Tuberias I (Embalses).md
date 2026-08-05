Se tiene la siguiente tuberia, que simula una troncal principal, con distribucion a lo largo de la longitud.
![[Pasted image 20260528221409.png|681]]
Donde se tiene
$Q_0$: Caudal de entrada
$Q$: Caudal de salida
$q$: [[Caudal Unitario]]
$L$: Longitud de la tuberia

Por continuidad sabemos que el caudal que entra menos el caudal que sale distribuido, es igual al caudal que sale, es decir.
$$
Q_{entra}-Q_{distribuido}=Q_{sale}
$$
Lo cual seria igual a 
$$
Q_0-qL=Q \tag{1}
$$
Si analizamos ahora un embalse, el cual tiene una descarga por una tuberia, y analizamos un tramo diferencial, la perdida de carga sera dada por $dh_{f}$, para una longitud diferencial $dL$.
![[Pasted image 20260529001627.png]]
Entonces mediante la ecuacion de [[Ecuacion Darcy-Weisbach]] en funcion del caudal se tiene.
$$
dh_f = \frac{8 \cdot f \cdot Q^2}{\pi^2 \cdot g \cdot D^5 } \cdot dL\ \tag{2}
$$
Integrando (2)
$$
\begin{align*}
\int_{0}^{h_f}dh_f &= \frac{8 \cdot f \cdot Q^2}{\pi^2 \cdot g \cdot D^5 } \cdot \int_{0}^{L} dL \tag{3}
\end{align*}
$$
Tomaremos los terminos constantes y los agruparemos en $k$
$$
82.626 \cdot 10^{-3}\cdot \frac{f }{D^5 } = k \tag{4}
$$
Luego en (3).
$$
\begin{align*}
\int_{0}^{h_f}dh_f &= k \cdot Q^2\int_{0}^{L} dL \tag{5}
\end{align*}
$$
Tomando la ecuacion (1) e introduciendola en (5).
$$
\begin{align*}
\int_{0}^{h_f}dh_f &= k \int_{0}^{L}(Q_0-qL)^2  dL \tag{6}
\end{align*}
$$
Resolviendo la integral, operando los terminos y volviendo a reemplazar $q$ por $Q_0-Q$.
$$
h_f=\frac{k \cdot L}{3} \cdot \left(Q_0^2+Q_0 \cdot Q+Q^2\right) \tag{7}
$$
La cual es la perdida de carga en un sistema con distribucion filtrable, osea con huequitos, si es que no hay una salida del otro lado debido a que hay un tapon, entonces el caudal $Q=0$, por lo que la ecuacion (7) quedaria como.
$$
h_f=\frac{k \cdot L}{3} \cdot \left(Q_0^2\right) \tag{8}
$$


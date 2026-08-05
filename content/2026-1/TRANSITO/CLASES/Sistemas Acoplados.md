Tiene que ver con el tema de [[Camara de Equilibrio]].
El ejemplo mas conocido se ve en el tema de esclusas, como las vistas en el canal de Panama, las cuales sirven para poder transportar embarcaciones de una altura mayor a una menor y vice-versa.
![[Pasted image 20260511161355.png|500]]

Tenemos entonces el sistema de funcionamiento tipico de dos tanques o depositos, los cuales empiezan con niveles distintintos, y deben de nivelarse para que la embarcacion pueda continuar su camino.
![[Pasted image 20260511174045.png]]

De la imagen se tiene.
$A_a$: Area de la primera camara
$A_b$: Area de la camara donde se trasladara el fluido
$A_0$: Area por donde el fluido pasa de $A_a$ hacia $A_b$.
$H_1,\ H_2$: Alturas iniciales.
# Demostracion
Empezaremos por ver que la carga hidraulica o energia potencial que permitira el paso del fluido de un depositvo a otro, es la diferencia de alturas, teniendo de forma diferencial.
$$
dh=dy_H-dy_h \tag{1}
$$
Por otro lado, sabemos que por continuidad, se tiene que el caudal que entra por la segunda camara es igual al caudal que sale de la primera, por lo que el balance deberia de ser igual a 0.
$$
\begin{align*}
Q &=\Sigma (v\cdot A) \\
0 &=\frac{dy_H}{dt}A_a+\frac{dy_h}{dt}A_b \\
\frac{dy_h}{dt}A_b &=-\frac{dy_H}{dt}A_a \\
\frac{dy_h}{dt} &=-\frac{A_a}{A_b}\cdot \frac{dy_H}{dt} \tag{2}
\end{align*}
$$
Si nos deshacemos de la derivada de tiempo, introducimos (2) en (1).
$$
\begin{align*}
dh &= dy_H+ \frac{A_a}{A_b}\cdot dy_H \\
dh &= dy_H (\frac{A_a+A_b}{A_b}) \\
dy_H &= \frac{A_b}{A_a+A_b} \cdot dh \tag{3}
\end{align*}
$$
Luego tenemos el caudal de salida el cual sale por el orificio de area $A_0$, el cual se puede describir mediante la ecuacion de Torricelli, tal como se vio en [[Tiempo de vaciado por gravedad]].
$$
Q=\frac{dV}{dt}=C_d \cdot A_0 \cdot \sqrt{2 \cdot g \cdot H} \tag{4}
$$
Pero el flujo viene desde el deposito A, por lo que el volumen tambien sera de este.
$$
V=A_a \cdot y_H \tag{5}
$$
Haciendo (5) en (4), se tiene.
$$
A_a \cdot \left(-\frac{dy_H}{dt}\right)=C_d \cdot A_0 \cdot \sqrt{2 \cdot g \cdot H} \tag{6}
$$
**Por que se le agrego un signo negativo?**, debido a que la formula de torricelli es siempre positiva, sin embargo, el nivel del primer depostivo esta disminuyendo, por ello agregamos el simbolo negativo para asegurarnos de que ello este pasando.

Luego reemplazamos (3) en (6), y despejamos los diferenciales.

$$
\begin{align*}
A_a \cdot \left(-\frac{A_b}{A_a+A_b} \cdot dh\right) &=C_d \cdot A_0 \cdot \sqrt{2 \cdot g \cdot H} \\
-H^{-1/2}dh &=\frac{A_a+A_b}{A_a \cdot A_b} \cdot C_d \cdot A_0 \cdot \sqrt{2 \cdot g} \cdot dt \tag{7}
\end{align*}
$$
Para integrar la ecuacion (7), con los limites de integracion tal que para un tiempo inicial, la altura $h$ sera igual a la diferencia del primer y segundo deposito, luego en un tiempo posterior, esta diferencia sera nula, ya que los depositos se habran nivelado.
$$
\begin{align*}
t=0 &\rightarrow h=H_1-H_2 \\
t=\Delta t &\rightarrow h=0
\end{align*}
$$
Entonces, integrando (7), recordando tambien que los limites de integracion se invierten con el signo negativo, se tendria.
$$
\begin{align*}
-\int_{H_1-H_2}^{0}H^{-1/2}dh &=\frac{A_a+A_b}{A_a \cdot A_b} \cdot C_d \cdot A_0 \cdot \sqrt{2 \cdot g} \cdot \int_{0}^{\Delta t} dt \\
\int_{0}^{H_1-H_2}H^{-1/2}dh &=\frac{A_a+A_b}{A_a \cdot A_b} \cdot C_d \cdot A_0 \cdot \sqrt{2 \cdot g} \cdot \int_{0}^{\Delta t} dt \\

2 \cdot \sqrt{H_1-H_2} &= \frac{A_a+A_b}{A_a \cdot A_b} \cdot C_d \cdot A_0 \cdot \sqrt{2 \cdot g} \cdot  \Delta t \tag{8}
\end{align*}
$$
Finalmente despejando la ecuacion (8) tenemos, el tiempo en el cual tardan los depositos en nivelarse.
$$
\Delta t=\frac{2 \cdot A_a \cdot A_b}{C_d \cdot (A_a+A_b) \cdot A_0 \cdot \sqrt{2\cdot g}} \cdot (\sqrt{H_1-H_2})\tag{9}
$$
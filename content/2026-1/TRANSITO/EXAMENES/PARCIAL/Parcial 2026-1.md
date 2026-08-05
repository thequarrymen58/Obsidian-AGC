# Examen Parcial de Flujo Transitorio
Escuela de Ingeniería Mecánica de Fluidos, FCF, UNMSM
Profesor: Dr.-Ing. C. Carbonel

Nombre: Alejandro Gonzales Cipriano
Cod: 20130134
Fecha: 25/05/2026
Ciclo: 2026 - 1
# Pregunta 1
Un recipiente de área de sección $A_i$, con orificio de descarga de área $A_0$ con carga de agua instantánea $H$ y en donde una variación es representada por $dh$. El recipiente cuenta con un caudal de salida $Q_o$.
a) Deducir el intervalo de tiempo $\Delta t_{70}$ que es necesario para el vaciado del 70% del total del recipiente.
b) Si existiera una descarga de ingreso $Q_i$ con un caudal igual a $Q_o/10$, ¿cual seria el $\Delta t_{70}$?
## Solucion
### Item a
**Se pide deducir el intervalo de tiempo $\Delta t_{70}$ que es necesario para el vaciado del 70% del total del recipiente.**

Se asumira un sistema permanente, teniendose el siguiente sistema.
![[Pasted image 20260525130512.png|327]]
S tiene la ecuacion de balance de caudales en el sistema.
$$
\frac{dV}{dt}=Q_i-Q_0 \tag{1a.1}
$$
Usando Torricelli, tenemos que la velocidad de salida es igual a.
$$
v_0=\sqrt{2\cdot g\cdot H} \tag{1a.2}
$$
Pero si sabemos que el caudal es igual a la velocidad por el area, tendremos que.
$$
Q_0=v_0\cdot A_0 \tag{1a.3}
$$
(1a.3) en (1a.2).
$$
Q_0= C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_0 \tag{1a.4}
$$
Donde la ecuacion (1a.4) se le agrego un coeficiente de descarga $C_d$, el cual depende de la salida del reservorio, a continuacion se muestran valores para este coeficiente, dependiendo del tipo de salida.
![[Pasted image 20260511164526.png|628]]
Reemplazando (1a.4) en (1a.1).
$$
\frac{dV}{dt}=Q_i-C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_0 \tag{1a.5}
$$
Pero recordemos que el volumen del tanque viene dando por $V=A_1 \cdot h(t)$, luego reemplazando en (1a.5) y despejando los terminos diferenciales, se tiene.
$$
dt=\frac{A_i}{Q_i-C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_0} \cdot dh \tag{1a.6}
$$
Como no mencionan que este entrando caudal podemos decir que $Q_i=0$, teniendo.
$$
dt=-\frac{A_i}{C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_0} \cdot dh \tag{1a.7}
$$
Como nos piden el tiempo necesario para vaciar el 70% del tanque, integramos esta ecuación evaluando los límites correspondientes. Si se vacía el 70% del volumen, en el tanque restará el 30% del volumen inicial. Por lo tanto los limites quedarian como 
$$
\begin{align*}
t &\rightarrow [0,\Delta t_{70}] \\
h &\rightarrow [H,0.3 \cdot H]
\end{align*}
$$
Luego, en (1a.7).
$$
\begin{align*}
\Delta t_{70} &=\int_{H}^{0.3H}\frac{A_i}{-C_d\cdot A_0\cdot \sqrt{2g\,H}}\,H^{-1/2}\,dH \\
\Delta t_{70} &=\frac{2A_i}{C_d\cdot A_0\cdot \sqrt{2g}}\left(\sqrt{H}-\sqrt{0.3H}\right)
\end{align*}
$$
Finalmente se tiene el tiempo en el que tarde en vaciarse el tanque llenado a un 70%.
$$
\Delta t_{70} =\frac{2 \cdot A_i\, \sqrt{H}}{C_{d} \cdot A_{0} \cdot\sqrt{2g}}\,(1-\sqrt{0.3}) \tag{1a.8}\\
$$
### Item b
**Se pide $\Delta t_{70}$, si existiera una descarga de ingreso $Q_i$ con un caudal igual a $Q_o/10$.**

Al agregar un caudal de ingreso $Q_i$​, la ecuación de balance de caudales en (1a.1), se modifica. Luego sustituyendo la condición de que $Q_i​$ es una décima parte del caudal de salida nos queda.
$$
\frac{dV}{dt}=\frac{Q_{o}}{10}-Q_{o}=-0.9Q_{o} \tag{1b.1}
$$
Reemplazando el diferencial de volumen y la fórmula del caudal de salida, visto en (1a.4)
$$
\frac{dH}{dt}=-\frac{0.9\left(C_d\,A_{0}\cdot \sqrt{2gH}\right)}{A_i} \tag{1b.2}
$$
Luego integrando (1b.2) con los mismo limites de integracion en el item a, se tiene.
$$
\Delta t_{70}=\int_{H}^{0.3\,H}\frac{A_i}{-0.9\cdot C_d\cdot A_0\cdot \sqrt{2gH}}\,\mathrm{d}H
$$
Finalmente se tiene el tiempo en el que tarde en vaciarse el tanque llenado a un 70%, teniendo un caudal de entrada el cual es igual la decima parte del caudal de salida.
$$
\Delta t_{70}(\text{con ingreso})=\frac{1}{0.9}\left[\frac{2 \cdot A_i \cdot\sqrt{H}}{C_d\cdot A_0\cdot \sqrt[\,]{2g}}\right](1-\sqrt{0.3}) \tag{1b.3}
$$
### Comparacion item a y b
Si tomamos (1b.3), notamos que se parte de esta se encuentra en (1a.8), entonces. 
$$
\begin{align*}
\Delta t_{70}(\text{con ingreso}) &=\frac{1}{0.9} \cdot \Delta t_{70}(\text{sin ingreso}) \\
&= 1.1111 \cdot \Delta t_{70}(\text{sin ingreso}) \\
&=111.11\% \cdot \cdot \Delta t_{70}(\text{sin ingreso}) \\ 
\end{align*}
$$
Es decir para el 70% del tanque lleno, y con un caudal de entrada demoraria en vaciarse un 11.11% mas que si no entrase caudal.
# Pregunta 2
Para un líquido en un tubo en U simple, en donde $L$ es la longitud de la columna de fluido: 
a) Deducir la ecuación de movimiento no permanente para el caso de un líquido con resistencia laminar, considerando que el esfuerzo de Poiseuille es $\tau_o = \frac{8\mu v}{D}$, siendo $\mu$ la viscosidad dinámica, $D$ es el diámetro del tubo y $v$ la velocidad del flujo en el tubo. 
b) Obtener la solución analítica.
## Solucion
### Item a
**Se pide deducir la ecuacion de movimiento en su forma transitoria, con resistencia laminar.**

Se hara uso de la ecuacion de movimiento de Euler, la cual esta dado como.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} = 0\tag{2a.1}
$$
Si analizamos la imagen en detenimiento, se tiene, el analisis de un elemento fluido de forma diferencial, en forma de cilindro (puesto que se aplicara en tuberias) con diametro $D$ y area $A$.
![[Pasted image 20260525142601.png|410]]
Se tiene entonces la fuerza de friccion ($F_{Friccion}$), segun la ecuacion.
$$
F_{Friccion}=\tau_0 \times \pi \times D \times \partial s \tag{2a.2}
$$
Donde:
$\tau_0$: Es el esfuerzo cortante entre capas de fluido y pared-fluido.
$D$: Diametro del elemento fluido.
$\partial s$: Parte diferencial de la linea de corriente.

De la Segunda Ley de Newton, se tiene que el despeje de la aceleracion, y justamente es esta aceleracion la cual deberemos de añadir a la ecuacion (2a.1)
$$
\begin{align*}
a &=\frac{F_{Friccion}}{m} \\
&= \frac{F_{Friccion}}{\rho \times V} \tag{2a.3}
\end{align*}
$$
Donde el volumen del elemento fluido viene dado por.
$$
V=A \times\partial s
$$
Pero $A=\frac{\pi \times D^2}{4}$, entonces.
$$
V=\frac{\pi \times D^2 \times \partial s}{4} \tag{2a.4}
$$
Reemplazando (2a.4) y (2a.2) en (2a.3), se tiene.
$$
a=\frac{4 \times\tau_0 \times \pi \times D \times \partial s }{\rho \times \pi \times D^2 \times \partial s}
$$
Depejando y eliminando terminos.
$$
a=\frac{4\times \tau_0 }{\rho \times D} \tag{2a.5}
$$
Añadiendo el termino (2a.5) en (2a.1), se tiene.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{4\times \tau_0 }{\rho \times D}= 0\tag{2a.6}
$$
Lo que nos dice la ecuacion (6) es que para tanto para el regimen transitorio como el permanente, para una misma velocidad la fuerza de friccion sera la misma.

Segun Hagen-Poiseuille, para un flujo laminar en una tuberia circular se tiene la igualdad para el esfuerzo cortante en una pared.
$$
\tau_0=\frac{8\times \mu\times v}{D} \tag{2a.7}
$$
Reemplazando (2a.7) en (2a.6)
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{32 \times \mu\times v }{\rho \times D^2}= 0\tag{2a.8}
$$
Lueho haciendo $(2a.8)\times \partial s$, e integrando sobre toda la region fluida $s$ de 1 a 2, la cual es igual a la longitud del fluido estirada horizontalmente $L$.
$$
\frac{\partial v}{\partial t}L+\frac{v_2^2-v_1^2}{2g}+g(z_2-z_1)+(P_2-P_1)+\frac{32 \times \mu\times v }{\rho \times D^2}L= 0\tag{2a.9}
$$
- La velocidad de bajada es igual a la subida, $v_2^2=v_1^2$.
- La presion es atmosferica en ambos casos $P_2=P_1=P_{atm}$.
- La altura que sube y baja, es $z$ en ambos casos, por ello, $z_1-z_2=2z$.

Luego de aplicar estos factos, nos queda.
$$
\frac{\partial v}{\partial t}L+2gz+\frac{32 \times \mu\times v }{\rho \times D^2}L= 0\tag{2a.10}
$$
Multiplicando por (2a.10) por $1/L$, m.a.m.
$$
\frac{\partial v}{\partial t}+\frac{2gz}{L}+\frac{32 \times \mu\times v }{\rho \times D^2}= 0\tag{2a.11}
$$
Asi mismo, sabemos que la velocidad es igual a la derivada de la posicion con respecto al tiempo, pero en nuestro caso, solo se mueve en el eje z, por lo que.
$$
v=\frac{\partial z}{\partial t} \tag{2a.12}
$$
Reemplazando (2a.12) en (2a.11), y recordando que $\nu=\mu/\rho$.
$$
\frac{\partial^2 z}{\partial t^2}+\frac{2gz}{L}+\frac{32\times \nu }{ D^2} \frac{\partial z}{\partial t}= 0\tag{2a.13}
$$
Luego nos queda un sistema de ecuaciones con (2a.12) y (2a.13).
$$
\begin{cases}
\frac{\partial^2 z}{\partial t^2}+\frac{2gz}{L}+\frac{32 \times \nu}{D^2}\frac{\partial z}{\partial t}= 0 \\
v =\frac{\partial z}{\partial t}
\end{cases} \tag{2a.14}
$$
### Item b
**Se pide la solucion analitica hallada en el punto (2a.13)**
Esta ecucion es una EDO de segundo orden y tiene una solucion de la forma.
$$
z=C_1e^{at}+C_2e^{bt} \tag{2b.1}
$$
Las variables a y b salen debido a que nos dejaran dos soluciones, ademas de que estas mediante la ecuacion cuadratica una quedara con signo positivo y la otra con signo negativo, tal que.
$$
\begin{align*}
a^2+\frac{32\cdot\nu}{D^2}a+\frac{2g}{L}=0 \\
b^2+\frac{32\cdot\nu}{D^2}b+\frac{2g}{L}=0
\end{align*}
$$
Entonces por ecuacion cuadratica, se tiene.
$$
\begin{align*}
a=-\frac{16\cdot\nu}{D^2}+\sqrt{\left(\frac{16\cdot\nu}{D^2}\right)^2-\frac{2g}{L}} \\
b=-\frac{16\cdot\nu}{D^2}-\sqrt{\left(\frac{16\cdot\nu}{D^2}\right)^2-\frac{2g}{L}}
\end{align*}
$$
Reemplazaremos variables.
$$
\begin{align*}
m &=\frac{16\cdot\nu}{D^2} \\
n &=\sqrt{\left(\frac{16\cdot\nu}{D^2}\right)^2-\frac{2g}{L}}
\end{align*}
$$
Luego reemplazando m y n en (2b.1), se tiene.
$$
z=C_1e^{(-m+n)t}+C_2e^{(-m-n)t} \tag{2b.2}
$$
De la solucion de esa ecuacion, se llegan a dos casos, el primero de ellos es cuando
$$
\frac{16\cdot\nu}{D^2}>\sqrt{\frac{2g}{L}}
$$
De donde se tiene su solucion asociada, la cual nos da el maximo desplazamiento para Z, esta ecuacion se usa cuando se empieza desde la posicion de equilibrio.
$$
Z=\frac{V_0}{\sqrt{m^2-n^2}}\left(\frac{m-n}{m+n}\right)^{m/2n}=V_0\sqrt{\frac{L}{2g}}\left(\frac{m-n}{m+n}\right)^{m/2n} \tag{2b.3}
$$
Donde
$V_0$: Es la velocidad cuando $t=0$

Mientras que el segundo es caso es.
$$
\frac{16\cdot\nu}{D^2}<\sqrt{\frac{2g}{L}}
$$
El cual tambien tiene su solucion asociada
$$
Z=\frac{V_0}{\sqrt{n'^2+m^2}}\exp{\left(-\frac{m}{n'}\arctan{\frac{n'}{m}}\right)}=V_0\sqrt{\frac{L}{2g}}\exp{\left(-\frac{m}{n'}\arctan{\frac{n'}{m}}\right)} \tag{2b.4}
$$
Donde por ejemplo
$\exp(algo)=e^{(algo)}$
$n'$: Esta fraccion saldra imaginaria, por lo que nos deberemos de quedar con la parte real, e.g, $\sqrt{-6.387}=i\cdot2.527$, por lo que $n'=2.527$.
# Pregunta 3

![[Pasted image 20260525123932.png|528]]
En el caso de un sistema compuesto por reservorio, tubería y cámara de equilibrio, mostrado en la figura, la cámara de equilibrio (chimenea) tiene área de sección $A_c$ y la tubería de longitud $L$, posee un área de sección $A_t$. A partir del nivel de referencia (NR) se indican las alturas y niveles de puntos referenciales del sistema.
a) Deducir la ecuación no permanente de continuidad de la cámara. 
b) Deducir la ecuación de movimiento no permanente en la tubería que abastece la cámara. 
c) ¿Cómo se determina el nivel de agua en la cámara de equilibrio cuando el flujo en el sistema fluye en estado permanente?
## Solucion
### Item a
**Se pide deducir la ecuación no permanente de continuidad de la cámara.** 

Si hacemos un analisis del sistema, tendremos tal que la tasa de cambio del volumen con respecto al tiempo, es igual al caudal que entra menos el caudal que sale.
$$
\frac{dV}{dt}=Q-Q_s \tag{3a.1}
$$
Claramente, si el caudal que entra y sale es el mismo, no habra variacion es decir, $dV/dt=0$.

Pero el volumen $V$ es igual a el area de la camara por la altura, es decir.
![[Pasted image 20260525124406.png|240]]
$$
V=A_c(h)\cdot h(t) \tag{3a.2}
$$
En este caso el volumen es h-d2, pero la derivada del volumen (3a.2), hara que $d_2$ sea cero ya que es una constante.

Luego tambien se tiene que el caudal $Q$, es igual a el area de la tuberia multiplicada por su velocidad.
$$
Q=A_t\cdot v_t \tag{3a.3}
$$
Reemplazando (3a.2) y (3a33) en (3a.1), y despejando $dh/dt$.
$$
\frac{dh(t)}{dt}=\frac{1}{A_c(h)} (A_t\cdot v_t-Q_s) \tag{3a.4}
$$
En este caso el $dh(t)/dt$ no es parcial por que se toma que el nivel no variara con respecto al espacio, solo al tiempo, esto es debido a que hemos tomado un sistema concentrado, si fuese un sistema distribuido si deberia de ser parcial.
Este tipo de sistemas se discuten con mayor profundidad [aqui](https://www.youtube.com/watch?v=SNYoTaKlXPg&t=34s).
### Item b
**Se pide deducir la ecuación de movimiento no permanente en la tubería que abastece la cámara.** 

Si tomamos el tramo de tuberia podremos hacer un analisis de cantidad de momento.
![[Pasted image 20260525124922.png|585]]
Segun la Segunda Ley de Newton, hacemos $\Sigma F=m\cdot a$, teniendo
$$
F_{Presion\ 1}-F_{Presion\ 2}-F_{Friccion}+F_{Gravedad}=m\cdot a \tag{3b.1}
$$
Donde
$F_{Presion\ 1}=P_1\cdot A_t$
$F_{Presion\ 2}=P_2\cdot A_t$
$F_{Gravedad}=m\cdot g\cdot \sin{\theta}=\rho\cdot V \cdot g \cdot \sin{\theta}=\rho\cdot g\cdot A_t\cdot L\cdot \sin{\theta}$
$a=dv/dt$
$m=\rho \cdot V=\rho \cdot A_t\cdot L$
Entonces reemplazando en (3b.1), se tiene.
$$
P_1\cdot A_t-P_2\cdot A_t-F_{Friccion}+\rho\cdot g\cdot A_t\cdot L\cdot \sin{\theta}=\rho \cdot A_t\cdot L\cdot \frac{dv}{dt} \tag{3b.2}
$$
Si hacemos un analisis de la presion, en metros de columna de agua nos queda que.
$$
\begin{align*}
\frac{P_1}{\rho\cdot g}=H-d_1 \\
\frac{P_2}{\rho\cdot g}=h-d_2
\end{align*} \tag{3b.3}
$$
Asi mismo, si vemos el angulo $\theta$, se cumple que,
$$
\sin{\theta}=\frac{d_1-d_2}{L} \tag{3b.4}
$$
Ademas, podriamos incluir el caudal en lugar de la velocidad, sabiendo que.
$$
\begin{align*}
Q &=A_t \cdot v \\
v &= \frac{Q}{A_t} \tag{3b.5}
\end{align*}
$$
Reemplazando (3b.3), (3b.4), y (3b.9) en (3b.5), se tiene.
$$
A_t\cdot \rho \cdot g\cdot (H-d_1-h+d_2)-F_{Friccion}+\rho\cdot g\cdot A_t\cdot L\cdot \frac{d_1-d_2}{L}=\rho \cdot A_t\cdot L\cdot \frac{1}{A_t}\cdot \frac{dQ}{dt} \tag{b6}
$$
Si dividimos (3b.6) por $A_t\cdot \rho \cdot g$.
$$
\begin{align*}
 (H-d_1-h+d_2)-\frac{F_{Friccion}}{A_t\cdot \rho \cdot g}+d_1-d_2 &= \frac{L}{g\cdot A_t}\cdot \frac{dQ}{dt}  \\
H-h-\frac{F_{Friccion}}{A_t\cdot \rho \cdot g} &=\frac{L}{g\cdot A_t}\cdot \frac{dQ}{dt} \tag{3b.7}
\end{align*}
$$
Si hacemos un Analisis Dimensional del termino $F_{Friccion}$, tendremos que.
$$
\begin{align*}
\frac{F_{Friccion}}{A_t\cdot \rho \cdot g} = \frac{[\frac{kg\cdot m}{s^2}]}{[\frac{m^2\cdot kg\cdot m}{m^3\cdot s^2}]}
= [m]
\end{align*}
$$
Toda el cociente no es mas que las perdidas por friccion en metros, es decir $h_f$, finalmente en (3b.7).
$$
\begin{align*}
H-h-h_f &=\frac{L}{g\cdot A_t}\cdot \frac{dQ}{dt} \\
\frac{dQ}{dt} &=\frac{A_t}{L}\cdot g\cdot (H-h-h_f) \tag{3b.8}
\end{align*}
$$

### Item c
**Se pide determinar el nivel de agua en la cámara de equilibrio cuando el flujo en el sistema fluye en estado permanente.**

Esto se da cuando, la valvula se cierra, y la energia cinetica que viaja por la tuberia se transforma en energia potencial que va hacia arriba de la camara.
![[Pasted image 20260511160825.png|525]]

Comenzaremos por igualar la energia potencial y cinetica, es decir $E_k=E_{p}$
$$
\frac{1}{2}\cdot m_t\cdot v^2=m_c\cdot g\cdot z \tag{3c.1}
$$
Tomaremos de forma diferencial, donde:
$m_t$: Es la masa de fluido que viaja por la tuberia y es igual a 
$$
m_t=\rho \cdot A_t\cdot \tag{3c.2}ds
$$
$m_t$: Masa de fluido que viaja por la camara y es igual a 
$$
m_c=\rho \cdot A_c \cdot \tag{3c.3}dz
$$
Reemplazando en (3c.2) y (3c.3) en (3c.1).
$$
\frac{1}{2}\cdot \cancel{\rho} \cdot A_t\cdot ds\cdot v^2=\cancel{\rho} \cdot A_c \cdot dz\cdot g\cdot z \tag{3c.4}
$$
Si quisieramos integrar sobre todo el sistema, para ambos casos se tendrian los limites tal que.
$$
\begin{align*}
s &\rightarrow[0-L] \\
z &\rightarrow[0-h]
\end{align*}
$$
Integrando en (3c.4), y despejando h
$$
\begin{align*}
\frac{1}{2}\cdot A_t \cdot v^2 \cdot \int_{0}^{L}ds &=A_c\cdot g\cdot \int_{0}^{h}z\cdot dz \\
\frac{1}{\cancel{2}}\cdot A_t \cdot v^2 \cdot L &=A_c\cdot g\cdot \frac{h^2}{\cancel{2}} \\
h &= v \cdot \sqrt{\frac{A_t}{A_c}\cdot \frac{L}{g}}\ [m] \tag{3c.5}
\end{align*}
$$
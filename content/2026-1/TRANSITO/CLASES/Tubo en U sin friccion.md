Todo comienza teniendo la imagen, donde se muestra un tubo en U, abierto a la atmosfera.
![[Pasted image 20260331103538.png|225]]
Luego de ello se tiene la [[Ecuacion del Movimiento de Euler#Aceleracion|Ecuacion del movimiento de Euler]], para un fluido incompresible, es decir la densidad es constante $\rho =cte$.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} = 0\tag{1}
$$
Donde.
$p$: Es el campo de presiones
$v$: Es el campo de velocidades

Tomando la ecuacion (1), y multiplicando m.a.m, por $\partial ds$, se tiene.
$$
\frac{1}{\rho}\partial p+ g\partial z + v\partial v + \frac{\partial v}{\partial t}\partial s = 0\tag{2}
$$
Integrando m.a.m la ecuacion (2), y con limites en los puntos 1 y 2 en la imagen, se tiene.
$$
\frac{1}{\rho}\int_{1}^{2}\partial p+ g\int_{1}^{2}\partial z + v\int_{1}^{2}v\partial v + \int_{1}^{2}\frac{\partial v}{\partial t}\partial s = 0\tag{3}
$$

Entonces, resolviendo en (3) se tiene.
$$
\frac{1}{\rho}(p_2-p_1)+g(z_2-z_1)+\frac{v_2^2-v_1^2}{2}+\int_{1}^{2}\frac{\partial v}{\partial t}\partial s=0\tag{4}
$$
Pero si notamos, la tuberia esta abierta a la atmosfera, por lo que la presion 1 y 2 seran iguales es decir.
$$
p_1=p_2=p_{atm}
$$
Asi mismo, las velocidades en los puntos tambien seran iguales.
$$
v_1=v_2
$$
Entonces reemplazando en (4), se tiene.
$$
g(z_2-z_1)+\int_{1}^{2}\frac{\partial v}{\partial t}\partial s=0\tag{5}
$$
Se dice que $\frac{\partial v}{\partial t}$ no depende de la posicion $s$, 
==lo cual no entendi ya que la velocidad es funcion de la distancia y el tiempo==, la explicacion que se da es que el fluido avanza como un solo bloque, y que la velocidad es la misma en cualquier punto de la tuberia.

Pasamos (5) al otro lado, teniendo.
$$
g(z_2-z_1)=-\frac{\partial v}{\partial t}\int_{1}^{2}\partial s\tag{6}
$$
Veamos la integral
$$
\begin{align*}
\int_{1}^{2}\partial s=s|_{1}^{2}\tag{7}\\
\end{align*}
$$
Al integrar esta ecuacion desde la posicion 1 hasta 2, lo que se hizo fue calcular la longitud de toda la columna, como si estuviese dispuesta de forma horizontal, pero justamente toda esa columna tiene por longitud "$L$".
$$
\int_{1}^{2}\partial s=s|_{1}^{2}=L\tag{8}
$$
Luego tambien, se tiene que la distancia de $z_2$ hasta el punto medio es $z$, y la distancia de $z_1$ es $-z$, por lo que 
$$
z_2-z_1=z-(-z)=2z\tag{9}
$$
Entonces reemplazando (8) y (9) en (6) se tiene.
$$
g(2z)=-\frac{\partial v}{\partial t}L\tag{10}
$$

Tambien se dice que $\frac{\partial v}{\partial t}$ solo depende del tiempo, y por ello, ==por algo que tampoco entiendo== la expresion se vuelve en una segunda derivada de $z$ con respecto a $t$, es decir.

Como tenemos un bloque de fluido que se mueve en el eje z.
![[Pasted image 20260401114841.png]]
Entonces la posicion solo dependedera de $z$, por lo que la velocidad seria
$$
v=\frac{d(posicion)}{dt}
$$
En este caso la posicion seria $z$, por lo que nos quedaria
$$
v=\frac{dz}{dt}
$$
Entonces (10), nos pide la derivada de la velocidad, teniendo.
$$
\frac{\partial v}{\partial t}=\frac{\partial d}{\partial t}\left(\frac{\partial z}{\partial t}\right)=\frac{\partial^2z}{dt^2}\tag{11}
$$
Entonces reemplazando (11) en (10)
$$
g(2z)=-\frac{\partial^2z}{dt^2}L\tag{12}
$$
De donde se tiene la ecuacion diferencial parcial de segundo orden.
$$
(2g)\partial{t^2}=-L\frac{\partial^2z}{z}\tag{13}
$$
==La cual no se como se soluciona, pero queda de la siguiente forma.==
$$
z = C_1 \cos\left(\sqrt{\frac{2g}{L}}\,t\right) + C_2 \sin\left(\sqrt{\frac{2g}{L}}\,t\right)\tag{14}
$$
Como $C_1$ y $C_2$ son constantes, las cuales dependen de las condiciones iniciales del problema, se derivara la ecaucion (14)
$$
\frac{dz}{dt} = -C_1 \sin\left(\sqrt{\frac{2g}{L}}\,t\right)\sqrt{\frac{2g}{L}} + C_2 \cos\left(\sqrt{\frac{2g}{L}}\,t\right)\sqrt{\frac{2g}{L}}\tag{15}
$$
Para un $t=0$, se tiene.
$$
\frac{dz}{dt}=0\tag{16}
$$
Resolviendo (16).
$$
z=0\tag{17}
$$
Entonces si reemplazamos (17) en (15), se tiene que.
$$
C_2=0
$$
Por lo que (15), quedaria de la siguiente manera.
$$
\frac{dz}{dt} = -C_1 \sin\left(\sqrt{\frac{2g}{L}}\,t\right)\sqrt{\frac{2g}{L}}\tag{18}
$$
Con lual volveremos a derivar la ecuacion (18), teniendo.
$$
\frac{d^2z}{dt^2} = -C_1\cos\left(\sqrt{\frac{2g}{L}}\,t\right)\frac{2g}{L}\tag{19}
$$
En (19) hacemos de nuevo $t=0$.
$$
\begin{align*}
\frac{d^2z}{dt^2} = -C_1\cos\left(0\right)\frac{2g}{L} \\
\frac{d^2z}{dt^2}=-C_1\frac{2g}{L}\tag{20}
\end{align*}
$$
Si tomamos notamos podemos reemplazar (20) en (12), teniendo.
$$
\frac{d^2z}{dt^2}L=-C_12g=-2gz\tag{21}
$$
De donde se observa que la constante arbitraria $C_1=z$, pero este $z$ sera cambiado por $Z_0$, para evitar confusiones y para denotar que $Z_0$ es cuando se parte de la posicion inicial, es decir partir del reposo

Luego de haber obtenido las constantes y valores para las diferenciales se tienen las condiciones iniciales.
$$
\begin{align*}
t=0 \rightarrow \ \frac{dz}{dt}=0 \\
C_2=0 \\
C_1=z
\end{align*}
$$
Entonces, reemplazando en la solucion de la edp, eq (14)
$$
z(t) = Z_0\cos\left(\sqrt{\frac{2g}{L}}\,t\right) \tag{22}
$$
Recordando una vez mas que para un $t=0$ 
$$
z=Z_0
$$

ya que si $t=0$, se tiene.
$$
z(0) = Z_0\cos\left(\sqrt{\frac{2g}{L}}\,0\right)=Z_0 \tag{22}
$$
Lo cual se dice que tiene la forma de una ecuacion de [[Movimiento Armonico Simple]]
$$
T_{oscilacion}^{ideal}=2\pi \sqrt{\frac{L}{g}}
$$
Asi mismo, en la ecuacion (22), se tiene que la frecuencia angular $(\omega)$ es igual a
$$
\sqrt{\frac{2g}{L}}=\omega \tag{23}
$$
La ecuacion que usa en todos los casos, para la aplicacion analitica es (22).

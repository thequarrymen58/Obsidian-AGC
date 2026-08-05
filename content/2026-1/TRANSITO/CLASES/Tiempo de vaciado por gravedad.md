# Derivacion
Si recordamos del tema [[Camara de Equilibrio]], se tenia la ecuacion de balance de caudales en el sistema.
$$
\frac{dV}{dt}=Q_1-Q_2 \tag{1}
$$
Por otro lado, se tiene un tanque con area de ingreso $A_1$ y caudal $Q_1$, y su area de salida $Q_2$ con un caudal $Q_2$, y de altura $H$
![[Pasted image 20260511163021.png|425]]
Si usamos la igualdad de Torricelli, tendriamos que la velocidad de salida es igual a.
$$
v_2=\sqrt{2\cdot g\cdot H} \tag{2}
$$
Pero si sabemos que el caudal es igual a la velocidad por el area, tendremos que.
$$
Q_2=v_2\cdot A_2 \tag{3}
$$
(3) en (2).
$$
Q_2= C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_2 \tag{4}
$$
Donde la ecuacion (4) se le agrego un coeficiente de descarga $C_d$, el cual depende de la salida del reservorio.
![[Pasted image 20260511164526.png|650]]
Reemplazando (4) en (1).
$$
\frac{dV}{dt}=Q_1-C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_2 \tag{5}
$$
Pero recordemos que el volumen del tanque viene dando por $V=A_1 \cdot h(t)$, luego reemplazando en (5) y despejando los terminos diferenciales, se tiene.
$$
dt=\frac{A_1}{Q_1-C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_2} \cdot dh \tag{6}
$$
Para integrar (6), se tendrian los limites tal que.
$$
\begin{align*}
t &\rightarrow [t_1,t_2] \\
h &\rightarrow [h_1,h_2]
\end{align*}
$$
Luego.
$$
\begin{align*}
\int_{t_1}^{t_2}dt &= \int_{h_1}^{h_2}\frac{A_1}{Q_1-C_d\cdot \sqrt{2\cdot g\cdot H}\cdot A_2} \cdot  dh \tag{7}
\end{align*}
$$
Esta integral, tal cual, se resolveria de manera numerica, puesto que el tanque se esta llenando y vaciando al mismo tiempo.

En el caso de que solo se este vaciando, en tonces $Q_1=0$, y ya podriamos integrar, quedando.
![[Pasted image 20260511170018.png|450]]
$$
\begin{align*}
\int_{t_1}^{t_2}dt &= \frac{A_1}{-C_d\cdot \sqrt{2\cdot g}\cdot A_2} \cdot  \int_{h_1}^{h_2} \frac{1}{\sqrt{H}} dh \tag{8}
\end{align*}
$$
Luego

$$
\begin{align*}
t_2-t_1=\Delta t &=\frac{2\cdot A_1}{C_d\cdot A_2 \cdot \sqrt{2\cdot g}} \cdot (\sqrt{H_1}-\sqrt{H_2}) \tag{9}
\end{align*}
$$
Si hacemos que el nivel $H_2$ se encuentre en mismo nivel de referencia, es decir $H_2=0$ nos quedaria.
$$
\begin{align*}
t_{vaciado} &=\frac{2\cdot A_1}{C_d\cdot A_2 \cdot \sqrt{2\cdot g}} \cdot \sqrt{H_1} \\
t_{vaciado} &=\frac{2\cdot A_1}{C_d\cdot A_2 \cdot \sqrt{2\cdot g \cdot H_1}} \cdot H_1 \tag{10}
\end{align*}
$$
# Analisis de Caudal
Si analizamos la ecuacion (10), veremos que el numerador no es mas que dos veces el volumen, mientras que el denominador seria el caudal, es decir.
$$
\begin{align*}
t_{vaciado} &=\frac{2 \cdot V_1}{Q_1} \\
Q_1 &= \frac{2 \cdot V_1}{t_{vaciado}}
\end{align*}
$$
Esto quiere decir que el caudal ira disminuyendo a medida que el tiempo avanza, tiene sentido puesto que la carga hidraulica o energia potencial tambien disminuye.


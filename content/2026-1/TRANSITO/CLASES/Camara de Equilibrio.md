O tambien llamada chimenea de equilibrio
# Material 
## Puro texto y funcionamiento
Parece de ia pero es interensate
[OpenFlows | Water Infrastructure - Modeling Reference - Surge Tanks - Communities](https://bentleysystems.service-now.com/community?id=kb_article_view&sysparm_article=KB0014039)
Esta otra, es un pdf, donde se ven valvulas que funcionan con el principio
[Microsoft Word - White Paper Transient and Surge Related Pipe Bursts](https://www.singervalve.com/hubfs/Transient_and_Surge_Related_Pipe_Bursts.pdf)
## Simulacion
[Microsoft Word - 04_2009_030_Riasi_377-384_3k](https://www.sv-jme.eu/wp-content/uploads/ns_articles/files/ojs3/1500/submission/1500-1-1988-1-2-20171103.pdf)
## Tesis
[Surge Tank Pressure Transient Analysis | PDF | Gas Technologies | Chemical Engineering](https://www.scribd.com/document/923712917/Encv3fa-Prac-Surge-Tank)

# Derivacion
En chadwick se encuentra en la pag 465 del lector edge, pero no es lo mismo que hace el profesor.

Se tiene un sistema de la siguiente manera
![[Pasted image 20260508154100.png|525]]

## Analisis Global
Si hacemos un analisis del sistema, tendremos tal que la tasa de cambio del volumen con respecto al tiempo, es igual al caudal que entra menos el caudal que sale.
$$
\frac{dV}{dt}=Q-Q_s \tag{1}
$$
Claramente, si el caudal que entra y sale es el mismo, no habra variacion es decir, $dV/dt=0$.

Pero el volumen $V$ es igual a el area de la camara por la altura, es decir.
![[Pasted image 20260508154559.png|135]]
$$
V=A_c(h)\cdot h(t) \tag{2}
$$
En este caso el volumen es h-d2, pero la derivada del volumen (2), hara que $d_2$ sea cero ya que es una constante.

Luego tambien se tiene que el caudal $Q$, es igual a el area de la tuberia multiplicada por su velocidad.
$$
Q=A_t\cdot v_t \tag{3}
$$
Reemplazando (2) y (3) en (1), y despejando $dh/dt$.
$$
\frac{dh(t)}{dt}=\frac{1}{A_c(h)} (A_t\cdot v_t-Q_s) \tag{4}
$$
En este caso el $dh(t)/dt$ no es parcial por que se toma que el nivel no variara con respecto al espacio, solo al tiempo, esto es debido a que hemos tomado un sistema concentrado, si fuese un sistema distribuido si deberia de ser parcial.
Sobre estos tipos de sistemas, ver mas [aqui](https://www.youtube.com/watch?v=SNYoTaKlXPg&t=34s).
## Analisis conservacion de momento
Si tomamos el tramo de tuberia podremos hacer un analisis de cantidad de momento.
![[Pasted image 20260508162400.png|525]]
Segun la [[Segunda Ley de Newton]], hacemos $\Sigma F=m\cdot a$, teniendo
$$
F_{Presion\ 1}-F_{Presion\ 2}-F_{Friccion}+F_{Gravedad}=m\cdot a \tag{5}
$$

Donde
$F_{Presion\ 1}=P_1\cdot A_t$
$F_{Presion\ 2}=P_2\cdot A_t$
$F_{Gravedad}=m\cdot g\cdot \sin{\theta}=\rho\cdot V \cdot g \cdot \sin{\theta}=\rho\cdot g\cdot A_t\cdot L\cdot \sin{\theta}$
$a=dv/dt$
$m=\rho \cdot V=\rho \cdot A_t\cdot L$

Entonces reemplazando en (5), se tiene.
$$
P_1\cdot A_t-P_2\cdot A_t-F_{Friccion}+\rho\cdot g\cdot A_t\cdot L\cdot \sin{\theta}=\rho \cdot A_t\cdot L\cdot \frac{dv}{dt} \tag{6}
$$

Si hacemos un analisis de la presion, en metros de columna de agua nos queda que.
$$
\begin{align*}
\frac{P_1}{\rho\cdot g}=H-d_1 \\
\frac{P_2}{\rho\cdot g}=h-d_2
\end{align*} \tag{7}
$$
Asi mismo, si vemos el angulo $\theta$, se cumple que,
$$
\sin{\theta}=\frac{d_1-d_2}{L} \tag{8}
$$
Ademas, podriamos incluir el caudal en lugar de la velocidad, sabiendo que.
$$
\begin{align*}
Q &=A_t \cdot v \\
v &= \frac{Q}{A_t} \tag{9}
\end{align*}
$$
Reemplazando (7), (8), y (9) en (6), se tiene.
$$
A_t\cdot \rho \cdot g\cdot (H-d_1-h+d_2)-F_{Friccion}+\rho\cdot g\cdot A_t\cdot L\cdot \frac{d_1-d_2}{L}=\rho \cdot A_t\cdot L\cdot \frac{1}{A_t}\cdot \frac{dQ}{dt} \tag{10}
$$
Si dividimos (10) por $A_t\cdot \rho \cdot g$.
$$
\begin{align*}
 (H-d_1-h+d_2)-\frac{F_{Friccion}}{A_t\cdot \rho \cdot g}+d_1-d_2 &= \frac{L}{g\cdot A_t}\cdot \frac{dQ}{dt}  \\
H-h-\frac{F_{Friccion}}{A_t\cdot \rho \cdot g} &=\frac{L}{g\cdot A_t}\cdot \frac{dQ}{dt} \tag{11}
\end{align*}
$$
Si hacemos un [[Analisis Dimensional]] del termino $F_{Friccion}$, tendremos que.
$$
\begin{align*}
\frac{F_{Friccion}}{A_t\cdot \rho \cdot g} = \frac{[\frac{kg\cdot m}{s^2}]}{[\frac{m^2\cdot kg\cdot m}{m^3\cdot s^2}]}
= [m]
\end{align*}
$$
Toda el cociente no es mas que las perdidas por friccion en metros, es decir $h_f$, finalmente en (11).
$$
\begin{align*}
H-h-h_f &=\frac{L}{g\cdot A_t}\cdot \frac{dQ}{dt} \\
\frac{dQ}{dt} &=\frac{A_t}{L}\cdot g\cdot (H-h-h_f) \tag{12}
\end{align*}
$$

Luego entre (12) y (4), tendremos un sistema de EDOS.
## EDOS finales

$$
\begin{cases}
\frac{dh(t)}{dt} =\frac{1}{A_c(h)} (A_t\cdot v_t-Q_s) \\
\frac{dQ}{dt} =\frac{A_t}{L}\cdot g\cdot (H-h-h_f)
\end{cases} \tag{13}$$
Con las siguientes condiciones de contorno.
$$
\begin{align*}
t\ge\tau_{man} &\rightarrow \ Q_s(t)=0  \tag{14}\\
0\le t \le \tau &\rightarrow \ Q_s(t)=Q_0\cdot(1-\frac{t}{\tau_{man}}) \tag{15}
\end{align*}
$$
Donde
$\tau_{man}$: Tiempo de maniobra de la valvula.
$Q_0$: Sera el caudal inicial en regimen permanente, antes de que se cierre la valvula.

### Que es t?
En el caso que se tenga una valvula con un tiempo de cierre de $\tau_{man}=10\ [s]$, entonces, el caudal $Q_s(t)$, sera igual a cero cuando $t=\tau_{man}$, en ese caso $t=10$.
A partir de ahi el tiempo sigue avanzando para analizar el transitorio.
Entonces las notaciones $Q_s(t)$ y $h(t)$, nos quieren decir que esos niveles cambian conforme avanza el tiempo.

# Maximo nivel que puede alcanzar
Esto se da cuando, la valvula se cierra, y la energia cinetica que viaja por la tuberia se transforma en energia potencial que va hacia arriba de la camara.
![[Pasted image 20260511160825.png|525]]

Comenzaremos por igualar la energia potencial y cinetica, es decir $E_k=E_{p}$
$$
\frac{1}{2}\cdot m_t\cdot v^2=m_c\cdot g\cdot z \tag{16}
$$
Tomaremos de forma diferencial, siendo.

$m_t$: Es la masa de fluido que viaja por la tuberia y es igual a 
$$
m_t=\rho \cdot A_t\cdot ds
$$
$m_t$: Masa de fluido que viaja por la camara y es igual a 
$$
m_c=\rho \cdot A_c \cdot dz
$$
Reemplazando en (16).
$$
\frac{1}{2}\cdot \cancel{\rho} \cdot A_t\cdot ds\cdot v^2=\cancel{\rho} \cdot A_c \cdot dz\cdot g\cdot z \tag{17}
$$
Si quisieramos integrar sobre todo el sistema, para ambos casos se tendrian los limites tal que.
$$
\begin{align*}
s &\rightarrow[0-L] \\
z &\rightarrow[0-h]
\end{align*}
$$
Integrando en (18), y despejando h
$$
\begin{align*}
\frac{1}{2}\cdot A_t \cdot v^2 \cdot \int_{0}^{L}ds &=A_c\cdot g\cdot \int_{0}^{h}z\cdot dz \\
\frac{1}{\cancel{2}}\cdot A_t \cdot v^2 \cdot L &=A_c\cdot g\cdot \frac{h^2}{\cancel{2}} \\
h &= v \cdot \sqrt{\frac{A_t}{A_c}\cdot \frac{L}{g}}\ [m] \tag{18}
\end{align*}
$$

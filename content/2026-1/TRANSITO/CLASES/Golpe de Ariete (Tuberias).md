[[Joukowsky]]
# Demostracion
## Ecuaciones Gobernantes
![[Pasted image 20260610110533.png|496]]
### Movimiento
Se dice que se tiene la ecuacion de movimiento, en terminos del caudal, altura, area.
$$
\frac{\partial Q}{\partial t}+g \cdot A_0 \cdot \frac{\partial h}{\partial s}+g \cdot A_0 \cdot S_f=0 \tag{1}
$$
Donde:
$S_f$: Pendiente hidraulica, y $S_f=h_f/L$.
### Continuidad
Y tambien la ecuacion de continuidad, en el cual se le añade la [[Celeridad]], ya que este contiene valores para la expansion del fluido, el cual es importante para cuantificar su compresibilidad.
$$
\frac{\partial h}{\partial t}+\frac{C^2}{g \cdot A_0} \cdot \frac{\partial Q}{\partial s}=0 \tag{2}
$$
Donde
$C$: Celeridad de onda visto en la ecuacion de [[Joukowsky]].
## Condiciones
### Frontera
![[Pasted image 20260610112009.png|543]]
$$
\begin{cases}
h=h_R \rightarrow s=0 \\ \\
Q=Q_s(t) \rightarrow s=L
\end{cases}
$$
### Iniciales
Para la altura y el caudal, se propone una funcion $f(s)$ la cual describe el estado inicial del sistema, cuando solamente se tiene la perdida de carga hidraulica debido a la friccion.
$$
\begin{cases}
h(s,t=0)=f(s) \\ \\
Q(s, t=0)=Q_0 \rightarrow s=L
\end{cases}
$$
## Metodo de las Caracteristicas
### Planteamiento
Se empezara por tomar la ecuacion (2), y se multiplicara por $\frac{g \cdot A_0}{C}$, el cual es un artificio para agrupar las EDP mas adelante.
$$
g \cdot \frac{A_0}{C} \cdot \frac{\partial h}{\partial t}+C \cdot \frac{\partial Q}{\partial s}=0 \tag{3}
$$
Ahora sumaremos (1) y (3), reagrupando.
$$
\begin{align*}
\frac{\partial Q}{\partial t}+g \cdot A_0 \cdot \frac{\partial h}{\partial s}+g \cdot A_0 \cdot S_f + g \cdot \frac{A_0}{C} \cdot \frac{\partial h}{\partial t}+C \cdot \frac{\partial Q}{\partial s}=0 \\ \\

\left(\frac{\partial Q}{\partial t}+C \cdot \frac{\partial Q}{\partial s}\right)+g \cdot \frac{A_0}{C} \cdot \left(\frac{\partial h}{\partial t}+C \cdot \frac{\partial h}{\partial s}\right)+g \cdot A_0 \cdot S_f=0 \tag{4}
\end{align*}
$$
Y restaremos (1) con (3), tambien reagrupando.
$$
\begin{align*}
\frac{\partial Q}{\partial t}+g \cdot A_0 \cdot \frac{\partial h}{\partial s}+g \cdot A_0 \cdot S_f - \left(g \cdot \frac{A_0}{C} \cdot \frac{\partial h}{\partial t}+C \cdot \frac{\partial Q}{\partial s}\right)=0 \\ \\

\left(\frac{\partial Q}{\partial t}-C \cdot \frac{\partial Q}{\partial s}\right)-g \cdot \frac{A_0}{C} \cdot \left(\frac{\partial h}{\partial t}-C \cdot \frac{\partial h}{\partial s}\right)+g \cdot A_0 \cdot S_f=0 \tag{5}
\end{align*}
$$
Se obtiene una ecuacion positiva y otra negativa, justamente para detallar el movimiento de ida ($+C$) y vuelta ($-C$) de la celeridad.

Entonces se tiene la ecuacion (4) y (5), con la cual se dice que se puede armar, un grafico como una especie rectas que se intersectan, donde $S$, es una seccion de la tuberia.
![[Pasted image 20260626153805.png|513]]

De manera resumida se tiene para ambos signos.
$$
\begin{align*}
\left(\frac{\partial Q}{\partial t} \pm C \cdot \frac{\partial Q}{\partial s}\right) \pm g\cdot \frac{A_0}{C} \cdot \left(\frac{\partial h}{\partial t} \pm C \cdot \frac{\partial h}{\partial s}\right)+g \cdot A_0 \cdot S_f=0 \tag{6}
\end{align*}
$$
Agrupando estos terminos con su [[Enfoques Lagrangiano y Euleriano#Derivada Material|Derivada material]], recordando que es un problema unidimensional, aplicado solo en la coordenada $s$.
Para el termino que incluye el caudal $Q$, se tiene.
$$
\frac{dQ}{dt}=\frac{\partial Q}{\partial t}+(\vec V \cdot \nabla Q)
$$
Donde $\vec V=\frac{\partial s}{\partial t}=\pm C$, ya que el vector es solo unidimensional. Ademas que la [[Celeridad]] entra con dos signos ya que puede tener valor positivo y negativo, luego.
$$
\begin{align*}
\frac{dQ}{dt} &=\frac{\partial Q}{\partial t}+ (\pm C \cdot \nabla Q) \\
&=\frac{\partial Q}{\partial t}+ (\pm C \cdot \frac{\partial Q}{\partial s})
\end{align*}
$$
De forma resumida, para el caudal, quedaria como 
$$
\left(\frac{\partial Q}{\partial t} \pm C \cdot \frac{\partial Q}{\partial s}\right)=\frac{dQ}{dt} \tag{7}
$$
Mientras que para el segundo termino, donde se cuentra la altura $h$, seria de manera similar
$$
\left(\frac{\partial h}{\partial t} \pm C \cdot \frac{\partial h}{\partial s}\right)=\frac{dh}{dt} \tag{8}
$$
Entonces introduciendo (7) y (8) en (6)
$$
\frac{dQ}{dt} \pm g\cdot \frac{A_0}{C} \cdot \frac{dh}{dt}+g \cdot A_0 \cdot S_f=0 \tag{9}
$$
Factorizando la derivada, y mandando las constantes al otro lado, se tendria.
$$
\frac{d}{dt}\left(Q \pm g\cdot \frac{A_0}{C} \cdot h \right)=-g \cdot A_0 \cdot S_f \tag{10}
$$
Esta energia es la que quita energia debido a la friccion, y el termino $\left(Q \pm g\cdot \frac{A_0}{C} \cdot h \right)$ es denominado como cuasi-invariante de Riemman, cuasi por que en realidad si varia.
### Integracion $I\rightarrow P$
Luego multiplicamos la ecuacion (10) por $1/dt$ m.a.m, e integramos de izquierda (I) hasta el punto medio (P), esta linea pertenece a la curva carteristica positiva $+C$.
$$
\begin{align*}
\int^{P}_{I}d\left(Q + g\cdot \frac{A_0}{C} \cdot h \right)=-\int^{P}_{I}g \cdot A_0 \cdot S_f\,dt \\ \\
\left(Q + g\cdot \frac{A_0}{C} \cdot h \right)^{P}_{I}=-\int^{P}_{I}g \cdot A_0 \cdot S_f\,dt \tag{11}
\end{align*}
$$
### Discretizacion
Teniendo la grafica.
![[Pasted image 20260701172342.png|411]]
Donde:
$I,\ D$: Lado izquierdo y derecho de un tramo de tuberia 
$P$: Punto el cual se desea saber el valor

Tomaremos la ecuacion (11) y la discretizaremos, quedando.
$$
\left(Q + g\cdot \frac{A_0}{C} \cdot h \right)^{P}_{I}=-\int^{P}_{I}g \cdot A_0 \cdot S_f\,dt \approx =-g \cdot A_0 \cdot S_f\,\Delta t \tag{12}


$$
Se dice que la integral de la derecha es complicada de resolver, ya que el caudal varia rapidamente en el tiempo. 

Pero este delta de tiempo es muy pequeña por lo que se igualara el valor que tuvo inicialmente, $S_f=S_{f,\ I}$, es decir se mantendra constante. 

Entonces se tiene, por un lado la ecuacion evaluada para el caudal y la altura, y por el otro el estado inicial en I.
$$
(Q_P-Q_I)+(h_P-h_I)\cdot g\cdot \frac{A_0}{C}=-g \cdot A_0 \cdot S_{f,\ I} \cdot \Delta t \tag{13}
$$
Multiplicamos (13) por $Z=C/(gA_0)$ m.a.m.
$$
\begin{align*}
\underbrace{\frac{C}{g \cdot A_0}}_{Z} \cdot (Q_P-Q_I)+\cancel{\frac{C}{g \cdot A_0}} \cdot (h_P-h_I)\cancel{\cdot g\cdot \frac{A_0}{C}}&=-\frac{C}{\cancel{g \cdot A_0}} \cdot \cancel{g \cdot A_0} \cdot S_{f,\ I} \cdot \Delta t \\ \\

Z \cdot (Q_P-Q_I)+(h_P-h_I)&=-S_{f,\ I} \cdot C \cdot \Delta t
\end{align*}
$$
Recordemos que $\partial s/\partial t=\Delta s/ \Delta t=C$, por lo que $\Delta s=\Delta t \cdot C$, entonces.
$$
Z \cdot (Q_P-Q_I)+(h_P-h_I)=-S_{f,\ I} \cdot \Delta s \tag{14}
$$
Asi como la pendiente hidraulica $S_{f,\ I}$, la cual como se sabe es igual a $S_f=H_f/L$, luego de hacer los reemplazos tenemos que.
$$
S_{f,\ I}=\frac{f \cdot Q_I \cdot |Q_I|}{2 \cdot g \cdot D \cdot A_0^2} \tag{15}
$$
Luego (15) en (14).
$$
Z \cdot (Q_P-Q_I)+(h_P-h_I)=-\frac{f \cdot Q_I \cdot |Q_I|}{2 \cdot g \cdot D \cdot A_0^2} \cdot \Delta s 
$$
Excluimos "P" por un lado e "I" por el otro.
$$
\begin{align*}
Z \cdot Q_P+h_P=Z\cdot Q_I+h_I-\frac{f \cdot Q_I \cdot |Q_I|}{2 \cdot g \cdot D \cdot A_0^2} \cdot \Delta s \tag{16}
\end{align*}
$$
### Integracion $D\rightarrow P$
Haciendo un analisis similar al anterior, partiremos de la ecuacion (12), cambiandolo el signo ya que la celeridad es negativa $-C$.
$$
\left(Q - g\cdot \frac{A_0}{C} \cdot h \right)^{P}_{D}=-\int^{P}_{D}g \cdot A_0 \cdot S_f\,\Delta t \tag{17}
$$
En este caso, la integral en la derecha nosotros conocemos las condiciones en el punto D, por lo que la perdida tomara este valor, ademas evaluamos la integral en la parte izquierda.
$$
(Q_P-Q_D)-(h_P-h_D)\cdot g\cdot \frac{A_0}{C}=-g \cdot A_0 \cdot S_{f,\ D} \cdot \Delta t \tag{18}
$$
Multiplicando por Z, reemplazando $\Delta s=\Delta t \cdot C$.
$$
Z(Q_P-Q_D)-(h_P-h_D)=- S_{f,\ D} \cdot \Delta s \tag{19}
$$
Teniendo su pendiente hidraulica.
$$
S_{f,\ D}=\frac{f \cdot Q_D \cdot |Q_D|}{2 \cdot g \cdot D \cdot A_0^2} \tag{20}
$$
Luego reemplazando (20) en (19)
$$
Z(Q_P-Q_D)-(h_P-h_D)=-\frac{f \cdot Q_D \cdot |Q_D|}{2 \cdot g \cdot D \cdot A_0^2} \cdot \Delta s 
$$
Y excluimos "P" por un lado e "I" por el otro.
$$
Z\cdot Q_P-h_P= Z\cdot Q_D-h_D-\frac{f \cdot Q_D \cdot |Q_D|}{2 \cdot g \cdot D \cdot A_0^2} \cdot \Delta s
$$
A esta ecaucion para que la altura quede con el mismo signo que la ecuacion (16), multiplicaremos por (-1) m.a.m, quedando.
$$
-Z\cdot Q_P+h_P= -Z\cdot Q_D+h_D+\frac{f \cdot Q_D \cdot |Q_D|}{2 \cdot g \cdot D \cdot A_0^2} \cdot \Delta s \tag{21}
$$

### Simplificaciones
Reducimeros de tamaño las ecuaciones (16) y (21) haciendo
$$
R=\frac{f}{2 \cdot g \cdot D \cdot A_0^2} \cdot \Delta s \tag{22}
$$
Teniendo
$$
\begin{align*}
Z \cdot Q_P+h_P &=Z\cdot Q_I+h_I- R \cdot Q_I \cdot |Q_I|\tag{23} \\ \\
-Z\cdot Q_P+h_P &=-Z\cdot Q_D+h_D+ R \cdot Q_D \cdot |Q_D|\tag{24}
\end{align*}
$$
Y podemos seguir reduciendo si en los terminos de la parte izquierda los igualamos a un termino $C_D$ o $C_I$, ==**no confundir con la celeridad!**==
$$
\begin{align*}
C_I&=Z\cdot Q_I+h_I- R \cdot Q_I \cdot |Q_I| \tag{25} \\ \\
C_D&=-Z\cdot Q_D+h_D+ R \cdot Q_D \cdot |Q_D|\tag{26}
\end{align*}
$$
Entonces usando (25) y (26) en (23) y (24)
$$
\begin{align*}
Z \cdot Q_P+h_P &=C_I\tag{27} \\ \\
-Z\cdot Q_P+h_P &= C_D \tag{28}
\end{align*}
$$
Si sumamos y restamos (27 y (28) podremos obtener algunas igualdades, no se con que fin se hace esto, creo que lo que importa hasta ahora es usar algo que conocemos, que en este caso es el caudal y la altura. 
$$
\begin{align*}
h_P&=\frac{C_I+C_D}{2} \tag{29} \\ \\
Q_P&=\frac{C_I-C_D}{2 \cdot Z} \tag{30}
\end{align*}
$$
![[Pasted image 20260626163556.png|431]]
De donde se dice que en el tiempo $t=0$, se conocen las condiciones de la tuberia como la presion, caudal, etc.
Y que se calcula para cada punto de izquierda a derecha.

### Extremos
En los extremos las ecuaciones se saben las condiciones
- **Izquierdo**
Aqui es donde se da la conexion Tanque - Tuberia, por lo que no habra una caracteristica positiva, solo negativa.
![[Pasted image 20260703182532.png|408]]
Por lo que se tendra que la altura $h_P$ sera igual a la altura total del reservorio, es decir
$$
h_P=H
$$
Entonces si tomamos la ecuacion (28) nos quedaria
$$
\begin{align*}
-Z\cdot Q_P+h_P &= C_D \\ \\
-Z\cdot Q_P+H &= C_D \\ \\
Q_P &=\frac{H-C_D}{Z} \tag{31}

\end{align*}
$$
- **Derecho**
Para este lado se tiene que no hay una caracteristica negativa, solo positiva.
![[Pasted image 20260703190846.png|418]]
Entonces en el caudal $Q_P$ seria igual al caudal de salida tomado en cuenta en la condicion de frontera, es decir.
$$
Q_P=Q_s(t)
$$


Luego (27) tendriamos.
$$
\begin{align*}
Z \cdot Q_P+h_P &=C_I \\ \\
Z \cdot Q_s(t)+h_P &=C_I \\ \\
h_P &=C_I-Z \cdot Q_s(t) \tag{32}
\end{align*}
$$
Entonces tendriamos las ecuaciones para todo el tramo, adicionalmente para los puntos extremos.
$$
\begin{cases}
Q_P =\frac{H-C_D}{Z} &\rightarrow s=0 \\ 
h_P =C_I-Z \cdot Q_s(t) &\rightarrow s=L \\ \\
h_P=\frac{C_I+C_D}{2} &\rightarrow 0<s<L \\ 
Q_P=\frac{C_I-C_D}{2 \cdot Z} &\rightarrow 0<s<L
\end{cases}
$$

## Valvula de Cierre
Si analizamos la valvula en un momento de cierre
![[Pasted image 20260706161201.png|147]]
Se denota como $\alpha (t)$ al cierre de la valvula con respecto al tiempo.
Este cierre causa una perdida local, la cual es cuantificada como.
$$
h_f=K \cdot \frac{Q \cdot |Q|}{2 \cdot g \cdot A_0^2}
$$
Donde:
$K$: Es el coeficiente de perdida de la valvula.
Graficamente se tiene la relacion entre el cierre $\alpha (t)$ y el coeficiente $K$.
![[Pasted image 20260706161546.png|510]]


# Succion Negativa
Se tiene el siguiente sistema, el cual conciste de una tanque bajo, del cual mediante una canastilla, se conecta una tuberia, a una bomba, de la cual sale y se encuentra con una valvula check, y prosigue su camino hasta el desfogue a una cota mayor.
![[Pasted image 20260521140605.png]]
Donde:
$\nabla C_1$: Cota del liquido del tanque inferior, o cisterna.
$\nabla C_0$: Cota del eje de la bomba
$\nabla T_0$: Nivel del suelo
$\nabla C_2$: Cota del liquido del tanque superior

$H_S$: Altura de succion, desde el nivel de liquido en la cisterna, hasta el eje de la bomba.
$$
H_S=\nabla C_0-\nabla C_1 \tag{1}
$$
$H_I$: Altura de Impulson, liquido que la bomba impulsa, desde el eje hasta el tanque elevado.
$$
H_I=\nabla C_2-\nabla C_0 \tag{2}
$$
$H_g$: Altura geometrica, es la suma de la altura de succion e impulsion, es decir.
$$
H_g=H_I+H_S \tag{3}
$$
## Succion
El diametro de la tuberia debe ser mayor que la de impusion, para que las perdidas de carga sean minimas.
$$
D\uparrow \alpha \ h_f \downarrow
$$
## Impulsion
## Analisis de Carga Util
Si trazamos las cargas piezometricas en m.c.a, para que el fluido pueda llegar de la bomba al tanque elevado, entonces debe de vencer tanto la altura geometrica ($H_g$), como la sumatoria de la perdida de carga en las tuberias de succion e impulsion y los accesorios ($\Sigma(h_f+h_l)$) 
![[Pasted image 20260521143634.png]]
Entonces de la grafica se extrae que.
$$
H_{util}=H_g+\Sigma(h_f+h_l)_{S,I} \tag{4}
$$
Donde:
$\Sigma(h_f+h_l)_{S,I}$: Perdidas de carga mayores y menores para la tuberia de succion e impulsion, si son de diferente diametro, deberan de tener diferentes factores de friccion.

Entonces esta altura util debera ser entregada por la bomba, y la potencia de esta, finalmente la potencia de esta se calcula mediante.
$$
Pot=\gamma \cdot Q \cdot H_{util} \cdot \tag{5}
$$
Donde.
$\gamma$: Peso especifico, $\gamma=\rho \cdot g$
$Q$: Caulda en $m^3/s$

Como ya se sabe en la [[Ecuacion de Bernoulli]], queda un termino de Bomba, justamente es ese despeje, del cual se obtiene la ecuacion (4).
# Succion Positiva

En este caso, el reservorio ya no se encontraria abajo, sino arriba, aportando hacia la bomba, en este caso ya no ocurre el problema de cavitacion.
![[Pasted image 20260521160342.png]]
De la imagen se oberva que, la altura geometrica, ahora es la diferencia entre la altura de impulsion y la altura de succion, es decir.
$$
H_g=H_I-H_S \tag{6}
$$
## Analisis de Carga Util
Ahora el tanque elevado provee energia potencial a la bomba, por lo cual su altura util sera menor.
![[Pasted image 20260521162331.png]]
Tenemos por un lado una energia de succion, $E_{S}=H_S-h_{f1}$, y otra energia de impulsion $E_{I}=H_I+h_{f2}$, entonces, lo que debera darnos la bomba es, la diferencia entre la altura de impulsion, menos la altura de succion, ya que esta altura de succion en realidad esta aportando energia, es decir.
$$
\begin{align*}
H_{util} &=E_I-E_S \\
&=H_I+h_{f2}-(H_S-h_{f1}) \\
&=H_I+h_{f2}-H_S+h_{f1} \\
&=\underbrace{H_I-H_S}_{H_g}+\underbrace{h_{f2}+h_{f1}}_{\Sigma(h_f+h_l)}
\end{align*}
$$
Es decir, se tiene, que la altura util es igual a.
$$
H_{util} =H_g+\Sigma(h_f+h_l)_{S,I}
$$
La cual es la misma formula obtenida en (4), pareceria incorrecto, pero en este caso, altura geometrica es menor, por lo tanto la altura util tambien, y a su vez, la potencia.

Podriamos llegar a la misma ecuacion aplicando la [[Ecuacion de Bernoulli]], como se hizo anteriormente.
# Enunciado
Segun el diagrama, que potencia deberia de tener la bomba para elevar $139\ l/s$, si las tuberias son de hierro fundido nuevo, y el agua tiene una viscocidad cinematica de $1\cdot 10^{-6}\ m^2/s$.
![[Pasted image 20260521170605.png]]

## Datos
$Q=139\ l/s$
$\nu=1\cdot 10^{-6}\ m^2/s$
$L_1=300\ m, \ \phi_1=6\ inch$
$L_2=800\ m, \ \phi_2=8\ inch$
## Solucion
Se trata de un sistema de succion positiva, y ubicando el nivel de referencia a nivel del eje de la bomba, al aplicar la [[Ecuacion de Bernoulli]], entre las cotas de los tanques, se tiene.
$$
\begin{align*}
B =H_{util}&=Z_1-Z_2+\Sigma(h_f+h_l)_{1.2} \\
&=6-36+\Sigma(h_f+h_l)_{1,2} \\
&=30+\Sigma(h_f+h_l)_{1,2} \tag{E1.1}
\end{align*}
$$
Luego, no se consideran perdidas menores, y se tienen las perdidas de carga por longitud para el tramo 1.
$$
h_{f1}=f_1 \cdot \frac{L_1 \cdot v_1}{2 \cdot g \cdot D_1}
$$
Y para el tramo 2.
$$
h_{f2}=f_2 \cdot \frac{L_2 \cdot v_2}{2 \cdot g \cdot D_2}
$$
Entonces, introduciendo estas perdidas en (E.1.1) se tendra.
$$
H_{util}=30+f_1 \cdot \frac{L_1 \cdot v_1}{2 \cdot g}+f_2 \cdot \frac{L_2 \cdot v_2}{2 \cdot g \cdot D_2} \tag{E.1.2}
$$
Se determino mediante Moody, que $f_1=0.021$ y $f_2=0.022$.

Introduciendo todo se obtiene en (E.1.2) 
$$
H_{util}=315.27
$$
Finalmente utilizando la ecuacion (5), obtenemos
$$
Pot=429723.729\ W = 576.26\ HP
$$


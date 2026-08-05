# Entrainment 

Se habla del Entrainment, que es la mezcla de un fluido con otro, siendo estos de diferentes densidades.
Se ve mas aqui [Air Entrainment Template | FLOW-3D HYDRO Webinar](https://www.youtube.com/watch?v=ZvGgUXMKXCA)


## Agua-Aire
Donde se observa que el flujo turbulento al moverse absorbe aire, haciendolo entrar y combinandolo con el resto del flujo aguas abajo, (aireacion).
![[Pasted image 20260706180810.png|360]]
## Agua-Suelo
Al ser un canal de tierra, tambien el flujo puede erosionar sedimentos del fondo y llevarlos combinarlos mediante transporte por suspencion, rodamiento o saltacion cambiando la densidad del agua.
![[Pasted image 20260706181331.png|360]]
Entonces para el presente caso de estudio, se tomara que la ==densidad sera homogenea==, es decir no habra flujo multifasico, solo el transporte y comportamiento transitorio del agua.
# Demostracion
Para el caso de distintas secciones transversales
![[Pasted image 20260706182941.png|610]]
Se observa que se tiene el tirante $h$, una altura hasta el nivel de referencia $Z$, y una altura total desde la superficie del agua hasta el nivel de referencia igual a.
$$
H=h+z \tag{1}
$$
Derivando la ecuacion (1), A lo largo de una linea de corriente, entonces sera con respecto a $s$, ==no se por que se hizo total la altura H y luego con parciales el h y Z, sera por la regla de la cadena?== 
$$
\frac{dH}{ds}=\frac{\partial h}{\partial  s}+\frac{\partial z}{\partial s}  \tag{2}
$$
La variacion de la altura $Z$ con resspecto a $s$, tiene que ver con la pendiente geometrica $S_0$, ademas es negativa, ==se dice que por que es final menos inicial, y la derivada saldria negativa, pero la pendiente siempre es negativa, entonces se hace para poder denotar la pendiente como positiva, el profesor menciono que era por un tema de convencion, y creo que tiene sentido por que nunca vi una pendiente negativa, por lo menos e hidraulica.==
$$
-\frac{\partial z}{\partial s}=S_0\tag{3}
$$
## Conservacion de la masa
En el volumen de control se cumple.
![[Pasted image 20260706193911.png|473]]
### Caudal masico que entra y sale
En un tramo diferencial $ds$, entra un caudal Q, pero como queremos trabajar con el [[Caudal Masico]], entonces hacemos.
$$
\dot m=\rho \cdot \frac{dV}{dt}=\rho \cdot Q \tag{4}
$$
Entonces
Entra: $\dot m_{in}=\rho \cdot Q$
Sale: $\dot m_{out}=\rho \cdot Q+d(\rho \cdot Q)$

Luego en la grafica.
![[Pasted image 20260707165539.png|493]]
El caudal de salida varia con respecto al tiempo y al espacio, en este caso el espacio seria $s+ds$ 
Por lo que el caudal seria una funcion de ambos, es decir
$$
Q=Q(s+ds,t)
$$
==Por una razon que no se por que, la diferencial $d(\rho \cdot Q)$ se expande con una serie de Taylor de primer orden, pero tiene que ver con lo puesto anteriormente==

Por lo que el flujo masico saliente seria.
$$
\dot m_{out}=\rho \cdot Q+\rho \cdot \frac{\partial Q}{\partial s}ds \tag{5}
$$
### Variacion de la masa almacenada
Si usamos la eq (4), tendriamos la variacion de la masa dentro del volumen de control con respecto al tiempo, ello se puede expandir para el volumen de control en el tramo $ds$ y para un area $A$.
$$
\dot m_{var}=\rho \cdot \frac{dV}{dt}=\rho \cdot \frac{d(A \cdot ds)}{dt}
$$
El area es una funcion del espacio y tiempo.
$$
A=A(s,t)
$$
Pero solo varia con respecto al tiempo, ya que el tramo se mantiene igual, por lo que quedaria.
$$
\dot m_{var}=\rho \cdot \frac{\partial A}{\partial t} \cdot ds \tag{6}
$$
### Balance
Haciendo uso de las eq's (5) y (6), se tiene.
![[Pasted image 20260707173257.png|566]]
$$
\dot m_{in}-\dot m_{out}=\dot m_{var}
$$
Operando y simplificando, se tiene.
$$
\begin{align*}
(\rho \cdot Q)-(\rho \cdot Q+\rho \cdot \frac{\partial Q}{\partial s}ds)&=\rho \cdot \frac{\partial A}{\partial t} \cdot ds \\ \\

\cancel{\rho \cdot Q}-\cancel{\rho \cdot Q}-\cancel{\rho} \cdot \frac{\partial Q}{\partial s}ds&=\cancel{\rho} \cdot \frac{\partial A}{\partial t}ds \\ \\

-\frac{\partial Q}{\partial s}\cancel{ds}&=\frac{\partial A}{\partial t}\cancel{ds} \\ \\

\frac{\partial A}{\partial t}+\frac{\partial Q}{\partial s}&=0 \tag{7}

\end{align*}
$$
## Conservacion del momento
Parecida al teorema de transporte de Reynolds, la idea aqui aqui es hacer el balance
$$
\Sigma F=\dot p_{out}-\dot p_{in}+\text{Acumulacion}
$$
Por lo que debermos de hallar las fuerzas externas que actuan sobre el volumen de control, las cuales son 
- Fuerza de presion
- Fuerza de friccion 
- Fuerza gravitacional
### Flujo de momentum
[Mass Flow Rate | Glenn Research Center | NASA](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/mass-flow-rate/)
La cantidad de movimiento se define como el producto de la masa por la velocidad
$$
p=m \cdot v\ [kg \cdot \frac{m}{s}]
$$
Pero nosotros no analizamos la cantidad de movimiento de una solo particula, sino el **flujo de la cantidad de movimiento** que atravieza el volumen de control, entonces seria el producto del [[Caudal Masico]] por la velocidad.
$$
\dot p=\dot m \cdot v=\rho \cdot Q \cdot v\ [kg \cdot \frac{m}{s^2}=N] \tag{8}
$$
Analizado en el mismo canal, añadiremos una inclinacion $\alpha$ que representara la pendiente
![[Pasted image 20260708000854.png|654]]
### Balance del flujo de momentum
$\dot p_{in}=\rho \cdot Q \cdot v$, para un caudal $Q=Q(s,t)$, y una velocidad $v=v(s,t)$

$\dot p_{out}=\rho \cdot Q \cdot v+d(\rho \cdot Q \cdot v)$, para un caudal $Q=Q(s+ds,t)$, y una velocidad $v=v(s+ds,t)$ por lo que expandiremos Taylor de primer orden.
$$
d(\rho \cdot Q(s+ds,t) \cdot v(s+ds,t))=\rho \cdot \frac{\partial (Q \cdot v)}{\partial s}ds
$$
Luego en la cantida de salida.
$$
\dot p_{out}=\rho \cdot Q \cdot v+\rho \cdot \frac{\partial (Q \cdot v)}{\partial s}ds
$$
Luego aplicando la operacion $\dot p_{out}-\dot p_{in}$ para hallar el flujo neto de cantidad de movimiento.
$$
\begin{align*}
\dot p_{out}-\dot p_{in}&=\rho \cdot Q \cdot v+\rho \cdot \frac{\partial (Q \cdot v)}{\partial s}ds+(-\rho \cdot Q \cdot v) \\ \\
\Delta \dot p&=\rho \cdot \frac{\partial (Q \cdot v)}{\partial s}ds \tag{9}
\end{align*}
$$
### Fuerza de Presion
$P_{in}=\rho \cdot g \cdot h$, donde la altura $h=h(s,t)$
$P_{out}=\rho \cdot g \cdot h+d(\rho \cdot g \cdot h)$, donde la altura $h=h(s+ds,t)$, tambien expandiremos una serie de Taylor de primer orden.
$$
d(\rho \cdot g \cdot h(s+ds,t))=\rho \cdot g \cdot \frac{\partial h}{\partial s}ds
$$
Luego en la presion de salida.
$$
P_{out}=\rho \cdot g \cdot h+\rho \cdot g \cdot \frac{\partial h}{\partial s}ds
$$
Teniendo la resultante
$$
\begin{align*}
F_P&=\rho \cdot g \cdot h+\rho \cdot g \cdot h+\rho \cdot g \cdot \frac{\partial h}{\partial s}ds \\ \\

&=2\cdot \rho \cdot g \cdot h+\rho \cdot g \cdot \frac{\partial h}{\partial s}ds \tag{10}
\end{align*}
$$
### Peso
Ejercida por la fuerza gravitacional, $F_g$
![[Pasted image 20260708011927.png|627]]
Segun la fuerza descompuesta, se tiene el peso por el seno del angulo que forma.
$$
\begin{align*}
W \cdot \sin{\alpha}&=m \cdot g \cdot \sin{\alpha} \\
&= \rho \cdot V \cdot g \cdot \sin{\alpha} \\
&= \rho \cdot A \cdot ds \cdot g \cdot \sin{\alpha}
\end{align*}
$$
Graficamente el seno
$$
\sin{\alpha}=\frac{dz}{ds}
$$
Esta fraccion no es mas que la pendiente geometrica, hallada en (3), por lo que es negativa para que la pendiente hidarulica salga positiva
$$
\sin{\alpha}=-\frac{dz}{ds}=S_f
$$
Quedando
$$
\begin{align*}
F_g&=-\rho \cdot A \cdot ds \cdot g \cdot \frac{dz}{ds} \\
&=\rho \cdot A \cdot g \cdot ds \cdot S_f \tag{11}
\end{align*}
$$
### Friccion
Como fue detallado en [[Tubo en U con friccion#Fuerza de Friccion| Tubo en U con friccion]] la fuerza de friccion es el producto entre el esfuerzo cortante por el area.
$$
F_F=\tau_0 \cdot A \tag{12}
$$
Y esta fuerza actua sobre las **paredes**, por lo que el area no es mas que el area del perimetro mojado por la longitud, que en este caso es el tramo del fluido diferencial $ds$, es decir $A=P_m \cdot ds$, entonces. en (12)
$$
F_F=\tau_0 \cdot P_m \cdot ds \tag{13}
$$
==Observemos entonces que para un flujo uniforme, el agua no acelera, por lo que las fuerzas gravitacionales y de friccion se cancelan, no se si esta explicacion es correcta==
![[Pasted image 20260708115018.png|460]]
Entonces, igualando (11) y (13), se tiene.
$$
\begin{align*}
F_g&=F_F \\
\rho \cdot A \cdot g \cdot ds \cdot S_f &= \tau_0 \cdot P_m \cdot ds
\end{align*}
$$
Despejando la pendiente hidarulica.
$$
S_f=\frac{\tau_0 \cdot P_m}{\rho \cdot g \cdot A} \tag{14}
$$
==Un momento, y que pasa con $S_0$??, creo que confundi pendiente hidraulica y pendiente geometrica==

### Balance
Efectuando el balance final para todas las fuerzas involucradas, se tiene.
$$
\begin{align*}
F_p+F_P+ =0 \\ \\
\rho \cdot \frac{\partial (Q \cdot v)}{\partial s}ds+2\cdot \rho \cdot g \cdot h+\rho \cdot g \cdot \frac{\partial h}{\partial s}ds=0
\end{align*}
$$




# Saint-Venant
Tiene algunas suposiciones, y arrastran las ecuaciones anteriores.
## Suposiciones
Flujo uniforme
Poca pendiente

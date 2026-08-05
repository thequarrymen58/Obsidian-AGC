Similar a el caso de [[Tubo en U sin friccion]], se parte del caso en la imagen, en donde mas adelante el cambio mas significativo es añadir la fuerza de friccion en la ecuacion (1), y como se sabe la solucion de una ecuacion es solo un conjunto de soluciones, por lo tanto al añadir un termino entonces la solucion ahora debera de tener una solucion mas.
![[Pasted image 20260331103538.png|225]]
Luego de ello se tiene la [[Ecuacion del Movimiento de Euler#Aceleracion|Ecuacion del movimiento de Euler]], para un fluido incompresible, es decir la densidad es constante $\rho =cte$.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} = 0\tag{1}
$$
# Forma Laminar
Si analizamos la imagen en detenimiento, se tiene, el analisis de un elemento fluido de forma diferencial, en forma de cilindro (puesto que se aplicara en tuberias) con diametro $D$ y area $A$.
![[Pasted image 20260422110136.png|600]]
Debido a que se añadira una fuerza de friccion a la [[Ecuacion del Movimiento de Euler]], esta debe de ser dimensionalmente correcta, si analizamos notaremos que la unidad predominante es $[m/s^2]$ y tiene sentido puesto que el nombre de la ecuacion es, la ecuacion de movimiento.

Se tiene entonces la fuerza de friccion ($F_{Friccion}$), segun la ecuacion.
$$
F_{Friccion}=\tau_0 \times \pi \times D \times \partial s \tag{2}
$$
Donde:
$\tau_0$: Es el esfuerzo cortante entre capas de fluido y pared-fluido.
$D$: Diametro del elemento fluido.
$\partial s$: Parte diferencial de la linea de corriente.

De la [[Segunda Ley de Newton]], se tiene que el despeje de la aceleracion, y justamente es esta aceleracion la cual deberemos de añadir a la ecuacion (1)
$$
\begin{align*}
a &=\frac{F_{Friccion}}{m} \\
&= \frac{F_{Friccion}}{\rho \times V} \tag{3}
\end{align*}
$$
Donde el volumen del elemento fluido viene dado por.
$$
V=A \times\partial s
$$
Pero $A=\frac{\pi \times D^2}{4}$, entonces.
$$
V=\frac{\pi \times D^2 \times \partial s}{4} \tag{4}
$$
Reemplazando (4) y (2) en (3), se tiene.
$$
a=\frac{4 \times\tau_0 \times \pi \times D \times \partial s }{\rho \times \pi \times D^2 \times \partial s}
$$
Depejando y eliminando terminos.
$$
a=\frac{4\times \tau_0 }{\rho \times D} \tag{5}
$$
Añadiendo el termino (5) en (1), se tiene.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{4\times \tau_0 }{\rho \times D}= 0\tag{6}
$$
Lo que nos dice la ecuacion (6) es que para tanto para el regimen transitorio como el permanente, para una misma velocidad la fuerza de friccion sera la misma.

Segun [[Hagen-Poiseuille]], para un flujo laminar en una tuberia circular se tiene la igualdad para el esfuerzo cortante en una pared.
$$
\tau_0=\frac{8\times \mu\times v}{D} \tag{7}
$$
Reemplazando (7) en (6)
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{32 \times \mu\times v }{\rho \times D^2}= 0\tag{8}
$$
Lueho haciendo $(8)\times \partial s$, e integrando sobre toda la region fluida $s$ de 1 a 2, la cual es igual a la longitud del fluido estirada horizontalmente $L$.
$$
\frac{\partial v}{\partial t}L+\frac{v_2^2-v_1^2}{2g}+g(z_2-z_1)+(P_2-P_1)+\frac{32 \times \mu\times v }{\rho \times D^2}L= 0\tag{9}
$$
- La velocidad de bajada es igual a la subida, $v_2^2=v_1^2$.
- La presion es atmosferica en ambos casos $P_2=P_1=P_{atm}$.
- La altura que sube y baja, es $z$ en ambos casos, similar al analisis hecho en [[Tubo en U sin friccion]], por ello, $z_1-z_2=2z$.

Luego de aplicar estos factos, nos queda.
$$
\frac{\partial v}{\partial t}L+2gz+\frac{32 \times \mu\times v }{\rho \times D^2}L= 0\tag{10}
$$
Multiplicando por (10) por $1/L$, m.a.m.
$$
\frac{\partial v}{\partial t}+\frac{2gz}{L}+\frac{32 \times \mu\times v }{\rho \times D^2}= 0\tag{11}
$$
Asi mismo, sabemos que la velocidad es igual a la derivada de la posicion con respecto al tiempo, pero en nuestro caso, solo se mueve en el eje z, por lo que.
$$
v=\frac{\partial z}{\partial t} \tag{12}
$$
Reemplazando (12) en (11), y recordando que $\nu=\mu/\rho$.
$$
\frac{\partial^2 z}{\partial t^2}+\frac{2gz}{L}+\frac{32\times \nu }{ D^2} \frac{\partial z}{\partial t}= 0\tag{13}
$$
Luego nos queda un sistema de ecuaciones con (12) y (13).
$$
\begin{cases}
\frac{\partial^2 z}{\partial t^2}+\frac{2gz}{L}+\frac{32 \times \nu}{D^2}\frac{\partial z}{\partial t}= 0 \\
v =\frac{\partial z}{\partial t}
\end{cases} \tag{15}
$$
El cual se podria resolver usando el metodo de [[Metodo Predictor - Corrector]] o cualquier otro metodo para resolver [[Ecuaciones Diferenciales#Ordinarias|EDOS]], ==que tampoco se.==

Pero en el libro de Streeter 12, english, 584, se da la comprobacion, de lo que la ecuacion (13), es una EDO de segundo orden y tiene una solucion de la forma.
$$
z=C_1e^{at}+C_2e^{bt} \tag{15.1}
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
Luego reemplazando m y n en (15.1), se tiene.
$$
z=C_1e^{(-m+n)t}+C_2e^{(-m-n)t} \tag{15.1}
$$
De la solucion de esa ecuacion, se llegan a dos casos, el primero de ellos es cuando
$$
\frac{16\cdot\nu}{D^2}>\sqrt{\frac{2g}{L}}
$$
De donde se tiene su solucion asociada, la cual nos da el maximo desplazamiento para Z, ==esta ecuacion se usa cuando se empieza desde la posicion de equilibrio, eso creo.==
$$
Z=\frac{V_0}{\sqrt{m^2-n^2}}\left(\frac{m-n}{m+n}\right)^{m/2n}=V_0\sqrt{\frac{L}{2g}}\left(\frac{m-n}{m+n}\right)^{m/2n}
$$
Donde
$V_0$: Es la velocidad cuando $t=0$

Mientras que el segundo es caso es.
$$
\frac{16\cdot\nu}{D^2}<\sqrt{\frac{2g}{L}}
$$
El cual tambien tiene su solucion asociada
$$
Z=\frac{V_0}{\sqrt{n'^2+m^2}}\exp{\left(-\frac{m}{n'}\arctan{\frac{n'}{m}}\right)}=V_0\sqrt{\frac{L}{2g}}\exp{\left(-\frac{m}{n'}\arctan{\frac{n'}{m}}\right)}
$$
Donde
$\exp(algo)=e^{(algo)}$
$n'$: Esta fraccion saldra imaginaria, por lo que nos deberemos de quedar con la parte real, e.g, $\sqrt{-6.387}=i\cdot2.527$, por lo que $n'=2.527$.
# Forma Turbulenta (1 borrar)
Como se vio en la parte de [[6. Turbulencia y Capa Limite#RANS (reynolds average ns simulation)|Flujo Turbulento]], la velocida se desdobla en terminos de velocidad media y velocidad fluctuate.
$$
u=\overline{u}_i+u'_i \tag{16}
$$
Luego, basado en experimentos empiricos se llego a la conclusion de que el esfuerzo cortante es igual a un parametro ($f$), que representa la friccion, multiplicado por el cuadrado de la velocidad, es decir.
$$
\tau_0=f \times v^2
$$
==AQUI LAS UNIDADES DE TAU SON M^2/S^2, PERO SUS UNIDADES SON DIFERENTES, FALTARIA LA DENSIDAD ABAJO DE ESTE.==

Pero como la velocidad, vectorialmente, puede tomar valores negativos entonces se divide en el termino de velocidad multiplicada por el valor absoluto de esta, quedando.
$$
\tau_0=f \times v \times |v| \tag{17}
$$
Introduciendo (17) en (6), se tiene.
$$
\begin{align*}
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{4\times \tau_0 }{\rho \times D} &= 0 \\
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{4\times f\times v\times |v| }{\rho \times D} &= 0

\tag{18}
\end{align*}
$$
Multiplicamos (18), por $\partial s$, e integramos, recordemos que la velocida sera la misma al igual que la presion.
$$
2\cdot g\cdot z+\frac{\partial v}{\partial t}L+\frac{4\cdot f\cdot v\cdot |v| }{\rho \cdot D}L=0 \tag{19}
$$
Dividimos (19) por $L$
$$
2\cdot g\cdot z+\frac{\partial v}{\partial t}\frac{1}{L}+\frac{4\cdot f\cdot v\cdot |v| }{\rho \cdot D}=0 \tag{19}
$$
# Forma Turbulenta (Correcion)
Como se vio en la parte de [[6. Turbulencia y Capa Limite#RANS (reynolds average ns simulation)|Flujo Turbulento]], la velocida se desdobla en terminos de velocidad media y velocidad fluctuate.
$$
u=\overline{u}_i+u'_i \tag{16}
$$
## Balance de fuerzas
Conciste en igualar la caida de presion con la ecuacion de [[Ecuacion Darcy-Weisbach]].
### Fuerza de Presion
Se sabe que la presion es igual a,
$$
\Delta P=\frac{F_{Presion}}{A} \tag{17}
$$
Donde $\Delta P$ es la diferencia entre presion mayor y menor, lo que hace que el flujo se mueva, si reemplazamos el area y despejamos la fuerza, se tiene.
$$
F_{Presion}=\frac{\Delta P\cdot 4}{\pi D^2} \tag{18}
$$
### Fuerza de Friccion
Recordemos que el [[Esfuerzo Cortante]], es como otra presion.
$$
\tau_0=\frac{F_{Friccion}}{A} \tag{19}
$$
El area de influencia es en el lateral de la tuberia, es decir.
![[Pasted image 20260503135906.png|425]]
Por ello el Area sera igual a la base (Longitud) por la altura (perimetro), perimetro de una circunferencia, $Perimetro=2\pi R=\pi D$.
Reemplazando en (19) y despejando la fuerza.
$$
F_{Friccion}=\tau_0 \cdot (\pi D L) \tag{20}
$$
Igualando (18) y (20), y despejando la caida de presion se tiene.
$$
\Delta P = \frac{4 \tau_0 L}{D} \tag{21}
$$
### [[Ecuacion Darcy-Weisbach]]
$$
\Delta P= f\cdot \rho \left( \frac{L}{D} \right) \left( \frac{v^2}{2} \right) \tag{22}
$$
### Final
Igualando (21) y (22), y despejando $\tau_0$.
$$
\tau_0 = \frac{f \cdot \rho \cdot v^2}{8}
$$
Pero como la velocidad, vectorialmente, puede tomar valores negativos entonces se divide en el termino de velocidad multiplicada por el valor absoluto de esta, quedando.
$$
\tau_0 = \frac{f \cdot \rho \cdot v \cdot |v|}{8} \tag{23}
$$

Introduciendo (23) en (6), se tiene.
$$
\begin{align*}
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{4\times \tau_0 }{\rho \times D} &= 0 \tag{6} \\

\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{\cancel{4} }{\cancel{\rho} \cdot D}\cdot \frac{f \cdot \cancel{\rho} \cdot v \cdot |v|}{\cancel{8}}  &=0 \\

\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{f \cdot v \cdot |v|}{2\cdot D} &=0 \tag{24}

\end{align*}
$$
Integrando (24), se tiene.
$$
2\cdot g \cdot z + \frac{\partial v}{\partial t}L + \frac{f \cdot v \cdot |v|}{2\cdot D}L=0 \tag{25}
$$
Diviendo (25) por $L$
$$
\frac{\partial v}{\partial t} +\frac{2\cdot g \cdot z}{L} +  \frac{f \cdot v \cdot |v|}{2\cdot D}=0 \tag{26}
$$
Como ya se vio en (12), podemos hacer un cambio de variable.
$$
\frac{\partial^2 z}{\partial t^2} +\frac{2\cdot g \cdot z}{L} +  \frac{f \cdot \frac{\partial z}{\partial t} \cdot |\frac{\partial z}{\partial t}|}{2\cdot D}=0 \tag{27}
$$
Quedando un sistema de ecuaciones entre (12) y (27)
$$
\begin{cases}
\frac{\partial^2 z}{\partial t^2} +\frac{2\cdot g \cdot z}{L} +  \frac{f \cdot \frac{\partial z}{\partial t} \cdot |\frac{\partial z}{\partial t}|}{2\cdot D}=0 \\
v =\frac{\partial z}{\partial t}
\end{cases} \tag{28}
$$
## Donde queda la velocidad turbulenta
Este enfoque matematico nace mucho despues de los experimentos empiricos, pero ocurria un problema de cierre, tensor de reynolds, el cual se vio en [[6. Turbulencia y Capa Limite#RANS (reynolds average ns simulation)|RANS]].
Ese problema de cierre se soluciono con los enfoques empiricos, a nivel global lo que nos interesa es el factor de friccion.
A nivel local, se usa la hipotesis de Boussinesq.

Por lo tanto la ecuacion (26) ya integra la velocidad media, mientras que la fluctuacion ya fue eliminada.

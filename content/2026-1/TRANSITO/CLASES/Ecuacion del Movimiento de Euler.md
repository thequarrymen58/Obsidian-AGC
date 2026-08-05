Se parte desde la [[Segunda Ley de Newton]], al eliminar fuerzas compresibles, viscosas y turbulentas. 

Se tiene un elemento diferencial de fluido, en forma cilindrica.
![[Pasted image 20260331115529.png|232]]
## Volumen
Se tiene el volumen $ds$
## Area
Se tiene un area $dA$
## Presion
Se tiene una presion de forma normal hacia las caras, por lo cual es en la primera es $pdA$, y en la posterior seria $(p+\frac{\partial p}{\partial s}ds)dA$.
Esto sale gracias a la [[Series de Taylor]], o expansion de Taylor de primer orden. 
## Gravedad
Como el cuerpo se encuentra rotado, la fuerza de gravedad actuara sobre este volumen, con un angulo $\theta$.
Entonces, como el peso es masa por gravedad.
$$
W=mg\tag{1}
$$
Y sabemos que la masa es igual a la densidad por el volumen.
$$
m=\rho\times V
$$
Mientras que el volumen seria igual al area por la altura, es decir.
$$
V=dA\times ds
$$
Entonces la masa se tiene 
$$
m=\rho\times dA\times ds
$$
Finalmente reemplazando en la ecuacion (1).
$$
W=g\times\rho\times dA\times ds\tag{2}
$$
## Derivacion
Procedemos a aplicar la [[Segunda Ley de Newton]] para la sumatoria de fuerzas, teniendo.
$$
F=ma\tag{3}
$$
$$
pdA-(p+\frac{\partial p}{\partial s}ds)dA-g\rho dAds \cos(\theta)=\rho dA ds\times a\tag{4}
$$
Desdoblando la ecuacion (4), se iran varios terminos, veamos.
$$
\cancel{pdA-pdA}-\frac{\partial p}{\partial s}dsdA-g\rho dAds \cos(\theta)=\rho dA ds\times a
$$
$$
-\frac{\partial p}{\partial s}dsdA-g\rho dAds \cos(\theta)=\rho dA ds\times a\tag{5}
$$
Dividiendo la ecuacion (5) m.a.m por el termino $\rho dA ds$, se tendra.
$$
-\frac{1}{\rho}\frac{\partial p}{\partial s}-g\cos(\theta)= a\tag{6}
$$
Si hacemos un analisis geometrico dentro del cuerpo.
![[Pasted image 20260331120213.png|300]]
Notaremos que el termino del coseno se puede dejar en funcion de ds y dz, pero como z varia de otras variables tambien como la misma posicion o el tiempo, sera parcial.
$$
\cos(\theta)=\frac{\partial z}{\partial s}\tag{7}
$$
Entonces reemplazando (7) en (6), se tiene.
$$
-\frac{1}{\rho}\frac{\partial p}{\partial s}-g\frac{\partial z}{\partial s}= a\tag{8}
$$
## Aceleracion
Para finalizar veamos de donde proviene el termino de aceleracion, se tiene que la velocidad depende de la posicion $s$ y del tiempo $t$, pero a su vez la posicion tambien depende del tiempo, es decir.

![[Pasted image 20260331121005.png]]
$$
v=f(s,t) \ \land \ s=f(t)
$$
Asi mismo, se tiene que la velocidad es la derivada de la posicion con respecto al tiempo.
$$
v=\frac{ds}{dt}\tag{9}
$$
Pero la aceleracion es la derivada de la velocidad con respecto al tiempo, es decir.
$$
a=\frac{dv}{dt}\tag{10}
$$
Entonces reemplazando (10) en (9) y descomponiendo en derivadas parciales , se tiene que.
$$
a=\frac{\partial v}{\partial s} \frac{\partial s}{\partial t}+\frac{\partial v}{\partial t}\tag{11} 
$$
Pero si vemos dentro de la ecuacion (11), el termino en ecuacion (9) de velocidad puede ser reemplazado, quedando.
$$
a=\frac{\partial v}{\partial s} v+\frac{\partial v}{\partial t}\tag{12} 
$$
Finalmente reemplazando (12) en (8), se tiene.
$$
-\frac{1}{\rho}\frac{\partial p}{\partial s}-g\frac{\partial z}{\partial s}= \frac{\partial v}{\partial s} v+\frac{\partial v}{\partial t}\tag{13}
$$
Pasando los terminos al otro lado se tiene la ecuacion final de Euler.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s}+g\frac{\partial z}{\partial s}+v\frac{\partial v}{\partial s}+\frac{\partial v}{\partial t}=0\tag{14}
$$
Donde:

$\frac{1}{\rho}\frac{\partial p}{\partial s}$: Fuerza de presion
$g\frac{\partial z}{\partial s}$: Fuerza de gravedad o masica
$v\frac{\partial v}{\partial s}+\frac{\partial v}{\partial t}$: Fuerzas inerciales
# Analisis de las fuerzas inerciales
Recordemos que segun la derivacion de la aceleracion, tenemos por un lado una aceleracion total, que se trata de un enfoque [[Enfoques Lagrangiano y Euleriano#Lagrangiano (material)|Lagrangiano]], pero esta se desdobla en enfoques [[Enfoques Lagrangiano y Euleriano#Euleriano (espacial)|Eulerianos]], es decir.
- Un termino de aceleracion local, que depende del tiempo.
- Un termino de aceleracion advectiva, que depende del espacio.
$$
\underbrace{\frac{dv}{dt}}_{\text{Lagrangiano (lo que siente la particula)}} = \underbrace{\frac{\partial v}{\partial t}}_{\text{Local (Euleriano)}} + \underbrace{v \frac{\partial v}{\partial s}}_{\text{Advectivo (Euleriano)}}
$$

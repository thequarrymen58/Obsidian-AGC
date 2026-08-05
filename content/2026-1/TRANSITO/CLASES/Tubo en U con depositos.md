Al igual que el caso de [[Tubo en U con friccion]], pero esta vez se tienen depostivos con diferentes areas.
![[Pasted image 20260503190732.png|232]]
# Derivacion
Partiremos desde la ecuacion (24) desde la derivacion de [[Tubo en U con friccion#Forma Turbulenta (Correcion)|Tuberia en U con friccion]], es decir.
$$
\frac{1}{\rho}\frac{\partial p}{\partial s} + g\frac{\partial z}{\partial s} + v\frac{\partial v}{\partial s} + \frac{\partial v}{\partial t} + \frac{f \cdot v \cdot |v|}{2\cdot D} =0 \tag{1}
$$
Multiplicando (1) por $\partial s$, e integrando con limites de 2 a 1, se tiene.
$$
\begin{align*}
\frac{\partial p}{\rho} + g\cdot \partial z + v\cdot \partial v + \frac{\partial v}{\partial t}\cdot \partial s + \frac{f \cdot v \cdot |v|}{2\cdot D}\cdot \partial s &=0 \\
\int_{2}^{1}\frac{\partial p}{\rho}+\int_{2}^{1}g\cdot \partial z +\int_{2}^{1}v\cdot \partial v  +\frac{\partial v}{\partial t}\int_{2}^{1} \partial s +\frac{f \cdot v \cdot |v|}{2\cdot D}\int_{2}^{1} \partial s &=0
\end{align*}
$$
Recordemos de integraciones anteriores que entre 1 y 2, las presiones son iguales, al igual que las velocidades, por lo que quedaria.
$$
\begin{align*}
\int_{2}^{1}g\cdot \partial z +\frac{\partial v}{\partial t}\int_{2}^{1} \partial s +\frac{f \cdot v \cdot |v|}{2\cdot D}\int_{2}^{1} \partial s &=0 \\

g\cdot (z_1-z_2)+\frac{\partial v}{\partial t}L+\frac{f \cdot v \cdot |v|}{2\cdot D}L &=0
\end{align*}
$$
Reemplazaremos $z_1$ y $z_2$, si notamos la imagen, vectorialmente, $z_2=-z_2$, y $z_1=z_1$, por lo que quedaria como.

$$
\begin{align*}
g\cdot (z_1+z_2)+\frac{\partial v}{\partial t}L+\frac{f \cdot v \cdot |v|}{2\cdot D}L &=0 \tag{2}
\end{align*}
$$
## Perdidas menores
Hasta ahora solo se esta tomando en cuenta las perdidas mayores o por longitud.
$$
\text{Perdidas Mayores}=\frac{f \cdot v \cdot |v|}{2\cdot D}L
$$
Por ello, a la ecuacion (2), se añadira una perdida menor o por accesorio.
Dentro de esta perdida podria entrar la perdida por contraccion justo en las salidas de los depositos, de igual manera se coloca como sumatoria, de modo que se cuantifiquen todas esas perdidas.
$$
\text{Perdidas Menores} = \sum K \frac{v \cdot |v|}{2}
$$
Si lo añadimos a la ecuacion (2), quedaria como.
$$
\cdots+ \frac{f \cdot v \cdot |v|}{2\cdot D}L +\sum K \frac{v \cdot |v|}{2}=0 \tag{2.1}
$$
Factorizando
$$
\cdots+\frac{f \cdot v \cdot |v|}{2\cdot D} \left[ L + \frac{(\sum K) \cdot D}{f} \right]=0 \tag{2.2}
$$
Si hacemos
$$
\frac{(\sum K) \cdot D}{f}=L_k
$$
En (2.2) quedaria.
$$
\cdots+\frac{f \cdot v \cdot |v|}{2\cdot D} \left[ L + L_k \right]=0 \tag{2.3}
$$
## Longitud Equivalente
Simplificamos esta suma de longitudes en (2.3), a una denominada como Longitud Equivalente
$$
L_e=L+L_k
$$
Esta longitud equivalente lo que hace es emular las perdidas por accesorios como si fuese una longitud adicional de tuberia.

Entonces la ecuacion (2), estaria quedando como.
$$
\begin{align*}
g\cdot (z_1+z_2)+\frac{\partial v}{\partial t}L+\frac{f \cdot v \cdot |v|}{2\cdot D}L_e &=0 \tag{3}
\end{align*}
$$
## Analisis de Depositos
Se sabe que el caudal debe de ser el mismo para ambos depositos, por lo que se cumple
$$
A_t\cdot z=A_1\cdot z_1=A_2\cdot z_2
$$
El area es conocida para 1 y 2, mientras que $z_1$ y $z_2$ no. 
Por lo que el termino general $z$, nos dice donde se encuentra el fluido en cualquier momento, si lo hallamos podriamos hallar $z_1$ y $z_2$, por lo que dejaremos estos dos en funcion del termino general $z$.
$$
\begin{align*}
z_1 &=\frac{A_t}{A_1}z \\
z_2 &=\frac{A_t}{A_2}z
\end{align*} \tag{4}$$
Reemplazando (4) en (3).
$$
\begin{align*}
g\cdot A_t(\frac{1}{A_1}+\frac{1}{A_2})z+\frac{\partial v}{\partial t}L+\frac{f \cdot v \cdot |v|}{2\cdot D}L_e &=0 \tag{5}
\end{align*}
$$
Pero recordemos que 
$$
v=\frac{\partial z}{\partial t} \tag{6}
$$
Entonces reemplazando (6) en (5), para hacer un cambio de variable.
$$
\begin{align*}
\frac{\partial^2 z}{\partial t^2}L+g\cdot A_t(\frac{1}{A_1}+\frac{1}{A_2})z+\frac{f \cdot \frac{\partial z}{\partial t} \cdot |\frac{\partial z}{\partial t}|}{2\cdot D}L_e &=0 \tag{7}
\end{align*}
$$
## Final
Diviendo (7) por $L$, se tiene.
$$
\begin{align*}
\frac{\partial^2 z}{\partial t^2}+g\cdot \frac{A_t}{L}(\frac{1}{A_1}+\frac{1}{A_2})z+\frac{f \cdot \frac{\partial z}{\partial t} \cdot |\frac{\partial z}{\partial t}|}{2\cdot D}\cdot\frac{L_e}{L}=0  \tag{8}
\end{align*}
$$
De donde nuevamente quedaria un sistema de [[Ecuaciones Diferenciales#Ordinarias|EDO'S]] de segundo orden.
$$
\begin{cases}
\frac{\partial^2 z}{\partial t^2}+g\cdot \frac{A_t}{L}(\frac{1}{A_1}+\frac{1}{A_2})z+\frac{f \cdot \frac{\partial z}{\partial t} \cdot |\frac{\partial z}{\partial t}|}{2\cdot D}\cdot\frac{L_e}{L}=0 \\
v=\frac{\partial z}{\partial t} 
\end{cases} \tag{9}$$

# TL:DR
Relaciona [[Enfoques Lagrangiano y Euleriano]], es decir el teorema de transporte sirve como un puente para pasar entre ambos enfoques.
# Derivacion
Se parte de un dominio material $\Omega$ que contiene una masa constante de particulas, es decir partimos puramente desde un enfoque [[Enfoques Lagrangiano y Euleriano#Lagrangiano (material)|langrangiano o material]].
![[Pasted image 20260406180150.png|142]]
Tambien tenemos una [[Propiedad Extensiva e Intensiva#Extensiva|Propiedad Extensiva]] ($F$), la cual sera igual a la integral volumetrica de una [[Propiedad Extensiva e Intensiva#Intensiva|Propiedad Intensiva]] ($f$) que depende del espacio ($x_i$) y del tiempo ($t$), evaluada en el dominio $\Omega$.

Es decir
$$
F(t)=\int_{\Omega} f(x_i,t)\ d\Omega\tag{1}
$$
Pero nosotros queremos saber como varia esa propiedad extensiva a lo largo del tiempo, es decir queremos la tasa de cambio temporal, por lo que derivaremos (1) m.a.m con respecto al tiempo.
$$
\frac{dF(t)}{dt}=\frac{d}{dt}\left(\int_{\Omega} f(x_i,t)\ d\Omega \right) \tag{2}
$$
Esta derivada no puede entrar en la integral, puesto que al variar la posicion tambien varian los limites de la integral, ya que el dominio varia con el tiempo $\Omega(t)$.

Pero al variar la forma del dominio en el tiempo hace que sus coordenadas tambien cambien.
Como se aprecia en la imagen, en el instante $t>0$, la forma y posicion del cuerpo cambiaron.
![[Pasted image 20260407115150.png|319]]

Entoncesla idea es pasar 5


de un enfoque [[Enfoques Lagrangiano y Euleriano#Lagrangiano (material)|Material o Lagrangiano]] a uno [[Enfoques Lagrangiano y Euleriano#Euleriano (espacial)|Espacial o Euleriano]] por lo que las coordenadas pasan del estado inicial $(\xi_1, \xi_2, \xi_3)$ a $(X_1,X_2,X_3)$

Esta transformacion se da mediante una operacion que usa el [[Jacobiano]], con lo cual relacionamos el volumen que se distorsiona ($t>0$) con su condicion inicial ($t=0$), y esto se hace basicamente para que la derivada puede entrar en la integral en (2).

![[Pasted image 20260407152410.png|550]]

Entonces para relacionar las coordenadas eulerianas con las lagrangianas se usara un factor.
$$
d\Omega_0 \times Factor=d\Omega(t)
$$
Ese factor es la operacion del [[Jacobiano]] ($J$)
$$
d\Omega_0 \times J=d\Omega(t)\tag{3}
$$
Y se toma la derivada puesto que nos interesa como varia la parte infinitesimal del volumen, no la parte total.
Ahora colocamis (3) en (2).
$$
\frac{dF(t)}{dt}=\frac{d}{dt}\left(\int_{\Omega} f(\xi_i,t)\ J\times d\Omega_0 \right) \tag{4}
$$
Como $d\Omega_0$ esta congelado, es decir depende solo de la posicion y forma del cuerpo inicial, la derivada ya puede entrar en la integral, puesto que $d\Omega_0$ ya no depende del tiempo, pero como $f$ y $J$ tambien dependen de otras variables y solo nos interesa el tiempo, tomaremos la derivada parcial, y para simplificar simplemente escribiremos $fJ$.
$$
\frac{dF(t)}{dt}=\int_{\Omega}\frac{\partial}{\partial t} \left(fJ\right)d\Omega_0  \tag{5}
$$
Veamos que en (5) hay una derivada del producto es decir.
$$
\frac{\partial (fJ)}{\partial t}=\frac{\partial f}{\partial t}J+\frac{\partial J}{\partial t}f
$$
- [ ] Verificar el material del profesor acerca del jacobiano


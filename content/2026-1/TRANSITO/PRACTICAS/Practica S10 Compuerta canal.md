# Enunciado
Calcular la evolución de un pulso de agua (sube $10\ cm$) que se presenta al subir una compuerta en el extremo aguas arriba de un canal sin movimiento. El canal es de $20\ km$ con profundidad de $10\ m$

Las ecuaciones gobernantes son las siguientes

$$
\begin{align*}
\frac{\partial v}{\partial t}+v \cdot \frac{\partial v}{\partial s}+g \cdot \frac{\partial h}{\partial s}=0 \\ \\ 
\frac{\partial h}{\partial t}+v \cdot \frac{\partial h}{\partial s}+h \cdot \frac{\partial v}{\partial s}=0 
\end{align*}
$$
Que reusltan en las ecuaciones caracteristicas
$$
\frac{d}{dt}(v \pm 2 \cdot C)=0
$$
Con condiciones iniciales:
$$
\begin{cases}
v=0\ m/s \\  
h=10\ m 
\end{cases}\ \rightarrow t=0
$$
Y condiciones frontera
$$
\begin{cases}
 t>0,\ s=0 &\rightarrow h=10.1\ m \\
 v=0 &\rightarrow h=20\ km
\end{cases}
$$
![[Pasted image 20260624125935.png|351]]
Se pide
1. Calcular la evolución temporal del pulso de agua.

## Solucion

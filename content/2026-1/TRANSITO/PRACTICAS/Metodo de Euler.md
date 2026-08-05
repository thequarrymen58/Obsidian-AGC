# Fundacion
Teniendo la ecuacion de la forma
$$
dy/dx=f(x,y) \tag{1}
$$
Se pueden resolver de la forma
$$
y_{i+1}=y_i+h\cdot \phi \tag{2}
$$
Donde:
$h$: Es el tamaño de paso, es decir $h=x_{i+1}-x_i$, en este metodo se toma como constante, ya que la suelen dar como 0.1, 0.01, etc.
El problema viene para obtener una respuesta precisa los pasos deben de ser pequeños, incrementa el numero de iteraciones.

$\phi$: Es la pendiente, es decir $\phi=(y_{i+1}-y_i)/(x_{i+1}-x_i)$, como la derivada nos da la pendiente, es ahi donde debemos reemplazar por la ecuacion diferencial, es decir.
$$
y_{i+1}=y_i+h\cdot f(x_i,y_i) \tag{3}
$$
![[Pasted image 20260512153117.png|338]]
Entonces lo que se quiere lograr con este metodo es ir obteniendo pendientes para poder trazar la posible solucion.
## Ejemplo
### Metodo
Se tiene la funcion $y'=2x^2$, con condicion inicial $y(0)=0$, calcular el intervalo $x=[0,4]$.
1. Tomaremos un paso de $h=0.5$, es decir que tendremos valores para x, como
$$
\begin{align*}
x_0 &=0\\
x_1 &=0.5 \\
x_2 &=1 \\
x_3 &=1.5 \\
x_4 &=2 \\
&\vdots \\
x_8 &=4

\end{align*}
$$
2. Utilizando la ecuacion (3), comenzaremos por la iteracion 1, 
$$
\begin{align*}
y_1 &=y_0+h\cdot f(x_0,y_0) \\
y_1 &=y_0+h\cdot f(0,0) \\
&=0+0.5\cdot (2\cdot 0^2) \\
&=0
\end{align*}
$$
3. Entonces $y_1=0$, pasemos a la iteracion 2.
$$
\begin{align*}
y_2 &=y_1+h\cdot f(x_1,y_1) \\
&=0+0.\cdot f(0.5,0) \\
&=0+0.5\cdot (2\cdot 0.5^2) \\
&=0.25
\end{align*}
$$
4. Entonces $y_2=0.25$, pasemos a la iteracion 3.
$$
\begin{align*}
y_3 &=y_2+h\cdot f(x_2,y_2) \\
&=0.25+0.5\cdot f(1,0.25) \\
&=0.25+0.5\cdot (2\cdot 1^2) \\
&=1.25
\end{align*}
$$
5. De manera analoga con los siguientes.
$$
\begin{align*}
x_3=1.5 &\rightarrow y_4=3.5\\
x_4=2 &\rightarrow y_5=7.5 \\
x_5=2.5 &\rightarrow y_6=13.75\\
x_6=3 &\rightarrow y_7=22.75\\
x_7=3.5 &\rightarrow y_8=35\\
\end{align*}
$$
### Analitica
Reordenando e integrando en los limites se tiene.
$$
\begin{align*}
dy/dx &=2x^2 \\
dy &=2x^2dx \\
\int_{0}^{y}dy &=2\int_{0}^{4}x^2dx \\
y &=2\frac{x^3}{3}|_{0}^{4} \\
y &= 42.667
\end{align*}
$$
### Comparacion
Si graficamos cada punto de la solucion numerica y analitica tendremos, la grafica, donde se aprecia que las solucion de Euler tiende a tener un error de truncamiento, tanto local como propagado.
![[Pasted image 20260512154246.png|575]]


# Enunciado
Diseñar el sistema de conducción, si las tuberías tienen un factor de Hazen - Williams de 120, de tal manera que en operación transporte $200\ l/s$ de agua con una viscosidad de $10^{-6}\ m^2/s$, y cumpla con las siguientes condiciones.
$P_{Max}=50\ mca$
$P_{Min}=3\ mca$
$v_{Max}=4\ m/s$
$v_{Min}=0.6\ m/s$
![[Pasted image 20260519142848.png]]
# Solucion
## Datos
$Q=200\ l/s=0.2\ m^3/s$
$C=120$
$\nu=1 \cdot 10^{-6} \ m^2/s$
$P_{Max}=50\ mca$
$P_{Min}=3\ mca$
$v_{Max}=4\ m/s$
$v_{Min}=0.6\ m/s$
## Formulas a utilizar
Se utilizará como primer paso, la determinacion del caudal utilizando la ecuación de tubería  y canales.
Ecuación de [[Ecuacion de Hazen-Williams]], para la perdida de carga
$$
h_f=\left(\frac{Q \cdot L^{0.54}}{0.27842\cdot C_H \cdot D^{2.63}}\right)^{1/0.54} \tag{1}
$$
Asi como el diametro.
$$
D=\sqrt{\frac{4 \cdot Q}{\pi \cdot v}} \tag{2}
$$
# Tramo 1
## Determinacion diámetro
Utilizando la ecuacion (2).
### Velocidad Minima
Aqui deberemos de redondear el diametro hacia abajo, puesto que hacia arriba haria que la velocidad aumentara, y por algo es minima, para que siga siendo minima, el diametro debe de bajar, hasta un diametro comercial.
$$
\begin{align*}
D_{0.6} &=\sqrt{\frac{4 \cdot 0.2}{\pi \cdot 0.6}} \\
&=0.65 \ m \\
&\approx25.64\ inch
\approx25\ inch \\
&=0.635\ m
\end{align*}
$$
### Velocidad Maxima
$$
\begin{align*}
D_{4} &=\sqrt{\frac{4 \cdot 0.2}{\pi \cdot 4}} \\
&=0.25 \ m \\
&\approx9.93\ inch
\approx10\ inch \\
&=0.254\ m
\end{align*}
$$
## Determinacion perdida de Carga
Usaremos la ecuacion (1), la idea es obtener una perdida de carga para la cual la carga pueda llegar hasta la cota 1100, no muy encima lo que causaria mucho caudal, o muy por debajo, lo que haria que el agua llegue en forma de vapor por tener presion negativa.
### Perdida 1
Por algun motivo que no se, calculamos la perdida con la velocidad maxima, es decir con el diametro minimo, ==y creo que es por que el diseño siempre se hace con el maximo de caudal.==
Luego segun el grafico, el primer tramo tiene una longitud de $2000\ Km$.
$$
\begin{align*}
h_{f,D10} &=\left(\frac{0.2 \cdot 2000^{0.54}}{0.27842\cdot 120 \cdot 0.254^{2.63}}\right)^{1/0.54} \\
&=121.148\ m
\end{align*}
$$
Si vemos se tiene una perdida de carga de $121.148\ m$, graficamente se tiene que 
$$
1200-121.148=1078.85\ m
$$
Es decir, se encuentra por debajo de 1100, el agua llegara como vapor, si nos colocamos en esa cota tenemos una presion minima de $1078.85-1100=-21.49\ m$, si notamos tenemos un limite de presion minima de $3\ m$. 

Se concluye que hay mucha perdida de carga.
![[Pasted image 20260519154629.png]]
### Perdida 2
Como la perdida y el diametro son inversamente proporcionales, entonces para reducir la perdida, se debe de aumentar el diametro, por lo que intentaremos con 12''.
$$
\begin{align*}
h_{f,D12} &=\left(\frac{0.2 \cdot 2000^{0.54}}{0.27842\cdot 120 \cdot 0.3048^{2.63}}\right)^{1/0.54} \\
&=49.85\ m
\end{align*}
$$
Notamos que la perdida se disminuyo a mas de la mitad, siendo la diferencia de cotas.
$$
1200-49.85=1150.15\ m
$$
Graficamente se tiene que nos encontramos algo por encima de nuestra cota de interes, es decir $1150.15-1100=50.15\ m$, es decir una presion mayor a la presion maxima de $50\ m$.
![[Pasted image 20260519154629.png]]
### Perdida 3
Para arreglar el problema anterior deberiamos de aumentar mas el diametro de la tuberia, lo que resultaria no tan apropiado economicamente, por lo que, pasaremos a crear un sistema en serie, es decir dos tramos de tuberia para el tramo I.
Los tramos son a calcular, por ejemplo, podriamos tener 2 tramos de $1\ Km$, o 1 tramo  de $1.5\ Km$, y el otro de $0.5\ Km$. 
Asi como el diametro de la tuberia tambien podria cambiar.

Se proponen dos tramos.
$L_{I.1}=1000 \ | \ D_{I.1}=10\ inch=0.254\ m$
$L_{I.2}=500 \ | \ D_{I.2}=14\ inch= 0.3048\ m$

Cada uno de estos tendra una perdida de carga asosiada que sera sumada al final.

**Perdida 3.1**
$$
\begin{align*}
h_{f,D10} &=\left(\frac{0.2 \cdot 1500^{0.54}}{0.27842\cdot 120 \cdot 0.254^{2.63}}\right)^{1/0.54} \\
&=90.86\ m
\end{align*}
$$
**Perdida 3.2**
$$
\begin{align*}
h_{f,D14} &=\left(\frac{0.2 \cdot 500^{0.54}}{0.27842\cdot 120 \cdot 0.3048^{2.63}}\right)^{1/0.54} \\
&=5.88\ m
\end{align*}
$$
**Perdida Total**
$$
\begin{align*}
h_{f,D10}+h_{f,D14} &= 90.86+5.88 \\
&=96.74\ m
\end{align*}
$$
Siendo la diferencia de cotas.
$$
1200-96.74=1103.25\ m
$$
Es decir estamos $3.25\ m$ por encima de la cota de interes ($1100\ m$), lo cual cumple con la condicion de la presion minima de $3\ m$.
# Tramo 2
## Determinacion de la Longitud
Si notamos, segun la grafica, entre la cota 1100 y 1010, se tiene $90\ m$ para la vertical, por lo que, de manera horizontal se tendra una longitud de $L=720\ m$.
![[Pasted image 20260519170227.png]]
## Selección Diámetro
Seguirmos usando diametro similares a la seccion anterior entre 10 y 14 inch.
## Determinacion perdida de Carga
### Perdida 1
Se comenzara con el diametro minimo, el cual es de 10 inch.
$$
\begin{align*}
h_{f} &=\left(\frac{0.2 \cdot 720^{0.54}}{0.27842\cdot 120 \cdot 0.254^{2.63}}\right)^{1/0.54} \\
&=43.61\ m
\end{align*}
$$
Si tomamos nuestra ultima cota, es decir, $1103.25\ m$, entonces, nuestra nueva cota sera. 
$$
1103.25-43.61=1059.64\ m
$$
Por lo que nuestra presion sobre el punto C, sera de $1059-1010=49.64\ m$, la cual se encuentra en el limite de la presion maxima, es decir $50\ m$.
![[Pasted image 20260519171429.png|643]]
Teniendo esa perdida y cota, la dejamos, puesto que el diametro seleccionado es el menor por limite de velocidad, por ende, el de menor costo.
# Tramo 3
Finalmente, teniendo la cota $1059.64\ m$, y nuestra cota final de $1000\ m$, calculamos la perdida de carga, con los diametros desde el 10 hasta 14 inch.
## Determinacion perdida de Carga
Para una longitud de $L=1500\ m$, se tiene.
### Perdida 1
Se comenzara con el diametro minimo, el cual es de 10 inch.
$$
\begin{align*}
h_{f} &=\left(\frac{0.2 \cdot 1500^{0.54}}{0.27842\cdot 120 \cdot 0.254^{2.63}}\right)^{1/0.54} \\
&=90.86\ m
\end{align*}
$$
En este caso, se tiene una cota nueva de 
$$
1059.64-90.86=968.78\ m
$$
El cual esta por debajo de la cota inferior de $1000\ m$, es decir, se tiene una presion de $-31.21\ m$, no cumple, esta saliendo aire.
![[Pasted image 20260519173846.png|450]]
[Importante](https://youtu.be/BQQZOT8AZEY?t=27)
### Perdida 2
Se probara ahora el siguiente diametro de 12 inch.
$$
\begin{align*}
h_{f} &=\left(\frac{0.2 \cdot 1500^{0.54}}{0.27842\cdot 120 \cdot 0.3048^{2.63}}\right)^{1/0.54} \\
&=37.38\ m
\end{align*}
$$
Se tiene una cota nueva de.
$$
1059.64-37.38=1022.25\ m
$$
Es decir, en el punto D, se tiene una presion de, $1022.25-1000=22.25\ m$, la cual cumple con los parametros de presion minima y maxima.



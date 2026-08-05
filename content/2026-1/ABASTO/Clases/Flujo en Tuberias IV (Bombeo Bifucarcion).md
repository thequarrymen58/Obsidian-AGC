# Enunciado
En el sistema mostrado, determinar:
1. Diametro del tramo II, la cual es de hierro forjado.
2. Caudal por cada una de las tuberias.
3. Potencia de la bomba en HP, si esta impulsa $1.2\ m^3/s$ a 25°C.
4. Determinar lectura en el manometro "P" en $atm$, si en "O" se registra $500\ mmHg$.
Considerar $f_1=f_2=0.02$.
![[Pasted image 20260617120943.png|678]]
## Tablas y diagramas
*Tabla de rugosidades absolutas ($\epsilon$).*
![[Pasted image 20260521184938.png|359]]
*Tabla de propiedades fisicas del agua.*
![[Pasted image 20260521214304.png|508]]
## Datos
$Q=1.2\ m^3/s$

$L_1=200\ m, \ D_1=70\ cm=0.07\ m$, $f_1=0.02$
$L_2=120\ m, \ D_1=?\ m$, $f_2=?$
$L_3=100\ m, \ D_1=50\ cm=0.5\ m$, $f_3=0.02$

$\nu=0.893\cdot 10^{-6}\ m^2/s$, $\rho=997\ kg/m^3$ determinado segun tabla para una temperatura de 25°C.

$\epsilon_{\text{Hierro forjado}}=4.5 \cdot 10^{-5}$, determinado segun tabla de rugosidades absolutas.

## Formulas a Utilizar
 [[Ecuacion Darcy-Weisbach]] para al perdida de carga.
$$
h_f =(82.626 \cdot 10^{-3}) \cdot \frac{ f \cdot Q^2 \cdot L}{ D^5}\ [m] \tag{1}
$$
[[Ecuacion de Bernoulli]], para el balance de energia.
$$
\frac{v_1^2}{2g}+\frac{P_1}{\gamma}+Z_1+B-T=\frac{v_2^2}{2g}+\frac{P_2}{\gamma}+Z_2+\Sigma(h_f+h_l) \tag{2}
$$
Numero de Reynolds, en funcion del caudal.
$$
Re=\frac{4 \cdot Q }{\pi \cdot D \cdot \nu} \tag{3}
$$
Rugosidad Relativa
$$
r=\frac{\epsilon}{D} \tag{4}
$$
Ecuacion de continuidad
$$
Q=v \cdot A\ [m^3/s] \tag{5}
$$
Area de una tuberia
$$
A=\frac{\pi \cdot D^2}{4}\ [m^2] \tag{6}
$$
Potencia
$$
Pot=\gamma \cdot Q \cdot H_{util} \ [W] \tag{7}
$$
Coolebrook-White
$$
\frac{1}{\sqrt{f}}=-2 \cdot \log{\left(\frac{\epsilon/D}{3.7}+\frac{2.5}{Re\ \cdot\sqrt{f}} \right)} \tag{8}
$$
## Solucion Analitica
### Determinacion diametro en II.
Haciendo $Z_Q=111\ m$, entonces el caudal que ira por el tramao II sera de $Q=1.2 \ m/s$, con una perdida de carga igual a $h_{f2}=10\ m$

Luego en (1), solo asumimos un factor de friccion $f_{2a}=0.02$
$$
\begin{align*}
10 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.02 \cdot 1.2^2 \cdot 120}{ D^5} \\ \\
D_2 &= 0.49106\ m
\end{align*}
$$
Usando Reynolds (3).
$$
Re=\frac{4 \cdot 1.2 }{\pi \cdot 0.4910 \cdot 0.893\cdot 10^{-6}}=3484189.8664
$$
Y Coolebrook (8) para obtener el factor de friccion calculado, y compararlo con el asumido.
$$
\begin{align*}
\frac{1}{\sqrt{f}} &=-2 \cdot \log{\left(\frac{4.5 \cdot 10^{-5}/0.49106}{3.7}+\frac{2.5}{3484189.8664\cdot \sqrt{f}} \right)} \\ \\
f_{2c} &=0.01231
\end{align*}
$$
Como $f_{2a}=0.02$ y $f_{2c}=0.01231$ son diferentes, continuaremos con otra iteracion, usando el calculado como valor de entrada.

De vuelta en (1)
$$
\begin{align*}
10 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.01231 \cdot 1.2^2 \cdot 120}{ D^5} \\ \\
D_2 &= 0.44569\ m
\end{align*}
$$
Luego Reynolds.
$$
Re=\frac{4 \cdot 1.2 }{\pi \cdot 0.44569 \cdot 0.893\cdot 10^{-6}}=3838834.0151
$$
Y Coolebrook.
$$
\begin{align*}
\frac{1}{\sqrt{f}} &=-2 \cdot \log{\left(\frac{4.5 \cdot 10^{-5}/0.49106}{3.7}+\frac{2.5}{3838834.0151\cdot \sqrt{f}} \right)} \\ \\
f_{2c} &=0.01245
\end{align*}
$$
Teniendo ello, concluimos que el primer diametro para el tramo II, sera de
$$
D_2=0.44569\ m
$$

==Creo que todo lo anterior no fue necesario, por que a continuacion, se asumira una altura piezometrica diferente de 111, lo cual hara que el calculo efectuado arriba se haga de nuevo, ya que en realidad por la tuberia II no pasara todo el caudal, sino el embalse A estaria por demas.==  
por la weba hice esto? ?
![[Pasted image 20260617160037.png|338]]
### Asumir Presion en Q
Con $Z_Q=120\ m$, se tiene, para el tramo III, una perdida de $h_{f3}=120-111=9\ m$, luego en (1), hallaremos el caudal.
$$
\begin{align*}
9 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.02 \cdot Q_3^2 \cdot 100}{ 0.5^5} \\ \\
Q_3 &= 1.304\ m^3/s
\end{align*}
$$
Absurdo, ya que no puede circular mas caudal del suministrado por la bomba, por lo que se disminuira la altura en Q.

Con $Z_Q=115\ m$, se tiene $h_{f3}=115-111=4\ m$, luego en (1) el caudal es.
$$
\begin{align*}
4 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.02 \cdot Q_3^2 \cdot 100}{ 0.5^5} \\ \\
Q_3 &= 0.87\ m^3/s
\end{align*}
$$
Es mas razonable, luego por el tramo II, estaria pasando.
$$
\begin{align*}
Q1 &=Q_2+Q_3 \\
1.2 &=Q_2+0.87 \\
Q_2 &= 0.33\ m^3/s
\end{align*}
$$
Con este nuevo caudal, determinaremos el diametro y la perdida de carga para el tramo II.
### Determinacion f y D en el tramo II.
#### Iter 1
La perdida para el tramo II, sera de $h_{f2}=115-101=14\ m$
Luego en (1), solo asumimos un factor de friccion $f_{2a}=0.012$
$$
\begin{align*}
14 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.012 \cdot 0.33^2 \cdot 120}{ D^5} \\ \\
D_2 &= 0.24732\ m
\end{align*}
$$
Usando Reynolds (3).
$$
Re=\frac{4 \cdot 0.33 }{\pi \cdot 0.24732 \cdot 0.893\cdot 10^{-6}}=1902377.8762
$$
Y Coolebrook (8) para obtener el factor de friccion calculado, y compararlo con el asumido.
$$
\begin{align*}
\frac{1}{\sqrt{f}} &=-2 \cdot \log{\left(\frac{4.5 \cdot 10^{-5}/0.54732}{3.7}+\frac{2.5}{1902377.8762\cdot \sqrt{f}} \right)} \\ \\
f_{2c} &=0.01404
\end{align*}
$$
#### Iter 2
De vuelta en (1)
$$
\begin{align*}
14 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.01404 \cdot 0.33^2 \cdot 120}{ D^5} \\ \\
D_2 &= 0.25522\ m
\end{align*}
$$
Luego Reynolds.
$$
Re=\frac{4 \cdot 0.83 }{\pi \cdot 0.25522 \cdot 0.893\cdot 10^{-6}}=1843547.69429
$$
Y Coolebrook.
$$
\begin{align*}
\frac{1}{\sqrt{f}} &=-2 \cdot \log{\left(\frac{4.5 \cdot 10^{-5}/0.25522}{3.7}+\frac{2.5}{1843547.69429\cdot \sqrt{f}} \right)} \\ \\
f_{2c} &=0.01398
\end{align*}
$$
#### Iter 3
De vuelta en (1)
$$
\begin{align*}
14 &=(82.626 \cdot 10^{-3}) \cdot \frac{ 0.01398 \cdot 0.33^2 \cdot 120}{ D^5} \\ \\
D_2 &= 0.25502\ m
\end{align*}
$$
Luego Reynolds.
$$
Re=\frac{4 \cdot 0.83 }{\pi \cdot 0.25502 \cdot 0.893\cdot 10^{-6}}=1844998.74178
$$
Y Coolebrook.
$$
\begin{align*}
\frac{1}{\sqrt{f}} &=-2 \cdot \log{\left(\frac{4.5 \cdot 10^{-5}/0.25502}{3.7}+\frac{2.5}{1844998.74178\cdot \sqrt{f}} \right)} \\ \\
f_{2c} &=0.01398
\end{align*}
$$

No hubieron cambios, por lo tanto, el diametro y perdidas finales para el tramo II, seran.
$$
\begin{align*}
D_2 &=0.25502\ m = 10.04\ inch =10\ inch \ (comercial) \\ \\
f &=0.01294
\end{align*}
$$
### Calculo Potencia de la bomba
Primero, graficaremos las presiones que se tienen en el grafico. En el punto "O" se da la presion de
$$
\left(\frac{P}{\gamma}\right)_O=500\ \text{mmHg}
$$
Pero se sabe que.
$$
760\ \text{mmHg} = 10.33\ \text{m.c.a}
$$
Luego en la presion O, por regla de tres,
$$
\begin{array}{lcl}
760\ \text{mmHg} \ \longrightarrow  \ 10.33\ \text{m.c.a} \\
500 \ \text{mmHg} \ \longrightarrow \  (P/\gamma)_O\ \text{m.c.a}
\end{array}
$$
$$
\left(\frac{P}{\gamma}\right)_O=\frac{500 \cdot 10.33}{760}=6.79\ \text{m.c.a}
$$
Luego graficamente se tiene que.
![[Pasted image 20260617144719.png]]
Pero esa presion en "O", debe de ser sumada a la cota, por lo que sumandola y graficando tambien la presion en "Q", se tiene.
![[Pasted image 20260617145044.png]]
Pero aun nos faltaria saber la presion en "P", si graficamos una aproximacion, se veria tal que.
![[Pasted image 20260617152222.png]]
Entonces si notamos, la presion en "P", restada la perdida en el tramo I, nos dara la presion en el nodo "Q".
Por lo que la ecuacion quedaria como.
$$
\begin{align*}
\left(\frac{P}{\gamma}\right)_P-h_{f1} &=115\ m \\ \\
\left(\frac{P}{\gamma}\right)_Q &=115+h_{f1}
\end{align*}
$$
Calculando la perdida $h_{f1}$ mediante (1).
$$
h_{f1} =(82.626 \cdot 10^{-3}) \cdot \frac{ 0.02 \cdot 1.2^2 \cdot 200}{ 0.7^5}=2.83\ m
$$
Luego la presion en Q.
$$
\left(\frac{P}{\gamma}\right)_P =115+2.83=117.83\ m
$$
![[Pasted image 20260617152324.png]]
La altura util de la bomba en este caso, seria la resta entre la lectura de manometros, es decir.
$$
\text{Hu}=117.83-101.79=16.04\ m
$$
Luego calculando la potencia con la formula (7).
$$
Pot=(997 \cdot 9.81) \cdot 1.2 \cdot 16.04 =188256.41136\ W
$$
Para expresarla HP, usaremos el siguiente factor de conversion
$$
1\ W=0.00134102\ HP
$$
Entonces
$$
\begin{align*}
Pot&=188256.41136 \cdot 0.00134102  \\
&=252.45\ HP
\end{align*}
$$
### Determinacion presion "P"
Se pedia determinar la presion en atm, como se determino anteriormente, la presion en ese punto es de
$$
\left(\frac{P}{\gamma}\right)_P =117.83\ m
$$
Pero manometricamente, esta presion sera.
$$
\left(\frac{P}{\gamma}\right)_{Pman} =117.83-95=22.83\ m
$$
Por lo que.
$$
\begin{array}{lcl}
1\ \text{atm} \ \longrightarrow  \ 10.33\ \text{m.c.a} \\
\left(\frac{P}{\gamma}\right)_{Pman} \ \text{atm} \ \longrightarrow \ 22.83\ \text{m.c.a}
\end{array}
$$
$$
\left(\frac{P}{\gamma}\right)_{Pman}=\frac{22.83}{10.33}=2.2\ \text{atm}
$$
## Solucion Numerica
Se tiene el sistema
![[Pasted image 20260617164437.png]]
Luego en las tuberias, se consigna un valor de.
$Q_2=0.8583\ m^3/s$
$Q_3=0.3417\ m^3/s$
Lo cual se asemeja a los valores obtenidos de 0.88 y 0.33.
![[Pasted image 20260617164512.png]]

Asi mismo, en el branch se tiene una presion de 19.85, sumado a la cota de 95, nos da un valor de $114.85\ m$, cercano al valor declarado para los $115\ m$ asumidos en el nodo "Q" 
![[Pasted image 20260617164526.png]]

Finalmente se obtiene la altura util para bomba $dH=15.92$, que esta cercano a nuestro valor obtenido de $16.04\ m$, mientras que la potencia obtenida es igual a $Pot=250.6\ hp$, cercano tambien a nuestro valor calculado de $252.45\ hp$.
![[Pasted image 20260617164604.png|502]]


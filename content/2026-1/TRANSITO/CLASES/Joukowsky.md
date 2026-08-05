# Demostracion
Esta demostracion es macroscopica, no diferencial, por lo cual se usa $\Delta$.
Joukowsky no considero la friccion.

Si hacemos un analisis usando la [[Segunda Ley de Newton]], para un tanque de altura $H$, longitud de tuberia $L$ de diametro $A_0$.
![[Pasted image 20260527132337.png|400]]
$$
F=ma\tag{1}
$$
La fuerza de presion que actua en la valvula para un diferencial de presion macroscopico.
$$
F_{presion}=\Delta P \cdot A_0 \tag{2}
$$
Asi mismo, la masa seria igual a.
$$
m=\rho \cdot A_0 \cdot L \tag{3}
$$
Y la aceleracion como ya se sabe vendria a ser igual a la variacion de la velocidad con respecto al tiempo, de manera macroscopica.
$$
a=\frac{\Delta v}{\Delta t} \tag{4}
$$
Entonces reemplazando (2), (3) y (4) en (1).
$$
\Delta P \cdot A_0=(\rho \cdot A_0 \cdot L ) \cdot \frac{\Delta v}{\Delta t} \tag{5}
$$
Como nuestra intencion es analizar la sobrepresion, la velocidad a la que se mueve la onda de presion en el medio seria la mas importante y mucho mayor que la presion estatica.
$$
L=C \cdot \Delta t \tag{6}
$$
Donde.

$C$: [[Celeridad]] de la onda, o velocidad de propagacion en $m/s$.

Reemplazando (6) en (5)
$$
\begin{align*}
\Delta P \cdot \cancel{A_0} &=(\rho \cdot \cancel{A_0} \cdot L ) \cdot \frac{\Delta v}{\Delta t} \\
&=(\rho \cdot \cancel{L} ) \cdot \frac{C \cdot \Delta v}{\cancel{L}} \\
\Delta P &=\rho \cdot C \cdot \Delta v \tag{7}
\end{align*}
$$
Diviendo (7) entre la densidad especifica, es decir $\gamma=\rho*g$, para expresarla en metros.
$$
\begin{align*}
\underbrace{\frac{\Delta P}{\rho \cdot g}}_{\Delta H} &=\frac{\cancel{\rho} \cdot C \cdot \Delta v}{\cancel{\rho} \cdot g} \\
\end{align*}
$$
Finalmente se tendria la ecuacion que calcula la maxima presion para un tiempo de cierre igual a cero, $t_{cierre}=0$, lo cual es irreal, pero sirve de forma teorica para calcular la sobrepresion en el sistema. 
$$
\Delta H=\frac{C \cdot \Delta v}{g}\ [m] \tag{8}
$$
# Tiempo de cierre
Esta parte ya no compete a Jukowsky, sino mas bien es una variacion realizada por Alievi.

Para que la onda vaya y regrese, usando la ecuaciones (6), se tiene que el recorrido de la onda para que vaya de la valvula hasta el tanque y del tanque hasta la valvula, debe de recorrer 2 veces la longitud, por lo que el tiempo de reflexion sera.
$$
\Delta t=t_R=\frac{2 \cdot L}{C} \tag{7}
$$
## Lento
Para que se considere lento, el tiempo de cierre, debe ser mayor al tiempo que la onda de celeridad regrese a la valvula, por lo que.
$$
t_c>\frac{2 \cdot L}{C}=t_R \tag{8}
$$
### Michaud
Sabemos que la aceleracion es igual a la eq. (9), donde el comportamiento es parcial, devido a que el cierre todavia no se ha dado, ya que es lento, aunque el tiempo de reflexion no es cuando la onda ya viajo dos veces y ya llego a la valvula?, entonces como podemos decir que todavia no se ha cerrado?
$$
\begin{align*}
a&=\frac{\Delta v_{parcial}}{t_R}  \\ \\
\Delta v_{parcial}&= a \cdot t_R \tag{9}
\end{align*}
$$
Analisemos la aceleracion, cuando tenemos una variacion total de velocidad.
$$
a=\frac{\Delta v_{total}}{t_c}=\frac{v_f-v_o}{t_c} \tag{10}
$$
Cuando nuestra valvula esta completamente cerrada, tenemos que la velocidad final sera igual a cero, $v_f=0$, lo cual hara que nuestra eq. (10) quede negativa, pero a nosotros solo nos interesa la magnitud por lo que tomaremos el valor absoluto de esta, quedando.
$$
a=\frac{v_o}{t_c} \tag{11}
$$
Luego introduciendo (11) y (7) en (9) se tiene.
$$
\Delta v_{parcial}=\frac{v_o}{t_c} \cdot \frac{2 \cdot L}{C} \tag{12}
$$
Luego reemplazando (12) en la ecuacion de Joukowsky (8), tendriamos la ecuacion de Michaud, el termino $\Delta v_{parcial}=\Delta v$.
$$
\begin{align*}
\Delta H&=\frac{\cancel{C}}{g} \cdot \frac{v_o}{t_c} \cdot \frac{2 \cdot L}{\cancel{C}} \\ \\
\Delta H&=\frac{2 \cdot L \cdot v_0}{g  \cdot t_c} \tag{13}
\end{align*}
$$
## Rapido
Por otro lado, se considera rapido cuando la onda regresa y la valvula ya esta cerrada, en este caso se podria observar un mayor poder destructivo sobre la valvula.
$$
t_c \le \frac{2 \cdot L}{C}=t_R \tag{14}
$$
En este caso la valvula ya se ha cerrado completamente antes de que la onda regrese a la valvula, por lo que nuestra unica velocidad es la que teniamos al inicio.
$$
\begin{align*}
\Delta v_{parcial}&= \Delta v_{total}= v_0 \tag{15}
\end{align*}
$$
Reemplazando (15), en la ecuacion de Joukowsky (8), tendriamos la ecuacion de Allievi.
$$
\Delta H=\frac{C \cdot v_0}{g} \tag{16}
$$

# Enunciado 1
Se diseña una conducción por gravedad de 820 metros de longitud en cuyo tramo final se encuentra una válvula para dar servicio a unas parcelas de riego. 

El tubo es de PE100 de 160 mm de diámetro y presión nominal de 10bar fabricado según norma UNE-EN 12201. El espesor de la pared del tubo es de 9,5 mm.

La presión máxima admisible es igual a la presión nominal. 
La presión estática: 65 metros. 
El tiempo de cierre de la válvula: 5 segundos. 
1. Calcular la sobrepresión, y el tiempo de cierre de la válvula para evitar un golpe de ariete, suponiendo que por la tubería circulará un caudal máximo de 43 1/s.
![[Pasted image 20260722145101.png|497]]
## Sol. Analitica
### Datos
$L=820\ m$
$D_{nom}=160 \cdot 10^{-3}\ m$
$e=9.5\cdot 10^{-3}\ m$
$D_{in}=160 \cdot 10^{-3}-2\cdot 9.5\cdot 10^{-3}=141 \cdot 10^{-3}\ m$
$H_g=65\ m$
$t_c=5\ s$
$Q=43 \ l/s=43 \cdot 10^{-3}\ m^3/s=154.8\ m^3/h$
$v_0=\frac{Q}{A}=\frac{4\cdot 43 \cdot 10^{-3}}{\pi (141 \cdot 10^{-3})^2 }=2.75\ m/s$
$PMA=P_{nom}=100\ \text{m.c.a}$
$E_{PE100}=1 \cdot 10^8\ \text{kgf}/m^2$
### Celeridad
Con la forma simplificada de la [[Celeridad]].
$$
\begin{align*}
C &= \frac{9900}{\sqrt{48.3 + \frac{10^{10}}{E} \cdot \frac{D}{e}}} 
=\frac{9900}{\sqrt{48.3 + \frac{10^{10}}{1 \cdot 10^8} \cdot \frac{141 \cdot 10^{-3}}{9.5 \cdot 10^{-3}}}} =252.89105 \ m/s \approx253\ m/s
\end{align*}
$$
### Tiempo de reflexion
Usando la eq. (7).
$$
\begin{align*}
t_R&=\frac{2 \cdot L}{C}=\frac{2 \cdot 820}{253}=6.48\ s \approx 6.5\ s
\end{align*}
$$
Notamos que 
$$
\begin{align*}
t_c &<t_R \\
5\ s &<6.5\ s
\end{align*}
$$
### Sobrepresion
Entonces estamos ante un cierre rapido, por lo que para calcular la sobrepresion usaremos la ecuacion de Alievi (16).
$$
\Delta H=\frac{C \cdot v_0}{g}=\frac{253 \cdot 2.75}{9.81}=70.92\ m\approx 71\ m
$$
Entonces la presion que soporta la tuberia seria.
$$
P_{\text{max}}=H_g+\Delta H=65+71=136\ m
$$
![[Pasted image 20260722161014.png|560]]
Lo cual es mayor que nuestra presion admisible, $PMA=100\ m$, por lo que se obtendra una sobrepresion a partir de la presion adimisble, es decir.
$$
\begin{align*}
100&\geq H_g+\Delta H \\ \\
100&\geq65+\Delta H \\ \\
\Delta H&\leq100-65=35\ m
\end{align*}
$$
Entonces nuestra sobrepresion como maximo puede ser igual a $35\ m.c.a$.
### Cierre lento
Usando la formula de Michaud (13), despejaremos el tiempo de cierre, para poder calcularlo teniendo el valor de la sobrepresion.
Con esto obtendremos el tiempo de cierre para que no ocurra golpe de ariete. 
$$
\begin{align*}
\Delta H&=\frac{2 \cdot L \cdot v_0}{g  \cdot t_c} \\ \\
t_c&=\frac{2 \cdot L \cdot v_0}{g  \cdot \Delta H}=\frac{2 \cdot 820 \cdot 2.75}{9.81 \cdot 35}=13.13\ s
\end{align*}
$$
## Sol. Numerica
Armamos el sistema
![[Pasted image 20260722182105.png|406]]
Para el valor del modeulo de Young o flexibilidad se debe de obtener en $Pa$.
$$
E_{PE100}=1 \cdot 10^8\ \frac{\text{kgf}}{m^2} \cdot \frac{9.8067 N}{\text{kgf}}=980.67\ \text{Mpa}
$$
Con una rugosidad absoluta.
$$
\epsilon=0.0015\ mm
$$
### CV (Coefficient Valve)
Se refiere a la cantidad de flujo que pasa por la valvula cuando esta completamente abierta con respecto a la caida de presion a travez de la valvula.
$$
\text{CV}=Q\cdot \sqrt{\frac{SG}{\Delta P}} \tag{17}
$$
Donde:
$Q$: Caudal en $\text{USGPM}$
$SG$: Gravedad especifica del fluido, para el agua a $60°F$, $SG=1$
$\Delta P$: Caida de presion a travez de la valvula en $\text{psi}$, la cual se calcula como $\Delta P=P_{in}-P_{out}$

#### KV (Flow factor)
Es lo mismo que el CV, solo que este es en el sistma metrico.
$$
\text{KV}=Q\cdot \sqrt{\frac{SG}{\Delta P}} \tag{18}
$$
Donde:
$Q$: Caudal en $m^3/h$
$\Delta P$: Caida de presion a travez de la valvula en $\text{bar}$

### Obtencion $\Delta P$
Se sabe que la valvula esta abierta a la atmosfera, por lo que la diferencial de presion es tal que.
$$
\Delta P=P_{in}-P_{out}=P_{in}-0=P_{in}
$$
Esta presion de entrada no es mas que la presion en estado permanente, para ello deberemos de calcularla.
Teniendo.
$$
\Delta h=Hg-h_f \tag{E1.1}
$$
![[Pasted image 20260722172539.png]]
Obtendremos $h_f$ usando.
$$
h_f =(82.626 \cdot 10^{-3}) \cdot \frac{ f \cdot Q^2 \cdot L}{ D^5}=(82.626 \cdot 10^{-3}) \cdot \frac{ f \cdot (43 \cdot 10^{-3})^2 \cdot 820}{ (141 \cdot 10^{-3})^5} \tag{E1.2}
$$
Determinaremos el factor de friccion usando Reynolds y Coolebrook, (agua a 20°)
$$
Re=\frac{v_0 \cdot D}{\nu}=\frac{2.75 \cdot 141 \cdot 10^{-3}}{1.003 \cdot 10^{-6}}=386590.2293
$$
Luego en Coolebrook
$$
\begin{align*}
\frac{1}{\sqrt{f}}&=-2 \cdot \log(\frac{0.0015/141}{3.71}+\frac{2.51}{386590.2293 \cdot \sqrt{f}}) \\ \\
f&=0.01392
\end{align*}
$$
Luego en (E1.2)
$$
h_f =(82.626 \cdot 10^{-3}) \cdot \frac{ 0.0139 \cdot (43 \cdot 10^{-3})^2 \cdot 820}{ (141 \cdot 10^{-3})^5}=31.245\ m
$$
En (E1.1)
$$
\Delta h=Hg-h_f=65-31.245=33.7\ m
$$
Para obtener la presion con unidades en bares, hacemos.
$$
\begin{align*}
\Delta h&=\frac{\Delta P}{\rho \cdot g}=33.7\ m \\ \\
\Delta P&=\rho \cdot g \cdot 33.7=998.2 \cdot 9.81 \cdot 33.7=330001.9254\ Pa \cdot \left(\frac{10^{-5}\ bar}{Pa}\right)=3.300019254\ bar
\end{align*}
$$
Luego en (18) para obtener el KV.
$$
\text{KV}=154.8\cdot \sqrt{\frac{1}{3.300019254}}=85.21
$$
### Resultados
#### Carga y sobrepresion

![[Pasted image 20260722180925.png]]
Se tiene la carga en estado permanente, la cual es igual a $33.25\ m$, mientras que lo calculado analiticamente fue de $33.7\ m$, teniendo un error.
$$
ERP\%=|\frac{\text{Analitico}-\text{Numerico}}{\text{Analitico}}|\cdot 100=|\frac{33.7-33.25}{33.7}|\cdot 100=1.33\%
$$
Asi mismo, se obtiene analiticamente una presion maxima de $136\ m$, mientras que numericamente obtenemos el mismo valor, sin embargo esto es sin seccionar la tuberia, es de esperar que la presion maxima disminuya debido a la friccion dentro de la tuberia.

Haciendo un seccionamiento igual a 100, se tiene que la presion maxima ahora es de 123.2 m, teniendo asi un error de casi 10%.
$$
ERP\%=|\frac{136-123.2}{136}|\cdot 100=9.4\%
$$
![[Pasted image 20260722185905.png|618]]
#### KV
Se observa un comportamiento de cierre lineal
![[Pasted image 20260722190138.png|522]]
# Enunciado 2
Del problema anterior no se sabe la presion, ni el caudal, calcular ellos.
## Sol. Analitica
### Velocidad
Se comenzara por determinar la velocidad en estado permanente, para ello planteamos la [[Ecuacion de Bernoulli]] entre los puntos 1 y 2.
![[Pasted image 20260724124634.png]]
Donde no se consideraran perdidas menores, tampoco bombas o turbinas.
$$
\begin{align*}
\cancel{\frac{v_1^2}{2g}}+\cancel{\frac{P_1}{\gamma}}+Z_1+\cancel{B-T}&=\frac{v_2^2}{2g}+\cancel{\frac{P_2}{\gamma}}+Z_2+\Sigma(\cancel{h_m}+h_f) \\ \\
Z_1&=\frac{v_2^2}{2g}+Z_2+h_f \\ \\
65-h_f&=\frac{v_2^2}{2g} \\ \\
v&=\sqrt{2\cdot g\cdot (65-h_f)} 
\end{align*}
$$
Donde $h_f$ se determinara segun la [[Ecuacion Darcy-Weisbach]].
$$
\begin{align*}
v&=\sqrt{2\cdot g\cdot (65-f \left( \frac{L}{D} \right) \left( \frac{v^2}{2g} \right)\ )} \\ \\
v&=\sqrt{65\cdot 2 \cdot g-f \frac{L \cdot v^2}{D}} \\ \\
v&=\sqrt{1275.3-f \frac{L \cdot v^2}{D}} \tag{E2.1}
\end{align*}
$$
Notamos que se necesita tanto la velocidad como el factor de friccion, pero el factor de friccion depende de la velocidad. Este factor lo podremos obtener mediante la [[Ecuacion de Coolebrook - White]].
Donde, $\epsilon=0.0015\ mm$, $D=141\ mm$
$$
\frac{1}{\sqrt{f}}=-2 \cdot \log(\frac{\epsilon/D}{3.71}+\frac{2.51}{Re \cdot \sqrt{f}})
$$
De manera que supondriamos un factor de friccion, para luego obtener la velocidad mediante E2.1, obtener una velocidad y usar el [[Numero de Reynolds]], finalmente calcular un f con C-W y compararlo con el asumido, es decir.
![[Pasted image 20260724134518.png|157]]
#### Iteracion 1

| $f_{asumido}$ |
| ------------- |
| 0.02          |

En E2.1, 
$$
\begin{align*}
v&=\sqrt{1275.3-0.02\cdot \frac{820 \cdot v^2}{141\cdot 10^{-3}}} \\ \\
v&=3.29712\ m/s
\end{align*}
$$
En Re, utlizando una viscocidad cinematica de $\nu=1.003 \cdot 10^{-6}\ m^2/s$ correspondiente para el agua a 20°C.
$$
\begin{align*}
Re&=\frac{v \cdot D}{\nu} \\ \\
Re&=\frac{3.29712 \cdot 141 \cdot 10^{-3}}{1.003 \cdot 10^{-6}} \\ \\
Re&=463503.40977
\end{align*}
$$

En C-W

$$
\begin{align*}
\frac{1}{\sqrt{f}}&=-2 \cdot \log(\frac{0.0015/141}{3.71}+\frac{2.51}{463503.40977 \cdot \sqrt{f}}) \\ \\
f_{calculado}&=0.013486
\end{align*}
$$

| $f_{asumido}$ | $f_{calculado}$ |
| ------------- | --------------- |
| 0.02          | 0.013486        |
#### Iteracion 2

| $f_{asumido}$ | E2.1 (v) | RE           | C-W ($f_{calculado}$) |
| ------------- | -------- | ------------ | --------------------- |
| 0.013486      | 4.00696  | 563291.48554 | 0.01304               |
Entonces nos quedamos con un factor de friccion final de $f=0.013$, y una velocidad de $4\ m/s$, con lo que el caudal seria de.
$$
\begin{align*}
Q=v \cdot A=4 \cdot \frac{\pi \cdot (141\cdot 10^{-3})^2}{4}=0.06245\ m^3/s=62.458\ l/s
\end{align*}
$$
Lo cual esta alejado del valor dado inicialmente de $43\ l/s$, se debe tambien a que no se consideraron perdidas menores, como bridas, codos, reentrada en el tanque, etc. 
### Presion
La maxima presion admisible depende del tipo de fluido a transportar asi como su temperatura, las cuales se podrian encontrar en el piping class.
#### Normativas
Si fuese agua se usaria la norma [[B31.9]], si fuese slurry [[B31.4]], y si fuese gas [[B31.8]] para el diseño de el espesor de la tuberia y su presion.




















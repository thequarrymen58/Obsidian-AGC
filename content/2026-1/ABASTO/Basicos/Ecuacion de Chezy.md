Utilizada para canales abiertos y conductos.
Se da de la siguiente manera
$$
v=C \cdot \sqrt{R_h \cdot S} \tag{1} 
$$
Donde
$v$: Velocidad del fluido en $m/s$.
$C$: Coeficiente de rugosidad de Chezy, adimensional.
$R_h$: [[Radio hidraulico]] en $m$.
$S$: Pendiente o gradiente hidraulico.
## Caudal
Si multiplicamos por el area m.a.m a (1), se tendra el caudal.
$$
Q=C \cdot A \cdot\sqrt{R_h \cdot S}\ [m^3/s] \tag{2} 
$$

## Tuberia
Si es el caso para un conductor cerrado como una tuberia, se tendra que el [[Radio hidraulico]] sera igual a.
$$
R_h=\frac{D}{4}
$$
Mientras que el area.
$$
A=\frac{\pi \cdot D^2}{4}
$$
Luego reemplazando en (2)
$$
\begin{align*}
Q &=\frac{\pi \cdot D^{5/2}}{4 \cdot \sqrt{2}} \cdot \sqrt{S} \\
Q &=0.392699 \cdot C \cdot D^{5/2} \cdot \sqrt{S} \\
Q &=0.392699 \cdot C \cdot \sqrt{S\cdot D^5} \tag{3}
\end{align*}
$$
## Tuberia y hf
Podriamos reemplazar la pendiente o el gradiente hidraulico por su definicion, la cual es, perdida por longitud, es decir.
$$
S=\frac{h_f}{L}
$$
Luego en (3).
$$
Q =0.392699 \cdot C \cdot \sqrt{\frac{h_f}{L}\cdot D^5}\ [m^3/s] \tag{4}
$$

# Expresar C en f
Cuando queremos simular en fathom, o solo obtener el factor de friccion teorica en terminos del coeficiente de Chezy.

Se tiene la [[Ecuacion Darcy-Weisbach]] para la perdida de carga.
$$
h_f = f \left( \frac{L}{D} \right) \left( \frac{v^2}{2g} \right)\ \tag{5}
$$
(5) se divide por L, y recordando que la pendiente hidraulica es igual a $h_f/L$.
$$
\frac{hf}{L}=S=f \left( \frac{1}{D} \right) \left( \frac{v^2}{2g} \right)\ \tag{6}
$$
De la ecaucion (1), podemos despejar tal que.
$$
\begin{align*}
v &=C \cdot \sqrt{R_h \cdot S} \\ \\
v &=C \cdot \sqrt{\frac{D}{4} \cdot S} \\ \\
v^2 &= C^2 \cdot \frac{D}{4} \cdot S \tag{7}
\end{align*}
$$
Luego (7) en (6).
$$
\begin{align*}
S=\frac{f}{D} \cdot \frac{C^2 \cdot D \cdot S}{4 \cdot 2 \cdot g} \\ \tag{8}
\end{align*}
$$
Finalmente, simplificando y despejando $f$ en (8).
$$
f=\frac{8 \cdot g}{C^2} \tag{8}
$$



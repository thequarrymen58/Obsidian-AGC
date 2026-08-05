Usado para calcular la perdida de carga en tuberias, realciona las propiedades del material con la perdida con rugosidad de la misma.

# Velocidad
Originalmente se tiene la ecuacion en funcion de la velocidad.
## Metrico
$$
V = 0.849 \cdot C_H \cdot R_h^{0.63} \cdot S^{0.54} \tag{1}
$$
Donde
$C_H$: Coeficiente de Hazen-Williams
$V$: Velocidad en $[m/s]$
$R_h$: [[Radio hidraulico]] en $[m]$
$S$: Pendiente en $[m/m]$
## Imperial
$$
V = 1.318 \cdot C_H \cdot R_h^{0.63} \cdot S^{0.54} \tag{2}
$$
Donde
$V$: Velocidad en $[ft/s]$
$R_h$: [[Radio hidraulico]] en $[ft]$
$S$: Pendiente en $[ft/ft]$
# Pendiente hidraulica
$$
S=\frac{h_f}{L} \ [m/m]\tag{3}
$$
Donde
$h_f$: Es la perdidad de carga en $[m]$
$L$: Es la longitud total de la tuberia en $[m]$
# Caudal
## Metrico
Tomando la ecuacion (1) y multiplicando m.a.m por $A$, se tiene.
$$
A\cdot V = A\cdot 0.849 \cdot C_H \cdot R_h^{0.63} \cdot S^{0.54} \tag{4}
$$
Luego se tiene que $Q=A \cdot V$, asi como el radio hidraulico $R_h=D/4$, y el area igual a $A=\pi D^2/4$, todo ello en (4).
$$
Q = \frac{0.849 \cdot \pi}{4^{1.63}}\cdot C_H \cdot D^{2.63} \cdot S^{0.54}
$$
Operando se tiene.
$$
Q = 0.27842\cdot C_H \cdot D^{2.63} \cdot S^{0.54} \ [m^3/s]\tag{5}
$$
Donde
$D$: Diametro de al tuberia en $[m]$
### Perdida de Carga
Si despejamos para solo dejar la perdida de carga $h_f$, se tiene.
$$
h_f=\left(\frac{Q \cdot L^{0.54}}{0.27842\cdot C_H \cdot D^{2.63}}\right)^{1/0.54} \tag{4}
$$
### Diametro
$$
D=\left(\frac{Q \cdot L^{0.54}}{0.27842 \cdot C_H \cdot h_f^{0.54}}\right)^{1/2.63} \tag{5}
$$

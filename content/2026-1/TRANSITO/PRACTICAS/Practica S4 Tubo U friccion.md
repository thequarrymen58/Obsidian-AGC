---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Ejercicio 1
Se trata de un tubo en U, con longitud L de menisco a menisco, en donde los meniscos se desplazan a partir de un movimiento inicial.
![[Pasted image 20260415121901.png|194]]
Teniendo las siguientes condiciones iniciales.
$z(0)=0.25\ m$
$v(0)=1\ m/s$
$L=1.225\ m$
$\nu=1\cdot10^{-5}\ m^2/s$
Se tienen las siguientes EDOs, que describen el movimiento,

$$
\begin{align*}
\frac{dv}{dt} &=-\frac{2g}{L}\cdot z-\frac{32\cdot \nu}{D^2}\cdot v \tag{1} \\
\frac{dz}{dt} &=v \tag{2}
\end{align*}
$$
Reemplazando la velocidad de (2) en (1), se tiene, para la parte izquierda de la ecuacion.
$$
\frac{\partial^2z}{\partial t^2}+\frac{2g}{L}\cdot z+\frac{32\cdot \nu}{D^2}\cdot \frac{\partial z}{\partial t}=0 \tag{3}
$$
1. Calcular la evolucion temporal de la velocidad $v$ y la posicion $z$, usando el sistema de EDOs con resistencia laminar. Para esto construir el codigo use un metodo predictor-corrector de segundo orden.
2. Resolver el ejercicio, pero ahora con la influencia turbulenta con $f=0.03$ cuando las ecuaciones gobernantes son.
$$
\begin{align*}
\frac{dv}{dt}=-\frac{2g}{L}\cdot z-\frac{f}{2\cdot D}\cdot v \cdot |v| \tag{4} \\
\frac{dz}{dt}=v \tag{5}
\end{align*}
$$
## Explicacion del problema

## Solucion Analitica
## Solucion Numerica en Matlab
### Diagrama de Flujo

### Codigo

# Ejercicio 2
![[Pasted image 20260422143041.png]]
## Explicacion del problema
## Solucion Analitica
## Solucion Numerica
### Diagrama de Flujo

### Codigo


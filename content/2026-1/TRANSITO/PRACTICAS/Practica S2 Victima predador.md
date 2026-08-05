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
    display_name: hidraulica
    language: python
    name: python3
---

# Ejercicio 1
![[Pasted image 20260408122155.png|667]]
## Explicacion del problema
Tiene que ver con las [[Ecuaciones de Lotka-Volterra]], tambien se usara el [[Metodo de Heun]]
## Solucion analitica
## Pseudo-Codigo
## Codigo
```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Constantes del sistema
alpha, beta = 0.25, -0.01
gamma, delta = -1.0, 0.01

# Parámetros de simulación
t_final = 30
dt = 0.1
pasos = int(t_final / dt)

# Vectores de almacenamiento
x = np.zeros(pasos + 1)
y = np.zeros(pasos + 1)
t = np.linspace(0, t_final, pasos + 1)

# Condiciones iniciales
x[0], y[0] = 100, 40

# Sistema de EDOs
def sistema(x_val, y_val):
    dxdt = alpha * x_val + beta * x_val * y_val
    dydt = gamma * y_val + delta * x_val * y_val
    return dxdt, dydt

# 2. Bucle de Integración (Heun)
for i in range(pasos):
    dx, dy = sistema(x[i], y[i])
    x_pred = x[i] + dx * dt
    y_pred = y[i] + dy * dt
    
    dx_p, dy_p = sistema(x_pred, y_pred)
    x[i+1] = x[i] + (dt / 2.0) * (dx + dx_p)
    y[i+1] = y[i] + (dt / 2.0) * (dy + dy_p)

# 3. Representación Gráfica (Subplots para evitar el error de escala)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, x, 'g-', label='Victimas')
plt.plot(t, y, 'r-', label='Predadores')
plt.title('Evolucion en el Tiempo')
plt.grid(True); plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y, 'b-')
plt.title('Plano de Fase (El Circulo)')
plt.xlabel('Victimas (x)'); plt.ylabel('Predadores (y)')
plt.grid(True)

plt.tight_layout()
plt.show()
```


# Ecuacion
Se dice que el problema debe de realizarce primero con primer orden, y se pide que nosotros mismos lo hagamos, puesto que mas adelante vendran problemas no lineales, como de una camara de equilibrio.

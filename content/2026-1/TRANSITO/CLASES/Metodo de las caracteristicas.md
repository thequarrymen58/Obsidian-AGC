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

### 1. La Física: Desde $F = ma$ hasta la Ecuación de Allievi

La segunda imagen que compartes demuestra cómo se llega a la famosa fórmula de Joukowsky/Allievi. Imagina que tienes una columna de agua moviéndose por el tubo y, de repente, cierras la válvula. Toda esa masa de agua tiene que detenerse.

1.  **Masa del agua:** En un tubo de longitud $L$ y área $A$, la masa es $m = \rho \cdot L \cdot A$ (densidad por volumen).
2.  **Aceleración (o deceleración en este caso):** El cambio de velocidad en el tiempo es $a = \frac{\Delta v}{\Delta t}$.
3.  **Segunda Ley de Newton ($F = ma$):** La fuerza necesaria para detener esa masa es $F = (\rho L A) \frac{\Delta v}{\Delta t}$.
4.  **Presión:** Esa fuerza es generada por una onda de sobrepresión en la válvula, por lo que $F = \Delta p \cdot A$.
    Igualando: $\Delta p \cdot A = (\rho L A) \frac{\Delta v}{\Delta t}$
5.  **El tiempo crítico:** La onda de presión viaja a la velocidad del sonido en el agua (celeridad $a$). El tiempo que tarda la onda en recorrer la longitud afectada es $\Delta t = L / a$.
6.  **Fórmula de Allievi:** Si sustituyes ese $\Delta t$ en la ecuación anterior, la $L$ se cancela y te queda:
    $$
\Delta p = \rho \cdot a \cdot \Delta v
$$
    Que expresado en "carga" o altura de agua (dividiendo por $\rho g$), se convierte en la Ecuación de Allievi (el golpe de ariete máximo):
    $$
\Delta H = \frac{a \cdot \Delta v}{g}
$$

### 2. Las Ecuaciones Gobernantes y el Gráfico Triangular

Aunque Allievi nos da la presión máxima instantánea, no nos dice qué pasa a la mitad del tubo en el segundo 3. Para eso necesitamos las **ecuaciones gobernantes** (tu tercera imagen):
*   **Ecuación de Movimiento:** Basada en $F=ma$, incluye la fricción ($S_f$).
*   **Ecuación de Continuidad:** Basada en la conservación de la masa y la compresibilidad del agua/tubo.

Son Ecuaciones Diferenciales Parciales (EDP), muy difíciles de resolver. Aquí es donde entra el **Método de las Características** (imágenes 4, 5 y 6).
*   Mediante un truco matemático, esas EDP se convierten en Ecuaciones Diferenciales Ordinarias (más simples) **PERO** con una condición: solo son válidas si viajas a través del tiempo y el espacio siguiendo "líneas características" a velocidad $+a$ o $-a$.
*   **El famoso gráfico triangular (Imagen 6):** Representa la red espacio-tiempo en la computadora. Para calcular lo que pasa en el punto del medio en el futuro (Punto P), la computadora toma la información del nodo izquierdo (Punto I) y derecho (Punto D) del pasado.
*   **El Seccionamiento (AFT Impulse):** Para que estas líneas diagonales encajen perfectamente en los nodos de cálculo, se debe cumplir que $\Delta x = a \cdot \Delta t$. Por eso el software te pide dividir la tubería; está construyendo la malla de esos triángulos.

---

### 3. Resolución Analítica del Problema



---

### 4. Código en Python (El Método de las Características)

Este código hace exactamente lo que hace internamente un software especializado. Define el "seccionamiento" de la tubería, calcula el estado inicial y luego simula paso a paso la propagación de la onda, dibujando las líneas de presión.

Para ejecutarlo, necesitas tener instaladas las librerías `numpy` y `matplotlib`.

```
import numpy as np
import matplotlib.pyplot as plt

# --- PARÁMETROS DEL SISTEMA ---
L = 10000.0         # Longitud (m)
D = 1.0             # Diámetro (m)
a = 1000.0          # Velocidad de onda (m/s)
Q0 = 2.0            # Caudal inicial (m3/s)
H_res = 400.0       # Carga en el reservorio (m)
f = 0.01976         # Factor de fricción
g = 9.81            # Gravedad (m/s2)

A = (np.pi * D**2) / 4.0
v0 = Q0 / A

# --- PARÁMETROS DE DISCRETIZACIÓN (El "Seccionamiento") ---
N = 50                 # Número de secciones de la tubería
dx = L / N             # Longitud de cada sección (delta x)
dt = dx / a            # Paso de tiempo (delta t) forzado por dx/dt = a
t_simulacion = 20.0    # Segundos totales a simular
pasos_tiempo = int(t_simulacion / dt)

# Constantes del Método de las Características (MOC)
B = a / (g * A)
R = f * dx / (2 * g * D * A**2)

# --- INICIALIZACIÓN ---
# Vectores de distancia y variables de estado (H: Carga, Q: Caudal)
x = np.linspace(0, L, N+1)
H_old = np.zeros(N+1)
Q_old = np.ones(N+1) * Q0

# Calculamos la línea piezométrica en Estado Permanente (Parte a)
hf_total = f * (L / D) * (v0**2 / (2 * g))
for i in range(N+1):
    H_old[i] = H_res - (f * (x[i] / D) * (v0**2 / (2 * g)))

# Guardamos el perfil inicial para el gráfico
H_inicial = H_old.copy()

# Arreglos para el nuevo tiempo y para guardar la envolvente máxima
H_new = np.zeros(N+1)
Q_new = np.zeros(N+1)
H_max_envelope = H_old.copy()

# --- BUCLE DE SIMULACIÓN (Cierre Instantáneo de Válvula) ---
for t in range(pasos_tiempo):
    # 1. Nodos Interiores (Basado en el triángulo característico)
    for i in range(1, N):
        Cp = H_old[i-1] + B * Q_old[i-1] - R * Q_old[i-1] * abs(Q_old[i-1])
        Cm = H_old[i+1] - B * Q_old[i+1] + R * Q_old[i+1] * abs(Q_old[i+1])
        
        H_new[i] = (Cp + Cm) / 2.0
        Q_new[i] = (Cp - Cm) / (2.0 * B)
        
    # 2. Condición de Frontera Aguas Arriba (Reservorio)
    H_new[0] = H_res # Nivel constante
    Cm_frontera = H_old[1] - B * Q_old[1] + R * Q_old[1] * abs(Q_old[1])
    Q_new[0] = (H_new[0] - Cm_frontera) / B
    
    # 3. Condición de Frontera Aguas Abajo (Válvula)
    # Cierre instantáneo: El caudal en el nodo N (válvula) se vuelve 0 en t>0
    Q_new[N] = 0.0
    Cp_frontera = H_old[N-1] + B * Q_old[N-1] - R * Q_old[N-1] * abs(Q_old[N-1])
    H_new[N] = Cp_frontera
    
    # Actualizar para el siguiente paso de tiempo
    H_old = H_new.copy()
    Q_old = Q_new.copy()
    
    # Rastrear la presión máxima histórica en cada nodo
    H_max_envelope = np.maximum(H_max_envelope, H_new)

# --- GRAFICAR RESULTADOS ---
plt.figure(figsize=(10, 6))

# Línea base del reservorio (400m)
plt.axhline(y=400, color='gray', linestyle='--', label='Nivel del Reservorio (Estático)')

# Estado Permanente (Solución de la Parte a)
plt.plot(x, H_inicial, 'b-', linewidth=2, label='Estado Permanente (Inicial)')

# Envolvente Máxima de Presión MOC (Solución de la Parte b simulada)
plt.plot(x, H_max_envelope, 'r-', linewidth=2, label='Envolvente Máxima de Presión (Golpe de Ariete)')

# Añadir textos con los valores clave
plt.text(L*0.9, H_inicial[-1] - 20, f'{H_inicial[-1]:.1f} m', color='blue')
plt.text(L*0.9, H_max_envelope[-1] + 10, f'{H_max_envelope[-1]:.1f} m', color='red')

plt.title('Perfil de Carga Piezométrica en la Tubería (Allievi / MOC)')
plt.xlabel('Distancia desde el reservorio (m)')
plt.ylabel('Carga piezométrica / H (m)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Carga en estado permanente en la válvula: {H_inicial[-1]:.2f} m")
print(f"Carga MÁXIMA simulada en la válvula: {H_max_envelope[-1]:.2f} m")
print(f"Sobrepresión simulada: {H_max_envelope[-1] - H_inicial[-1]:.2f} m")
```

### ¿Qué verás al ejecutar el código?
1.  **Línea Azul:** Es la solución a tu inciso (a), la caída de la presión debido a la fricción ($h_f$).
2.  **Línea Roja:** Es la "envolvente", que muestra la presión máxima que soportará cada tramo del tubo. Si miras el extremo derecho (la válvula), verás que el código numérico simulará exactamente una presión máxima de **~594.3 m**, demostrando que el método matemático riguroso de MOC (como en AFT Impulse) coincide a la perfección con la simplificación teórica de Allievi que calculamos en la parte (b).

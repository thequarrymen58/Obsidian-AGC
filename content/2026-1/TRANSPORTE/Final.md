¡Perfecto! Vamos a resolver el **PROBLEMA No. 1 (8 PUNTOS)** de esta nueva hoja de examen. 

El problema trata sobre el diseño de un **sistema de transporte neumático a succión**, muy similar al primer problema que hicimos, pero con diferentes datos, accesorios y un requerimiento explícito de usar el gráfico para un "producto pulverulento". 

Además, te daré las instrucciones exactas de cómo debes hacer el **bosquejo (croquis)** al final para que asegures todos los puntos.

---

### **DATOS DEL PROBLEMA**
*   **Capacidad ($W$):** $2500 \text{ Lbs/hora}$
*   **Material:** Producto pulverulento
*   **Peso específico ($\gamma$):** $400 \text{ Kg/m}^3$
*   **Codos:** $4$ codos a $90^\circ$, Radio ($R$) = $5 \text{ pies}$
*   **Ángulo de deslizamiento ($\alpha$):** $25^\circ$
*   **Longitud horizontal ($L_H$):** $90 \text{ pies}$
*   **Longitud vertical ($L_V$):** $60 \text{ pies}$
*   **Pérdidas en entrada del ducto ($P_{ent}$):** $2 \text{ pulgadas de H}_2\text{O}$
*   **Pérdidas en el ciclón ($P_{ciclon}$):** $2.5 \text{ pulgadas de H}_2\text{O}$
*   **Pérdidas en filtro de mangas ($P_{filtro}$):** $2.5 \text{ pulgadas de H}_2\text{O}$
*   **Eficiencia del ventilador ($\eta$):** $70\% = 0.70$
*   **Componentes:** 1 toma de aire, 1 tolva, 1 ciclón, 1 filtro de mangas, 1 receptáculo, 1 ventilador centrífugo, 1 motor.

---

### **PASO 1: Obtener Velocidad y Volumen de Aire del Gráfico**
El problema exige utilizar el gráfico para un material pulverulento de $400 \text{ Kg/m}^3$. Entramos a la **Figura 41 (pág. 105 del manual)**:
1.  **Velocidad de transporte ($V$):** Intersectando $400 \text{ kg/m}^3$, la curva marca $\approx 22.9 \text{ m/s}$.
    *   Convertimos: $22.9 \text{ m/s} \times 3.281 \times 60 \approx \mathbf{4500 \text{ pies/min}}$.
    *   En pies/seg: $V_{seg} = 4500 / 60 = \mathbf{75 \text{ pies/seg}}$.
2.  **Volumen de aire:** La curva marca $\approx 2.5 \text{ m}^3\text{/kg}$.
    *   Convertimos: $2.5 \times (3.281)^3 / 2.2046 \approx \mathbf{40 \text{ pie}^3\text{ de aire / Lb de material}}$.

---

### **PASO 2: Cálculo de Flujos y Diámetro del Ducto**
1.  **Flujo de material ($W$):** 
    $$
W = \frac{2500 \text{ Lbs/hora}}{60 \text{ min/hora}} = \mathbf{41.67 \text{ Lbs/min}}
$$
2.  **Caudal de Aire Requerido ($Q_s$):**
    $$
Q_s = W \times (\text{Volumen por Lb}) = 41.67 \text{ Lbs/min} \times 40 \text{ pie}^3\text{/Lb} = \mathbf{1666.8 \text{ CFM}}
$$
3.  **Selección del Diámetro ($D$):**
    Constante de tubería = $\frac{Q_s}{V_{seg}} = \frac{1666.8}{75} = \mathbf{22.22}$
    En la Tabla N° 06 de los apuntes (Schedule 30), el valor comercial más cercano es **21.32**, que corresponde a una tubería de **$8 \text{ pulgadas}$ de diámetro nominal**.

---

### **PASO 3: Cálculo de las Energías del Material (E)**
Datos para fórmulas: $g = 32.2 \text{ pies/seg}^2$, fricción $f = \tan(25^\circ) = \mathbf{0.4663}$.

*   **$E_1$ (Energía de Aceleración):**
    $$
E_1 = \frac{W \cdot V^2}{2g} = \frac{41.67 \times (75)^2}{2 \times 32.2} = \mathbf{3640 \text{ Lbs}\cdot\text{pie/min}}
$$
*   **$E_2$ (Energía Vertical):**
    $$
E_2 = W \cdot L_V = 41.67 \times 60 = \mathbf{2500 \text{ Lbs}\cdot\text{pie/min}}
$$
*   **$E_3$ (Fricción Horizontal):**
    $$
E_3 = W \cdot f \cdot L_H = 41.67 \times 0.4663 \times 90 = \mathbf{1749 \text{ Lbs}\cdot\text{pie/min}}
$$
*   **$E_4$ (Fricción en Codos):**
    Para $1$ codo: $E_{codo} = \frac{W \cdot V^2}{g} \cdot f \cdot \frac{\pi \cdot \alpha}{180^\circ}$
    $$
E_{codo} = \left( \frac{41.67 \times 75^2}{32.2} \right) \times 0.4663 \times \left( \frac{\pi \times 90^\circ}{180^\circ} \right) = 7280 \times 0.4663 \times 1.5708 = 5332 \text{ Lbs}\cdot\text{pie/min}
$$
    Para los **$4$ codos**: $E_4 = 4 \times 5332 = \mathbf{21328 \text{ Lbs}\cdot\text{pie/min}}$

**Energía total del material ($E_{mat}$):**
$$
E_{mat} = 3640 + 2500 + 1749 + 21328 = \mathbf{29217 \text{ Lbs}\cdot\text{pie/min}}
$$

**Transformando a caída de presión ($P_{mat}$):**
$$
P_{mat} = \frac{E_{mat}}{Q_s \times 5.2} = \frac{29217}{1666.8 \times 5.2} = \mathbf{3.37 \text{ pulg. de H}_2\text{O}}
$$

---

### **PASO 4: Pérdidas por Fricción del Aire en Tubería ($P_{tub}$)**
*   **Longitud equivalente de los 4 codos:**
    $$
L_{eq} = 4 \times \left( \frac{\pi \cdot R \cdot \alpha}{180^\circ} \right) = 4 \times \left( \frac{\pi \times 5 \times 90^\circ}{180^\circ} \right) = \mathbf{31.4 \text{ pies}}
$$
*   **Longitud total del ducto ($L_T$):**
    $$
L_T = 90 + 60 + 31.4 = \mathbf{181.4 \text{ pies}}
$$
*   **Pérdida en la tubería limpia ($P_{tub}$):**
    De la carta de fricción (para $8"$ y $1667 \text{ CFM}$), la pérdida es $\approx 1.0 \text{ pulg. de H}_2\text{O}$ por cada $100 \text{ pies}$.
    $$
P_{tub} = 181.4 \times \left(\frac{1.0}{100}\right) = \mathbf{1.81 \text{ pulg. de H}_2\text{O}}
$$

---

### **PASO 5: Presión Total y Selección del Motor**
Sumamos todas las caídas de presión indicadas en el problema:
$$
P_{total} = P_{mat} + P_{tub} + P_{ent} + P_{ciclon} + P_{filtro}
$$
$$
P_{total} = 3.37 + 1.81 + 2.0 + 2.5 + 2.5 = \mathbf{12.18 \text{ pulg. de H}_2\text{O}}
$$

**Potencia requerida ($HP$):**
$$
HP = \frac{Q_s \times P_{total}}{6346.15 \times \eta} = \frac{1666.8 \times 12.18}{6346.15 \times 0.70} = \frac{20301.6}{4442.3} = \mathbf{4.57 \text{ HP}}
$$

**Selección del Motor Eléctrico:**
Como necesitamos $4.57 \text{ HP}$, seleccionamos el tamaño comercial inmediato superior, que es un **Motor de $\mathbf{5 \text{ HP}}$**.

---

### **EL BOSQUEJO (CROQUIS) EXIGIDO POR EL PROFESOR**
En la parte inferior de tu hoja o en el reverso, debes dibujar el sistema a mano alzada. Te explico cómo estructurarlo para que esté perfecto (basado en la *Figura 16* de los apuntes):

1.  **Dibuja a la izquierda abajo:** Una pequeña boquilla de entrada abierta con una flecha que diga **"Toma de aire (Aire)"**.
2.  **Seguido a eso:** Dibuja un embudo (la **Tolva de Carga**) con un aspa debajo que diga **"Alimentador rotatorio"**. Aquí cae el material.
3.  **Tubería:** Dibuja la tubería avanzando en horizontal (ponle una cota que diga **$L_H = 90'$**). Luego haz que suba con un **Codo**. Dibuja la subida (ponle cota **$L_V = 60'$**). 
4.  *(Dibuja curvas que representen los 4 codos en los cambios de dirección)*.
5.  **Ciclón:** La tubería llega a la parte superior de un cilindro con fondo cónico. Señálalo como **"Ciclón"**. Debajo del cono dibuja una caja o válvula y ponle **"Receptáculo"**.
6.  **Filtro:** De la parte de arriba del Ciclón sale otra tubería que va hacia una caja grande con líneas punteadas adentro. Señálalo como **"Filtro de mangas de tela"**. Debajo también lleva otra salida (receptáculo de polvo fino).
7.  **Ventilador:** De la parte de arriba del Filtro sale una tubería que entra al centro del caracol de un ventilador. Señálalo como **"Ventilador Centrífugo"** y pon al lado un cuadrito que diga **"Motor 5 HP"**.
8.  Del ventilador sale una flecha hacia arriba que diga **"Aire limpio a la atmósfera"**.

Con todo el cálculo sustentado y ese bosquejo, el problema 1 está resuelto al $100\%$ para llevarte los 8 puntos. 

¿Quieres que sigamos con el **PROBLEMA No. 2** de la foto (el del tanque de petróleo)? 
![[Pasted image 20260716153314.png]]



# Enunciado 2
Aquí tienes la resolución directa y paso a paso, aplicando las fórmulas del manual API 650 (criterio de cátedra) y manteniendo el texto al mínimo.

### **a.- Dimensiones del tanque (Criterio Ingenieril)**
**1. Volumen de Diseño ($V_d$):**
Fórmula de variación volumétrica (API): $V_d = V + \Delta V = V + (\alpha \cdot V \cdot \Delta T)$
*   $V_d = 100,000 + (8 \times 10^{-4} \cdot 100,000 \cdot 50) = 104,000 \text{ Barriles}$
*   Conversión a pies cúbicos (Criterio de clase: $1 \text{ gal} = 0.13 \text{ pie}^3$): 
    $V_d = 104,000 \text{ bbl} \times 42 \text{ gal/bbl} \times 0.13 \text{ pie}^3\text{/gal} = \mathbf{567,840 \text{ pie}^3}$

**2. Dimensiones teóricas y reales:**
Fórmula de volumen cilíndrico: $V_d = \frac{\pi \cdot D^2}{4} \cdot H$
Reemplazando la condición $D = \frac{8}{3}H$:
*   $567,840 = \frac{\pi \cdot (\frac{8}{3}H)^2}{4} \cdot H \implies 567,840 = 5.585 \cdot H^3 \implies H_{teorico} = 46.67 \text{ pies}$

**Criterio Ingenieril:** Ajustamos a múltiplos de planchas comerciales grandes ($5' \times 10'$). 
*   Adoptamos **$H = 45 \text{ pies}$** (9 paños de 5 pies de altura).
*   Despeja  mos el diámetro real: $D = \sqrt{\frac{4 \cdot 567,840}{\pi \cdot 45}} = 126.78 \text{ pies}$.
*   Ajustamos a un perímetro múltiplo de 10 pies para no cortar planchas: $L_c = 400 \text{ pies} \implies \mathbf{D = 127.32 \text{ pies}}$.

### **b.- Espesor de cada paño del casco**
Gravedad específica ($Ge$): $800 / 1000 = \mathbf{0.8}$
Fórmula simplificada de la API 650 para el casco: $t = 0.0001456 \cdot (H_i - 1) \cdot D \cdot Ge + CA$
*Margen por corrosión (CA) estándar = 1/16" (0.0625").*
Reemplazando fijos: $t_i = 0.0001456 \cdot (H_i - 1) \cdot (127.32) \cdot (0.8) + 0.0625$

*   **Paño 1 ($H=45'$):** $t_1 = 0.01483(44) + 0.0625 = 0.715" \implies$ **Uso: $3/4"$**
*   **Paño 2 ($H=40'$):** $t_2 = 0.01483(39) + 0.0625 = 0.640" \implies$ **Uso: $11/16"$**
*   **Paño 3 ($H=35'$):** $t_3 = 0.01483(34) + 0.0625 = 0.566" \implies$ **Uso: $5/8"$**
*   **Paño 4 ($H=30'$):** $t_4 = 0.01483(29) + 0.0625 = 0.492" \implies$ **Uso: $1/2"$**
*   **Paño 5 ($H=25'$):** $t_5 = 0.01483(24) + 0.0625 = 0.418" \implies$ **Uso: $7/16"$**
*   **Paño 6 ($H=20'$):** $t_6 = 0.01483(19) + 0.0625 = 0.344" \implies$ **Uso: $3/8"$**
*   **Paño 7 ($H=15'$):** $t_7 = 0.01483(14) + 0.0625 = 0.270" \implies$ **Uso: $5/16"$**
*   **Paño 8 ($H=10'$):** $t_8 = 0.01483(9) + 0.0625 = 0.196" \implies$ **Uso: $5/16"$** *(Mínimo API para $D>120'$)*
*   **Paño 9 ($H=5'$):** $t_9 = 0.01483(4) + 0.0625 = 0.121" \implies$ **Uso: $5/16"$** *(Mínimo API)*

### **c.- Cantidad de planchas (Casco y Fondo)**
Utilizaremos las planchas mayores ($5' \times 10'$ $\implies$ Área = $50 \text{ pie}^2$).
*   **Casco:** Perímetro de 400 pies $\implies 40$ planchas/anillo $\times 9$ anillos = **$360 \text{ planchas}$**.
*   **Fondo:** Área de círculo ($A_f = \frac{\pi \cdot D^2}{4}$): $A_f = \frac{\pi \cdot 127.32^2}{4} = 12,732 \text{ pie}^2$.
    *   Fórmula: $\text{Cant} = \frac{A_f}{\text{Área plancha}} = \frac{12,732}{50} = 254.6 \implies$ **$255 \text{ planchas}$** *(Espesor ref: 1/4")*

### **d.- Cantidad de planchas para el Techo**
El techo es un cono con inclinación $\theta = 15^\circ$ y Radio $R = \frac{127.32}{2} = 63.66 \text{ pies}$.
*   Generatriz ($L_g$): $L_g = \frac{R}{\cos 15^\circ} = \frac{63.66}{0.9659} = 65.91 \text{ pies}$
*   Área lateral del cono: $A_t = \pi \cdot R \cdot L_g = \pi \cdot 63.66 \cdot 65.91 = 13,180.6 \text{ pie}^2$
*   Cantidad: $\frac{13,180.6}{50} = 263.6 \implies$ **$264 \text{ planchas}$** *(Espesor ref: 1/4")*

### **e.- Cantidad y costo de electrodos**
Se halla el peso sumando Volúmenes $\times$ Densidad del acero ($7850 \text{ kg/m}^3$).
*(Constante: 1 plancha $5' \times 10'$ de 1" de espesor pesa $926.2 \text{ kg}$)*
*   **Peso Casco:** $(40 \times 926.2 \text{ kg}) \times [0.75 + 0.6875 + 0.625 + 0.5 + 0.4375 + 0.375 + 3(0.3125)] = \mathbf{159,768 \text{ kg}}$
*   **Peso Fondo (asumiendo 1/4"):** $255 \times 926.2 \times 0.25 = \mathbf{59,045 \text{ kg}}$
*   **Peso Techo (asumiendo 1/4"):** $264 \times 926.2 \times 0.25 = \mathbf{61,129 \text{ kg}}$
*   **Peso Tubo (H = $45'$ + Altura cono):**
    Altura cono = $R \cdot \tan 15^\circ = 63.66 \cdot 0.2679 = 17.05'$.
    Longitud tubo = $45' + 17.05' = 62.05 \text{ pies} = \mathbf{18.91 \text{ m}}$.
    Peso = $18.91 \text{ m} \cdot 79.71 \text{ kg/m} = \mathbf{1,507 \text{ kg}}$

**Peso Total del acero:** $159,768 + 59,045 + 61,129 + 1,507 = \mathbf{281,449 \text{ kg}}$
**Cantidad Electrodos (3%):** $281,449 \times 0.03 = \mathbf{8,443.5 \text{ kg}}$
**Costo Electrodos:** $8,443.5 \text{ kg} \times 4.5 \text{ \$/kg} = \mathbf{\$37,995.75}$

### **f.- Costo Total de Materiales**
*   **Costo Planchas (Casco+Fondo+Techo):** $(159,768 + 59,045 + 61,129) \text{ kg} \times 2.5 \text{ \$/kg} = \mathbf{\$699,855.00}$
*   **Costo Tubo Central:** $18.91 \text{ m} \times 60 \text{ \$/m} = \mathbf{\$1,134.60}$
*   **Costo Electrodos:** $\mathbf{\$37,995.75}$

**COSTO TOTAL = $699,855.00 + 1,134.60 + 37,995.75 = \mathbf{\$738,985.35}$**
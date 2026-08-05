
# Enunciado 1
### **DATOS DEL PROBLEMA**
*   **Material:** Trigo en cáscara.
*   **Peso específico ($\gamma$):** $48 \text{ libras/pie}^3$.
*   **Tamaño máximo de grano:** $3/8\text{ pulgada}$.
*   **Temperatura de trabajo:** $75^\circ\text{F}$ (Condición normal, no requiere factores especiales).
*   **Capacidad requerida:** $20 \text{ Toneladas largas / hora}$.
*   **Distancia vertical ($H$):** $64 \text{ pies}$.
*   **Servicio:** $8 \text{ horas diarias}$ (Servicio normal, factor de servicio $f_s = 1.0 \text{ a } 1.2$).

---

### **PASO 1: Calcular la Capacidad de Diseño en Volumen**
Primero, convertimos las "Toneladas largas" (Long Tons) a libras.
*   $1 \text{ Tonelada Larga} = 2240 \text{ libras}$.
*   $\text{Capacidad Másica } (Q_m) = 20 \text{ Ton/h} \times 2240 \text{ lbs/Ton} = \mathbf{44,800 \text{ lbs/hora}}$.

Ahora, hallamos la capacidad volumétrica ($C$):
$$
C = \frac{44,800 \text{ lbs/hora}}{48 \text{ lbs/pie}^3} = \mathbf{933.33 \text{ pie}^3\text{/hora}}
$$

---

### **PASO 2: Selección del Tipo de Elevador y Parámetros Asumidos**
Como el trigo es un producto granular, suelto y de flujo libre, se debe utilizar un **Elevador de Cangilones de Descarga Centrífuga**.
*   **Velocidad asumida de la faja ($V_{faja}$):** Rango típico para granos es de $200$ a $400 \text{ pies/min}$. Asumiremos **$300 \text{ pies/minuto}$** para iniciar el tanteo.
*   **Espaciamiento entre cangilones ($t$):** Asumiremos un espaciamiento estándar de **$16 \text{ pulgadas}$** ($1.333 \text{ pies}$).

---

### **PASO 3: Selección del Cangilón (Tamaño y Tipo)**
Calculamos la capacidad *teórica* que debe tener cada cangilón para cumplir con el flujo, usando la fórmula de los apuntes:
$$
Cap_{teorica} = \frac{C \times t}{V_{faja} \times 60 \text{ min}}
$$
$$
Cap_{teorica} = \frac{933.33 \text{ pie}^3\text{/h} \times (16/12 \text{ pies})}{300 \text{ pies/min} \times 60 \text{ min/h}} = \frac{933.33 \times 1.333}{18000} = \mathbf{0.0691 \text{ pie}^3}
$$

Considerando un **coeficiente de llenado real del 75% ($0.75$)** para descarga centrífuga:
$$
Cap_{real\_requerida} = \frac{0.0691}{0.75} = \mathbf{0.0921 \text{ pie}^3}
$$

**Ir a Catálogo (Tabla II - Dimensiones de Cangilones Tipo "A"):**
Buscamos un cangilón que tenga una capacidad igual o ligeramente mayor a $0.0921 \text{ pie}^3$.
*   Seleccionamos el **Cangilón de $9" \times 6" \times 6 \ 1/4"$** (Largo $\times$ Ancho $\times$ Profundidad).
*   **Capacidad de tabla:** $\mathbf{0.11 \text{ pie}^3}$ (Cumple, pues es $> 0.0921$).
*   **Peso del cangilón vacío:** $\mathbf{6.1 \text{ libras}}$.

---

### **PASO 4: Recálculo de la Velocidad Real de la Faja ($V_R$)**
Con el cangilón seleccionado, recalculamos la velocidad exacta que necesita la faja:
$$
V_R = \frac{C}{\frac{\text{Cap. Tabla} \times \text{Llenado}}{t} \times 60}
$$
$$
V_R = \frac{933.33}{\frac{0.11 \times 0.75}{(16/12)} \times 60} = \frac{933.33}{0.061875 \times 60} = \mathbf{251.4 \text{ pies/minuto}}
$$

---

### **PASO 5: Poleas y Velocidad Crítica**
Diseñamos al $\approx 82\%$ de la velocidad crítica para asegurar una buena descarga centrífuga.
$$
V_{critica} = \frac{251.4}{0.82} = \mathbf{306.5 \text{ pies/min}}
$$

Revisando la **Tabla VII (Relaciones de Polea Superior)**, para acercarnos a una velocidad crítica de $315 \text{ pies/min}$, seleccionamos:
*   **Diámetro de Polea Superior ($D_{ps}$):** $\mathbf{24 \text{ pulgadas}}$.
*   **RPM de la Polea Superior ($N$):** $N = \frac{V_R}{\pi \times D_{ps}} = \frac{251.4}{\pi \times (24/12)} = \mathbf{40 \text{ RPM}}$.
*   **Diámetro de Polea Inferior ($D_{pi}$):** Usualmente es un 85% de la superior $\rightarrow 24" \times 0.85 = 20.4"$. Seleccionamos comercialmente **$20 \text{ pulgadas}$**.

---

### **PASO 6: Dimensiones de la Faja**
**Ancho de la faja ($a_f$):**
La faja debe ser más ancha que el largo del cangilón ($9"$) por un margen de $1"$ a cada lado.
$$
a_f = 9" + 2(1") = \mathbf{11 \text{ pulgadas de ancho}}
$$

**Longitud total de la faja ($L_{faja}$) y Número de Cangilones:**
$$
L_{faja} \approx 2H + \frac{\pi(D_{ps} + D_{pi})}{2}
$$
$$
L_{faja} \approx 2(64 \text{ pies}) + \frac{\pi(2 \text{ pies} + 1.667 \text{ pies})}{2} = 128 + 5.76 = \mathbf{133.76 \text{ pies}}
$$

*   $\text{N° Cangilones} = \frac{133.76 \text{ pies}}{1.333 \text{ pies (paso)}} = 100.3 \rightarrow$ **Se instalarán 100 cangilones en total.**

---

### **PASO 7: Cálculo de Tensiones y Selección del Motor (Potencia)**
Para hallar la potencia, calculamos la fuerza efectiva ($T_e$) que debe vencer el motor:

1.  **Peso de material en subida ($W_{mat}$):**
    $\text{Cangilones subiendo} = 100 / 2 = 50$.
    $\text{Peso de material por cangilón} = 0.11 \text{ pie}^3 \times 0.75 \times 48 \text{ lbs/pie}^3 = 3.96 \text{ lbs}$.
    $W_{mat} = 50 \times 3.96 = \mathbf{198 \text{ libras}}$.
2.  **Fuerza de excavación en la bota (carga):**
    Aproximado empírico: $F_{exc} \approx \mathbf{55 \text{ libras}}$.
3.  **Fricción de componentes (rodamiento/poleas):**
    Aproximadamente el $5\%$ del peso total en movimiento $\approx \mathbf{15 \text{ libras}}$.

**Fuerza efectiva total ($T_e$ o $\Delta T$):**
$$
T_e = 198 + 55 + 15 = \mathbf{268 \text{ libras}}
$$

**Potencia en el eje ($HP_{eje}$):**
$$
HP_{eje} = \frac{T_e \times V_R}{33000} = \frac{268 \text{ lbs} \times 251.4 \text{ pies/min}}{33000} = \mathbf{2.04 \text{ HP}}
$$

**Potencia del Motorreductor ($HP_{motor}$):**
Considerando una eficiencia de transmisión por cadena o faja y reductores ($\eta = 0.85$):
$$
HP_{motor} = \frac{2.04}{0.85} = \mathbf{2.4 \text{ HP}}
$$
*Se selecciona del catálogo un Motorreductor estándar de $\mathbf{3 \text{ HP}}$ acoplado para dar $40 \text{ RPM}$ de salida.*

---

### **PASO 8: Especificación de la Faja (Pliegues)**
Tensión Máxima del lado tenso ($T_1$) $\approx$ Peso faja + $W_{cangilones}$ vacíos (305 lbs) + $T_e$ (268 lbs) $\approx \mathbf{660 \text{ lbs}}$.
Tensión por pulgada de ancho (PIW) = $\frac{660 \text{ lbs}}{11 \text{ pulgadas}} = \mathbf{60 \text{ lbs/pulgada}}$.
De la **Tabla VIII (pág 9)**, una lona de $28 \text{ Onzas}$ resiste $27 \text{ lbs/pulgada por pliegue}$.
$\text{N° de pliegues} = \frac{60}{27} = 2.22 \rightarrow$ **Faja de 3 pliegues (Mínimo comercial).**

---

### **RESUMEN DEL DISEÑO (Respuesta Final Sugerida)**
1.  **Tipo:** Elevador de faja con descarga centrífuga.
2.  **Cangilones:** Tipo "A" normalizados de $9" \times 6" \times 6 \ 1/4"$. Cantidad: $100$ unidades.
3.  **Espaciamiento de cangilones:** $16 \text{ pulgadas}$.
4.  **Faja:** De lona/goma, $11 \text{ pulgadas}$ de ancho, $28 \text{ onzas}$, de $3 \text{ pliegues}$.
5.  **Velocidad de la faja:** $251.4 \text{ pies/minuto}$.
6.  **Poleas:** Polea superior motriz de $24"$ diámetro girando a $40 \text{ RPM}$. Polea inferior tensora de $20"$ diámetro.
7.  **Potencia:** Motorreductor eléctrico seleccionado de **$3 \text{ HP}$**. 

# Enunciado 2
Se trata del diseño completo de un **transportador de tornillo sin fin** para arena de fundición. 
### **DATOS DEL PROBLEMA**
*   **Material:** Arena de fundición.
*   **Peso específico ($W$):** $100 \text{ Libras/pie}^3$.
*   **Ángulo de reposo:** $39^\circ$ (Indica que es un material poco fluido y muy abrasivo).
*   **Distancia horizontal ($L$):** $18 \text{ metros}$.
*   **Capacidad ($Q$):** $20 \text{ Toneladas/hora}$.

**Conversiones previas necesarias:**
*   $1 \text{ pie}^3 = 0.028317 \text{ m}^3 \rightarrow W = \frac{100 \text{ lbs}}{0.028317 \text{ m}^3} \times 0.4536 \text{ kg/lb} = \mathbf{1601.8 \text{ kg/m}^3}$.
*   Capacidad en $\text{kg/hora} = 20 \text{ Ton/h} \times 1000 \text{ kg/Ton} = 20,000 \text{ kg/h}$.
*   Capacidad volumétrica ($C_{hora}$) $= \frac{20,000 \text{ kg/h}}{1601.8 \text{ kg/m}^3} = \mathbf{12.48 \text{ m}^3\text{/hora}}$.
*   Capacidad volumétrica ($C_{min}$) $= \frac{12.48}{60} = \mathbf{0.208 \text{ m}^3\text{/minuto}}$.

---

### **a.Calcular la potencia en el eje del tornillo sin fin**
Utilizamos la fórmula empírica del professor para hallar la potencia en **Caballos de Vapor (C.V.)**:
$$
P_{eje} = \frac{C \times L \times W_k \times F}{4500}
$$
Donde:
*   $C = 0.208 \text{ m}^3/\text{min}$
*   $L = 18 \text{ metros}$
*   $W_k = 1601.8 \text{ kg/m}^3$
*   $F$ = Factor de material. Para materiales pesados y muy abrasivos como la arena, los apuntes indican **$F = 1.4$**.

Reemplazando:
$$
P_{eje} = \frac{0.208 \times 18 \times 1601.8 \times 1.4}{4500} = \frac{8391.5}{4500} = \mathbf{1.86 \text{ C.V.}}
$$

---

### **b.Potencia del motor de accionamiento y seleccionarlo**
El profesor tiene una regla de diseño específica en sus apuntes (pág. 16 de su manuscrito): *"Como la potencia en el eje es menor que 2, tenemos que multiplicarlo por 2 para calcular la potencia del motor"*. 

1.  **Potencia calculada del motor:** $1.86 \text{ C.V.} \times 2 = \mathbf{3.72 \text{ C.V.}}$
2.  **Selección:** Se busca en el catálogo (ej. Delcrosa) la potencia comercial inmediata superior. Seleccionamos un **Motorreductor eléctrico de $4 \text{ HP}$**. (Para fines de diseño, lo asumimos con una salida típica de $60 \text{ RPM}$).

---

### **c.Seleccionar los componentes básicos**
La arena de fundición (altamente abrasiva y pesada) pertenece a la **Clase "d"** de los materiales. 
Entramos a la gráfica de **"MATERIALES DE LA CLASE d" (Pág. 15 de tu PDF 2)**:
*   Eje Horizontal (Capacidad): $12.5 \text{ m}^3\text{/hora}$.
*   Subimos hasta interceptar una curva de diámetro recomendada que esté debajo de la "velocidad máxima recomendada".
*   Cruzamos la curva del transportador de **$10" (25 \text{ cm})$**.
*   Proyectamos hacia la izquierda (Eje Y) y leemos la velocidad: **$N \approx 45 \text{ RPM}$**.

**Componentes seleccionados:**
*   **Diámetro de la hélice ($D$):** $10 \text{ pulgadas}$.
*   **Diámetro de la canaleta ($D_c$):** $11 \text{ pulgadas}$ ($D + 1"$).
*   **Paso de la hélice ($t$):** $10 \text{ pulgadas}$ (Paso estándar $= D$).
*   **Diámetro del eje hueco:** $2 \text{ pulgadas}$ (Tubo Schedule 40).
*   **Tramos y Soportes Colgantes:** La longitud es $18 \text{ m}$ ($59 \text{ pies}$). Utilizando tramos comerciales de $10 \text{ pies}$ ($3 \text{ m}$), requerimos **$6 \text{ tramos}$**. Por lo tanto, usaremos $6-1 =$ **$5 \text{ soportes colgantes}$** con cojinetes de bronce o fundición dura (resistentes a la abrasión).
*   **Chumaceras de rodamiento:** $2$ unidades (En las placas de los extremos).
*   **Chutes de carga y descarga:** Cuadrados de $11" \times 11"$.
*   **Tapa:** Plancha abisagrada o atornillada, calibre $14$. Soportes de pie cada $3 \text{ metros}$.

---

### **d.Hallar la velocidad de desplazamiento lineal del material**
Usamos la fórmula cinemática del transportador:
$$
V = \frac{t \times N}{60}
$$
Donde:
*   $t$ = paso en metros = $10 \text{ pulgadas} \times 0.0254 = 0.254 \text{ metros}$.
*   $N$ = RPM del eje del tornillo = $45 \text{ RPM}$ (Obtenido del gráfico de la Clase d).

$$
V = \frac{0.254 \text{ m} \times 45 \text{ RPM}}{60 \text{ s/min}} = \mathbf{0.1905 \text{ m/segundo}}
$$
*(Que también es equivalente a $\mathbf{11.43 \text{ metros/minuto}}$).*

---

### **e.Calcular la transmisión de accionamiento por cadena de rodillos**
Consideraremos que el motorreductor seleccionado tiene una salida de **$N_1 = 60 \text{ RPM}$** y necesitamos que el tornillo gire a **$N_2 = 45 \text{ RPM}$**.

1.  **Potencia de Diseño ($HP_d$):**
    $$
HP_d = HP_{motor} \times f_s
$$
    Para un transportador con carga moderada/pesada, el factor de servicio es $f_s = 1.3$.
    $$
HP_d = 4 \text{ HP} \times 1.3 = \mathbf{5.2 \text{ HP}}
$$
2.  **Relación de transmisión ($i$):**
    $$
i = \frac{N_1}{N_2} = \frac{60}{45} = \mathbf{1.333}
$$
3.  **Número de dientes:**
    *   Asumimos para el **Piñón ($Z_1$)** del motorreductor: **$21 \text{ dientes}$**.
    *   Para la **Catalina ($Z_2$)** del tornillo: $Z_2 = Z_1 \times i = 21 \times 1.333 = 28$. **Catalina de $28 \text{ dientes}$**.
4.  **Selección de la cadena:**
    Con $5.2 \text{ HP}$ y el piñón a $60 \text{ RPM}$, entrando a tablas de cadenas (ANSI), se recomienda una **Cadena Simple ASA 60-1** (Paso $P = 3/4" = 0.75"$).
5.  **Distancia entre centros y pasos ($L_p$):**
    Se asume una distancia entre centros preliminar de $C_p = 30 \text{ pasos}$.
    La longitud aproximada en pasos de la cadena será:
    $$
L_p \approx 2C_p + \frac{Z_1 + Z_2}{2} = 2(30) + \frac{21 + 28}{2} = 60 + 24.5 = \mathbf{84.5 \text{ pasos}}
$$
    Se toma un número par: **$84 pasos de cadena**

e $1 \text{ a } 2 \text{ HP}$ y $40$-$60 \text{ RPM}$ siempre usa cadena **ASA 50-1 o ASA 60-1**, y para potencias de $4 \text{ a } 8 \text{ HP}$ usa **ASA 80-1 o ASA 100-1**).
# Silo 1
## **1. DATOS INICIALES Y DE MATERIAL**
De la tabla de materiales (Ítem No. 3):
*   **Material:** Avena
*   **Capacidad de la planta ($Q$):** $30 \text{ Toneladas cortas/hora}$
*   **Peso específico ($\gamma$):** $26 \text{ lbs/pie}^3$
*   **Tiempo de almacenamiento (Silo 1):** $8 \text{ horas}$

**Gravedad específica relativa ($Ge$):**
El manual API requiere comparar la densidad con la del agua ($62.4 \text{ lbs/pie}^3$).
$$
Ge = \frac{26 \text{ lbs/pie}^3}{62.4 \text{ lbs/pie}^3} = 0.416
$$
*(Nota: Según la Norma API 650 (Pág. 31), el factor $G$ para el cálculo de espesores de tanques **en ningún caso debe ser menor a 1.0** por motivos de seguridad y pruebas hidrostáticas. Por lo tanto, usaremos $Ge = 1.0$).*
## **2. CÁLCULO DEL VOLUMEN DE DISEÑO**
1.  **Capacidad Másica total a almacenar:**
$$
M = 30 \text{ Ton cortas/h} \times 2000 \text{ lbs/Ton} \times 8 \text{ horas} = \mathbf{480,000 \text{ lbs}}
$$
2.  **Volumen real del material ($V_m$):**
$$
V_m = \frac{480,000 \text{ lbs}}{26 \text{ lbs/pie}^3} = \mathbf{18,461.54 \text{ pies}^3}
$$
## **3. DIMENSIONAMIENTO DEL SILO (Diámetro y Altura)**
Para optimizar costos en tanques de producción con techo cónico, el profesor recomienda una relación donde el Diámetro es igual a la Altura del cilindro ($D = H$). 

Para asegurar el volumen y dejar un margen de soeguridad (espacio libre o *ullage*), probaremos con dimensiones de números enteros múltiplos de las planchas estándar ($5 \text{ pies} \times 10 \text{ pies}$):
*   **Asumimos Diámetro ($D$):** $\mathbf{30 \text{ pies}}$
*   **Asumimos Altura del Casco ($H$):** $\mathbf{30 \text{ pies}}$ (Construido por 6 anillos de 5 pies de altura cada uno).

**Verificación del Volumen Cilíndrico ($V_{cil}$):**
$$
V_{cil} = \frac{\pi \cdot D^2}{4} \cdot H = \frac{\pi \cdot (30)^2}{4} \cdot 30 = \mathbf{21,205.7 \text{ pies}^3}
$$
*(El volumen del cilindro por sí solo ya es mayor a los $18,461.54 \text{ pies}^3$ requeridos. El volumen adicional aportado por la tolva de fondo cónico servirá como factor de seguridad perfecto).*
## **4. CÁLCULO DE ESPESORES DEL CASCO (Norma API 650)**
Utilizamos la fórmula del manual (Pág. 31) para acero al carbono con eficiencia de soldadura del 85% ($n = 0.85$ radiografiado por zonas) y un margen de corrosión de $1/16" (0.0625")$:
$$
t = \frac{2.6 \times D \times (H - 1) \times Ge}{n \times 21,000} + 0.0625"
$$

**Para el 1er Anillo (El más bajo y sometido a más presión, $H = 30'$):**
$$
t_1 = \frac{2.6 \times 30 \times (30 - 1) \times 1.0}{0.85 \times 21,000} + 0.0625" = \frac{2262}{17850} + 0.0625"
$$
$$
t_1 = 0.1267" + 0.0625" = \mathbf{0.1892"}
$$
*   *Condición API:* Para $D < 50'$, el espesor mínimo es $3/16"$ ($0.1875"$).
*   Como $0.1892" > 0.1875"$, debemos usar el espesor comercial inmediato superior.
*   **Selección Anillo 1:** Planchas de $\mathbf{1/4" \ (0.25")}$.

**Para el 2do Anillo ($H = 25'$):**
$$
t_2 = \frac{2.6 \times 30 \times (25 - 1) \times 1.0}{17850} + 0.0625" = 0.1048" + 0.0625" = \mathbf{0.1673"}
$$
*   Como $0.1673"$ es menor al mínimo de la norma, usamos el mínimo exigido.
*   **Selección Anillos 2 al 6:** Planchas de $\mathbf{3/16"}$.
## **5. CANTIDAD DE PLANCHAS REQUERIDAS (Usando planchas de 5' x 10')**

**A. Para el Casco (Cilindro):**
*   Longitud de circunferencia ($L_c$) $= \pi \times D = \pi \times 30 = 94.25 \text{ pies}$.
*   Número de planchas por anillo $= \frac{94.25}{10 \text{ pies de largo}} = 9.42 \rightarrow \mathbf{10 \text{ planchas / anillo}}$.
*   **Anillo 1:** $10 \text{ planchas}$ de $1/4" \times 5' \times 10'$.
*   **Anillos 2, 3, 4, 5, 6:** $50 \text{ planchas}$ de $3/16" \times 5' \times 10'$.

**B. Para el Techo Cónico:**
*   Asumimos una pendiente de $30^\circ$. Radio $R = 15'$.
*   Generatriz ($L_g$) $= \frac{15}{\cos(30^\circ)} = 17.32 \text{ pies}$.
*   Área del techo $= \pi \times R \times L_g = \pi \times 15 \times 17.32 = 816 \text{ pies}^2$.
*   Número de planchas $= \frac{816 \text{ pies}^2}{50 \text{ pies}^2/\text{plancha}} = 16.32 \rightarrow \mathbf{17 \text{ planchas}}$ de $3/16" \times 5' \times 10'$.

**C. Para el Fondo (Tolva Cónica para descarga de Avena):**
*   Asumimos un ángulo de caída de $45^\circ$ (necesario para el flujo de la avena).
*   Generatriz ($L_{g\_fondo}$) $= \frac{15}{\cos(45^\circ)} = 21.21 \text{ pies}$.
*   Área de la tolva $= \pi \times 15 \times 21.21 = 999.5 \text{ pies}^2$.
*   Número de planchas $= \frac{999.5}{50} = 19.99 \rightarrow \mathbf{20 \text{ planchas}}$ de $1/4" \times 5' \times 10'$ (usamos $1/4"$ por soportar el peso dinámico del grano).
## **6. ANILLO DE RIGIDEZ (Módulo de Sección)**
La fórmula de la norma para tanques indica:
$$
Z = 0.0001 \times D^2 \times H \ (\text{pulgadas}^3)
$$
$$
Z = 0.0001 \times (30)^2 \times 30 = 0.0001 \times 900 \times 30 = \mathbf{2.70 \text{ pulg}^3}
$$
Se debe seleccionar del catálogo de perfiles (SiderPerú/Gramil) un Perfil Angular o Canal que posea un módulo de sección $Z \ge 2.70 \text{ pulg}^3$.
## **7. METRADO DE MATERIALES Y COSTOS**
Calculamos el peso de acero estructural (Peso Específico Acero $\approx 490 \text{ lbs/pie}^3$).
Volumen de 1 plancha de $1/4" = 5 \times 10 \times (0.25/12) = 1.041 \text{ pies}^3 \rightarrow \text{Peso} = \mathbf{510 \text{ lbs}}$.
Volumen de 1 plancha de $3/16" = 5 \times 10 \times (0.1875/12) = 0.781 \text{ pies}^3 \rightarrow \text{Peso} = \mathbf{383 \text{ lbs}}$.

*   **Casco Anillo 1:** $10 \times 510 \text{ lbs} = 5,100 \text{ lbs}$
*   **Casco Anillos 2-6:** $50 \times 383 \text{ lbs} = 19,150 \text{ lbs}$
*   **Techo cónico:** $17 \times 383 \text{ lbs} = 6,511 \text{ lbs}$
*   **Fondo cónico (Tolva):** $20 \times 510 \text{ lbs} = 10,200 \text{ lbs}$
*   **PESO TOTAL DEL SILO:** $40,961 \text{ lbs} \times 0.4536 \text{ kg/lb} = \mathbf{18,580 \text{ kg}}$.

**Cálculo de Costos (Criterio del Profesor):**
*   **Costo de planchas de acero ($C_{planchas}$):** $18,580 \text{ kg} \times \$2.00\text{/kg} = \mathbf{\$37,160}$
*   **Costo de electrodos ($C_{elect}$):** Se asume 3% del peso $\rightarrow 557.4 \text{ kg} \times \$3.50\text{/kg} = \mathbf{\$1,951}$
*   **Costo Total de Materiales ($C_M$):** $37,160 + 1,951 = \mathbf{\$39,111}$
*   **Gastos de Logística y Mano de Obra ($60\% \ C_M$):** $0.60 \times 39,111 = \mathbf{\$23,467}$
*   **Ganancia por Fabricación ($25\% \ C_M$):** $0.25 \times 39,111 = \mathbf{\$9,778}$

**COSTO TOTAL DEL SILO DE 8 HORAS:**
$$
C_{TOTAL} = 39,111 + 23,467 + 9,778 = \mathbf{\$72,356 \ USD}
$$
# Silo 2

## **1. DATOS INICIALES Y DE MATERIAL**
*   **Material:** Avena
*   **Capacidad de la planta ($Q$):** $30 \text{ Toneladas cortas/hora}$
*   **Peso específico ($\gamma$):** $26 \text{ lbs/pie}^3$
*   **Tiempo de almacenamiento (Silo 2):** $6 \text{ horas}$
*   **Gravedad específica de cálculo ($Ge$):** Aunque la avena es ligera, por Norma API 650 el $Ge$ **mínimo a usar es $1.0$** (condición de prueba con agua).

## **2. CÁLCULO DEL VOLUMEN DE DISEÑO**
1.  **Capacidad Másica total a almacenar:**
    $$
M = 30 \text{ Ton cortas/h} \times 2000 \text{ lbs/Ton} \times 6 \text{ horas} = \mathbf{360,000 \text{ lbs}}
$$
2.  **Volumen real del material ($V_m$):**
    $$
V_m = \frac{360,000 \text{ lbs}}{26 \text{ lbs/pie}^3} = \mathbf{13,846.15 \text{ pies}^3}
$$
## **3. DIMENSIONAMIENTO DEL SILO (Diámetro y Altura)**
Buscamos dimensiones donde $D \approx H$, que utilicen planchas comerciales ($5' \times 10'$). 
*   **Asumimos Diámetro ($D$):** $\mathbf{27 \text{ pies}}$
*   **Asumimos Altura del Casco ($H$):** $\mathbf{25 \text{ pies}}$ (Construido exactamente por 5 anillos de 5 pies de altura).

**Verificación del Volumen Cilíndrico ($V_{cil}$):**
$$
V_{cil} = \frac{\pi \cdot D^2}{4} \cdot H = \frac{\pi \cdot (27)^2}{4} \cdot 25 = \mathbf{14,313.8 \text{ pies}^3}
$$
*(Como $14,313.8 > 13,846.15$, el volumen cumple perfectamente con la capacidad requerida y deja el espacio libre necesario).*
## **4. CÁLCULO DE ESPESORES DEL CASCO (Norma API 650)**
Usamos la fórmula del manual con $n = 0.85$ y margen de corrosión de $0.0625"$:
$$
t = \frac{2.6 \times D \times (H - 1) \times Ge}{n \times 21,000} + 0.0625"
$$

**Para el 1er Anillo (El más bajo, $H = 25'$):**
$$
t_1 = \frac{2.6 \times 27 \times (25 - 1) \times 1.0}{0.85 \times 21,000} + 0.0625" = \frac{1684.8}{17850} + 0.0625"
$$
$$
t_1 = 0.0944" + 0.0625" = \mathbf{0.1569"}
$$

*   **Regla de la Norma API:** Para diámetros menores a 50 pies, **el espesor mínimo permitido es $3/16"$ ($0.1875"$).**
*   Como nuestro cálculo arroja $0.1569"$, manda la norma.
*   **Selección para TODOS los anillos (1 al 5):** Planchas de $\mathbf{3/16"}$.
## **5. CANTIDAD DE PLANCHAS REQUERIDAS (Usando planchas de 5' x 10')**

**A. Para el Casco (Cilindro):**
*   Longitud de circunferencia $= \pi \times 27' = 84.82 \text{ pies}$.
*   Planchas por anillo $= \frac{84.82}{10} = 8.48 \rightarrow \mathbf{9 \text{ planchas / anillo}}$.
*   Total en el Casco ($5 \text{ anillos}$) $= 9 \times 5 = \mathbf{45 \text{ planchas}}$ de $3/16" \times 5' \times 10'$.

**B. Para el Techo Cónico:**
*   Asumiendo pendiente de $30^\circ$, Radio $R = 13.5'$.
*   Generatriz ($L_g$) $= \frac{13.5}{\cos(30^\circ)} = 15.59 \text{ pies}$.
*   Área $= \pi \times 13.5 \times 15.59 = 661.2 \text{ pies}^2$.
*   Número de planchas $= \frac{661.2}{50} = 13.22 \rightarrow \mathbf{14 \text{ planchas}}$ de $3/16" \times 5' \times 10'$.

**C. Para el Fondo (Tolva Cónica para descarga):**
*   Ángulo de caída de $45^\circ$ para facilitar la salida de la avena.
*   Generatriz ($L_g$) $= \frac{13.5}{\cos(45^\circ)} = 19.09 \text{ pies}$.
*   Área $= \pi \times 13.5 \times 19.09 = 809.6 \text{ pies}^2$.
*   Número de planchas $= \frac{809.6}{50} = 16.19 \rightarrow \mathbf{17 \text{ planchas}}$. Usaremos espesor de $\mathbf{1/4"}$ por impacto de descarga.
## **6. ANILLO DE RIGIDEZ (Módulo de Sección)**
$$
Z = 0.0001 \times D^2 \times H = 0.0001 \times (27)^2 \times 25 = \mathbf{1.82 \text{ pulg}^3}
$$
Se selecciona un perfil angular cuyo módulo de rigidez supere este valor para colocar en el borde superior del silo.
## **7. METRADO DE MATERIALES Y COSTOS**
Pesos comerciales de las planchas:
*   Plancha $1/4" \approx \mathbf{510 \text{ lbs}}$.
*   Plancha $3/16" \approx \mathbf{383 \text{ lbs}}$.

**Metrado de peso:**
*   **Casco:** $45 \text{ planchas} \times 383 \text{ lbs} = 17,235 \text{ lbs}$.
*   **Techo:** $14 \text{ planchas} \times 383 \text{ lbs} = 5,362 \text{ lbs}$.
*   **Fondo:** $17 \text{ planchas} \times 510 \text{ lbs} = 8,670 \text{ lbs}$.
*   **PESO TOTAL DEL SILO No. 2:** $31,267 \text{ lbs} \times 0.4536 \text{ kg/lb} = \mathbf{14,182 \text{ kg}}$.

**Cálculo de Costos:**
*   **Costo de planchas ($C_{planchas}$):** $14,182 \text{ kg} \times \$2.00\text{/kg} = \mathbf{\$28,364}$
*   **Costo de electrodos ($C_{elect}$):** $3\%$ del peso $\rightarrow 425.5 \text{ kg} \times \$3.50\text{/kg} = \mathbf{\$1,489}$
*   **Costo Total de Materiales ($C_M$):** $28,364 + 1,489 = \mathbf{\$29,853}$
*   **Gastos de Logística y Mano de Obra ($60\% \ C_M$):** $0.60 \times 29,853 = \mathbf{\$17,912}$
*   **Ganancia por Fabricación ($25\% \ C_M$):** $0.25 \times 29,853 = \mathbf{\$7,463}$

**COSTO TOTAL DEL SILO DE 6 HORAS:**
$$
C_{TOTAL} = 29,853 + 17,912 + 7,463 = \mathbf{\$55,228 \ USD}
$$

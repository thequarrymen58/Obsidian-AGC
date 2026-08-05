Se simulara un cilindro solida y posteriormente hueco de 38.1 de diametro, con una fuerza aplicada de 5kN para ambos casos, el cual sera aplicado a lo largo del cilindro.
# Elemento Solido
1. Asigancion de materiales
   Se utilizaran datos para ASTM A36
   ![[Pasted image 20260220210810.png|425]]
2. Mallado
   Por defecto se tiene
   ![[Pasted image 20260220175226.png|325]]
   - Quality
     Tenemos un avg de 80%, lo cual esta en el rango aceptable
   ![[Pasted image 20260220175308.png]]
   - Skewness
     Sin embargo tenemos que las barras se van a 0.5, cuando lo ideal es lo aproximado a 0 para garantizar una malla con elementos equilateros o equiangulares, y 1 nos dice que se tiene un mallado de calidad baja.
     *Segun Meshing USer Guide 2025 p.151*
     ![[Pasted image 20260220175846.png|400]]
     Se tiene en el nuestro se encuentra dentro de 0.3-0.4, lo cual dice que es buena, pero puede ser mejor.
   ![[Pasted image 20260220175330.png|500]]
   Para el mallado de un cilindro, se encontro el metodo O-Grid, el cual conciste en hacer un cuadrado al centro y formar capas al rededor de esta.
   [O-Grid Method](https://ansys13.ansys.com/KnowledgeArticles/Phase-2B/2056156/2056156.pdf)
   El cual se puede lograr tambien usando ICEM
   [ICEM-CFD Structured Meshing of a Cylinder 3D | Hexahedral Meshing ](https://www.youtube.com/watch?v=B7BdQnuutnQ)
   Luego de seguir los pasos, para la aplicacion de Static structural, se obtiene un numero de nodos y elementos mucho mayor, asi como la calidad de los elementos en promedio es pobre.
   ![[Pasted image 20260220225250.png|337]]
   (Sin embargo si se aplica inflation en los bordes, esta semejora, pero seria ideal para CFD ya que describiria mejor la capa limite de un fluido)
   **Se hara una variacion, de la siguiente manera.**
   Esto se hara usando metodo hexaedro y face meshing.
   Mesh, insert, Method, Multizone.
   Cambiando tambien Surface Mesh Method a Uniforme
   ![[Pasted image 20260220194323.png]]
   Luego Mesh, insert, Face Meshing.
   Se seleccionan ambas caras.
   ![[Pasted image 20260220194507.png]]
   Obteniendo
   ![[Pasted image 20260220194446.png|350]]
   La cual es una malla estructurada, veamos el skewness, donde se aprecia una mejor calidad segun la distribucion.
   ![[Pasted image 20260220194603.png|500]]
   Si vamos a Method, y colocamos prism, obtenemos mejores resultados para la calidad y el skewness, sin embargo aumenta el numero de elementos pero se reduce el numero de nodos.
   ![[Pasted image 20260220210639.png|350]]
   Como se aprecia, el minimo es mayor con prism, (0.66 vs 0.86)
   ![[Pasted image 20260220204000.png|525]]
   Luego en skewness se aprecia que con el metodo de prismas o wedges, la distribucion se vuelve parecida a una normal, a diferencia de la conseguida con los hexaedros, asi mismo, el numero de elementos bajo 0.2 es mayor con prismas, por ello se usara este metodo para la simulacion.
   ![[Pasted image 20260220204021.png]]
3. Configuracion Estructural
   Se añadira:
   - Gravedad Estandar de la tierra: -9.81 en el eje Y
   - Fixed Support: En una cara
   - Displacement: EN la cara opuesta a Fixed Support, con dos grados de libertad, excepto el eje Y=0.
   - Force: Como debe ser analogo al caso de un hexaedro o caja, donde la fuerza es aplicada en la cara superior, entonces en DesignModeller, se dividio la cara superior e  inferior, para ello.
     - Se partio el borde de una cara en 2, con split edges, fractional 0.5.
     - Se extruyo el borde superior seleccionando imprint faces.
     - Finalmente se tiene.
       ![[Pasted image 20260227164015.png|239]]
     Luego al aplicar la fuerza, selecionamos la cara superior y se aplicara la fuerza con componente Y=-5000N.
     ![[Pasted image 20260227164256.png|375]]
4. Solucion
   - Deformacion Total
     ![[Pasted image 20260227165601.png|475]]
   - Stress Equivalente (Von Misses)
     ![[Pasted image 20260227165553.png|475]]
   - Factor de Seguridad
     ![[Pasted image 20260227165642.png|475]]
# Elemento Linea - Estructural
1. Geometria - Cross Section
   Como no se especifico el diametro interno, se selecciono uno de 20mm, es decir se tiene un radio mayor de 19.05mm y un menor de 10mm.
   Luego se genera el elemento linea de 1000mm, y se seleciona la seccion.
   ![[Pasted image 20260227171127.png|228]]
2. Mallado
   Como es un elemento lineal, se mallara con 10mm
   ![[Pasted image 20260227171915.png|375]]
3. Configuracion Estructural
   La configuracion es analoga a la anterior, salvo que todo se aplicara en el elemento linea.
   ![[Pasted image 20260227172056.png|525]]
4. Solucion
   - Deformacion Total
     ![[Pasted image 20260227172244.png|475]]
   - Stress Combinado maximo
     ![[Pasted image 20260306181911.png|475]]
   - Diagrama de momento y corte
     ![[Pasted image 20260306182027.png|550]]
     
# Diferencias
Primero se tienen los resultados de la deformacion total.
- **Elemento Solido:** 1.2742 mm.
- **Elemento Linea (hueco):** 1.3879 mm.
El elemento linea como era de esperarse tiende a deformarse mas debido a que el material del centro es ausente lo cual hace que su momento de inercia sea menor, haciendolo un poco mas flexible ante la carga.
Tambien se tiene
Con respecto a los resultados de maximo stress.
- **Elemento Solido:** 122.09 MPa.
- **Elemento Linea (hueco):** 126.20 MPa.
A pesar de que en el elemento solido la fuerza se aplica en casi la mitad de la cara, la tuberia hueca tiene menos material para resistir la fuerza distribuida, por lo cual las caras exteriores de la seccion podria experimentar un mayor esfuerzo.

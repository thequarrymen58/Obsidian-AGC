# Teoria 
Los parametros mas importantes que se deben de cambiar
## Modulo de Young (E)
Nos da la rigidez de un material, si el E, es alto el material sera dificil de deformarse o es muy rigido

E=sigma/epsilon
### Ley de Hooke generalizada
Es la misma ley que el F=Kx, pero de manera que utiliza poisson y young para describir los esfuerzos (sigma) y las deformaciones (epsilon) en todas las direcciones

## Coeficiente de Poisson (V)
Es la deformacion lateral, es decir cuando se estira un material se adelgaza y cuando se comprime se ensancha
Nos dice la realcion entre las deformaciones (epsilon)
V=- (deformacion transversal) / (deformacion longitudinal)
El menos es solo para que el resultado al final quede con signo positivo
## Tensile Yield strenght
O limite elastico o fluencia, nos dice cual es el limite para que la deformacion sea permamnete, antes de eso es la zona elastica, donde todavia manda el modulo de young, es decir se le puede aplicar una fuerza y el material volvera a su estado original.
Lo usamos para calcular el factor de seguridad
- ANSYS SEGUIRA CALCULANDO, quiere decir que no nos dira si el material se deforma, si sobrepasa el limite igual lo mostrara. 
## Tensile Ultimate Strength
Luego de pasar este umbral, el material falla estrepitosamente rompiendose.

***Ahora tenemos los tipos de analisis que se pueden hacer.***

## Analisis de stress equivalente (Von Misses)
Cuando nuestro material sufre deformaciones por muchos lados simultaneamentem este analisis nos dice si nuestra pieza va a fallar o no.

Lo que hace es facilitar y juntar todas las deformaciones que sufre un material en las 3 dimenciones en una sola, por ejemplo si tenemos un cubo, este se puede estirar en x, comprimir en y, finalmente retorcerse en el eje z. 
Todo esto para poder compararlo con el Yield Stranght.
Es bueno para metales, pero no para concreto (rankine) o madera (fibras).

Se mide en Pa, 
## Factor de Seguridad
FOS=(Yield Strenght Experimental) / (Von Misses Teorico)
Von misses es lo que se obtiene por modelos matematicos de ansys, mientras que el experimental es el Yield, que se obtiene por ensayos de laboratorio.

## Cuando aplicar una fuerza y cuando una presion
Una fuerza se aplica cuando no necesariamente esta actua perpendicular a la superficie, mientras que la presion siempre actuara de manera perpendicular a la superficie, pensemos en que la nieve que esta pegada al techo de una casa, esta presiona sobre el techo, pero no de manera normal, sino perpendicular a la gravedad.
![[Pasted image 20260306160448.png|241]]

## Tipos de metal
- ASTM A36
  Acero al carbono
  Limite Elastico 250MPa = 36 000 psi
- ASTM A572
  Acero de alta resistencia
  Limite elastico 345 MPa = 50 000
- ASTM A992
  Vigas en forma de I o H
  Limite 345 MPa
- AISI 304
  bastante comun, inoxidable
- Titanio 4
  800 N???????
# Factor de seguridad
FS=IDEAL/REAL
![[Pasted image 20260217212547.png|405]]
# Elementos Finitos
![[Pasted image 20260217194338.png|375]]
El rango de fallo puede ser del 2%, es aceptable.
# Analisis estatico estructural estatico de pieza monosolida 
Se hace en sistemas en reposo, no hay aceleracion, velocidad constante
![[Pasted image 20260217195213.png|300]]
- Que es estructural elastico
  Que el factor de seguridad de todos los materiales es mayor a 1.
- Pieza mono solida
  Es solo una pieza
![[Pasted image 20260217200200.png]]
- Isotropico
  Todas las variables son iguales.
- Ortotropico
   Las propiedades no son iguales entre si, la resistencia de un eje es diferente a la de otra.
Lo que necesitamos para hacer el analisis, solo es necesario el modulo de young y el de poisson.
![[Pasted image 20260217201302.png|450]]
## Actividad 1

Se simulara un cilindro solida y posteriormente hueco de 38.1 de diametro, con una fuerza aplicada de 5kN para ambos casos, el cual sera aplicado a lo largo del cilindro.
### Elemento Solido
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
### Elemento Linea - Estructural
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
     
   

Para el mallado de la tuberia hueca se usara la siguiente tecnica
[How to mesh in ANSYS Meshing-Pipe, Cylinder](https://www.youtube.com/watch?v=1G5JuHues2I)
   
## Actividad 2
Se pide una simulacion estatica a un desatornillador plano.
1. Materiales
   Se usara el Structural Steel por defecto para la punta, pero el mango sera de HDPE, asi que se añadira Polyethylene usando la libreria.
2. Geometria
  ![[Pasted image 20260228142520.png|300]]
3. Mallado
   Se comenzara por un malla de 5mm, de donde se obtiene
   ![[Pasted image 20260228142820.png|350]]
   Con una calidad promedio de solo 54%, y un skewness en donde la distribucion se aprecia que esta pegada hacia la unidad, ambos son indicadores de que la calidad de la malla es mala
   ![[Pasted image 20260228142928.png|525]]
   Por ello se probara disminuyendo el tamaño a la malla global, la cual sera de 1mm, donde se obtiene.
   ![[Pasted image 20260228143201.png|350]]
   Del analisis de calidad se consiguio un promedio del 68%, mientras que se obtuvo un skewness, con pocos elementos pegados a la unidad, y mas al medio, aun no se puede considerar como buena.
   ![[Pasted image 20260228143259.png|525]]
   Se aprecia tambien, que la mayoria de problemas viene de la punta y de los anillos que conforman el mango, pero antes de esta hay una seccion uniforme, pero al ser un solo cuerpo no se puede aplicar un metodo, por lo que se partira este cuerpo en spaceclaim, para ello:
   - Se crearan dos planos normales a los extremos de la seccion uniforme
   - Se usara la herramienta Split Body, y cortar usando los planos
   - Finalmente, en la rama de los componentes, se cambiara el Share Topology a Merge, esto para que a pesar de que esten separados, Ansys los tome como un solo elemento, y asi las caras puedan unir sus nodos.
     ![[Pasted image 20260303115551.png|350]]
   Luego de ello, se aplicara.
   - En la punta, Body Sizing = 0.5mm
   - En la parte uniforme, Body Sizing = 1mm y Multizone = Hexa
   - En el mango, Body Sizing = 1mm
   - En los aros del mango, Face Sizing = 0.5mm
     ![[Pasted image 20260303121230.png|200]]
   Finalmente se tiene:
   ![[Pasted image 20260303121350.png|375]]
   Donde se consigue una calidad del 83%,  un skewness, con la mayoria de elementos por debajo de 0.5, ambas metricas son muy positivas para el mallado.
   ![[Pasted image 20260303121840.png|457]]
   ![[Pasted image 20260303121518.png|525]]
4. Configuracion Estructural
   - Se aplicara gravedad standar de la tierra.
   - Soporte fijo en las caras del mango.
   - Momento de 50 N.mm, en ambas caras de la punta, con respecto al eje X.  
5. Solucion
   - Total Deformation
     Se aprecia una deformacion de solo 0.017mm, tiene sentido debido a la fuerza de 50.Nmm, la cual no es de tanta magnitud consdierando el material que se uso. 
     ![[Pasted image 20260303122838.png|600]]
   - Equivalent Stress
     ![[Pasted image 20260303122936.png|600]]
     Como se aprecia, se obtiene un stress maximo de 27.6 MPa, lo cual es pequeña para la resistencia del acero que se usa para esa parte (250 MPa), pero justo en la union donde el mallado cambia de metodo de hexagonal a tetrahedrico se da la deformacion maxima, lo cual puede que no sea tan preciso debido al tipo de mallado. 
     ![[Pasted image 20260303123937.png|450]]
   - Safety Factor
     Se obtiene un factor de seguridad minimo de 9, lo cual, para la fuerza aplicada, es mas que aceptable. 
     ![[Pasted image 20260303123010.png|600]]
  6. Caso sin Mango.
     Para este caso ya no se usara el mango, esto se puede lograr facilmente, solo suprimiendo el mango desde el editor de geometria, para lo cual solo se duplicara el analisis anterior y se haran las modificaciones.
     - Total Deformation
       En comparacion, en el anterior caso so obtuvo 0.017 vs 0.011 actual, esto puede deberse a que solo se uso un solo material, el cual es mas fuerte que el polietileno, por lo cual, presento menos deformacion. 
       ![[Pasted image 20260303132538.png|575]]
     - Equivalent Stress
       Este resultado es practicamente identico, 27.6 vs 27.7.
       ![[Pasted image 20260303132617.png|575]]
     - Safety Factor
       En este apartado no se aprecio cambio.
       ![[Pasted image 20260303132642.png|575]]

## Actividad 3

Se obtienen errores, al parecer la fuerza aplicada es tanta que el material se contrae hacia adentro y se deforma de tal manera que el solver no sabe que hacer y crashea, pero antes de ello muestra hasta donde llego en el calculo.
Solo llega hasta **0.988 seconds**, y crashea, el ultimo reporte muestra el calculo hasta una fuerza de solo 6.91 MPa.
Sin embargo este resultado fue con una malla detallada, se regresara  los 35mm, solo con face meshing, y cambiando a 6 cores (Pcores vs Ecores)
![[Pasted image 20260303162850.png]]
Luego de pruebas similares, se observa tambien que, a medida que se refina la malla, la solucion no converge aun asi cambiando a una menor presion, los 35mm dados para comenzar si dan resultados, pero a costa de presicion, entonces se aprecia que un mallado menos detallado "ayuda" a que el material sea mas resistente.

Finalmente se probara con 6.95 MPa de presion, debido a que fue la unica que mostro resultados, y fue la mas cercana antes de no llegar a la convergencia.

1. Mallado
   Se dio un mallado global de 25 mm, a su vez se aplico un face meshing para ordenar los elementos de esta cara, sin embargo no se aplico un face sizing por que eso hace que el mallado global tambien deba de reducirse debido al alargamiento de los elementos, asi como tambien el tiempo de simulacion se eleva, ademas de que a veces no converge por la misma carga.
   ![[Pasted image 20260306172122.png|475]]
   La calidad del elemento es de 1, y el skewness se mantiene en 0, se podria decir que es una malla perfecta.
   ![[Pasted image 20260306172447.png|318]]
   ![[Pasted image 20260306172502.png|500]]
   Sin embargo hay zonas, como en la cara lateral, donde la distribucion de nodos no es la suficiente para ayudar a los nodos donde se produce singularidad, la cual tambien ocurre en los bordes interiores donde se debio aplicar un chanfer, pero estos detalles no se agregaron debido a que como ya se menciono, el tamaño de la malla tendria que disminuir.
   ![[Pasted image 20260306172734.png|221]]
2. Configuracion Estructural
   ![[Pasted image 20260306173103.png|475]]
3. Solucion
   - Deformacion Total
     La animacion se puede encontrar [aqui](https://drive.google.com/file/d/1pcZIq2K2OUImcYNr_s9os_YiV27OKHmM/view?usp=sharing).
     En el momento de mayor carga se tiene
     ![[Pasted image 20260306173608.png|575]]
     ![[Pasted image 20260306174133.png|575]]
     En el momento donde toda la carga se retira se tiene
     ![[Pasted image 20260306180909.png|575]]
     ![[Pasted image 20260306180931.png|575]]
     Aqui se ve como el material no regresa a su estado original, sino mas bien se mantiene con una deformacion de 195mm, lo cual quiere decir que se deformo permanentemente. 
   - Stress Equivalente
     Se tiene un stress maximo de 427MPa, para un material que resiste 250MPa se puede ver claramente por que se deformo irreversiblemente.
     ![[Pasted image 20260306173652.png|575]]
     ![[Pasted image 20260306174036.png|575]]
   - Strain Total equivalente
     ![[Pasted image 20260306173802.png|575]]
     ![[Pasted image 20260306174223.png|272]]
   - Analisis de Nodos
     Se crearan 6 nodos.
     ![[Pasted image 20260306174514.png|550]]
     Para el primer nodo, se aprecia que segun la grafica, y como era de esperarse, en esa zona ya el material sufrio una deformacion permanente.
     ![[Pasted image 20260306175016.png|575]]
     Analisemos ahora, un punto mas alejado, el nodo 4, cunple hasta cierta parte pero de igual manera, aun esta sufriendo un deformacion plastica.
     ![[Pasted image 20260306175403.png|575]]
     En el nodo 6 se tiene la grafica que se considera adecuada, pues describe un comportamiento elastico, seria adecuado.
     ![[Pasted image 20260306175511.png|575]]
      Entonces la zona anterior a esta es donde se debe de cortar el material, el cual se encuentra a 900mm, desde el origen, lo cual es casi la mitad del material.
## Examen Final
### Lineal - Aro de rueda
Los resultados varian con respecto al tamaño de malla seleccionado, segun [estudio](https://pdf.sciencedirectassets.com/314029/1-s2.0-S2452321621X00042/1-s2.0-S2452321621001013/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLWVhc3QtMSJIMEYCIQC2eOxZ22q33NZ1PbNgQL1GU0WWaFIbtkFXAY7KlVeq0QIhALo17Q7gwp1sOWydEv5CbCnxsRLF5yBuCqhOF7s7MtmtKrwFCNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1IgyeWjMg4BuZaHd1jHMqkAVustrAzF%2BJAqoW%2FpB1sdBcRAyAGzWqauHkSgWx7984CuDXkxzeIGyghtp1m8X2IH9gHZRrzF5%2FQwyT6EbIE%2F5wzy%2FtLjQ9rHCxYxd7aFb8dmfaCxvrPHw%2FUrXVsXs%2ByTenWel3mlVnqF0dQJVHHvF%2BAZKSMUrEArJbNaxGfzJ9grPaEgWLT%2F%2BW5YG99U2ExhzV9MU01De%2FlSGIWKMdaoHNhxgO0wwbbpZ3FpBWkfrjwsSZZt6guNtoIQaWHlkTJYtou0uhIKQLbpAtXLIOKxKqa4KSpUNKxv5FDWy%2FXJbTo9exWc26QbuwWOqL54ksMdyOkPGwGOSkBbJrB6EF2%2Bw5Kl0eGFXt3GoWLrT7sykF%2Fxl84KBGVmLG78NvhS2LZhU7O4uPr54IiLrXUms2sP4hwbOY3o22ml7T6uy130%2FSICvVWwIUxwW324ndtXFYzwPwxq9gs4ZXFxKH3Ltb4Ve4t9oqTWUvvNLF3J%2Bl7xeSOiWQ7BM6a7AxGfP3ckV1tr2Ma3Az0jOJldS0gK46tqyYU7KXq6IqfmpyifDEFSE81eqY6SJkgUohFnsApJR1SDld5qbxsbjF%2BuSSHYPPA8dPfZvlDPVjt5vmjt8E0wKTJAka7DDQqfu2%2BwJP6UMy%2B1xu7Kw05%2ByxuZLXMm%2F9DznGzhTGotJlKJn3g4xrREr9O1yfY6yqlt8AGXRToqalY7Dt%2F4HN6DC%2BYbOsLUT7Xkst9%2FCEknW4KfRgKHu26IJPDd%2FMJ8HkJADOsBn2q4Wcyx2lv5lSB3fTBUv5Y6NkWVGGTK76kB%2Bot%2Bmpu%2FsP4v1uNf2orsibP5BZrpZ69IP5y6Z8IB6vXJkoWznoWG9I1xs%2BH6lB1UnIH0g1t3FfOC6RhzDP0abNBjqwAcU98u4GFdBgOvmgLd%2FzX4ZcYWCDCPAmyACgF6pmcwXP%2BYB9Mnp7flw7e%2BmiLtXYeB8kgQxwnw7oH3w6IQWNqGjKtkJlgc%2Br60l4fa4RrCpCFn5hKqbqq5QMaNu7wD8rOktxootLodEJZvpSY4S1pKzLm9MJbjjiAwX6XYEtW3DLWp%2FuNuxLIjD2zpv5ay0SIkz8M0XA7l9062Gs72kl7KrrubJ%2FQIF%2FfH8E1%2FlzHsvI&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20260305T170653Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYWZAWLFOC%2F20260305%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ca06effd61d7fc6a50219341778b889a53535fe79eea079b37e224346dc6c610&hash=430a7fdf4ac12a28f410e1f9e38cac0d057baa25462d4a5b1778355ec92784fc&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S2452321621001013&tid=spdf-74392459-fc1d-4dc7-a40b-b52bca9fa4e9&sid=5df50d201d2ab3467d2adc9131ce990828f3gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=16055605530f0d570405&rr=9d7ab6bd4a6bcdcd&cc=pe).
1. Mallado
  Se dara un mallado global de 4mm
  ![[Pasted image 20260305131355.png|258]]
  Se aplico un Face Sizing al rededor de 3mm
  ![[Pasted image 20260305131829.png|237]]
  Asi mismo, se aplico un face y edge sizing en los agujeros de los pernos, de 2mm cada uno.
  ![[Pasted image 20260305131732.png|250]]
  Con ello se consiguio una calidad media de 75%, mientras que un skewness medio de 37%, lo cual indica que se trata de una malla aceptable.
  ![[Pasted image 20260305131945.png|362]]
  ![[Pasted image 20260305131929.png|525]]
2. Configuracion Estructural
  ![[Pasted image 20260305141547.png|400]]
3. Solucion
  - Total Deformation
    ![[Pasted image 20260305141915.png|450]]
  - Factor de Seguridad
    Se obtiene un factor minimo de 5.9, justo en las uniones de los pernos, donde se da el soporte fijo.
    ![[Pasted image 20260305141728.png|450]]
    ![[Pasted image 20260305141807.png|434]]
  - Stress equivalente
    La animacion se puede encontrar [aqui](https://drive.google.com/file/d/1yYYB1CxAOls-vLuZa9il2z5hTZO6bDe3/view?usp=sharing)
    ![[Pasted image 20260305150639.png|425]]

### No Lineal - Perfil Hueco
1. Mallado
   Se dejo el mallado, global=10mm, y face sizing=5mm
   ![[Pasted image 20260305153512.png|325]]
2. Configuracion Estructural
   ![[Pasted image 20260305153817.png|231]]
3. Solucion
   - Stress equivalente
     La animacion se puede encontrar [aqui](https://drive.google.com/file/d/19hu8zEHjIeyTIPn0Q73QqHU8LqqeDLKY/view?usp=sharing)
     ![[Pasted image 20260305171930.png|500]]
   - Analisis grarfico usando Charts
   Se tiene los nodos creados a lo largo de la superfice
   ![[Pasted image 20260305163627.png|350]]
   De los cuales para el primer nodo se tiene la grafica, donde se aprecia que ya paso el limite elastico, paso por el plastico y la descarga donde finalmente se deformo de forma permanente
   ![[Pasted image 20260305163650.png|450]]
   Para el nodo 5 se tiene.
   ![[Pasted image 20260305164107.png|450]]
   Para el nodo 6.
   ![[Pasted image 20260305164821.png|450]]
   Para el nodo 7.
   ![[Pasted image 20260305164630.png|450]]
   Como se ve desde el 6 ya se tiene un comportamiento elastico, pero analizemos la cercania entre 5 y 6
   ![[Pasted image 20260305165725.png|450]]
    Es aceptable, pero para tener mejor seguridad se elejira el nodo 6.
   Entonces analizemos la parte izquierda y derecha del Nodo 6.
   ![[Pasted image 20260305165827.png|273]]
   En los nodos N6R y N6L, se tienen respectivamente, donde se aprecia que tambien cumplen con lo visto en el nodo central, por lo cual la zona posterior a esta se mantiene, puesto que presenta un comportamiento elastico, mas la zona que le precede debe ser cortada.
   ![[Pasted image 20260305170044.png|450]]
   ![[Pasted image 20260305170055.png|450]]
   De donde segun la medicion desde el origen (0,0), son 130mm.
   ![[Pasted image 20260305170350.png|650]]
### Analisis de Viga
1. Geometria
   Se tiene la siguiente distribucion de elementos tipo linea y superficie de 12mm en la base, el material es Structural Steel.
   ![[Pasted image 20260305231703.png|475]]
2. Mallado
   Se dara un mallado global de 200m, sobre todo para tener mas elementos en la superficie.
   ![[Pasted image 20260305231832.png|475]]
3. Configuracion Estructural
   Se tiene la siguiente configuracion
   ![[Pasted image 20260305231903.png|475]]
   Con un una presion tabular de la siguiente manera
   ![[Pasted image 20260305231943.png]]
4. Solucion
   Se mostraran los resultados justo en el momento de mayor carga, es decir a los 2s.
   ![[Pasted image 20260305232406.png|550]]
   - Stress Equivalente
     La animacion se puede encontrar [aqui](https://drive.google.com/file/d/1vCAeY4OPg583Iuv_SZDhGXwWhjngQMcJ/view?usp=sharing).
     Se obtiene 2132MPa, lo cual esta muy por encima de lo que puede resistir el material (Structural Steel), el cual se deforma permanentemente cerca a los 250MPa.
     ![[Pasted image 20260305232219.png|525]]
   - Total Deformation
     Como se aprecia, la deformacion es de 387mm, claramente la estructura fallara por no tener soportes inferiores, ya que 0.2Mpa aplicado a cada elemento de malla equivale a que cargue 20ton.
     ![[Pasted image 20260305232129.png|525]]
   - Factor de Seguridad
     En el momento con mas carga, se obtiene un factor minimo de 0.11.
     ![[Pasted image 20260305233637.png|525]]
   - Stress Directo
     Se aprecia que la compresion alcanza un valor de 156MPa, mientras que en traccion se tienen 186MPa, lo cual esta por debajo del limite de fluencia del material.
     ![[Pasted image 20260306151957.png|525]]
   - Stress Combinado Maximo
     Como se ve, la superficie es la que actua en sobre las vigas, por ello tienen una fuerza de traccion de 1449 MPa.
     ![[Pasted image 20260306152331.png|525]]
     


# Mallado
1. Colabracion entre dos para la convergencia
   - Todo nodo de baja confianza (aristas, vertices), se debe de apoyar nodos de alta confianza (caras continuas), para lograr eso, se disminuye el tamaño de la malla
   - Ningun nodo de alta confianza puede ayudar a mas de dos nodos de baja confianza.

## Tpos de malla
![[Pasted image 20260219192507.png|475]]
Superficies, o conocido como shell, es mejor pues se trata de una placa en 2d, es mas facil para mallar, ya que si tuviese
Estructura, es lo que se hizo teoricamente en reisstencia de materiales, como el momento flector, a diferencia del SAP se pueden poner soportes de ayudas como cartelas.

## Estructurada o no estructurada
- Estructurada
  La forma en la que se enlazan los nodos en la estructurada se da forma ordenada.
  Se ve en cuadrilateros y hexaedros 
- No Estr.
  Se amolda a la forma irregular de los solidos.
  Se ve en Trinagulos, tetrahedros.
## Meshing
Referencia [Mesh Methods and Element Types in ANSYS](https://www.mechead.com/mesh-methods-and-element-types-in-ansys-workbench/)
- Method
  Se puede insertar metodo para obtener una tipo similar de mallado, por ejemplo hexaedro, tetraedro.
  Multizone: 
  Hex-Dominant: Lo que hace es completar las zonas regulares con hexaedros o cajas, y las zonas mas dificiles con elementos prismaticos. En Free face mesh type si sera Quad/Tri para permitir la interaccion de cuadrilateros y trinagulos, buena para mallar curvas.
  ![[Pasted image 20260227150252.png|279]]
  
- Face Meshing
  Es buena para arreglar zonas donde el punto de choque es desordenado.
  ![[Pasted image 20260227150426.png|186]]
  Hace que los elementos tomen un mejor orden imponiendo que tomen un patron regular. 
  con FaceMeshing / sin FaceMeshing
  ![[Pasted image 20260220212105.png|375]]
  Sin embargo a veces se necesita aplicar un Sizing adicional a la cara para reducir el tamaño del elemento hasta que ya no nos salga una alerta.
  ![[Pasted image 20260227150914.png|197]]
  
- Sizing
  Se utiliza para reducir el tamaño de los elementos en una area determinada.
## Shared Topology
Cuando se parte un cuerpo en varias partes, sin embargo ansys lo reonoce como una sola union, es decir en la parte de las caras los nodos se unen perfectamente, aunque siguen separados.
Incluso se le puede poner diferente material.
Se pueden ver varios ejemplos aqui [ANSYS DesignModeler: Shared Toplogy](https://www.youtube.com/watch?v=IO4ZtwZdD2I)
Sin Share Top/ Con Share Top
![[Pasted image 20260228151352.png]]
### Partir un elemento en dos pero que sigan juntos
Para esto se debe de abrir spaceclaim, para mayor info, aqui se ve [Ansys splitting](https://www.youtube.com/watch?v=6WPr-OD_WsY), y en los comentarios resulven la duda de merge.
1. Crear dos planos en donde se quiere cortar
2. Luego abrir split bodies
3. seleccionar el cuerpo, luego el plano
4. luego deseleccionar la sierra, y volver a seleccionar el cuerpo y el plano
Luego antes de salir, en propiedades del elemento total, en SHARED TOPOLOGY, se debe de colocar Merge, salir.
Luego en Static Structural se deben de borrar las juntas o conexiones que se crearon.
# Soluciones
- Von-Mises

# Espesores
Para que un superficie sea una superficie, la altura no debe ser mayor a la tercera parte de cualquiera de los lados
![[Pasted image 20260219191525.png|375]]
Para una viga se deb de cumplir que el largo de la viga debe ser 5 veces mayor que sus lados
![[Pasted image 20260219191942.png|300]]
# Design Modeler
Add frozen: no se fusiona con lo demas
Add Material: se fusiona

# Analisis no lineal
## Viga
![[Pasted image 20260305161035.png|325]]
Con una carga puesta encima y el extremo fijo, se tiene la siguiente grafica, como se ve, la curva va subiendo de poco a poco, lo cual no es dice que se va deformando, hasta que llega a un poco en el cual llego a su tope de limite elastico, en la segunda parte que es cuando el peso se saca, la cruva deberia de describir la linea en rojo, sin embargo hay partes que sufrieron deformacion permanente, es decir, llegaron a su limite plastico.
![[Pasted image 20260305161150.png|375]]
![[Pasted image 20260305161344.png|375]]
Por ello este analisis nos dira que parte de la viga a sufrido una deformacion permanmente, y con ello, cortarla.
![[Pasted image 20260305161514.png|350]]
Para ello usaremos el selector de nodo de malla.
![[Pasted image 20260305161640.png|375]]
Y seleccionamos nodo por nodo en la zona de interes, y N para crear un named selection
![[Pasted image 20260305162123.png|425]]
Luego para el analisis necesitaremos
![[Pasted image 20260305162207.png|575]]
![[Pasted image 20260305162228.png|575]]
Una vez obtenidos, se seleccionan al mismo tiempo y en named selection se analiza en el nodo.
Dar solve
Luego volver a tomar ambos y generar chat
![[Pasted image 20260305162525.png|220]]
Y luego configurar.
X axis: Equivalent Total Strain, maximo o minimo da igual
Time: omit
A: Omit
C: Omit
![[Pasted image 20260305162636.png|284]]
La grafica que sale no es tan buena para el nodo, puesto que de izquierda a derecha, sube la zona elastica, pasa a la zona elastica y finalmente ocurre la descarga, es decir, ahi el material ya fallo, y la deformacion ya ocurrio mas adelante de ese modo.
![[Pasted image 20260305162741.png|450]]
En otro nodo se tiene, lo cual es mejor pero 
![[Pasted image 20260305163129.png|475]]
## Simulacion simetrica (1/4 silla)
![[Pasted image 20260227111629.png|101]]
Cuando se tiene que simular solo una porcion del solido, ya que lo mismo se repetira en las demas.
Por ello se tiene la cuarta parte de una silla.
- Material
  Explicit Material -> Nylon -> Saldra un simbolo de interrogacion, el cual nos pide dureza, pero nosotros queremos elasticidad.
  Por ello vamos a Linear Elastic -> Isotropic Elasticity, y lo jalamos hasta Nylon, luego se llena esta propiedad con los datos.
  Luego vamos a Strenght -> Tensile Yield Strenght, se arrastra hasta nylon, y se llena.
- Espesor y Material
  Le daremos un espesor apropiado, como de 3mm, y seleccionamos el material tambien.
- Static Structural
  Standar Earth Gravity: gravedad
  Force: Como solo tenemos un cuarto de la silla, y la fuerza total es de 1000N, entonces para la cuerta parte solo tendra 250N, si fuese Presion, ahi no se divide por que la fuerza depende de la unidad de area.
  Simply Supported: Selecionamos las lineas o aristas de las patas, la escogemos por que no esta empotrada, como si fuese Fixed.
  ![[Pasted image 20260227111547.png|342]]
- Displacement: Como solo tenemos la cuarta parte, los lados se deben conectar con el resto de la silla, pero como no estan, se impedira el movimiento en el eje opuesto a los vertices.
  ![[Pasted image 20260227112321.png|425]]
- Solucion
  Total Deformation: Si vamos Result y cambiamos a 1.0 true scale, para ver la deformacion real, notaremos que la deformacion es de 172mm, y tambien notamos que nos saldra este aviso
  ![[Pasted image 20260227113607.png|458]]
  Normalmente en Ansys se simulan elementos rigidos, que no se deforman tanto, pero en este caso la deformacion es muy grade, o un Large Deflection
  ![[Pasted image 20260227113636.png|351]]
  Una manera de darnos cuenta de que que debemos activar Large Deflection es que la deformacion maxima no debe ser mayor a 5 veces el espesor del elemento, en este caos el espesor es de 3mm, es decir no debe de ser mayor a 15mm la deformacion.
$$
  Deformacion<5(Espesor)
$$
  Otra manera de darnos cuenta fue la alerta que salio, entonces para activarlo nos vamos a Static Structural -> Analysis Settings -> Large deflection lo cambiamos a On.
  Se puede encontrar mas acerca del tema aca [What is Large Deflection in Ansys?](https://www.mechead.com/what-is-large-deflection-in-ansys/)
  ![[Pasted image 20260227114239.png|359]]
  Haciendo ese cambio se tiene que la deformacion cambio a 13mm
  ![[Pasted image 20260227114421.png|375]]
  Factor de seguridad: Para esto necesitaremos la deformacion total que ya se genero previamente, Stress equivalente.
  ![[Pasted image 20260227114608.png|575]]
  Y finalmente, stress tool y maximo stress equivalente.
  ![[Pasted image 20260227114738.png|575]]
  De donde se obtiene que, un factor minimo de 5, lo cual es muy bueno.
  ![[Pasted image 20260227114818.png|368]]
  Finalmente los resultados que se obtiene para el stress equivalente son los mismos para el resto de la silla, no es que se sumen.
# Transferencia de Calor de una tuberia, aislante y concreto
Supongamos que en una fabrica se tranfiere un liquido a muy alta temperatura, y para que la gente no se queme se deberia de aislar la tuberia, primero con aislante epoxico, y luego con concreto.
![[Pasted image 20260227120600.png|320]]
Para este caso ya no se usara Satic Structural, sino Steady State Thermal
![[Pasted image 20260227120143.png]]
- Materials
  ![[Pasted image 20260227120655.png|550]]
- Geometry
  ![[Pasted image 20260227121220.png|325]]
- Steady State Thermal
  Temperature: Le asignamos una temperatura de 85 grados en la cara interior de la tuberia.
  ![[Pasted image 20260227131432.png|325]]
  Convection: Si lo dejamos libre eventualmente todo llegara a ser 85 grados, pero como esta al aire libre hay flujo de aire o conveccion el cual lo enfriara, normalmente si esta al aire libre, entonces seleccionamos la cara exterior, y luego completamos con 
  Film Coefficent, si tenemos un ventilador se debe de averiguar segun el alabe, velocidad y  tamaño del ventiladr, pero si esta al aire libre normalmente es de 5-20 W/m^2 C, o 5-20 W/mm^2 C,  
  Ambient Temperature, la temperatura exterior que normalmente es de 21C.
- Results
  Temperature: Vemos que por fuera quedo como 31C, se puede reducir el aislante para que la tempratura suba a 36, lo cual es aceptable pa=ra evitar accidentes y reducir el costo.
  ![[Pasted image 20260227131938.png|450]]
  Total Heat Flux: No serviria si tenemos componentes electronicos que no pueden sobrepasar cierta temperatura o pueden sufrir daños.
# Transferencia de Calor de un disipador de un condensador.
La diferencia con el anterior es que aqui, le daremos el flujo energetico en wats, y a partir de aqui mediante la simulacion nos dira a que temperatura llega.
- Material
  Aluminum alloy.
- Geometry
  El componente se encontrara metido hasta la mitad del cilindro, por lo que se debera dividir la cara, para ello nos ponemos en un plano y dibujamos una linea que tape el cilindro, luego damos en extruir, imprint faces, both symetric.
  ![[Pasted image 20260227132537.png|350]]
  Eso hara que la cara se corte en dos
  ![[Pasted image 20260227133219.png|350]]
- Steady State Thermal
  Convection: aqui selecionamos todo menos la cara donde ira el condensador y la cara pegada a la placa, para ello seleccionamos todo con ctrl+A, y luego deseleccionamos las caras de interes.
  ![[Pasted image 20260227134528.png|375]]
  Heat Flow: Aqui es donde pondremos los 5W generados por el condensador, selecionamos la cara y aplicamos.
  ![[Pasted image 20260227134812.png|398]]
- Results
  ![[Pasted image 20260227135057.png|475]]
  
# Analisis Vibracional para la Resonancia (MODAL)
Siempre existira la resonancia, todos los cuerpos tienen una resonancia especifica, por ello primero se debe de.
1. Identificar
   De cuanta es la frecuencia? 5Hz, 10Hz, ....10599Hz?
   Cada frecuencia a su vez es acompañada de una deformacion especifica.
2. Comparar con la realidad
   En la vida real mi mecanismo vibra a esa frecuencia? en caso de que sea asi, ocurrira resonancia.
3. Alejarme de la resonancia
   Puede ser reforzarndo el mecanismo, o modificando la geometria, el material, etc.

El analisis se logra con el siguiente componente en Workbench, TENER EN CUENTA DE QUE EN UN ANALISIS MODAL NO HAY STRESS, es decir no hay cargas, solo restricciones.
![[Pasted image 20260305102813.png|174]]
Entonces se tiene la siguiente geometria
![[Pasted image 20260305104006.png|325]]
En analisi Settings, nos pedira cuantas frecuencias nos mostrara, las cuales son infinitas, pero se puede tener.
![[Pasted image 20260305104454.png|377]]
- 5 Hz: Una persona podria hacerlo
- 15 Hz: de aqui para abajo solo maquinas como motores.
- 60 Hz
- 80 Hz
- 500 Hz
- 1400 Hz
Entonces en Modes to Find, por lo general van 6.
Luego como no se colocan cargas, si no mas bien restricciones, solo fijamos una y al resto le damos 2 grados de libertad menos en Y.
![[Pasted image 20260305104734.png|350]]
Damos en Solve, y cuando aparezca la ventana tabular data, le damos select all, y de nuevo anticlick, Create Mode Shape Results, en el arbol se crearan las deformaciones totales, donde nos muestra los escenarios donde habria resonancia para cada frecuencia.
Es decir, nosotros no colocamos las frecuencias, sino el programa mismo calcula a que frecuencias, podria resonar.
![[Pasted image 20260305105111.png|350]]
![[Pasted image 20260305105132.png|350]]
   
A su vez tambien, podemos analizar una geometria tipo linea o estructura, es decir, cuando se aplico un cross section en C, I, Z, etc.
![[Pasted image 20260305105829.png|375]]
![[Pasted image 20260305110525.png|375]]

## Toma de medidas en un elemento deformando
Si se requiere de precision en un analisis modal, el elemento debe tener las medidas exactas en el momento, por lo que no se puede medir solamente con un vernier y dibujar, por que ya tiene una deformacion, la cual a veces puede ser imperceptible, por ello, primero se debe
- Hacer un analisis estructural estatico
  Por ejemplo se tiene el caso de una plancha de 2mm, la cual esta emprotada por tornillos laterales, y sin desplazamiento en las caras laterales en el eje y, esta plancha tiene encima 4 aparatos que causan deformacion, la cual se hizo con imprint faces, donde ira la carga debe de estar coloreado, por lo que si esta volteado se tiene que hacer un flip a la superficie (Surface Flip), quedando de la deformacion total.
  ![[Pasted image 20260305113639.png|500]]
- Mover resultados Modal
  Para esto solo soltamos el modulo encima de resultados en la parte de analisi estatico.
  ![[Pasted image 20260305113845.png]]
  De ahi, se abre Setup, Solve, y evaluamos las frecuencias para ver las deformaciones, por ejemplo antes se tenia de deformacion solo 22mm, pero agregando una frecuencia de 32Hz esta se eleva a 34mm.
  ![[Pasted image 20260305114119.png|500]]
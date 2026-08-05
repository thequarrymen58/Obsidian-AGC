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

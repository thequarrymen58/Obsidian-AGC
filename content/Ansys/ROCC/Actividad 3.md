# Observacion
Se obtienen errores, al parecer la fuerza aplicada es tanta que el material se contrae hacia adentro y se deforma de tal manera que el solver no sabe que hacer y crashea, pero antes de ello muestra hasta donde llego en el calculo.
Solo llega hasta **0.988 seconds**, y crashea, el ultimo reporte muestra el calculo hasta una fuerza de solo 6.91 MPa.
Sin embargo este resultado fue con una malla detallada, se regresara  los 35mm, solo con face meshing, y cambiando a 6 cores (Pcores vs Ecores)
![[Pasted image 20260303162850.png|650]]
Luego de pruebas similares, se observa tambien que, a medida que se refina la malla, la solucion no converge aun asi cambiando a una menor presion, los 35mm dados para comenzar si dan resultados, pero a costa de presicion, entonces se aprecia que un mallado menos detallado "ayuda" a que el material sea mas resistente.

Finalmente se probara con 6.95 MPa de presion, debido a que fue la unica que mostro resultados, y fue la mas cercana antes de no llegar a la convergencia.
# Resolucion
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
# Lineal - Aro de rueda
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

# No Lineal - Perfil Hueco
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
# Analisis de Viga
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
     


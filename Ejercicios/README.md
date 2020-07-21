# Curso de Python desde cero, con ejemplos

Creado por:
   + Ramón Invarato [:link:](https://www.linkedin.com/in/rinvarato)
   + Ricardo Moya  [:link:](https://www.linkedin.com/in/phdricardomoya)
   
<hr>

# Enunciado de los ejercicios:

#### Tema 1: Introducción [:link:](https://jarroba.com/curso-de-python-1-introduccion)
#### # Ejercicio [1.1-input_print.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/1.1-input_print.py)

Crea un programa que admita un texto por teclado y lo imprima.
Pista: usa la documentación de Python 3 [https://docs.python.org/3/]([https://docs.python.org/3/]) para encontrar el método «input»
Ejemplo de lo que tiene que mostrar por la consola:
```
Escribe un texto: hola
hola
```
### Tema 2: String - Tipos básicos de datos [:link:](https://jarroba.com/curso-de-python-2-tipos-basicos-de-datos)
#### # Ejercicio [2.1-tienda_ropa.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/2.1-tienda_ropa.py)

* Crea una variable «formato» con el texto: «{ropa} cuesta {numero} euros»
* Crea dos variables con prendas de ropa
* Crea otras dos variables con un número escrito
* Crea dos variables de «formato_aplicado», y aplica el formato a cada una de ellas una ropa y un número

Pista: si imprimes las dos variables del punto anterior podrás leer algo así por pantalla:
```
Pantalón cuesta cinco euros
Camisa cuesta diez euros
```

* Crea una última variable que junte las otras dos con el formato:
«Su carro de la compra tiene: <formato_aplicado1> y <formato_aplicado2>»

* Imprime la última variable para ver el resultado

Pista: al final tendrás que leer algo así:

```
Su carro de la compra tiene: Pantalón cuesta cinco euros y Camisa cuesta diez euros
```

#### # Ejercicio [2.2-almacen_vino.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/2.2-almacen_vino.py)

Trabajamos para una empresa de vinos que tiene tres tipos de vinos tinto, blanco y rosado; cada tipo de vino se almacena en un almacén diferente y el vino se guarda en barriles en cada almacén.

* Crear tres variables que representen almacenes de barriles para cada uno de los tres tipos de vinos. El valor de 
cada variable será un número entero (el que queramos) que representarán los barriles que hay en cada almacén (ejemplo: almacen_barriles_tinto = 123)
* También crearemos otras tres variables que guardarán el nombre de cada almacén (ejemplo: str_almacen_tinto = 
“Almacén tinto”)

El jefe nos pide que calculemos el total de barriles que tiene nuestra empresa (pista: tinto + blanco + rosado). Imprimir el resultado con una plantilla como: “Tenemos un total de {número de barriles} barriles”

Por otro lado, nos dice calculemos los litros de vino de cada almacén, sabiendo que cada barril de vino tinto tiene 2. litros, cada barril de vino blanco tiene 47 litros y cada barril de vino rosado tiene 73 litros (pista: barriles x litros). Imprimir cada almacén con la plantilla: “El {nombre_almacen} tiene {cantidad_litros} litros”

Por último, nos pide que imprimamos una tabla con las comparaciones de litros entre almacenes, si son iguales, menores o inferiores entre cada uno (pista de una posible plantilla: “{cantidad_litros_tinto} > {cantidad_litros_rosado} = {resultado_comparación}” y de su posible salida de consola: “100 > 10 = True”)

### Tema 3: Colecciones [:link:](https://jarroba.com/curso-de-python-3-colecciones)
#### # Ejercicio [3.1-texto.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/3.1-texto.py)
1.- Crea un texto de al menos 10 caracteres

2.- Imprime la letra que está en el índice 7

3.- Imprime las letras que están en el rango desde la posición 3 a la 8

#### # Ejercicio [3.2-supermercado.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/3.2-supermercado.py)
Copia el siguiente listado: lista_de_inicio

```
lista_de_inicio = [
    "fruta y verduras",
    "carnes y pescados",
    "lácteos y huevos",
    "dulces y pan",
    "hogar y jardín",
    "cuidado y limpieza"
]
```

1.- Imprime la longitud del listado
2.- Elimina el elemento «hogar y jardín» (pista: usa la posición)
3.- Inserta en el listado el elemento: «entretenimiento y deportes»
4.- Imprime por pantalla cada uno de los elementos (por posición) formateado con: «En el mercado hay <primero> pero no 
<segundo>». Para obtener primero y segundo son cada una de las líneas separadas por » y » (pista: crea una lista desde un String con split. Ejemplo: «fruta y verduras».split(» y «) ).

Ejemplo para el primer elemento: «fruta y verduras» (primero será «fruta» y segundo «verduras»). Tiene que imprimir: «En el mercado hay fruta, pero no verduras».

#### # Ejercicio [3.3_lista_campeones_del_mundo.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/3.3_lista_campeones_del_mundo.py)
Dadas las siguientes variables que representan a los jugadores de la selección Española de fútbol que jugo el mundial
 del 2010:
 ```
portero = "Casillas"
defensas_titulares = ["Ramos", "Pique", "Puyol", "Capdevila"]
centrocampistas = ["Xabi Alonso", "Busquets", "Xavi Hernandez", "Iniesta"]
delanteros = ["Pedrito", "Villa"]
suplentes = ["Marchena", "Torres", "Valdes", "Fabregas", "Mata", "Arbeloa",
             "Llorente", "Javi Martinez", "Silva", "Reina", "Navas"]
```

Se pide:

a)	Contar con cuantos delanteros jugo España la final del mundial. (lista delanteros)

b)	Crear una nueva lista llamada “titulares” que contenga a los jugadores titulares de la selección Española.
 
c)	En el minuto 60’ del partido se realiza un cambio: entra Navas por Pedrito. En la lista de “titulares” hay que meter a Navas que está en la lista de “suplentes” y eliminar a Pedrito de la lista de titulares y meterle en la de suplentes.

d)	Crear una lista llamada “selección” que contenga a todos los jugadores de la selección Española.

#### # Ejercicio [3.4_lista_campeones_del_mundo_dorsal.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/3.4_lista_campeones_del_mundo_dorsal.py)
Dada la siguiente lista:
 ```
futbolistas = ["1 - Casillas", "15 - Ramos", "3 - Pique", "5 - Puyol",
               "11 - Capdevila", "14 - Xabi Alonso", "16 - Busquets",
               "8 - Xavi Hernandez", "18 - Pedrito", "6 - Iniesta",
               "7 - Villa"]
```
Se pide ordenar la lista de forma descendente por el dorsal del futbolista. El resultado tendrá que ser el siguiente:

 ```
['18 - Pedrito', '16 - Busquets', '15 - Ramos', '14 - Xabi Alonso', '11 - Capdevila', '8 - Xavi Hernandez', '7 - Villa', '6 - Iniesta', '5 - Puyol', '3 - Pique', '1 - Casillas']
```

#### # Ejercicio [3.5_diccionario_campeones_del_mundo.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/3.5_diccionario_campeones_del_mundo.py)
Dado el siguiente diccionario que representan a los jugadores de la selección Española de fútbol que jugo el mundial del 2010:

 ```
futbolistas = {
    1: "Casillas", 15: "Ramos",
    3: "Pique", 5: "Puyol",
    11: "Capdevila", 14: "Xabi Alonso",
    16: "Busquets", 8: "Xavi Hernandez",
    18: "Pedrito", 6: "Iniesta",
    7: "Villa"
}
```
Se pide:

    1. Contar el número de jugadores (elementos) en el diccionario.
    2. Modificar el nombre de “Casillas” por “Iker Casillas” en el diccionario.
    3. En el minuto 60’ del partido se realiza un cambio: entra “Navas” con el dorsal 22 por “Pedrito” (dorsal 18). En el 
    minuto 87 se realiza otro cambio: entra “Fabregas” con el dorsal 10 por “Xabi Alonso” (dorsal 14). Hay que eliminar del diccionario a los dos jugadores titulares y añadir a los dos jugadores nuevos.
    4. Crear una lista con los dorsales de los jugadores que hay en el diccionario.
    5. Crear una lista con los nombres de los jugadores que hay en el diccionario.
    6. Crear una copia del diccionario “futbolistas” llamada “campeones_del_mundo”.
    7. Eliminar el diccionario “futbolistas”.

### Tema 4: Estructuras de control de flujo [:link:](https://jarroba.com/curso-de-python-4-estructuras-de-control-de-flujo)
4.1.-

### Tema 5: Funciones [:link:](https://jarroba.com/curso-de-python-5-funciones)
5.1.- 

### Tema 6: Bibliotecas/Paquetes [:link:](https://jarroba.com/curso-de-python-6-bilbiotecas-paquetes)
6.1.-

### Tema 7: Excepciones [:link:](https://jarroba.com/curso-de-python-7-excepciones)
7.1.-

### Tema 8: Ficheros [:link:](https://jarroba.com/curso-de-python-8-ficheros)
8.1.-
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
1. Contar con cuantos delanteros jugo España la final del mundial. (lista delanteros)
2. Crear una nueva lista llamada “titulares” que contenga a los jugadores titulares de la selección Española.
3. En el minuto 60’ del partido se realiza un cambio: entra Navas por Pedrito. En la lista de “titulares” hay que meter
 a Navas que está en la lista de “suplentes” y eliminar a Pedrito de la lista de titulares y meterle en la de suplentes.
4. Crear una lista llamada “selección” que contenga a todos los jugadores de la selección Española.

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
#### # Ejercicio [4.1-pan_y_chocolate.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/4.1-pan_y_chocolate.py)
Crea un programa que pregunte por teclado (pista: input) si hay «chocolate» primero y si hay «harina» después (pista: bool(«Cualquier valor») es True o bool(«») es False).

* Si ambos son ciertos imprimiremos «Cocinamos una tarta»

* Si solo es cierto «chocolate» imprimiremos «Haremos bombones»

* Si solo es cierto «harina» imprimiremos «Hornearemos pan»

* Si ninguna es cierta imprimiremos «Hoy descanso»

 ```
¿Hay Chocolate?:
¿Hay harina?: True
Hornearemos pan
```
#### # Ejercicio [4.2-tablas_de_la_verdad.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/4.2-tablas_de_la_verdad.py)
Crea un programa que cree las tablas de la verdad AND y OR.

Para ello utiliza dos variables «a» y «b» que es vayan actualizando en cada iteración de un bucle «while» y que termine después de que «a» y «b» sean False (pista: comprobar solo con AND).

E imprima cada resultado de la iteración con un formato legible como (no hace falta que los espacios estén perfectos, aunque puede ayudar tabular \t):

 ```
  A   o    B    = A or B
True  o  True   = True
True  o  False  = True
False o  True   = True
False o  False  = True
```

#### # Ejercicio [4.3-base_de_datos_banco.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/4.3-base_de_datos_banco.py)
Trabajamos para un banco y tenemos que crear una base de datos para guardar dinero de nuestros usuarios. El programa nos preguntará eternamente (pista: while true) por el nombre del usuario (clave) y luego un dinero positivo o negativo (un valor numérico; valor). En caso de que el usuario ya exista habrá que sumar al dinero que hubiera el nuevo dinero introducido, sino existiera simplemente lo guardaríamos.

Podremos imprimir el diccionario en cada iteración para saber que hemos introducido y qué se ha actualizado.

```
Usuario: Juan
Dinero: 100
{'Juan':100}
Usuario: Maria
Dinero: 80
{'Juan':100, 'Maria': 80}
Usuario: Juan
Dinero: -30
{'Juan':70, 'Maria': 80}
```

#### # Ejercicio [4.4.-diccionario_seleccion_futbol.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/4.4.-diccionario_seleccion_futbol.py)
Dado el siguiente diccionario que representan a los jugadores de la selección Española de fútbol que jugo el mundial del 2010:
```
futbolistas = ["1 - Casillas", "15 - Ramos", "3 - Pique", "5 - Puyol",
               "11 - Capdevila", "14 - Xabi Alonso", "16 - Busquets",
               "8 - Xavi Hernandez", "18 - Pedrito", "6 - Iniesta",
               "7 - Villa"]
```
Se pide:
1. Recorriendo una sola vez el diccionario, añadir a otro diccionario llamado “pares” los jugadores cuya clave sea par 
(clave: dorsal, valor: nombre) y en una lista llamada “impares” los nombres de los jugadores cuya clave sea impar.
2. Orden por orden alfabético la lista “impares”.
3. Dado el diccionario “pares”, crear otro diccionario “pares_al_reves” que tenga como clave el nombre del jugador y 
como valor el dorsal del jugador.


### Tema 5: Funciones [:link:](https://jarroba.com/curso-de-python-5-funciones)
#### # Ejercicio [5.1-cajero_automatico.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/5.1-cajero_automatico.py)
Vamos a crear sistema de registros de un cajero automático.

Crearemos un método para imprimir cada una de las líneas que tenga de parámetro «fecha» y «concepto» como obligatorios, y «cantidad» será opcional, sino se pasa será 0 y «movimiento» si no se pasa nada será «Domiciliación» que si en caso de que sea negativa la cantidad tiene que marcarse en la línea de algún modo, tiene que estar ordenado por «fecha»

La entrada de los datos puede ser por consola o por un listado

```
[2020-01-01]      Domiciliación      Nómina               100€
[2020-01-01]      Transferencia      Pagar concierto      -50€  <=Déficit
[2020-01-01]      Intereses          Recibos              0€   
```

### Tema 6: Bibliotecas/Paquetes [:link:](https://jarroba.com/curso-de-python-6-bilbiotecas-paquetes)
#### # Ejercicio [6.1-ruleta_casino.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/6.1-ruleta_casino.py)
Realizar el juego de la ruleta de casino simplificada.

<img src="https://jarroba.com/wp-content/uploads/2020/07/15162656651431693743roulette-wheel-clipart.med_.png">

Nuestra consola nos pedirá apostar a un número (del 1 al 36, comprobar que no se introduzca otro) que no se a el 0 al pulsar la tecla Intro se realizará la jugada y nos devolverá si hemos ganado algo o no.

* Si toca 0 habremos perdido
* Si toca nuestro número habremos ganado
* Si toca un color y nuestro número es de ese color habremos ganado también (indicar que ha tocado el color y no el 
número)

Al devolver la solución volverá a preguntar por otro número inmediatamente (el programa estará en bucle hasta que escribamos la palabra «salir»)

Cada vez que se reinicie el juego, tendrá que salir un historial de las partidas ganadas y perdidas (el número jugado y si se ha ganado o perdido)

Ejemplo de programa:

#### # Ejercicio [6.2-videojuego.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/6.2-videojuego.py)
Realizaremos un minijuego de combate contra la máquina donde se pedirá al usuario decidir si: atacar, defenderse o curarse.
Habrá dos contadores de vida: el nuestro y el del enemigo, el que llegue a cero pierde.
El enemigo elije al azar si nos ataca, se defiende o se cura.

En caso de:
* Si alguien se defiende de un ataque, entonces perderá 0 vidas
* Si alguien ataca mientras el otro le ataca, entonces ambos perderán -2 vidas
* Si alguien se cura mientras el otro le ataca, entonces el que no ataca perderá -2 vidas
* Quien se cura recuperará +1 vida sea atacado o no

Crearemos mínimo los métodos curarse y recibir_ataque para reutilizarlos (al que se le pasa el jugador y los valores necesarios)

Ampliación: añade alguna función extra al juego (ideas: golpe fuerte que quite -4, hechizo que roba vida, otros medidores para los jugadores como maná o fatiga, etc.)

<img src="https://jarroba.com/wp-content/uploads/2020/07/Ejercicio-juego-www.jarroba.png">

#### # Ejercicio [6.3-velocidad_de_escape.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/6.3-velocidad_de_escape.py)
Nos han contratado en la Agencia Espacial Internacional, tienen intención de poner en órbita unos satélites, pensando en el futuro cuando lleguemos a Marte y a la Luna también querrán lanzar satélites desde ahí.

Por lo que quieren una calculadora que introduciendo la masa de un planeta y su radio nos devuelva la «velocidad de escape» de cada planeta en concreto.

Pistas:

1. Nos documentamos https://es.wikipedia.org/wiki/Velocidad_de_escape
2. Buscamos la fórmula que nos piden crear en la calculadora
3. Localizamos las variables de la fórmula (G es Constante de gravitación universal, M es Masa del planeta y r es Radio
 del planeta)
4. Programamos la calculadora

Una vez que lo tengamos, probaremos con los datos de los planetas que nos han pedido (Buscamos los datos en Internet): Tierra, Marte y Luna

Es importante comprobar los datos que introduzca el usuario: si han metido números y no otra cosa, que no sean vacíos, etc.

Ejemplo:

<img src="https://jarroba.com/wp-content/uploads/2020/07/Ejercicio-velocidad-de-escape-www.jarroba.com_.png">

#### # Ejercicio [6.4-datetime.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/6.4-datetime.py)
Se pide crear un script que pida introducir por pantalla una fecha de nacimiento con formato “DD/MM/YYYY” y que imprima por pantalla los días que ha vivido desde su nacimiento hasta el instante de ejecutar el script y que también imprima por pantalla la edad en años.


### Tema 7: Excepciones [:link:](https://jarroba.com/curso-de-python-7-excepciones)
#### # Ejercicio [7.1-frutas.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/7.1-frutas.py)
Crea un listado con cinco frutas.

Pregunta al usuario por pantalla el índice del listado para devolvérselo. En caso de que devuelva una excepción tendrá que ser capturada y avisar al usuario del error.

<img src="https://jarroba.com/wp-content/uploads/2020/07/Ejercicio-frutas-www.jarroba.png">

#### # Ejercicio [7.2-contador_limitado.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/7.2-contador_limitado.py)
Crea un while True que esté siempre iterando y sumando a un contador +1 (e imprímelo).

El ordenador donde lo ejecutamos está un poco limitado y no puede darse que el contador sea mayor que 9999. En ese momento se lanzará una excepción BufferError con un mensaje «Se ha superado los 9999 registros», ya que no se podrá sumar más. Si ejecutas con este código (ahora, sin avanzar más en el ejercicio) el programa terminará con un error en tiempo de ejecución.

<img src="https://jarroba.com/wp-content/uploads/2020/07/Ejercicio-contador-error-www.jarroba.com_.png">

Pero no queremos terminar el programa, queremos después del bucle que continúe el programa. Para ello capturaremos la excepción fuera del bucle, será donde mostremos el mensaje de error con el siguiente formato: «Se ha detectado el error ‘{mensaje_del_buffererror}'»

 Y para terminar fuera del bucle imprimiremos el texto: «el código continua»

<img src="https://jarroba.com/wp-content/uploads/2020/07/Ejercicio-contador-sin-error-www.jarroba.com_.png">

### Tema 8: Ficheros [:link:](https://jarroba.com/curso-de-python-8-ficheros)
#### # Ejercicio [8.1-crear_fichero_y_leer_fichero.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/8.1-crear_fichero_y_leer_fichero.py)
<img src="https://jarroba.com/wp-content/uploads/2020/07/Ejercicio-fichero-www.jarroba.png">

En una ubicación de tu ordenador crear un directorio y dentro un fichero

Dentro del fichero escribir cinco líneas de número aleatorios del 1 al 10 (Parte 1)

Luego leer ese fichero e imprimir cada línea por pantalla

A continuación, añadir al final del fichero un par de líneas de texto (Parte 2)

Volver a leer el fichero

#### # Ejercicio [8.2-futbolistas.py](https://github.com/jarroba/Curso-Python/blob/master/Ejercicios/8.2-futbolistas.py)
Dado el fichero “futbolistas.txt”  en el que en cada línea contiene datos de un futbolista, se pide:

1. Implementar una función llamada “file_to_list(file_dir)” que dada la ruta del fichero futbolista.txt, devuelva una 
lista en la que cada elemento corresponde con una línea del fichero; es decir, que cada elemento representa a los datos del futbolista.
2. Implementar una función llamada “get_top_goals_players(list_players, top_n)” que dada la lista de futbolistas 
devuelva en otra lista los “top_n” futbolistas más goleadores.
3. Implementar una función llamada “get_players_by_team(list_players, team)” que dada la lista de futbolistas devuelva 
en otra lista con todos los jugadores que han militado en el equipo que se pasa como parámetro (team), ordenados de forma descendente por el número de minutos que han jugado.
4. Implementar una función llamada “write_list_to_file(list_to_write, file_dir)” que dada la lista que se pasa como 
parámetro (list_to_write), escriba en el fichero que se pasa como parámetro “file_dir” cada elemento de la lista en una línea.
5. Escribir las listas creadas en los puntos b y c en un fichero, utilizando la función implementada en el punto d.

En el fichero de futbolistas.txt, cada línea contiene datos de un jugador de futbol y los datos están separados por el separador “::”. Los datos que hay en cada posición son los siguientes:


|1|id|14|PartidosCompletos|27|Numligas|
|1|id|14|PartidosCompletos|27|Numligas|

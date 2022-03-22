# Curso Profesional de Python

# 1. ****¿Qué necesitas saber para tomar el curso?****

Profesor Facundo García

Requisitos: Python Básico, Python Intermedio, Curso de Git y Git Hub, POO

# 2. ****¿Cómo funciona Python?****

Es hora de conocer una de las clasificaciones más conocidas, existe compilado vs interpretado. ¿Que significa cada una de estas palabras?

Ej: en C++  creamos na función void main. y la palabra clave cout

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled.png)

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%201.png)

c++ Es un lenguaje compilado, quiere decir que convierte el código de c++  y lo convierte a binario al lenguaje de la computadora.

Las partes se comunican mediante un proceso llamado compilación.

Python en cambio no entra en este grupo. Python es interpretado.

Ej: al hace un hola mundo no lo pasa de una a instrucciones maquina si no que usa un lenguaje llamado bytecode, el cual puede ser leído por el interprete de python y es leído por una maquina virtual. Esta maquina virtual puede ser ejecutado en diferentes sistemas operativos. Solo se necesita el lenguaje y el interprete.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%202.png)

Cuando hablamos de lenguajes interpretados siempre tenemos un intermediario, un interprete.

## Preguntas frequentes:

Interpretado es más lento  que complicado ¿?
C cuando se debe, Python cuando se puede. 

Python ( Cuando la velocidad no es un factor importante )

Sin embargo no será importante hasta que sea en un nivel muy avanzado o especifico.

## ¿Que es el garbage colector?

Tomar los objetos y las variables que no están en uso y eliminarlas.

## ¿Que es la carpeta **pycache**?

Es el bytecode, el código intermedio que genera python y funciona cómo una especie de recuperación del código en el que he trabajado. Funciona para ahorrar tiempo y no tener que generar ese bytecode de nuevo.

# 3. ¿Cómo organizar los archivos de tus proyectos?

## Paquetes y módulos

Ej: random

## Modulo

Un módulo es cualquier archivo de python. (que termina en la extensión .py) Generalmente contiene código que se puede reutilizar. 

Ej: Se podría crear un módulo con funciones matemáticas para calcular en otro archivo e importarla

## Paquete

Es un conjunto de módulos. Un paquete es una carpeta que tiene módulos, son característicos por el. Es un lugar en donde voy a encontrar módulos que voy  a poder importar después en otro archivo.

Algo característico de estas carpetas o folders es que tienen un archivo característico llamado `__init__.py`

Se lee así: Dunder init .py

Denota el que una carpeta es un paquete. Si una carpeta no tiene este paquete python no la va a tratar cómo un conjunto de módulos.

Ej: Supongamos que vamos a construir una nave espacial.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%203.png)

Observemos que  las funcionalidades se pueden segmentar de tal forma que todo quede aislado, generando alta cohesión y bajo acoplamiento.

Esto en una estructura de carpetas se vería así:

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%204.png)

Exploración espacial es un paquete, el archivo tunder .py (__init__.py) Y los módulos de nuestro programa.

La estructura de carpetas depende del proyecto y del framwork que uno use.

# 4. ¿Qué son los tipados?

(Estático, dinámico, débil, y fuerte)

Pensemos un momento en las estructuras de datos mutables (Listas o arreglos). Los tipos de datos primitivos.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%205.png)

Un lenguaje de programación tendrá un tipado diferente de acuerdo a cómo trata a los tipos  de datos que tenemos en un programa.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%206.png)

 Python es de tipado fuerte y dinámico. 

El proceso de un lenguaje compilado.

1. Escribimos una serie de código  
2. Se pasa a código maquina 
3. Pasa a nuestra computadora (llamado tiempo de ejecución). En donde podemos ver a nuestro programa funcionando.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%207.png)

## Static

Los lenguajes de tipado estático, son los que levantan los errores de tipo en tiempo de compilación.

¿Que quiere decir esto?

EJ: Si mientras estamos programando  una cadena de caracteres es tratada cómo número, el lenguaje nos dirá que hay un error en tiempo de compilación.

En Java

```java
String str = "Hello"; //Statially typed as String
str = 5; // Would throw an error since java is statically tyed
```

## Dynamic

Hacen lo opuesto a los lenguajes estáticos. Ej: Python, cómo Python es interpretado (Que tiene una maquina virtual con un interprete) el pasa a Bytecode y luego pasa a código maquina.

En el paso a bytecode, python no lo detecta. Simplemente lo detecta en tiempo de ejecución.

Ej:

```python
str = "Hello"
str = 5
```

En Python funcionaría, porqué es tipado y levantara los errores en tiempo de ejecución.

Python también comparte características **strong and week** en su tipado.

ej:

 

```python
x = 1 ;
y = "2" ;
z = x + y ; // This will fail because python has strong typed form
```

Los lenguajes con tipado fuerte, son aquellos que tratan con mayor severidad a los datos de diferentes tipos.

Los lenguajes con tipado débil, tendrán más excepciones.

Ej: si hacemos el mismo ejercicio en Java Script

```jsx
const x = 1 ;
const y = "2" ;
const z = x + y ; // 12 because it is Java Script :v
```

Y es normal, al no tener una manera estricta de tratar los datos, el los convierte o lo castea para combinar la operación de suma (concatenando las dos cadenas)

```php
<?php
$str = 5 + "5" ; 
```

Ej: En php pasa lo contrario que en Java Script, en este caso la cadena representada cómo “5” será convertida en un entero para poder realizar la suma y retornar 10.

El tipado dinámico en ocasiones puede ser peligroso.

# 5. Tipado estático en Python

Vamos a convertir python de tipado dinamico a tipado estatico 

```python
print("¡Hello, world!")
# Some code
a = 1
print(type(a))
```

Ejemplo:

Este programa solicita el número de telefono al usuario, esto genera un error porqué estamos intentando redondear una cadena de caracteres.

```python
FALLBACK_PHONE = '+e000000000'

def get_phone():
	phone = input('Give me your phone: ')
	if not phone_
		return FALLBACK_PHONE.round()
	return int(phone)

def run():
	my_phone = get_phone()
	print(f'Your Phone is: {my_phone}')

run()
```

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%208.png)

## Static Typing

Lo único que debemos hace es agregar un poco de código declarativo al que ya agregábamos antes.

```python
a: int = 5
print(a)
b: str = 'Hola'

c: bool = True
print(c)

```

Así es cómo se le agrega el tipo de dato a las variables en Python.

```python
def sum(a: int, b: int) -> int:
	return a + b

print(suma(1,2))

print(suma('1','2'))
```

En este caso ambas se ejecutan, en el segundo caso concatenando las dos cadenas, y el problema es que python sigue siendo de tipado debil.

```python
# De esta manera se declara una variable, se colocan los dos puntos (:), el tipo de dato y para finalizar se usa el signo igual para asignar el valor a la variable.

#<variable> : <tipo_de_dato> = <valor_asignado>

a: int = 5
print(a)

b: str = "Hola"
print(b)

c: bool = True
print(c)
```

## Ejemplo con Dict y List

```python

from turtle import pos
from typing import Dict, List
positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
    'Argentina':1,
    'Mexico':34,
    'Colombia':45
}

countries: List[Dict[str, str]] = [
{
'name': 'Argentina',
'population': '17826312',
}
,
{
'name': 'Mexico',
'population': '716237123',
}
,
{
'name': 'Colombia',
'population': '0978189723',
}
]

print(countries)
```

## Ejemplo con Tuple

```python
from typing import Tuple
#Ejemplo con un tipo de dato Tupla que a diferencia de las listas
# No puede ser inmutable
number: Tuple[int, float, int] = (1, 0.5, 1)
print(number)
```

## Creando un Alias para un tipo de dato especifico

```python
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int,int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1,2),
        'coord2': (3,5),
    },
    {
        'coord1': (0,1),
        'coord2': (2,5),
    }
]

print(coordinates)
```

 

## mypy y typing

Estos  módulos hace que sea más estricto la definición del tipado. Convirtiéndolo en un tipado estático.

# 6. Practicando el tipado estático

Vamos a crear nuestro proyecto y configurar el ambiente de trabajo. 

Lo primero es instalar `pip install mypy`

Ahora vamos a crear el ejemplo palíndromo con definición de datos

```python

def Is_palindrome(word: str ) -> bool:
    word = word.replace(" ","").lower()
    return word == word[::-1]

def run():
    print(Is_palindrome(10000))

if __name__ == '__main__':
    run()
```

## Probando mypy

```python
mypy palindrome.py --check-untyped-defs

palindrome.py:12: error: Argument 1 to "Is_palindrome" has incompatible type "int"; expected "str"
Found 1 error in 1 file (checked 1 source file)
```

El resultado quiere decir que ha encontrado un error de compatibilidad de datos, en este caso se esperaba un string, pero le estamos pasando un entero.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%209.png)

```python
"""Python module to check  if a number is prime :3"""

def sqrt_number(number: int) -> int:
    number = int(number**(1/2))
    return number

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
# check for 2 to sqrt to number
    for i in range(2,sqrt_number(number)+1):
        if number%i == 0:
            return False

    return True

def run():
    print(is_prime(6))

if __name__ == '__main__':
    run()
```

Cuando ejecuto el archivo de Python no se evidencia que no tiene problemas en la asignación del tipado.

`$ mypy reto_prime_numbers.py`

`Success: no issues found in 1 source file`

# 7. Scope: Alcance de las variables

¿Hacia donde va una variable cuando la creamos?

Una variable sólo está disponible dentro de la región en donde fue creada

```python
#local scope
def my_fun():
	y = 5 
	print(y)
```

Por ejemplo esta función tiene su propio scope, todo su propio alcance, está definida en la región en donde fue creada y no puede usar usada fuera de ella.

```python
#global scope
y = 5

def my_fun():
	print(y)

def my_other_fun():
	print(y)

my_other_fun()
fun()
```

```python
z = 5
def my_func():
	z = 3
	print(z)

print(my_func())

print(z)

3 
5
```

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2010.png)

# 8. Closures

Es un concepto usado en backend y ciencia de datos

## Nested functions

Es una técnica que se da cuando una variable que está en un scope superior, es recordada por una función que está en un scope inferior.

Aunque ese scope sea eliminado después incluso.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2011.png)

En este ejemplo vemos que aunque se elimine la función main, yo puedo seguir accediendo.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2012.png)

## Reglas para encontrar un closure

- Debemos tener un nested function
- La nested function debe referenciar un valor de scope superior
- La función que envuelve a la nested function debe retornarla también.

Cuando estar serie de pasos se cumple, tenemos un Closure

Este es un ejemplo de una prueba técnica:

Puedo crear una variable para asignar el primer valor de x y luego usar esa variable para usar la segunda función nested.

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2013.png)

## ¿Donde aparecen los Closures?

En programación OO si se tiene una clase que sólo tiene un metodo se pueden aplicar los closures. Cómo alternativa. También con decoradores.

# 9. Programando Closures

Son in tipo de caso especial en el cual hay tres regles

- Debemos tener un nested function
- La nested function debe referenciar un valor de scope superior
- La función que envuelve a la nested function debe retornarla también.

```python
def multiply_str(str):
    def multiplyer(n):
        return str * n 
    return multiplyer

def run():

    name = multiply_str("Cris")
    name(4)

    print(name(4))

if __name__ == '__main__':
    run()
```

# 10. Decoradores

Es el concepto más difícil para entender en los lenguajes de programación. 

Un decorador es un closure, pero con parámetros adicionales.

Def: Es una **Función** que recibe como parámetro otra **función**, le añade cosas, y retorna una **función** diferente.

Ej:  En este caso se le agrega una función a la función original. Creando una Nested function. 

```python
def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original")
        func()
    return envoltura

def saludo():
    print("!hola¡")

def run():
        

    saludito = decorador(saludo)
    saludito()

if __name__ == '__main__':
    run()
```

## Azucar sintactica (Syntactic Sugar)

Se refiere a todas esas construcciones que no aportan nueva funcionalidad a un lenguaje, pero que permiten que sea más fácilmente utilizable por seres humanos.

Muchas veces cuando estamos programando hay cosas muy complejas que no son fáciles de entender.

Entonces existe una forma más bonita por así decirlo, de crear Decoradores.

Ej:

```python
def decorador(func):
    def envoltura():
        print("Esto se ageraga a mi función original")
        func()
    return envoltura

@decorador
def saludo():
    print("¡Hola!")

def run():
    saludo()

if __name__ == '__main__':
    run()
```

Otro ejemplo con decoradores

```python
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste mensaje!'

def run():
    print(mensaje("Cesar"))

if __name__ == '__main__':
    run()
```

# 11. ****Programando decoradores****

Vamos a realizar un ejemplo util de decoradores

```python
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time -initial_time
        print("Time Elapsed: " + str(time_elapsed.total_seconds()) + " Seconds" )
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass
        # print(_)

@execution_time
def sum(a: int, b: int) -> int:
    # print( a + b )
    return a + b

@execution_time
def saludo(nombre='Camilo'):
    print(f'Hola {nombre}')

def run():
    saludo("Polola")
    random_func()
    x = sum(10000,10)
    print(x)

if __name__ == '__main__':
    run()
```

# ⛳ 12. Iteradores

Los iterables son todos los objetos que se pueden recorrer en un ciclo. Ej: listas, diccionarios, tuplas, strings. Todos los iterables pueden convertirse en itardores.

Es una estructura de datos para guardar datos infinitos.

Cuando hacemos un ciclo for, lo que hace python internamente es crear un while iterator: Recorriéndolo hasta que tenga una excepción.

```python
#Creating iterator
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# print(next(my_list))

#Itering interator
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
```

```python
#This is sintatic Sugar :D
for element in my_list:
    print(element)
```

## ¿Cómo construyo un iterador?

```python
class EvenNumbers:
    """ Clase que implementa un iterador de todos 
    los numeros pares hasta un máximo"""

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration
```

## Ventajas de usar iteradores

En el iterador puedo guardar la totalidad de los números pares de mi computadora, no usan mucha memoria. Es cómo las imágenes svg. Tengo una función matemática que explica cómo sacar los siguientes elementos. 

# 13. La sucesión de Fibonacci.

Cada elemento de la sucesión es el resultado de sumar los dos números anteriores.

# 14. Generadores “Sugar Syntax” de los iteradores

Un generador es un cómo un iterador sólo que escrito de manera más simple y más elegante. :3 . Con generadores no es tan difícil almacenar secuencias infinitas cómo si lo era con los iteradores.

Son funciones, a diferencia de los iteradores que son clases, esto porqué crear funciones es mucho más fácil que crear clases, una clase necesita más sintaxis más densidad de código etc. En cambio con una función nosotros sómos más libres podemos jugar un poco más con el código, en este caso tenemos un generador llamado `my_ge()`  y es un ejemplo de generadores, así está documentada esta función y hace lo siguiente:

```python
def my_gen():
    """This is an example of generators
    """
    print("Hello World!")
    n = 0
    yield n  #This keyword is similar to return, except that this doesn't finish the function, 
    
    print("hello heave!")
    n = 1
    yield n

    print("Hello hell")
    n = 2
    yield n

def run ():
    a = my_gen()
    print(next(a))
    print(next(a))
    print(next(a))
    # print(next(a)) StopIteration

if __name__ == '__main__':
    run()
```

## Generator expresions

# 15. Mejorando nuestra sucesión de Fiboacci

```python
import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1 , n2  = n2, aux
            counter +=1
            yield aux

def run():
    fibonacci = fibo_gen()
    for e in fibonacci:
        print(e)
        time.sleep(1)

if __name__ == "__main__":
    run()
```

# 16. Sets

Un set es una Estructura de datos de tipo colección de elementos únicos que deben ser **inmutables**

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2014.png)

Los elementos de la derecha hace que se convierta un set.

## ¿Cómo puedo crear un set?

```python
my_set = {3, 3, 6}
my_set.add(7)
my_set.update([1, 2, 5])

my_set.update((4, 7, 8))

my_set.update((4, 7, 8), {11, 4})
print(my_set)
my_set_empty = {}  # This is a dictionary
print(type(my_set_empty))
my_set_empty2 = set()
print(type(my_set_empty2))
my_set_two = {[1, 2], 3, 5, 6, 5}

```

Cuando uso el metodo add y agrego una lista, el interprete extrae cada elemento de la listay verifica is existe y los agrega.

# 17. Operaciones con sets

Union:

Interesección

Diferencia

Diferencia Simétrica (Todo menos la interseción)

```python
set_a = {1, 2, 3}
set_b = {4, 5, 6, 3, 1}

print(set_a.union(set_b))
print(set_a | set_b)
print(set_a.intersection(set_b))
print(set_a & set_b)
print(set_a-set_b)
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)
```

# 18. Eliminando los repetidos en una lista

```python
# This example is for elimintate duplicated elements in a list object in python

def remove_duplicates(somelist):
    without_duplicates = []
    for element in somelist:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def remove_duplicates_with_sets(somelist):
    return list(set(somelist))

def run():
    my_list = [1, 1, 1, 2, 3, 34, 5, 6, 66, 6, 6, ]
    print(my_list)
    print(remove_duplicates_with_sets(my_list))

if __name__ == '__main__':
    run()
```

# 19. Manejo de fechas

¿Cómo manejar el tiempo en una aplicación?

El modulo datetime contiene una clase llamada datetime, por eso es confuso cuando se llama. Ej:

```python
import datetime

my_time = datetime.datetime.now()
my_time_utc = datetime.datetime.utcnow()
my_day = datetime.datetime.today()
print(my_time)
print(my_time_utc)
print(my_day)

print(f'Day: {my_day.day} , Month: {my_day.month} , Year: {my_day.year} ')
```

## Formatos de fecha

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2015.png)

```python
# import datetime
from datetime import datetime

my_time = datetime.now()
my_time_utc = datetime.utcnow()
my_day = datetime.today()
print(my_time)
print(my_time_utc)
print(my_day)

print(f'Day: {my_day.day} , Month: {my_day.month} , Year: {my_day.year} ')

my_str = my_time.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str}')

my_streu = my_time.strftime('%m/%d/%Y')
print(f'Formato LATAM: {my_streu}')

my_stryear = my_time.strftime('%Y')
print(f'Estamos en el año {my_stryear}')
```

# 20. Time Zones

![Untitled](https://github.com/camilocbarrera/Curso-Profesional-de-Python/blob/main/images/Untitled%2016.png)

La mejor forma de operar sobre cambios de zonas horarias es con el módulo `pytz` ideal para estos casos de uso.
# Curso Profesional de Python

# 1. ****¿Qué necesitas saber para tomar el curso?****

Profesor Facundo García

Requisitos: Python Básico, Python Intermedio, Curso de Git y Git Hub, POO

# 2. ****¿Cómo funciona Python?****

Es hora de conocer una de las clasificaciones más conocidas, existe compilado vs interpretado. ¿Que significa cada una de estas palabras?

Ej: en C++  creamos na función void main. y la palabra clave cout

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ac95a27-bb82-46ad-b3e7-6b369cad533e/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6c23629-9bf8-4e47-8a10-8878656c266a/Untitled.png)

c++ Es un lenguaje compilado, quiere decir que convierte el código de c++  y lo convierte a binario al lenguaje de la computadora.

Las partes se comunican mediante un proceso llamado compilación.

Python en cambio no entra en este grupo. Python es interpretado.

Ej: al hace un hola mundo no lo pasa de una a instrucciones maquina si no que usa un lenguaje llamado bytecode, el cual puede ser leído por el interprete de python y es leído por una maquina virtual. Esta maquina virtual puede ser ejecutado en diferentes sistemas operativos. Solo se necesita el lenguaje y el interprete.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5af5a48c-e519-44c1-852e-5135eec7d5d1/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/14fdb60a-06f6-47cd-b49d-836d0a5bff28/Untitled.png)

Observemos que  las funcionalidades se pueden segmentar de tal forma que todo quede aislado, generando alta cohesión y bajo acoplamiento.

Esto en una estructura de carpetas se vería así:

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b7a63861-a974-4ef4-93d2-5c1e69ca8294/Untitled.png)

Exploración espacial es un paquete, el archivo tunder .py (__init__.py) Y los módulos de nuestro programa.

La estructura de carpetas depende del proyecto y del framwork que uno use.

# 4. ¿Qué son los tipados?

(Estático, dinámico, débil, y fuerte)

Pensemos un momento en las estructuras de datos mutables (Listas o arreglos). Los tipos de datos primitivos.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e2ffa7b1-187b-4aa7-84e0-2c2ed57684f9/Untitled.png)

Un lenguaje de programación tendrá un tipado diferente de acuerdo a cómo trata a los tipos  de datos que tenemos en un programa.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae63882e-8ad0-4cae-8994-18d014df833c/Untitled.png)

 Python es de tipado fuerte y dinámico. 

El proceso de un lenguaje compilado.

1. Escribimos una serie de código  
2. Se pasa a código maquina 
3. Pasa a nuestra computadora (llamado tiempo de ejecución). En donde podemos ver a nuestro programa funcionando.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/28416b32-dd78-41aa-9b63-3b1f2b50cd1e/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/80c17a39-7091-4ebd-9932-77701bc86527/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/23898edd-4223-4779-bafc-57626e3c6818/Untitled.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8ae05c75-027d-4cdb-bf0a-066a8c3d02e0/Untitled.png)

# 8. Closures

Es un concepto usado en backend y ciencia de datos

## Nested functions

Es una tecnica que se da cuando una variable que está en un scope superior, es recordada por una función que está en un scope inferior.

Aunque ese scope sea eliminado después incluso.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/24fa9a80-1ebb-442f-a1a1-b8190b458c74/Untitled.png)

En este ejemplo vemos que aunque se elimine la función main, yo puedo seguir accediendo.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/16dd53d8-5242-4f63-aaca-e0be0fc59fc1/Untitled.png)

## Reglas para encontrar un closure

- Debemos tener un nested function
- La nested function debe referenciar un valor de scope superior
- La función que envuelve a la nested function debe retornarla también.

Cuando estar serie de pasos se cumple, tenemos un Closure

Este es un ejemplo de una prueba técnica:

Puedo crear una variable para asignar el primer valor de x y luego usar esa variable para usar la segunda función nested.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6d6194ec-9471-41a3-922f-3e5e4f8ff494/Untitled.png)

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
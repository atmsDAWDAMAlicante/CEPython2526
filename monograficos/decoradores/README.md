# DECORADORES en Python: notas

## Ayuda facilitada por el ChatGPT:

### 1️⃣ ¿Qué es un decorador?

Una función que recibe otra función, la envuelve y añade comportamiento sin modificarla.

### 2️⃣ Estructura mínima (IMPRESCINDIBLE)
def decorador(func):
    def envoltorio(*args, **kwargs):
        # código extra
        return func(*args, **kwargs)
    return envoltorio


✔️ Tres niveles
✔️ El decorador devuelve la función envoltorio
✔️ El envoltorio llama a la función original

### 3️⃣ ¿Qué hace el decorador?

👉 Cosas transversales:
Validar datos
Convertir tipos
Mostrar mensajes
Medir tiempo
Controlar errores

❌ NO debería:
Pedir input()
Hacer la lógica principal

4️⃣ ¿Qué hace la función decorada?

👉 Su trabajo real:
Calcular
Mostrar resultados
Modificar datos
Retornar valores

5️⃣ ¿Por qué usar decoradores?

Para no repetir código y mantener la lógica limpia.
Si copias/pegas el mismo try/except varias veces → decorador.


#Un decorador permite añadir funcionalidad a varias funciones sin modificar su código, usando funciones de orden superior.
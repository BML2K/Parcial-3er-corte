"""
Sistema de Control de Inventario y Precios (Encapsulamiento y @property)
"""

class Producto:
    def __init__(self, nombre, precios_historicos: list = None):
        self._nombre = nombre
        
        if precios_historicos is None:
            self._precios_historicos = []
        else:
            self._precios_historicos = precios_historicos
        
        self._precio = (
            self._precios_historicos[-1]["precio"]
            if self._precios_historicos
            else None
        )

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if not 0 <= valor <= 10_000:
            raise ValueError("El precio debe estar entre $0 y $10,000.")

        self._precio = valor
        self._precios_historicos.append({"nombre": self._nombre, "precio": valor})

    def registrar_precio(self, precio: float):
        self.precio = precio
        
        
    def obtener_historial(self):
        return self._precios_historicos

    def precio_promedio(self):
        if not self._precios_historicos:
            return None

        total = sum(registro["precio"] for registro in self._precios_historicos)
        return f"precio promedio: {total / len(self._precios_historicos):.2f}"


"""
MAIN
"""

productos = []

cantidad = int(input("¿Cuántos productos vas a ingresar? "))

for _ in range(cantidad):
    nombre = input("Nombre del producto: ")
    producto = Producto(nombre)
    cantidad_precios = int(input(f"¿Cuántos precios registrarás para {nombre}? "))

    for indice in range(cantidad_precios):
        precio = float(input(f"Precio {indice + 1} de {nombre}: "))
        producto.registrar_precio(precio)

    productos.append(producto)

for producto in productos:
    print(producto.obtener_historial())
    print(producto.precio_promedio())

precios = [
    registro["precio"]
    for producto in productos
    for registro in producto.obtener_historial()
]

if precios:
    promedio_general = sum(precios) / len(precios)
    print(f"precio promedio general: {promedio_general:.2f}")
else:
    print("No hay precios registrados.")

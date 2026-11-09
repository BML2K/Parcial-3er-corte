"""
Sistema de Cotización de Envíos (Herencia y Polimorfismo)
"""

class Envio:
    def __init__(self, peso_kg: float, distancia_km: float):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base: float) -> float:
        raise NotImplementedError("Las subclases deben definir el cálculo del costo.")


class EnvioEstandar(Envio):
    def calcular_costo(self, monto_base: float) -> float:
        return monto_base * 1.05


class EnvioExpress(Envio):
    def calcular_costo(self, monto_base: float) -> float:
        return monto_base * 1.15


envios = [
    EnvioEstandar(peso_kg=2.5, distancia_km=120),
    EnvioExpress(peso_kg=1.2, distancia_km=60),
]

monto_base = 100.0
for envio in envios:
    tipo_envio = type(envio).__name__
    costo = envio.calcular_costo(monto_base)
    print(f"{tipo_envio}: ${costo:.2f}")



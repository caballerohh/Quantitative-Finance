import numpy as 
from scipy.stats import norm
import matplotlib.pyplot as plt

# Parámetros
F0 = 200      # Precio del futuro del café
K = 200       # Strike de la opción
r = 0.05      # Tasa libre de riesgo
sigma = 0.20  # Volatilidad
T = 1         # Tiempo en años
capital_total = 1000  # Monto total invertido (ej. $1000)

# 1. Valor presente del bono cupón cero
PV_bono = capital_total * np.exp(-r * T)

# 2. Modelo de Black (precio de la opción call sobre futuros)
d1 = (np.log(F0 / K) + 0.5 * sigma ** 2 * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
N_d1 = norm.cdf(d1)
N_d2 = norm.cdf(d2)
call_price = np.exp(-r * T) * (F0 * N_d1 - K * N_d2)

# 3. Presupuesto disponible para opciones
presupuesto_opciones = capital_total - PV_bono
cantidad_opciones = presupuesto_opciones / call_price

# 4. Simular valor final del producto estructurado según escenarios del futuro del café
precios_futuros = np.linspace(150, 250, 100)
ganancia_opcion = np.maximum(precios_futuros - K, 0)
retorno_cliente = PV_bono + cantidad_opciones * 0.5 * ganancia_opcion  # Participación del 50%

# Mostrar resultados clave
print("Valor presente del bono cupón cero (protección capital): ${:.2f}".format(PV_bono))
print("Precio de la call (modelo Black): ${:.2f}".format(call_price))
print("Cantidad de opciones compradas: {:.2f}".format(cantidad_opciones))
print("Presupuesto para opciones: ${:.2f}".format(presupuesto_opciones))

# 5. Gráfico del valor del producto estructurado
plt.figure(figsize=(10,6))
plt.plot(precios_futuros, retorno_cliente, label='Valor estructurado al vencimiento', color='green')
plt.axhline(capital_total, color='gray', linestyle='--', label='Capital protegido')
plt.xlabel('Precio del Futuro del Café al Vencimiento')
plt.ylabel('Valor del Producto Estructurado ($)')
plt.title('Simulación de Producto Estructurado con Participación del 50% en la Subida del Café')
plt.legend()
plt.grid(True)
plt.show()

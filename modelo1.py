import numpy as np
import matplotlib.pyplot as plt

# Parámetros iniciales
T = 30  # Duración de la simulación en días
U_iniciales = 1000  # Usuarios activos iniciales
r_base = 0.9  # Tasa de retención base
c_base = 0.05  # Tasa de conversión base
k_base = 0.2  # K-Factor base
presupuesto_marketing = 1000  # Presupuesto total para marketing
presupuesto_mejoras = 500  # Presupuesto total para mejoras
presupuesto_viralidad = 200  # Presupuesto para estrategias de viralidad

# Coeficientes para el impacto de las inversiones
alpha = 0.01  # Impacto de engagement en la retención
beta = 0.02  # Impacto de mejoras en la retención
gamma = 0.03  # Impacto de marketing en la conversión
delta = 0.05  # Impacto de estrategias de viralidad en el K-factor

# Variables para almacenar resultados
usuarios_activos = [U_iniciales]
usuarios_nuevos = []
usuarios_fuga = []
visitantes_diarios = 500  # Visitantes diarios fijos

# Simulación de la dinámica
for t in range(1, T + 1):
    # Cálculo del engagement (puede variar en función del tiempo o mantenerse constante)
    engagement = np.random.uniform(0.5, 1.0)
    
    # Actualización de tasas en función de las inversiones
    r_t = r_base + alpha * engagement + beta * (presupuesto_mejoras / T)
    c_t = c_base + gamma * (presupuesto_marketing / T)
    k_t = k_base + delta * (presupuesto_viralidad / T)
    
    # Cálculo de usuarios nuevos, activos y fuga de usuarios
    nuevos = int(usuarios_activos[-1] * k_t + visitantes_diarios * c_t)
    fuga = int(usuarios_activos[-1] * (1 - r_t))
    activos = usuarios_activos[-1] + nuevos - fuga

    # Almacenamiento de los resultados
    usuarios_activos.append(activos)
    usuarios_nuevos.append(nuevos)
    usuarios_fuga.append(fuga)

# Generación de gráficos
plt.figure(figsize=(12, 6))
plt.plot(range(T + 1), usuarios_activos, label="Usuarios Activos")
plt.plot(range(1, T + 1), usuarios_nuevos, label="Usuarios Nuevos", linestyle="--")
plt.plot(range(1, T + 1), usuarios_fuga, label="Fuga de Usuarios", linestyle="--")
plt.xlabel("Días")
plt.ylabel("Número de Usuarios")
plt.title("Simulación de Crecimiento y Engagement de Usuarios")
plt.legend()
plt.show()

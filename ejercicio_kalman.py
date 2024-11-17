import numpy as np



dt = 1.0  # Intervalo de tiempo

# Matrices de transición y observación
F = np.array([[1, 0, dt, 0],
              [0, 1, 0, dt],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
H = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0]])

# Proceso de ruido
sum_x = 0.1 * np.eye(4)  # Covarianza del ruido del proceso
sum_t = 0.1 * np.eye(4)  # Matriz de covarianza inicial

# Ruido de medición
sum_z = 0.1 * np.eye(2)  # Covarianza del ruido de medición

# Condiciones iniciales
x0 = np.array([[0],
               [0],
               [0],
               [0]])  
# Estado t = 1

sum_t = 0.1 * np.eye(4)  # Matriz de covarianza inicial

# Tiempo t = 1

# Predicción
x_t1 = np.dot(F, x0)
P = np.dot(F, np.dot(sum_t, F.T)) + sum_x

# Medición
z1 = np.array([[1],
               [1]])  # Valor medido en t = 1

# Ganancia de Kalman
K1 = np.dot(P, np.dot(H.T, np.linalg.inv(np.dot(H, np.dot(P, H.T)) + sum_z)))

# Actualización
x1 = x_t1 + np.dot(K1, (z1 - np.dot(H, x_t1)))

# Tiempo t = 2

# Predicción
x_t2 = np.dot(F, x1)


# Medición
z2 = np.array([[2],
               [1.8]])  # Valor medido en t = 2

# Ganancia de Kalman
K2 = np.dot(P, np.dot(H.T, np.linalg.inv(np.dot(H, np.dot(P, H.T)) + sum_z)))

# Actualización
x2 = x_t2 + np.dot(K2, (z2 - np.dot(H, x_t2)))


print("\nMatriz de transición:")
print(F)

print("\nMatriz de observación:")
print(H)

print("\nCovarianza del ruido del proceso:")
print(sum_x)

print("\nCovarianza del ruido de medición:")
print(sum_z)

print("\nEstado inicial t = 0:")
print(x0)

print("\nMatriz de covarianza inicial:")
print(sum_t)

print("\nValor medido en t = 1:")
print(z1)

print("\nValor medido en t = 2:")
print(z2)

print("\nPredicción en t = 1:")
print(x_t1)

print("\nPredicción en t = 2:")
print(x_t2)

print("\nGanancia de Kalman en t = 1:")
print(K1)
print("\nMu en t = 1:")
print(x1)
print("\nGanancia de Kalman en t = 2:")
print(K2)
print("\nMu en t = 2:")
print(x2)



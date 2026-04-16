import matplotlib.pyplot as plt

# Número de neuronas
input_neurons = 10
hidden_neurons = 128
output_neurons = 2

fig, ax = plt.subplots(figsize=(10, 8))

# Dibujar neuronas
for i in range(input_neurons):
    ax.scatter(0, i)

for i in range(hidden_neurons):
    ax.scatter(1, i)

for i in range(output_neurons):
    ax.scatter(2, i)

# Conexiones (esto es pesado)
for i in range(input_neurons):
    for j in range(hidden_neurons):
        ax.plot([0,1], [i,j], linewidth=0.1)

for i in range(hidden_neurons):
    for j in range(output_neurons):
        ax.plot([1,2], [i,j], linewidth=0.1)

ax.axis('off')
plt.show()
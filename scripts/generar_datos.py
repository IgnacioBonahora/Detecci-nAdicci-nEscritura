import numpy as np
import pandas as pd

np.random.seed(42)

# Número de muestras
num_samples = 1000

# Función para generar tiempos de escritura (en segundos)
def generate_typing_times(mean, stddev, size):
    return np.random.normal(loc=mean, scale=stddev, size=size)

# Generar datos sintéticos
data = {
    'writing_speed': np.concatenate([
        generate_typing_times(mean=0.2, stddev=0.05, size=int(num_samples * 0.5)),  # No adictivo
        generate_typing_times(mean=0.1, stddev=0.02, size=int(num_samples * 0.5))   # Adictivo
    ]),
    'errors': np.concatenate([
        np.random.poisson(lam=2, size=int(num_samples * 0.5)),  # No adictivo
        np.random.poisson(lam=5, size=int(num_samples * 0.5))    # Adictivo
    ]),
    'pauses': np.concatenate([
        generate_typing_times(mean=1.0, stddev=0.2, size=int(num_samples * 0.5)),  # No adictivo
        generate_typing_times(mean=0.5, stddev=0.1, size=int(num_samples * 0.5))   # Adictivo
    ]),
    'pattern_variability': np.concatenate([
        np.random.uniform(low=0.1, high=0.3, size=int(num_samples * 0.5)),  # No adictivo
        np.random.uniform(low=0.4, high=0.6, size=int(num_samples * 0.5))   # Adictivo
    ]),
    'label': np.concatenate([
        np.zeros(int(num_samples * 0.5)),  # No adictivo
        np.ones(int(num_samples * 0.5))    # Adictivo
    ])
}

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar datos
df.to_csv('C:/Users/Admin/Desktop/Red Neuronal/datos/synthetic_typing_data.csv', index=False)

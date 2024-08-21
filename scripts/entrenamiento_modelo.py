import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import tensorflow as tf

# Cargar el archivo CSV
df = pd.read_csv('C:/Users/Admin/Desktop/Red Neuronal/datos/synthetic_typing_data.csv')

# Separar características (X) y etiquetas (y)
X = df.drop(columns=['label']).values  # Características
y = df['label'].values  # Etiquetas

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
model = Sequential()

# Capa de entrada: 4 neuronas para las 4 características
model.add(Dense(64, input_dim=4, activation='relu'))

# Capas ocultas
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))  # Dropout para prevenir sobreajuste

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

# Capa de salida: 1 neurona con activación sigmoide para clasificación binaria
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
metrics=['accuracy'])

# Entrenamiento
history = model.fit(X_train, y_train,
                    epochs=50,  # Ajustable según los resultados
                    batch_size=32,
                    validation_data=(X_test, y_test))

# Evaluación
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Pérdida: {loss}, Precisión: {accuracy}')

# Predicciones
predicciones = model.predict(X_test)
umbral = 0.5
etiquetas_predichas = (predicciones > umbral).astype(int)
print("Predicciones (primeras 10):", etiquetas_predichas[:10])

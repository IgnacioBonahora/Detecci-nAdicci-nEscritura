# Detección de Adicción mediante Patrones de Escritura

## Descripción

Este proyecto tiene como objetivo el análisis de patrones de escritura para la detección de comportamientos adictivos en apuestas en línea utilizando redes neuronales. Desarrollado por **Ignacio Bonahora**, estudiante de tercer año en la **Universidad del Aconcagua**, este proyecto se basa en la generación de datos sintéticos para entrenar un modelo de clasificación que pueda identificar señales de adicción a partir de los patrones de escritura del usuario.

## Estructura del Proyecto

- **Generación de Datos Sintéticos**: Scripts para crear datos de escritura simulados que imitan comportamientos adictivos y no adictivos.
- **Entrenamiento del Modelo**: Implementación y entrenamiento de una red neuronal para clasificar los patrones de escritura.
- **Evaluación del Modelo**: Métodos para evaluar la precisión y el rendimiento del modelo.


## Explicación de la Salida
En la salida del modelo, los valores [1] y [0] tienen el siguiente significado:

[1]: Indica que el modelo ha clasificado el patrón de escritura como adictivo. Esto significa que el comportamiento de escritura detectado sugiere una posible adicción a las apuestas en línea.

[0]: Indica que el modelo ha clasificado el patrón de escritura como no adictivo. Esto sugiere que el comportamiento de escritura detectado no muestra señales claras de adicción.

## Requisitos

Asegúrate de tener instalados los siguientes paquetes:

- `numpy`
- `pandas`
- `tensorflow`
- `scikit-learn`

Puedes instalar estos paquetes usando `pip`:

```bash
pip install numpy pandas tensorflow scikit-learn






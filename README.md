# Predictor de Problemas Cardiacos

Este es un modelo de predicción desarrollado utilizando **Streamlit**, **scikit-learn**, y un modelo de máquina de soporte vectorial (**SVC**) entrenado con datos sobre edad y colesterol. La aplicación predice si una persona sufrirá problemas cardíacos en función de estos dos parámetros.

## Características

- **Entrada**: Edad (entre 25 y 80 años) y Nivel de Colesterol (entre 120 y 600).
- **Modelo**: SVC entrenado con los datos normalizados usando **MinMaxScaler**.
- **Resultado**: Predicción binaria (0 o 1):
  - **0**: No sufrirá problemas cardíacos.
  - **1**: Sufrirá problemas cardíacos.
- **Interfaz**: Se puede interactuar con los parámetros mediante sliders para ajustarlos de manera dinámica.
- **Visualización**: Dependiendo de la predicción, la aplicación mostrará una imagen que corresponde al resultado de la predicción.

## Instalación

### Requisitos

1. **Python 3.x**
2. **Dependencias**: Usa el archivo `requirements.txt` para instalar las dependencias necesarias.

### Pasos de instalación

1. Clona o descarga este repositorio en tu máquina local.
2. Instala las dependencias desde el archivo `requirements.txt` ejecutando el siguiente comando en tu terminal:

    ```bash
    pip install -r requirements.txt
    ```

3. Coloca los archivos `svc_model.jb` y `scaler.jb` en el mismo directorio que el archivo `app.py`.
4. Ejecuta la aplicación de Streamlit:

    ```bash
    streamlit run app.py
    ```

5. Abre tu navegador y ve a la URL indicada (por defecto `http://localhost:8501`) para interactuar con la aplicación.

## Uso

1. **Ajusta los sliders** para seleccionar la edad y el nivel de colesterol.
2. **Haz clic en "Predicción"** para obtener el resultado. Si la predicción es positiva (1), te mostrará una imagen relacionada con los problemas cardíacos. Si la predicción es negativa (0), se mostrará una imagen de una persona disfrutando de la vida.

## Estructura del Proyecto

- `app.py`: Código principal de la aplicación Streamlit.
- `svc_model.jb`: Modelo SVC entrenado y guardado con **joblib**.
- `scaler.jb`: Escalador MinMaxScaler usado para normalizar los datos de entrada.
- `requirements.txt`: Archivo que contiene las dependencias necesarias para ejecutar el proyecto.

## Tecnologías Usadas

- **Streamlit**: Para la creación de la interfaz web interactiva.
- **scikit-learn**: Para la creación y el entrenamiento del modelo SVC.
- **joblib**: Para guardar y cargar el modelo y el escalador.
- **numpy y pandas**: Para manejar y procesar los datos.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.

---

**Elaborado por ® UNAB 2025**


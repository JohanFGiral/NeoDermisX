# NeoDermisX

**Red Neuronal Convolucional para la clasificación binaria de lesiones cutáneas en imágenes dermatoscópicas**

Proyecto de grado — Universidad Antonio Nariño  
Programa: Tecnología en Construcción de Software  
Facultad de Ingeniería de Sistemas  
Bogotá, Colombia — 2026

---

## Descripción general

NeoDermisX es una aplicación web orientada a la detección temprana de cáncer de piel, desarrollada como proyecto de grado en la Universidad Antonio Nariño. El sistema integra una Red Neuronal Convolucional (CNN) entrenada para clasificar imágenes dermatoscópicas en dos categorías: **benigno** o **maligno**, entregando además un nivel de confianza asociado a cada predicción.

El proyecto surge como respuesta a una problemática real del sistema de salud colombiano: la escasez de dermatólogos especializados, los largos tiempos de espera para diagnóstico y la limitada cobertura en zonas rurales. NeoDermisX no reemplaza el criterio clínico profesional, sino que funciona como herramienta de apoyo para tamizaje temprano y toma de decisiones médicas.

---

## Características principales

- Clasificación binaria de lesiones cutáneas (benigno / maligno) mediante CNN
- Interfaz web funcional con carga de imágenes por arrastre o selección de archivo
- Visualización del diagnóstico y nivel de confianza en tiempo real
- Exportación del resultado en formato PDF
- Arquitectura modular con separación de BackEnd, FrontEnd e IA
- Despliegue mediante Docker Compose

---

## Arquitectura del modelo

El modelo utiliza una arquitectura basada en **EfficientNetB0** preentrenado con pesos de ImageNet, adaptado para clasificación binaria mediante las siguientes capas:

| Capa | Tipo | Parámetros | Activación |
|------|------|------------|------------|
| 1 | EfficientNetB0 | (7,7,1280) canales | Interna |
| 2 | GlobalAveragePooling2D | 1280 características | — |
| 3 | Dense | 128 neuronas | ReLU |
| 4 | Dropout | 0.5 | — |
| 5 | Dense (Salida) | 2 neuronas | Softmax |

**Optimizador:** Adam (`lr=0.0001`)  
**Función de pérdida:** Sparse Categorical Crossentropy  
**Métrica principal:** Accuracy

---

## Métricas obtenidas

El modelo seleccionado (NeoDermisXV1) fue evaluado sobre un conjunto de prueba independiente de **3.908 imágenes**, obteniendo los siguientes resultados:

| Métrica | Resultado |
|---------|-----------|
| Precisión (Accuracy) | 76% |
| Sensibilidad | 73.6% |
| Especificidad | 78.1% |

Estos resultados superan el umbral mínimo del 60% establecido en los objetivos del proyecto.

---

## Dataset

El modelo fue entrenado con imágenes provenientes de bases de datos públicas:

- **HAM10000**
- **ISIC 2019**
- **MILK10K**

Total de imágenes utilizadas: **19.612** (distribuidas equitativamente entre clases benigno y maligno)  
División de datos: 80% entrenamiento / 20% prueba  
Subdivisión de entrenamiento: 70% entrenamiento / 15% validación / 15% prueba

---

## Tecnologías utilizadas

### Inteligencia Artificial
- Python 3.14.0
- TensorFlow 2.21.0
- Keras 3.14.0
- Pandas 3.0.2
- Scikit-learn

### BackEnd
- Python
- Flask

### FrontEnd
- HTML5
- CSS3
- JavaScript
- jsPDF (exportación de reportes)

### Infraestructura
- Docker
- Docker Compose

---

## Estructura del repositorio

```
NeoDermisX/
├── BackEnd/               # Servidor Flask y lógica de procesamiento
├── FrontEnd/              # Interfaz web (HTML, CSS, JS)
├── IA/                    # Scripts de entrenamiento, modelo y datos
│   ├── model.py           # Arquitectura de la red neuronal
│   ├── train.py           # Proceso de entrenamiento
│   ├── data.py            # Preparación y normalización del dataset
│   ├── config.py          # Constantes y parámetros de configuración
│   └── prueba.py          # Script de evaluación de modelos
├── logs/                  # Registros de entrenamiento
├── NeoDermisXV1.h5        # Modelo seleccionado (mejor desempeño)
├── NeoDermisXV2-V9.h5     # Versiones alternativas del modelo
├── docker-compose.yml     # Configuración de despliegue
└── README.md
```

---

## Instalación y uso

### Requisitos previos

- Docker y Docker Compose instalados
- Python 3.14 (para ejecución local sin Docker)

### Despliegue con Docker

```bash
git clone https://github.com/JohanFGiral/NeoDermisX.git
cd NeoDermisX
docker-compose up --build
```

La aplicación estará disponible en `http://localhost` una vez iniciado el contenedor.

### Ejecución local (sin Docker)

```bash
cd BackEnd
python -m venv venv
.\venv\Scripts\activate        # Windows
source venv/bin/activate       # Linux / macOS

pip install -r requirements.txt
python app.py
```

---

## Uso de la aplicación

1. Acceder a la interfaz web desde el navegador
2. Cargar una imagen dermatoscópica en formato JPG o PNG
3. Presionar **"Continuar Proceso"** para iniciar el análisis
4. Visualizar el diagnóstico (Benigno / Maligno) y el nivel de confianza
5. Descargar el reporte en formato PDF si se requiere

---

## Consideraciones importantes

> **NeoDermisX es una herramienta de apoyo clínico y no reemplaza el diagnóstico médico profesional.** Los resultados deben ser interpretados por personal de salud calificado. El sistema no está certificado para uso clínico real ni integrado con sistemas hospitalarios.

---

## Metodología de desarrollo

El proyecto fue desarrollado bajo la metodología ágil **Scrum**, organizada en 4 sprints:

- **Sprint 1:** Recolección de datos y definición de métricas
- **Sprint 2:** Limpieza de datos, normalización y diseño del modelo
- **Sprint 3:** Entrenamiento y generación de versiones del modelo
- **Sprint 4:** Evaluación de métricas, desarrollo web e integración

---

## Autor

**Johan Nicolas Forero Giral**  
Estudiante de Tecnología en Construcción de Software  
Universidad Antonio Nariño — Bogotá, Colombia  
Director: Ph.D. Juan Camilo Ramírez  
Línea de Investigación: Inteligencia Artificial Computacional

---

## Licencia

Este proyecto fue desarrollado con fines académicos e investigativos. Para uso, distribución o modificación, contactar al autor.

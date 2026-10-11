import random
import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="Quiz de Machine Learning", page_icon="🤖", layout="centered"
)

# Banco con 10 preguntas sobre Machine Learning (Nivel Básico)
BANCO_PREGUNTAS = [
    {
        "pregunta": "¿Qué es el Aprendizaje Supervisado?",
        "opciones": [
            "Entrenamiento con datos que incluyen etiquetas o respuestas correctas",
            "Entrenamiento sin datos etiquetados, buscando patrones ocultos",
            "Entrenamiento mediante recompensas y castigos en un entorno",
            "Un algoritmo que no requiere datos para aprender",
        ],
        "respuesta_correcta": "Entrenamiento con datos que incluyen etiquetas o respuestas correctas",
    },
    {
        "pregunta": "¿Cuál de las siguientes tareas es un problema de Clasificación?",
        "opciones": [
            "Determinar si un correo es 'Spam' o 'No Spam'",
            "Predecir el precio de una casa el próximo año",
            "Calcular la temperatura máxima de mañana",
            "Agrupar clientes por sus hábitos de compra sin etiquetas previas",
        ],
        "respuesta_correcta": "Determinar si un correo es 'Spam' o 'No Spam'",
    },
    {
        "pregunta": "¿Cuál de las siguientes tareas es un problema de Regresión?",
        "opciones": [
            "Predecir la estatura exacta de una persona en centímetros",
            "Identificar si una imagen contiene un perro o un gato",
            "Detectar si una transacción bancaria es fraudulenta o no",
            "Clasificar sentimientos en comentarios como positivos o negativos",
        ],
        "respuesta_correcta": "Predecir la estatura exacta de una persona en centímetros",
    },
    {
        "pregunta": "¿Qué busca el Aprendizaje No Supervisado?",
        "opciones": [
            "Descubrir estructuras o agrupaciones inherentes en datos no etiquetados",
            "Aprender a jugar ajedrez mediante ensayo y error",
            "Predecir una variable continua basada en datos de entrenamiento",
            "Asegurar que todas las predicciones sean 100% exactas",
        ],
        "respuesta_correcta": "Descubrir estructuras o agrupaciones inherentes en datos no etiquetados",
    },
    {
        "pregunta": "¿Qué es el 'Overfitting' (Sobreajuste)?",
        "opciones": [
            "Cuando el modelo memoriza el ruido del entrenamiento y falla con datos nuevos",
            "Cuando el modelo es demasiado simple y no aprende los patrones básicos",
            "Cuando los datos de entrenamiento están completamente limpios",
            "Cuando un algoritmo se ejecuta más rápido de lo normal",
        ],
        "respuesta_correcta": "Cuando el modelo memoriza el ruido del entrenamiento y falla con datos nuevos",
    },
    {
        "pregunta": "¿Qué técnica se utiliza habitualmente para el Aprendizaje No Supervisado?",
        "opciones": [
            "Clustering (por ejemplo, K-Means)",
            "Regresión Lineal",
            "Regresión Logística",
            "Árboles de Decisión para clasificación",
        ],
        "respuesta_correcta": "Clustering (por ejemplo, K-Means)",
    },
    {
        "pregunta": "¿Qué representa el conjunto de prueba (Test set)?",
        "opciones": [
            "Datos no vistos durante el entrenamiento usados para evaluar el rendimiento final",
            "Los datos usados exclusivamente para ajustar los parámetros del modelo",
            "Un subconjunto de datos para limpiar valores nulos",
            "La base de datos original sin procesar",
        ],
        "respuesta_correcta": "Datos no vistos durante el entrenamiento usados para evaluar el rendimiento final",
    },
    {
        "pregunta": "¿Qué tipo de aprendizaje utiliza recompensas para guiar al agente?",
        "opciones": [
            "Aprendizaje por Refuerzo",
            "Aprendizaje Supervisado",
            "Aprendizaje No Supervisado",
            "Aprendizaje Auto-supervisado",
        ],
        "respuesta_correcta": "Aprendizaje por Refuerzo",
    },
    {
        "pregunta": "¿Qué es una 'Feature' (Característica) en Machine Learning?",
        "opciones": [
            "Una variable de entrada o propiedad cuantitativa/cualitativa usada para hacer predicciones",
            "El resultado final que entrega el modelo",
            "El tiempo que tarda un modelo en entrenar",
            "El porcentaje de error del algoritmo",
        ],
        "respuesta_correcta": "Una variable de entrada o propiedad cuantitativa/cualitativa usada para hacer predicciones",
    },
    {
        "pregunta": "¿Cuál es la función principal de la Matriz de Confusión?",
        "opciones": [
            "Evaluar el desempeño de un modelo de clasificación mostrando aciertos y errores",
            "Calcular la pendiente en una regresión lineal",
            "Eliminar registros duplicados en un dataset",
            "Agrupar datos en clústeres no etiquetados",
        ],
        "respuesta_correcta": "Evaluar el desempeño de un modelo de clasificación mostrando aciertos y errores",
    },
]

# Inicialización del estado de la sesión (Session State)
if "preguntas_seleccionadas" not in st.session_state:
    # Selecciona 5 preguntas al azar
    preguntas_muestra = random.sample(BANCO_PREGUNTAS, 5)

    # Mezcla las opciones de cada pregunta para que no siempre aparezcan en el mismo orden
    preguntas_preparadas = []
    for item in preguntas_muestra:
        opciones = item["opciones"].copy()
        random.shuffle(opciones)
        preguntas_preparadas.append(
            {
                "pregunta": item["pregunta"],
                "opciones": opciones,
                "respuesta_correcta": item["respuesta_correcta"],
            }
        )

    st.session_state.preguntas_seleccionadas = preguntas_preparadas
    st.session_state.evaluado = False

# Título y descripción
st.title("🤖 Quiz Básico de Machine Learning")
st.write(
    "Responde a las siguientes 5 preguntas aleatorias sobre los fundamentos de ML."
)
st.divider()

# Formulario para responder
with st.form("quiz_form"):
    respuestas_usuario = {}

    for idx, q in enumerate(st.session_state.preguntas_seleccionadas):
        st.subheader(f"{idx + 1}. {q['pregunta']}")
        respuestas_usuario[idx] = st.radio(
            "Selecciona tu respuesta:",
            q["opciones"],
            key=f"p_{idx}",
            index=None,
        )
        st.write("")

    boton_enviar = st.form_submit_button("Enviar respuestas")

# Procesamiento al hacer clic en Enviar
if boton_enviar:
    # Verificar si respondió todas
    if any(resp is None for resp in respuestas_usuario.values()):
        st.warning(
            "Por favor responde todas las preguntas antes de enviar."
        )
    else:
        puntaje = 0
        total_preguntas = len(st.session_state.preguntas_seleccionadas)

        st.subheader("Resultados:")

        for idx, q in enumerate(st.session_state.preguntas_seleccionadas):
            respuesta_correcta = q["respuesta_correcta"]
            respuesta_dada = respuestas_usuario[idx]

            if respuesta_dada == respuesta_correcta:
                puntaje += 1
                st.success(f"**Pregunta {idx + 1}:** Correcto ✅")
            else:
                st.error(
                    f"**Pregunta {idx + 1}:** Incorrecto ❌ — La respuesta correcta era: *{respuesta_correcta}*"
                )

        st.divider()
        st.write(f"### Tu puntaje: **{puntaje} / {total_preguntas}**")

        # Animación si todas son correctas
        if puntaje == total_preguntas:
            st.balloons()
            st.snow()
            st.success(
                "🎉 ¡Excelente trabajo! Respondiste todas las preguntas correctamente."
            )
        elif puntaje >= 3:
            st.info("¡Buen intento! Tienes buenos fundamentos de ML.")
        else:
            st.warning("Sigue repasando los conceptos básicos de ML.")

        st.session_state.evaluado = True

# Botón para reiniciar con un nuevo conjunto de preguntas
if st.button("Reintentar con preguntas nuevas"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

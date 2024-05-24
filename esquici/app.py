import streamlit as st
from scipy.stats import binom, poisson
import numpy as np

def calcular_probabilidad_binomial(n, p, x):
    probabilidad = binom.pmf(x, n, p)
    return probabilidad

def calcular_probabilidad_poisson(lmbda, k):
    probabilidad = poisson.pmf(k, lmbda)
    return probabilidad

def simular_cadena_markov(estados, transiciones, pasos):
    estado_actual = 0  # Asumimos que el estado inicial es el primero
    historial = [estado_actual]

    for _ in range(pasos):
        estado_actual = np.random.choice(estados, p=transiciones[estado_actual])
        historial.append(estado_actual)
    
    return historial

def calcular_politica_valor_markov(estados, transiciones, recompensas, gamma, iteraciones):
    V = np.zeros(len(estados))
    
    for _ in range(iteraciones):
        V_prev = np.copy(V)
        for s in range(len(estados)):
            V[s] = max([sum([transiciones[s][a][s_prime] * (recompensas[s][a][s_prime] + gamma * V_prev[s_prime]) for s_prime in range(len(estados))]) for a in range(len(transiciones[s]))])
    
    return V

def simular_sistema_multiagente(agentes, interacciones):
    resultados = []
    for i in range(interacciones):
        resultado_interaccion = np.random.choice(agentes)
        resultados.append(resultado_interaccion)
    return resultados

st.title("Calculadoras Estadísticas")

# Seleccionar la aplicación
app_type = st.selectbox("Seleccione la aplicación", ["", "Distribución Binomial", "Distribución de Poisson", "Cadena de Markov", "Proceso de Decisión de Markov", "Simulador de Sistema Multiagente"])

if app_type == "Distribución Binomial":
    st.header("Distribución Binomial")
    n = st.number_input("Número de ensayos (n)", min_value=0, value=10)
    p = st.number_input("Probabilidad de éxito (p)", min_value=0.0, max_value=1.0, value=0.5)
    x = st.number_input("Número de éxitos (x)", min_value=0, value=5)
    
    if st.button("Calcular Probabilidad Binomial"):
        resultado = calcular_probabilidad_binomial(int(n), float(p), int(x))
        st.write(f"Resultado Binomial con n={n}, p={p}, x={x}: {resultado}")

elif app_type == "Distribución de Poisson":
    st.header("Distribución de Poisson")
    lmbda = st.number_input("Lambda (λ)", min_value=0.0, value=1.0)
    k = st.number_input("Número de eventos (k)", min_value=0, value=1)
    
    if st.button("Calcular Probabilidad de Poisson"):
        resultado = calcular_probabilidad_poisson(float(lmbda), int(k))
        st.write(f"Resultado Poisson con lambda={lmbda}, k={k}: {resultado}")

elif app_type == "Cadena de Markov":
    st.header("Cadena de Markov")
    estados = st.text_input("Ingrese los estados separados por comas (ej. 0,1,2)").split(',')
    transiciones = st.text_area("Ingrese la matriz de transiciones en formato CSV (ej. 0.1,0.9;0.5,0.5)").split(';')
    transiciones = [list(map(float, fila.split(','))) for fila in transiciones]
    pasos = st.number_input("Número de pasos a simular", min_value=1, value=10)
    
    if st.button("Simular Cadena de Markov"):
        resultado = simular_cadena_markov(estados, transiciones, pasos)
        st.write(f"Historial de estados: {resultado}")

elif app_type == "Proceso de Decisión de Markov":
    st.header("Proceso de Decisión de Markov")
    estados = st.text_input("Ingrese los estados separados por comas (ej. 0,1,2)").split(',')
    transiciones = st.text_area("Ingrese las matrices de transición por acción en formato CSV (ej. 0.1,0.9;0.5,0.5)").split(';')
    transiciones = [[list(map(float, accion.split(','))) for accion in estado.split(',')] for estado in transiciones]
    recompensas = st.text_area("Ingrese las matrices de recompensa por acción en formato CSV (ej. 1,-1;0,0)").split(';')
    recompensas = [[list(map(float, accion.split(','))) for accion in estado.split(',')] for estado in recompensas]
    gamma = st.number_input("Factor de descuento (γ)", min_value=0.0, max_value=1.0, value=0.9)
    iteraciones = st.number_input("Número de iteraciones", min_value=1, value=10)
    
    if st.button("Calcular Política de Valor"):
        resultado = calcular_politica_valor_markov(estados, transiciones, recompensas, gamma, iteraciones)
        st.write(f"Política de Valor: {resultado}")

elif app_type == "Simulador de Sistema Multiagente":
    st.header("Simulador de Sistema Multiagente")
    agentes = st.text_input("Ingrese los agentes separados por comas (ej. A,B,C)").split(',')
    interacciones = st.number_input("Número de interacciones", min_value=1, value=10)
    
    if st.button("Simular Sistema Multiagente"):
        resultado = simular_sistema_multiagente(agentes, interacciones)
        st.write(f"Resultados de las interacciones: {resultado}")

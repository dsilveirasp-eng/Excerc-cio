import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

st.title("🟢 Calculadora de Circunferência - Exercício")

st.write("Preencha os valores do problema:")

# Entradas do usuário
xE = st.number_input("Coordenada x do ponto E", value=9.0)
delta_x = st.number_input("Deslocamento horizontal de E até G", value=12.0)
delta_y = st.number_input("Deslocamento vertical de E até G", value=16.0)

# Variáveis simbólicas
y, r = sp.symbols('y r', real=True)

# Coordenadas
E = (xE, y)
G = (xE + delta_x, y - delta_y)

# Equações da circunferência
eq1 = sp.Eq(E[0]**2 + E[1]**2, r**2)
eq2 = sp.Eq(G[0]**2 + G[1]**2, r**2)

# Resolver sistema
sol = sp.solve((eq1, eq2), (y, r))

# Mostrar resultados e gráfico
if sol:
    st.subheader("✅ Solução encontrada")
    for s in sol:
        y_val = float(s[0])
        r_val = float(s[1])
        st.write(f"y = {y_val:.2f}, r = {r_val:.2f}")

        # Pontos
        E_point = (xE, y_val)
        G_point = (xE + delta_x, y_val - delta_y)

        # Gráfico
        fig, ax = plt.subplots()
        circle = plt.Circle((0, 0), r_val, fill=False, color="blue", linewidth=2)
        ax.add_artist(circle)

        # Plotar centro, pontos E e G
        ax.plot(0, 0, "ro", label="Centro B(0,0)")
        ax.plot(E_point[0], E_point[1], "go", label=f"E{E_point}")
        ax.plot(G_point[0], G_point[1], "mo", label=f"G{G_point}")

        # Ajustes do gráfico
        ax.set_aspect("equal")
        ax.set_xlim(-5, max(E_point[0], G_point[0]) + 10)
        ax.set_ylim(-5, max(E_point[1], G_point[1]) + 10)
        ax.axhline(0, color="gray", linewidth=0.5)
        ax.axvline(0, color="gray", linewidth=0.5)
        ax.set_title("Circunferência e Pontos E e G")
        ax.legend()

        st.pyplot(fig)

else:
    st.error("Não foi possível encontrar solução com os valores informados.")
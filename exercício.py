import streamlit as st
import sympy as sp

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

# Mostrar resultados
if sol:
    st.subheader("✅ Solução encontrada")
    for s in sol:
        st.write(f"y = {float(s[0]):.2f}, r = {float(s[1]):.2f}")
else:
    st.error("Não foi possível encontrar solução com os valores informados.")
import streamlit as st

st.title("MOON Calculator App")

data = st.text_input("Enter expression (like 1+11+3+5)")

def eval_expression(expr: str):
    expr = expr.replace(" ", "")  # spaces hatao
    try:
        return eval(expr)  # modulus ke liye % as default
    except Exception as e:
        return f"Error: {e}"

if st.button("Calculate"):
    result = eval_expression(data)
    st.success(f"Result: {result}")
else:
    st.info("Enter an expression and press Calculate")

st.write("---")
st.write("Developed by **Abdul Haseeb** - find me online by typing **abdulhaseeb0330**")

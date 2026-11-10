import streamlit as st

st.set_page_config(page_title="Python Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Interactive Python Calculator")
st.write("A clean and responsive calculator app built with Python and Streamlit.")

# Layout for number inputs
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter first number", value=0.0, format="%.4f")
with col2:
    num2 = st.number_input("Enter second number", value=0.0, format="%.4f")

# Operation selector
operation = st.selectbox(
    "Choose an operation", 
    ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"]
)

# Calculation logic
if st.button("Calculate", type="primary"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"**Result:** {num1} + {num2} = **{result}**")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"**Result:** {num1} - {num2} = **{result}**")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"**Result:** {num1} * {num2} = **{result}**")
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"**Result:** {num1} / {num2} = **{result}**")
        else:
            st.error("Error: Division by zero is not allowed.")

# Footer notes
st.markdown("---")
st.caption("Built with Python & Streamlit | Ready for GitHub")

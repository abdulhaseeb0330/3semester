import streamlit as st
import pandas as pd


data = pd.read_csv(r"D:\python projects\library.csv", sep="#", header=None, names=["symptoms", "medicines", "advice"])


def clean_list(cell):
    if pd.isna(cell):
        return []
    return [item.strip().lower() for item in str(cell).split(",")]


data["symptoms_list"] = data["symptoms"].apply(clean_list)
data["medicines_list"] = data["medicines"].apply(clean_list)
data["advice_list"] = data["advice"].apply(clean_list)

st.title("Universal Medical Recommendation Robot")

# User input text block sy ly ga
user_input = st.text_input("Enter symptoms, disease, medicine, or advice").lower().strip()

if user_input:
    matches = []

    for i, row in data.iterrows():
        if (user_input in row["symptoms_list"] or
            user_input in row["medicines_list"] or
            user_input in row["advice_list"]):
            matches.append(row)

    if matches:
        st.subheader("Related Information")
        for row in matches:
            st.markdown(f"**Symptoms:** {', '.join(row['symptoms_list'])}")
            st.markdown(f"**Medicines:** {', '.join(row['medicines_list'])}")
            st.markdown(f"**Advice:** {', '.join(row['advice_list'])}")
            st.markdown("---")
    else:
        st.warning("No match found Try another input")



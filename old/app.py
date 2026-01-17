import streamlit as st
import os

st.title("Moon File Making App")

choice = st.selectbox("Choose option", ["Create empty file","Copy file", "Write data (overwrite)","Create new file with data","Delete file"])

filename = st.text_input("Enter file name / path")
extra = st.text_area("Extra data (if needed)")

if st.button("Submit"):
    try:
        if choice == "Create empty file":
            with open(filename, "x"):
                pass
            st.success(f"Empty file created: {filename}")

        elif choice == "Copy file":
            src = filename
            dst = extra.strip()
            with open(src, "r") as f:
                content = f.read()
            with open(dst, "w") as nf:
                nf.write(content)
            st.success(f"Copied {src} → {dst}")

        elif choice == "Write data (overwrite)":
            with open(filename, "w") as f:
                f.write(extra)
            st.success(f"Data written to {filename}")

        elif choice == "Create new file with data":
            with open(filename, "x") as f:
                f.write(extra)
            st.success(f"File created with data: {filename}")

        elif choice == "Delete file":
            if os.path.exists(filename):
                os.remove(filename)
                st.success(f"File deleted: {filename}")
            else:
                st.error("File not found")

    except Exception as e:
        st.error(f"Error: {e}")
st.write("Developed by Abdul-Haseeb if you find me just type \"abdulhaseeb0330\" ")
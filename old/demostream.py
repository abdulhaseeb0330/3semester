# 📘 Streamlit Complete Cheatsheet (A to Z)
# ________________________________________
# 🔹 Text & Titles
import streamlit as st
import os
st.title("My App")
st.header("Section Header")
st.subheader("Subsection")
st.text("Simple text")
st.markdown("Markdown **bold** and *italic*")
st.caption("Small gray caption")
st.code("print('Hello')")
st.latex(r"E = mc^2")
st.divider()
# ________________________________________
# 🔹 Data Display
# st.table(df)              # Static table
# st.dataframe(df)          # Interactive table
# st.data_editor(df)        # Editable table
st.json({"a": 1, "b": 2})
st.metric("Sales", 100, 15)
# ________________________________________
# 🔹 Charts
# st.line_chart(df)
# st.bar_chart(df)
# st.area_chart(df)
# st.scatter_chart(df)      # Scatter chart
# st.map(df)                # Needs lat/lon columns
# st.altair_chart(chart)
# st.bokeh_chart(fig)
# st.graphviz_chart(graph)
# st.plotly_chart(fig)
# st.pydeck_chart(deck)
# st.pyplot(fig)
# st.vega_lite_chart(spec)
# ________________________________________
# 🔹 Media
# st.image("image.png", caption="Sample")
# st.audio("audio.mp3")
# st.video("video.mp4")
# st.logo("logo.png")
# ________________________________________
# 🔹 Input Widgets
st.button("Click Me")
st.download_button("Download", data="Hello", file_name="D:\python projects\demostream.py")
st.link_button("Go to Google", "https://google.com")
# st.page_link("D:\python projects\demostream.py", label="Go to Page 1")

st.checkbox("Accept")
st.radio("Pick one:", ["A", "B", "C"])
st.selectbox("Choose option", ["Option 1", "Option 2"])
st.multiselect("Pick multiple", ["A", "B", "C"])
st.segmented_control("Choose", ["A","B","C"])
st.pills("Select", ["A","B","C"])
st.toggle("On/Off")

st.slider("Slide", 0, 100, 50)
st.select_slider("Quality", ["Low", "Medium", "High"])
st.number_input("Enter number", 0, 100)

st.text_input("Enter text")
st.text_area("Write something")
st.chat_input("Type message")

st.date_input("Pick a date")
st.time_input("Pick a time")

st.file_uploader("Upload file")
st.audio_input("Record audio")
st.camera_input("Take a photo")
st.color_picker("Pick a color")
# st.feedback("How’s this?")
# ________________________________________
# 🔹 Layout & Containers
st.sidebar.title("Sidebar")
col1, col2 = st.columns(2)
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with st.expander("See more"):
    st.write("Hidden text")
with st.popover("More options"):
    st.write("Popover content")
# ________________________________________
# 🔹 Flow Control
# st.form("my_form")
# # st.form_submit_button("Submit")
# # @st.dialog("Dialog Example")
# def show_dialog(): st.write("Inside dialog")
# st.fragment("my_fragment")(lambda: st.write("Fragment"))
# st.navigation([st.Page("home.py", "🏠 Home")])
# st.switch_page("pages/page2.py")

# st.stop()
# st.rerun()
# ________________________________________
# 🔹 Status & Progress
st.progress(50)   # 0–100
# with st.spinner("Loading..."):
    # time.sleep(2)
# ________________________________________
# 🔹 Chat
st.chat_message("user").write("Hello")
st.chat_message("assistant").write("Hi there!")
st.chat_input("Say something...")
# ________________________________________
# 🔹 Run Commands
# streamlit run app.py
# streamlit hello
# streamlit cache clear
# streamlit config show
# streamlit version


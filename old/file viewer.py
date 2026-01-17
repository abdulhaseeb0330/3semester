# import streamlit as st
# import os
# import pandas as pd

# st.title("File Viewer App")
# file=st.file_uploader("Upload a file", type=None, key="file_uploader",accept_multiple_files=True)
# # type=[
# #         "csv","txt","xlsx","xls","json","xml","html","md","pdf",
# #         "png","jpg","jpeg","svg","gif","bmp","tiff","webp",
# #         "mp3","wav","ogg","flac","aac","m4a",
# #         "mp4","mov","avi","mkv","webm","wmv",
# #         "zip","rar","tar","gz","7z",
# #         "ppt","pptx","doc","docx","rtf","odt","odp","ods"
# #     ]
# st.write("## Uploaded File Content")
# if file is not None:
#     file_extension = os.path.splitext(file.name)[1].lower()
    
#     if file_extension == ".csv":
#         df = pd.read_csv(file)
#         st.dataframe(df)
        
#     elif file_extension == ".txt":
#         content = file.read().decode("utf-8")
#         st.text(content)
        
#     elif file_extension == ".xlsx":
#         df = pd.read_excel(file)
#         st.dataframe(df)
        
#     elif file_extension in [".png", ".jpg", ".jpeg"]:
#         st.image(file)
        
#     elif file_extension == ".pdf":
#         st.write("PDF viewing is not supported directly. Please download the file to view it.")
#         st.download_button(label="Download PDF", data=file, file_name=file.name, mime="application/pdf")
        
#     elif file_extension == ".doc":
#         st.write("DOC viewing is not supported directly. Please download the file to view it.")
#         st.download_button(label="Download DOC", data=file, file_name=file.name, mime="application/msword")
        
#     else:
#         st.write("Unsupported file type.")







import streamlit as st
import os
import pandas as pd

st.title("File Viewer App")

files = st.file_uploader(
    "Upload one or more files",
    type=None,
    key="file_uploader",
    accept_multiple_files=True
)

st.write("Uploaded File")

if files:
    for file in files:
        file_extension = os.path.splitext(file.name)[1].lower()
        st.subheader(file.name)

        if file_extension == ".csv":
            df = pd.read_csv(file)
            st.dataframe(df)

        elif file_extension == ".txt":
            content = file.read().decode("utf-8")
            st.text_area("Text File Content", content, height=200)

        elif file_extension in [".xlsx", ".xls"]:
            df = pd.read_excel(file)
            st.dataframe(df)

        elif file_extension in [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"]:
            st.image(file, caption=file.name, use_container_width=True)

        elif file_extension == ".pdf":
            st.download_button("Download PDF", data=file, file_name=file.name, mime="application/pdf")

        elif file_extension in [".doc", ".docx"]:
            mime = "application/msword" if file_extension == ".doc" else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            st.download_button("Download Word", data=file, file_name=file.name, mime=mime)

        elif file_extension in [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"]:
            st.audio(file)

        elif file_extension in [".mp4", ".mov", ".avi", ".mkv", ".webm", ".wmv"]:
            st.video(file)

        else:
            st.download_button("Download File", data=file, file_name=file.name)
        
        st.markdown("---")

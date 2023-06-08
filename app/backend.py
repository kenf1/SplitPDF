from pdf2image import convert_from_bytes
import streamlit as sl
from math import ceil
import zipfile
import base64

#display image in app
def display_images(img_list):
    #set 3 col w/ labels
    controls = sl.columns(3)
    with controls[0]:
        if len(img_list) >= 5:
            batch_size = sl.select_slider("Batch size:",range(10,len(img_list),10))
        else:
            batch_size = sl.select_slider("Batch size:",range(len(img_list),len(img_list)+2,1))
    with controls[1]:
        row_size = sl.select_slider("Row size:",range(1,6),value=5)
        num_batches = ceil(len(img_list)/batch_size)
    with controls[2]:
        page = sl.selectbox("Page",range(1,num_batches+1))
    #split img_list into batches
    batch = img_list[(page-1)*batch_size:page*batch_size]
    grid = sl.columns(row_size)
    col = 0
    for image in batch:
        with grid[col]:
            sl.image(image)
        col = (col+1) % row_size

#store all images in zip
def create_zip(img_list):
    with zipfile.ZipFile("images.zip","w") as zip_file:
        for i, image in enumerate(img_list):
            image.save(f"image{i+1}.jpg")
            zip_file.write(f"image{i+1}.jpg")

#download zip
def dl_zip():
    with open("images.zip","rb") as f:
        sl.download_button('Download Zip',f,file_name='images.zip')

#store all links
class links:
    gh_issue = "https://github.com/kenf1//issues"
    author = "App by: [KF](https://github.com/kenf1)"

#page config
def pg_config():
    sl.set_page_config(initial_sidebar_state="expanded",layout="wide",page_icon="📂",
                       menu_items={"Get help":None,
                                   "Report a Bug":links.gh_issue,
                                   "About":links.author})

#homepage layout    
def homepage():
    sl.set_page_config(initial_sidebar_state="expanded",layout="wide",page_icon="📂",
                       menu_items={"Get help":None,
                                   "Report a Bug":links.gh_issue,
                                   "About":links.author})
    
    uploaded_pdf = sl.file_uploader("Upload pdf file",type=".pdf")
    #split & display images only when pdf is uploaded/stored in RAM
    if uploaded_pdf is not None:
        sl.markdown("#### Pdf upload detected")
        pdf_bytes = uploaded_pdf.read()
        temp_img = convert_from_bytes(pdf_bytes)
        display_images(temp_img)
        create_zip(temp_img)
        dl_zip()

#sidebar layout        
def sidebar():
    sl.sidebar.title("Split PDF")
    sl.sidebar.subheader("An app to convert pdf file into series of png images")
    sl.sidebar.markdown("#### Instructions: \n 1. Upload a single pdf file \n 2. Wait for app to finishing processing \n 3. View/download images")
    sl.sidebar.markdown("#### Scoll to bottom of page for button to download all images as zip file.")
    sl.sidebar.markdown("## Created By: [KF](https://github.com/kenf1)")
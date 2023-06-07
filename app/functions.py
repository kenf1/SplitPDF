import os
from pdf2image import convert_from_path

def conversion(file_path,output_path):
    images = convert_from_path(file_path)

    if output_path[-1] != "/":
        output_path = f"{output_path}/"
    else:
        output_path = output_path
    
    #save each page in jpg format
    for i in range(len(images)):
        images[i].save(f"{output_path}"+"page"+str(i)+".jpg","JPEG")

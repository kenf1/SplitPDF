import os
from sys import platform
from pdf2image import convert_from_path

#use absolute path
def splitPDF(inputPath,outputPath):
    """split pdf into images

    Args:
        inputPath (str): path to pdf file
        outputPath (str): path to save jpg files
    """
    img = convert_from_path(inputPath)
    
    #append os specific folder seperator
    if platform == "linux" or platform == "darwin":
        output_path = folderSep(outputPath,"/")
    elif platform == "win32":
        output_path = folderSep(outputPath,"\\")
    
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    
    for i in range(len(img)):
        img[i].save(f"{output_path}"+"page"+str(i)+".jpg","JPEG")

#prompt user for inputPath & outputPath (option to save to parent dir)
def promptUser():
    inputPath = input("Path to pdf file: ")
    outputPath = input("Path to save output jpg: ")
    
    #enter anything for outputPath if plan on saving to parent directory
    parentDir = input("Enter `T` or `True` to save to parent directory: ")
    if parentDir == "T" or parentDir == "True":
        outputPath = os.path.split(inputPath)[0]
    
    splitPDF(inputPath,outputPath)
    print("Finished")

#add os specific folder seperator
def folderSep(outputPath,entry):
    if outputPath[-1] != entry:
        output_path = f"{outputPath}{entry}"
    return output_path

#run app
if __name__ == "__main__":
    promptUser()

import os
from pdf2image import convert_from_path

#use absolute path
def splitPDF(inputPath,outputPath):
    """split pdf into images

    Args:
        inputPath (str): path to pdf file
        outputPath (str): path to save jpg files
    """
    img = convert_from_path(inputPath)
    
    if outputPath[-1] != "/":
        output_path = f"{outputPath}/"
    else:
        output_path = outputPath
    
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
    if parentDir=="T" or "True":
        outputPath = os.path.split(inputPath)[0]
    # else:
    #     outputPath = input("Path to save output jpg: ")
    
    splitPDF(inputPath,outputPath)
    print("Finished")

#run app
if __name__ == "__main__":
    promptUser()

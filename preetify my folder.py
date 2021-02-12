import os
def soldier(path,file,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")
    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file,f"{i}{format}")
            i += 1
if __name__ == '__main__':
    path = input("Enter the path of the directory\n")
    file = input("Enter the file path\n")
    format = input("Enter the file format\n")
    soldier(path,file,format)
import glob, os, zipfile

# 1 - Diretório atual de trabalho
os.getcwd() 

# 2 - Lista todos os arquivos .txt
for file in glob.glob("dados/*.txt"):
    print(file)

# 3 - Lista todos os arquivos .csv
for file in glob.glob("dados/*.csv"):
    print(file)

# 4 - Compactando arquivos .txt
with zipfile.ZipFile("names.zip", "w") as f:
    for file in glob.glob("dados/*.txt"):
        f.write(file)

# 5 - Compactando arquivos .csv
with zipfile.ZipFile("courses.zip", "w") as f:
    for file in glob.glob("dados/*.csv"):
        f.write(file)

# 6 - Compactando todos os arquivos
with zipfile.ZipFile("code.zip", "w") as f:
    for file in glob.glob("*"):
        f.write(file)

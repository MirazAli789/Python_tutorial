st = "Welcome to python programming"

# creating and writing a file
with open("file.xlsx","w") as f:
    f.write("hfieifhiewhifhiwehfiehfhwe")

# appending to a file
with open("file.docx","a") as f:
    f.write(st)

# reading a file
with open("file.docx","r") as file:
    t = file.read(100)
    print(t)

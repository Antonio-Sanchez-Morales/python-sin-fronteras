# c = open("lelo.txt", "w")
# c.write("\nAgregaremos una nueva linea a nuestro archivo")

# c.close()

# x = open("lelo.txt")

# print(x.read())

import os
if os.path.exists("lelo.txt"):
    os.remove("lelo.txt")
else:
    print("El archivo no existe")
os.rmdir("carpeta")
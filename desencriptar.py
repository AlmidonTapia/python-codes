#LIBRERIAS
from cryptography.fernet import Fernet

#CARGAR CLAVE
def cargar_clave():
    return open("clave.key","rb").read()

#DESENCRIPTAR ARCHIVO
def desencript(nom_archivo,clave):
    f = Fernet(clave)
    with open(nom_archivo,"rb") as file:
         encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(nom_archivo,"wb") as file:
        file.write(decrypted_data)
        
#CARGAR CLAVE
clave = cargar_clave()

#ENCRIPTAR CLAVE
nom_archivo ="text.txt"
desencript(nom_archivo,clave)
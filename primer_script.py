import socket
objetivo = input("ingresa una pagina (ej:google.com):")

try:
    ip = socket.gethostbyname(objetivo)
    print("la ip de", objetivo, "es:", ip)
except:
    print("no se pudo obtener ls ip")
    
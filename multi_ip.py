import socket
dominios = ["google.com", "faceboock.com", "github.com", "youtube.com"]
for dominio in dominios:
    try:
        ip = socket.gethostbyname(dominio)
        print("la ip de", dominio, "es", ip)
    except:
        print("no se pudo obtener la ip de", dominio)
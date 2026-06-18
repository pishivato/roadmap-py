import subprocess


def IPscan(IP):
    resultado = subprocess.run(
        ["ping", "-n", "1", "-w", "100", IP],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if resultado.returncode == 0:
        print(f"{IP} -activa")

def Solicitud():
    try:
        IP = str(input("Ingresa el rango base de IPs: ej.(192.168.1.): \n"))
        
        for i in range(1, 255):
            IPscan(f"{IP}{i}")
    
    except ValueError:
        print("No se ingreso una rengo de IPs correcto.\n")


if __name__ == "__main__":
    Solicitud()
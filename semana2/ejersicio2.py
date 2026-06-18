import requests

try: 
    resp = requests.get("https://jsonplaceholder.typicode.com/users")
    resp.raise_for_status()
    data = resp.json()

    #name, email y company.name

    for d in data:
        print(f"{d["name"]:15} | {d["email"]:15} | {d["company"]["name"]}\n")
except requests.exceptions.RequestException as e:
    print(f"Error de Conexion: {e}")
import requests

def obtener_tasas(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base.upper()}"
    response = requests.get(url)
    data = response.json()
    if data.get("result") != "success":
        raise Exception("Error al obtener tasas")
    return data["rates"]

def convertir_moneda(base, destino, cantidad):
    tasas = obtener_tasas(base)
    if destino not in tasas:
        raise ValueError(f"Moneda destino '{destino}' no válida")
    return cantidad * tasas[destino]
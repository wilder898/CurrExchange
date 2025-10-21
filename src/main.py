from utils import convertir_moneda

def main():
    base = input("Moneda base (ej: USD): ").upper()
    destino = input("Moneda destino (ej: EUR): ").upper()
    cantidad = float(input("Cantidad: "))
    try:
        resultado = convertir_moneda(base, destino, cantidad)
        print(f"{cantidad} {base} = {resultado:.2f} {destino}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
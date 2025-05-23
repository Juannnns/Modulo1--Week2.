monto = float(input("Ingrese el monto de su compra: $"))
vip = input("Es cliente VIP? (S/N): ")
aplicar = ""

while aplicar != "S" and aplicar != "N":
    aplicar = input("Desea aplicar el descuento? (S/N)")


monto_final= monto * (1 - descuento)
print(f"Monto final a pagar: {monto_final:.2}")

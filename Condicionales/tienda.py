'''
Una tienda ofrece una promocion, por la compra de 3 articulos,
el costo del elemento de menor valor tiene un descuento del 50%
'''

art1=int(input("Ingresa el valor del primer articulo: $"))
art2=int(input("Ingresa el valor del segundo articulo: $"))
art3=int(input("Ingresa el valor del tercer articulo: $"))

if art1 < art2:
    temp = art1
else:
    temp = art2    

if temp < art3:
    menor = temp

else:
    menor= art3


total = art1+art2+art3       

total_final = total -(menor * 0.5)

print("total a pagar es: $", total_final)




def dec_to_bin(x):
    return int(bin(x)[2:])
a=int(input("Ingrese x :"))
resultado=dec_to_bin(a)
print(resultado)
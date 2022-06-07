import sys
import calorias
argnumbers = len(sys.argv) - 1

if argnumbers == 2:
    calory = calorias.Calorias(1600)
    if sys.argv[1].lower() == "add":
        calory.add_calories(int(sys.argv[2]))
        print("")
        print("Las calorias totales son: " + str(calory.quantity))
        print("")
    elif sys.argv[1].lower() == "spend":
        calory.spend_calories(int(sys.argv[2]))
        print("")
        print("Las calorias totales son: " + str(calory.quantity))
        print("")
    else:
        print("")
        print("Los argumentos insertados son erroneos")
    sys.exit(0)

if argnumbers != 2:
    print("")
    print("As insertado " + str(argnumbers) + " Valores.")
    print("El número de calorias inicialmente es igual a 1600 calorias")
    print("")
    print("Uso de la aplicación:")
    print("")
    print("Para añadir calorias: './calculadora ADD nºCalorias'")
    print("Para eliminar calorias: './calculadora SPEND nºCalorias'")
    print("")
    sys.exit(1)

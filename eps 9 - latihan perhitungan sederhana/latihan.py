# latihan konversi suhu
print("\nPROGRAM KONVERSI TEMPRATUR\n")

kelvin = float(input('Masukan suhu dalam kelvin : '))
print("suhu adalah", kelvin, "kelvin")

fahrenheit = float(input('Masukan suhu dalam fahrenheit : '))
print("suhu adalah", fahrenheit, "fahrenheit")

# fahrenheit ke kelvin
kelvin = 5/9 * (fahrenheit - 273) + 273
print("suhu dalam kelvin adalah ", kelvin, "Kelvin")

# kelvin ke fahrenheit
fahrenheit = (9/5 (kelvin - 273)) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

#if-elif
print(" *** Wind classification ***")
wind=float(input("Enter wind speed (km/h) : "))
if wind >= 0 and wind <= 51.99:
    print("Wind classification is Breeze.")
if wind >= 52.00 and wind <= 55.99:
    print("Wind classification is Depression.")
if wind >= 56.00 and wind <= 101.99:
    print("Wind classification is Tropical Storm.")
if wind >= 102.00 and wind <= 208.99:
    print("Wind classification is Typhoon.")
if wind >= 209:
    print("Wind classification is Super Typhoon.")

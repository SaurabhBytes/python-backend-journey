print("=== Temperature Converter ===")

def celsius_to_fahrenheit(C):
    return  (C * 9/5) + 32

def fahrenheit_to_celsius(F):
    return (F - 32) * (5/9)

def temp(celsius):
    if celsius < 0:
        return "Freezing"
    if celsius < 15:
        return "Cold"
    if celsius < 25:
        return "Comfortable"
    if celsius >= 25:
        return "Hot"
    

ctof = celsius_to_fahrenheit(0)
print(f"{(0)} C = {ctof} F")

ctof = celsius_to_fahrenheit(100)
print(f"{(100)} C = {ctof} F")



ftoc = fahrenheit_to_celsius(32)
print(f"\n{(32)} F = {ftoc} C")


ftoc = fahrenheit_to_celsius(86)
print(f"{(86)} F = {ftoc} C")


print("\nTemperature Descriptions: ")

print(f" -2C is: {temp(-2)}")
print(f" 14C is: {temp(14)}")
print(f" 21C is: {temp(21)}")
print(f" 32C is: {temp(32)}")

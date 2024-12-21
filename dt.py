# Sonlarni ko‘paytiruvchi dastur
def multiply_numbers(a, b):
    return a * b

print("Birinchi sonni kiriting: ")
x = int(input())  # Stringni integerga o‘tkazamiz

print("Ikkinchi sonni kiriting: ")
y = int(input())

result = multiply_numbers(x, y)  # Funksiyani chaqirishda qavslar yopildi
print("Natija:", result)



name = input("Enter your Name:")

product1 = input("Enter the product Name:")
price1 = int(input("Enter the product Price:"))

product2 = input("Enter the product Name:")
price2 = int(input("Enter the product Price:"))


product3 = input("Enter the product Name:")
price3 = int(input("Enter the product Price:"))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount = subtotal * 0.20
elif subtotal >= 3000:
    discount = subtotal * 0.10
elif subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

final_total = subtotal - discount


print(f"Customer Name: {name}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")

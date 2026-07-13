# float.py
price_item_1 = 19.99
price_item_2 = 5.50
tax_rate = 0.16 

subtotal = price_item_1 + price_item_2
tax_amount = subtotal * tax_rate
total_price = subtotal + tax_amount

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax Amount (16%): ${tax_amount:.2f}")
print(f"Total Price: ${total_price:.2f}")

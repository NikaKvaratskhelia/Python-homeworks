cart_total = 60.0        
is_vip = False           
is_guest = False         
promo_code = "SAVE10"    

if cart_total >= 50 or is_vip:
    print("Shipping: You qualify for Free Shipping!")
else:
    print("Shipping: You pay for shipping.")

if promo_code and not is_guest:
    discount = cart_total * 0.10
    final_total = cart_total - discount
    print(f"Discount: 10% discount applied! You saved ${discount:.2f}.")
else:
    final_total = cart_total
    print("Discount: No discount applied.")

print(f"Final Total Price: ${final_total:.2f}")

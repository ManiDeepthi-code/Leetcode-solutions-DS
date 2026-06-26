# --- (Dynamic Input) ---
food_total = int(input("Enter food total: "))
delivery_charge = int(input("Enter delivery charge: "))
disscount_coupon = int(input("Enter discount coupon: "))
split_between = int(input("Enter number of friends: "))
def subtotal(food_total,delivery_charge):
   return food_total+delivery_charge
def discount(food_total,disscount_coupon):
   return food_total-disscount_coupon
def split(food_total,split_between):   
   return food_total/split_between
total=subtotal(food_total,delivery_charge)
coupon=discount(food_total,disscount_coupon)
split=split(food_total,split_between)
print(total)
print(coupon)
print(split)

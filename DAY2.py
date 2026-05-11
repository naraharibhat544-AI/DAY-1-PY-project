
total_bill=input("how is the total bill:")
percentage=input("enter the percentage of tip")
split=input("number of people to slipt")
new_amount=int(int(total_bill)*int(percentage)/100)+int(total_bill)
print(f"Total slipt amount is :{new_amount/int(split)}")

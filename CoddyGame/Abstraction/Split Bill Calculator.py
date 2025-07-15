print("Bill Split Calculator")

bill_amount = float(input())
tip_amount = float(input())
# splitting feature
people_splitting_bill = int(input())

tip_amount = (tip_amount / 100) * bill_amount

the_total_bill = bill_amount + tip_amount
split_bill = the_total_bill / people_splitting_bill

print(f"Total (including tip): ${the_total_bill}")
print(f"Each person pays: ${split_bill}")


def calculate_discount_and_payable(amount):
    if amount >= 5000:
        discount_rate = 0.20
    elif amount >= 300:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = amount * discount_rate
    final_payable = amount - discount_amount
    return discount_amount, final_payable


if __name__ == "__main__":
    amount = float(input("Enter purchase amount: "))
    discount, payable = calculate_discount_and_payable(amount)
    print(f"Discount Amount: Rs.{discount}")
    print(f"Final Payable Amount: Rs.{payable}")

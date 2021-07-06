import math

p_goingOut      = 0.10
p_Living        = 0.20
p_Savings       = 0.50
p_Groceries    = 0.10
p_Investment    = 0.05
p_Extra         = 0.05

print(
    "This is a simple budget calculator" + "\n"
    "10 percent going out" + "\n"
    "20 percent living expenses" + "\n"
    "50 percent savings" + "\n"
    "10 percent groceries" + "\n"
    "05 percent investment" + "\n"
    "05 percent extra" + "\n")

totalMonthlyNetPay = float(input("Please enter your total monthly pay:"))

print(
    "\n"
    "Here are your monthly totals" "\n"
    "10 percent going out {0}".format(p_goingOut*totalMonthlyNetPay) + "\n"
    "20 percent living expenses {0}".format(p_Living*totalMonthlyNetPay) + "\n"
    "50 percent savings {0}".format(p_Savings*totalMonthlyNetPay) + "\n"
    "10 percent groceries {0}".format(p_Groceries*totalMonthlyNetPay) + "\n"
    "05 percent investment {0}".format(p_Investment*totalMonthlyNetPay) + "\n"
    "05 percent extra {0}".format(p_Extra*totalMonthlyNetPay) + "\n"
    "Thank You for using the Simple Budget Calculator."
    "Made with ♡ ♥💕❤😘  by Rusheel Sai Nuthalapati")

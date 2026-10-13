#!python3

# Canada Income Tax Calculator part I

'''
It's tax season!  Nobody loves doing taxes, so EVERYONE uses computers to help them.  We will use
Python to determine Federal and Provincial Income Tax.

The Canadian income tax system is a tiered system, which means you pay different percentages of
your income for different parts of your income.
You pay 15% tax on the first 49020 you earn.  If you earn more than this amount, you pay
20.5% on amounts over 49020 that are less than 98040
26% on amounts over 98040 but less than 151978
29% on amounts over 151978 but less than 216511
33% on amounts over 216511

Write a program to calculate the amount of Federal Income Tax for people who earn over 100,000 but less than 150,000

Example:
Enter your income: 125000
Your federal income tax is: 24411.7

'''
income=float(input("Enter your income"))
tier1=0
tier2=0
tier3=0
tier4=0
if income<49021:
    tier1=income*0.15
if income>49020:
    tier1=49020*0.15
    if income<98041:
        tier2=(income-49020)*0.205
    if income>98040:
        tier2=(49020*0.205)
        if income<151979:
            tier3=(income-98040)*0.26
        if income>151978:
            tier3=(53938*0.26) 
            if income<216512:
              tier3=(income-151978)*0.29
            if income>216511:
              tier3=(64533*0.29) 
              tier4=(income-216511)*33
IT=round(tier1+tier2+tier3+tier4,2)
print(f"Your federal income tax is: {IT}")
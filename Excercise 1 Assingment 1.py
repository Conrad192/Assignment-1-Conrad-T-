#Prompt the user for revenue (float) and cost (float).
revenue = float(input("Enter the revenue: "))
cost = float(input("Enter the cost: "))

#Calculate profit = revenue - cost.
#Calculate margin = (profit / revenue) * 100 if revenue > 0, else print "Invalid revenue."
#Print the results formatted nicely, e.g., "Profit: $X.XX | Margin: Y.YY%" (round margin to 2 decimals using round or f-string formatting).
if revenue>0:
    profit = revenue - cost
    margin= (profit/revenue)*100
    print("Profit: ", round(profit,2), " | Margin:", round(margin,2), "%")
else:
     print("Invalid revenue.")



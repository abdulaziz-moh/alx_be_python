monthlyincome = int(input( "Enter your monthly income: "))
monthlyexpenses = int(input( "Enter your total monthly expenses: "))

monthlysavings = monthlyincome - monthlyexpenses
annual_interest_rate = 0.05

projected_annual_savings = (monthlysavings * 12) + (monthlysavings * 12 * 0.05)

print("Your monthly savings are $",monthlysavings,".")
print("Projected savings after one year, with interest, is: $",projected_annual_savings,".")
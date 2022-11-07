from datetime import date, time
from math import sqrt
import logging

#// Total Cost of Ownership = Annual Carrying Cost + Annual Order Cost + Purchasing Cost
#// Economic Order Quantity (EOQ) = sqrt(2RS/hC)

# TC = Total Cost
# Q = Lot Quantity
# h = Holding Cost
# C = Material Cost
# S = Fixed Purchasing Cost
# R = Demand/Forecast per n
# n = Order Frequency
# TC = Q/2*h*C+R/Q*S+C*R
# h = d/360*11%*C
# holding cost variables include: interest rate (6%), insurance (1%), Realestate & Other Taxes (1%), Space & People (3%)

logging.basicConfig(filename='tco_input.log', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG, filemode='w', format='%(asctime)s:%(message)s')

#Establishing variables for user inputs
industry = 'select industry'
#enter lot quantity
q = 3000
#enter holding cost as a %
h = 0.15
#enter unit cost in USD
c = 75
s = 150
r = 12000
n = r/q

#using calculus, take the derivative of the total cost function and set the derivative equal to zero and solve for Q. Total cost curve is convex i.e. curvature is upwars so to obtain the minimizer

#The total cost curve reaches its minimum where the inventory carrying and ordering costs are equal
#TC = total cost
tc = (q/2)*h*c+(n*s)+(c*r)
#EOQ = economic order quantity
eoq = sqrt(2*r*s/(h*c))
#OOQ = optimal order quantity
ooq = sqrt(2*r*s*h*c)
#Cycle stock = Average invetory held during the cycle
cycle_stock = q/2
#Average Flow Time = (q/2)/r
avg_flow_time = (q/2)/r

result_statement = 'See your results below: '

print(result_statement)
print('Total Cost '+'= ' + str(tc))
print('Economic Order Quantity '+'= ' + str(eoq))
print('Optimal Order Quantity '+'= ' + str(ooq))
print('Cycle Stock '+'= ' + str(cycle_stock))
print('Average Flow Time '+'= ' + str(avg_flow_time))

print('Share your information for calculator updates and other content from Muda Management:')
company_size = input('Enter your company size: ')
location = input('Enter city, state, country: ')
industry_name = input('Enter your industry: ')
email = input('Enter your business email: ')

logging.info(
    result_statement,
    'Total Cost '+'= ' + str(tc),
    'Economic Order Quantity '+'= ' + str(eoq),
    'Optimal Order Quantity '+'= ' + str(ooq),
    'Cycle Stock '+'= ' + str(cycle_stock),
    'Average Flow Time '+'= ' + str(avg_flow_time),
    company_size,
    location,
    industry_name,
    email
    )

print('THANK YOU FOR YOUR SUBMITTAL!')

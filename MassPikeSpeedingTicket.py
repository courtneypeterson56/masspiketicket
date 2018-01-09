#description: This program computes possible fines for motorists stopped on the Massachusetts Turnpike
#author: Peterson, Courtney
#date: September 13, 2016

ticket_amount = 0

def final_amount():
    print "The fine is $",ticket_amount, "including a $50 donation to the head injury fund"

Y = 1
N = 0

print "This program computes possible fines for motorists stopped on the Massachusetts Turnpike"
print
starting_con_time = input("What is the starting time for construction in 24 Hour Format: ")
ending_con_time = input("What is the ending time for construction in 24 Hour Format: ")
print

speed = input("Enter Speed in MPH: ")
speed_limit = input("Enter Speed Limit in MPH: ")

if speed > speed_limit:
    ticket_amount = ticket_amount + 50
    if speed > speed_limit + 10:
            ticket_amount = ticket_amount + 10 * (speed - (speed_limit + 10))
            if ticket_amount > 500:
                ticket_amount = 500
                
else:
    print "no fine or assessment: case dismissed"


if ticket_amount > 0:
    con_zone = input("Is it a Construction Zone? Enter Y or N: ")
    if con_zone == 1:
        con_time = raw_input("Enter Time in 24 Hour Format: ")
        if (con_time > starting_con_time) or (con_time < ending_con_time):
             ticket_amount = (ticket_amount * 3) + 50
             final_amount()
        else:
            ticket_amount = (ticket_amount * 2) + 50
            final_amount()
    elif con_zone == 0:
        ticket_amount = ticket_amount + 50
        final_amount()


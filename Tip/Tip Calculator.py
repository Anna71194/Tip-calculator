def usr_bill():
    while True:
        try:
            print('***Welcome to the tip calculator***')
            bill=(input('What\'s the damage?: '))
            bill = bill.strip('$')
            bill=float(bill)
        except ValueError:
            print('Not an acceptable value, try again.')
            continue
        else:
            break
    usr_percent(bill)

def usr_percent(bill):
    while True:
        try:
            amount=(input('...and what percentage would you like to tip?: '))
            amount = amount.strip('%')
            amount=float(amount)
            percent= amount/100
        except ValueError:
            print('Sorry, that is not an acceptable value, try again')
            continue
        else:
            break
    ttip_amount(percent, bill)

def ttip_amount(percent, bill):
    ttip= (percent + 1.0) * bill
    otip_amount (ttip, percent, bill)

def otip_amount(ttip, percent, bill):
    otip= percent * bill
    dis_tip(otip,ttip)

def dis_tip(otip,ttip):
    print('Your tip amount should be %.2f' %otip)
    print('The total cost should be %.2f' %ttip)

usr_bill()




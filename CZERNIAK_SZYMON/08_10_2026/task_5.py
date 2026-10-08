order_value = float(input('Enter the order value in PLN:'))

if order_value < 0:
    print('Invalid order value')
else:
    if order_value < 100:
        discount_percentage = 0
    elif order_value < 300
        discount_percentage = 5
    elif order_value < 1000
        discount_percentage = 10
    else:
        discount_percentage = 15
        

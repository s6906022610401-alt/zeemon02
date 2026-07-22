keep_g ='y'
while keep_g == 'y':
    sales = float(input("enter the amount of sales: "))
    comm_r = float(input("enter the commission of sales: "))
    
    commision =sales * comm_r
    print(f'the commision is ${commision:.2f}')
keep_g = input ('Do you want to calculate anotgher' + \
    'commision (enter y for yes): ')

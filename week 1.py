stocks = {'info' : '[600,630,620]',
          'ril' : '[1430,1490,1567]',
          'mtl': '[234,180,160]'}

averages = ['600,630,620','1430,1490,1567','234,180,160']

print('Do you want to print?')
print('Do you want to add')

program = input("What do you want to do: ")


if program == 'print':
    for key, values in stocks.items():
        
        values = values.strip('[]').split(',')
        values = [int(num) for num in values]

        average = round(sum(values)/len(values),2)
        

        print(key + '==>' + str(average))
if program == 'add':
    new = input("Stock Ticker: ")
    price = input('Price: ')
    if new in stocks:
        print("Stocks already in list")
    else:
        stocks[new] = price
        print(new + '==> [' + price + ']')



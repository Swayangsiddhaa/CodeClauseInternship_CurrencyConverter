""""
Currency Converter

This program converts an amount from one currency to another using predefined exchange rates.
The exchange rates are hardcoded and may not reflect real-time values.
"""
#Hardcoded exchange rates against a base currency (e.g., INR).
#This is the dictionary which contained currency name and exchange rate of currency in indian rupees.
currency_exchange_rate = {
    "USD" : 83.45,
    "EUR" : 90.54,
    "JPY" : 0.53,
    "NZD" : 51.37,
    "GBP" : 106.22,
    "AUD" : 55.42,
    "CHF" : 92.35,
    "CNH" : 11.49,
    "CAD" : 61.12,
    "SEK" : 7.91,
}
#This function Converts the given amount from the input currency to the target currency,after calculatuon.
def calculation(Amount,Input_currency,Target_currency):
    Target_ammount = (Amount*currency_exchange_rate[Input_currency])/currency_exchange_rate[Target_currency]
    print(Amount,Input_currency,"is equal to",Target_ammount,Target_currency )

#This function checks if both input and target currency is valid or not.
#Please note this function first takes both input and target currency....checks....and then gives result.
def check_and_convert(Input_currency,Target_currency):
    if(Input_currency in  currency_exchange_rate) and ( Target_currency in currency_exchange_rate ):    
        calculation(Amount,Input_currency,Target_currency)
    elif(Input_currency not in  currency_exchange_rate) and ( Target_currency not in currency_exchange_rate ):  
        print("Unsupported currency pair!. Please choose valid currencies.")
    elif(Input_currency not in  currency_exchange_rate) and (Target_currency in currency_exchange_rate):    
        a = input("Invalid input currency, please enter the correct input currency :").upper()
        if(a in currency_exchange_rate):
            Input_currency = a
            calculation(Amount,Input_currency,Target_currency)
        else:
            print("unsupported!.Again you enter an invalid input currency.Be carefull for next currency convertion.")
    elif(Input_currency  in  currency_exchange_rate) and (Target_currency not in currency_exchange_rate):   
            b = input("Invalid target currency, please enter the correct target currency:").upper()
            if(b in currency_exchange_rate):
                Target_currency = b
                calculation(Amount,Input_currency,Target_currency)
            else:
                print("unsupported!.Again you enter an invalid target currency.Be carefull for next currency convertion.")
            
#Opening statement
print("Hello!.This is Currency Converter,it converts amount form one currency to another currency .")
list=["USD","EUR","JPY","NZD","GBP","AUD","CHF","CNH","CAD","SEK"]
print("This is the list of the currencies we support:",list)

while(True):
    #Chacking of given amount validity.
    try:
        Amount = float(input("Enter the amount you want to change:"))
    except ValueError:
        print("Invalid amount input!, Please enter a valid amount")
        continue

    #Taking input of (Input_currency) curency which the user want to change and the curency(Target_currency)to which user want to convert it.
    Input_currency = input("Write the name of currency you want to change:").upper()
    Target_currency = input("Write the name of currency in which you want to convert to:").upper()
    check_and_convert(Input_currency,Target_currency)
    b = input("Do you want to Convert curerency further? only:-(yes or no):-").lower()

    #Asking user if user wants further currency convertion or not.
    if(b != "yes"):
        print("Thank you for using this Currency Converter!")
        break
    else:
        continue



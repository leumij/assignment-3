import colorama
from colorama import Fore, Back, Style
from tabulate import tabulate
colorama.init(autoreset=True)


def compute_total_apples(amount_apples):
    apple_price = 20
    apple_bought = amount_apples * apple_price
    apple_data = [['Fruits' , 'Quantity' , 'Prices'],
                  ['Apples' , apple_order , 'PHP 20.00'],
                  ['Total' , '' , f'PHP {apple_bought}']]
    print(tabulate(apple_data, headers="firstrow", tablefmt="pipe"))
    return apple_bought

def compute_total_oranges(amount_oranges):
    orange_price = 25
    orange_bought = amount_oranges * orange_price
    orange_data = [['Fruits' , 'Quantity' , 'Prices'],
                  ['Oranges' , orange_order , 'PHP 25.00'],
                  ['Total' , '' , f'PHP {orange_bought}']]
    print(tabulate(orange_data, headers="firstrow", tablefmt="pipe"))
    return orange_bought

def compute_total_fruits(amount_apples, amount_oranges):
    orange_price = 25
    apple_price = 20
    fruits_bought = (amount_apples * apple_price) + (amount_oranges * orange_price)
    both_data = [['Fruits' , 'Quantity' , 'Prices'],
                  ['Apples' , apple_order , 'PHP 20.00'],
                  ['Oranges' , orange_order , 'PHP 25.00'],
                  ['Total' , '' , f'PHP {fruits_bought}']]
    print(tabulate(both_data, headers="firstrow", tablefmt="pipe"))
    return fruits_bought

intro_mssg = f"{Fore.GREEN}{Style.BRIGHT}Great day, shopper! Welcome to {Fore.MAGENTA}F{Fore.RED}R{Fore.YELLOW}U{Fore.BLUE}I{Fore.GREEN}T {Style.BRIGHT}{Fore.CYAN}{Back.BLACK}NINJA!"
print(intro_mssg)
offer_mssg = print(f"{Fore.WHITE}{Style.BRIGHT}The products that we offer are:")

table_data = [['Fruits' , 'Prices'],
              ['Apples' , 'PHP 20.00'],
              ['Oranges' , 'PHP 25.00']]
print(tabulate(table_data, headers="firstrow", tablefmt="pipe"))

while True:
    order_selection = input(f"{Fore.WHITE}{Style.BRIGHT}Do you want to proceed to your transaction"
                            f" {Fore.GREEN}(yes{Fore.WHITE} or {Fore.RED}no){Fore.WHITE}? Enter here: ")
    
    if order_selection == "yes":
        fruit_selection = input(f"{Fore.WHITE}{Style.BRIGHT}What fruit would you like to buy"
                                f" {Fore.RED}(apple/{Fore.YELLOW}orange/{Fore.GREEN}both){Fore.WHITE}? Enter here: ")

        if fruit_selection == "apple":
            apple_order = int(input(f"{Fore.WHITE}How many {Fore.RED}apple/s{Fore.WHITE} would you like to buy? Enter here: "))
            apple_bought = compute_total_apples(apple_order)
            apple_result = print(f"{Fore.GREEN}{Style.BRIGHT}Transaction completed, thank you for choosing "
                                 f"{Fore.MAGENTA}F{Fore.RED}R{Fore.YELLOW}U{Fore.BLUE}I{Fore.GREEN}T {Style.BRIGHT}{Fore.CYAN}{Back.BLACK}NINJA!" 
                                 f"{Fore.GREEN}{Back.RESET} Your ordered apples costs: {Back.BLACK}PHP {apple_bought}")
            

        if fruit_selection == "orange":
            orange_order = int(input(f"{Fore.WHITE}How many {Fore.YELLOW}orange/s{Fore.WHITE} would you like to buy? Enter here: "))
            orange_bought = compute_total_oranges(orange_order)
            orange_result = print(f"{Fore.GREEN}{Style.BRIGHT}Transaction completed, thank you for choosing "
                                  f"{Fore.MAGENTA}F{Fore.RED}R{Fore.YELLOW}U{Fore.BLUE}I{Fore.GREEN}T {Style.BRIGHT}{Fore.CYAN}{Back.BLACK}NINJA!"
                                  f"{Fore.GREEN}{Back.RESET} Your ordered oranges costs: {Back.BLACK}PHP {orange_bought}")
            

        if fruit_selection == "both":
            apple_purchase_order = int(input(f"{Fore.WHITE}How many {Fore.RED}apple/s{Fore.WHITE} would you like to buy? Enter here: "))
            orange_purchase_order = int(input(f"{Fore.WHITE}How many {Fore.YELLOW}orange/s{Fore.WHITE} would you like to buy? Enter here: "))
            fruits_bought = compute_total_fruits(apple_purchase_order, orange_purchase_order)
            fruits_result = print(f"{Fore.GREEN}{Style.BRIGHT}Transaction completed, thank you for choosing "
                                  f"{Fore.MAGENTA}F{Fore.RED}R{Fore.YELLOW}U{Fore.BLUE}I{Fore.GREEN}T {Style.BRIGHT}{Fore.CYAN}{Back.BLACK}NINJA!"
                                  f"{Fore.GREEN}{Back.RESET} Your ordered apples and oranges costs: {Back.BLACK}PHP {fruits_bought}")
            

        other_transaction = input("Do you want another transaction?" f" {Fore.GREEN}(yes{Fore.WHITE} or {Fore.RED}no) ")
        if other_transaction == "no":
            print(f"{Fore.MAGENTA}That's sad, we hope you'll check out our shop next time! Thank you for your choosing our shop!")
            break
        
    

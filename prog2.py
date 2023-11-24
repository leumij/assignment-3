from tabulate import tabulate
from pyfiglet import Figlet 
f = Figlet(font='big')
from colorama import Fore, Back, Style


def compute_total_apples(apple_order, apple_money_input):
    apple_price = 20
    apple_bought = apple_order * apple_price
    apple_cash_left =  apple_money_input - apple_bought
    
    apple_table = [['Fruits' , 'Quantity' , 'Prices'],
                   ['Apple' ,  f'{apple_order} pcs' , 'PHP 20'],
                   ['Total', '' , f'PHP {apple_bought}'],
                   ['Cash', '' , f'PHP {apple_money_input}'],
                   ['Change Due' , '' ,f'PHP {apple_cash_left}']]
    print(f"{Fore.GREEN}{Back.BLACK}This is your receipt:")
    print(f"{Fore.WHITE}" , (tabulate(apple_table, headers="firstrow", tablefmt="fancy_grid")))
    return apple_bought
  

def compute_total_oranges(orange_order, orange_money_input ):
    orange_price = 25
    orange_bought = orange_order * orange_price
    orange_cash_left = orange_money_input - orange_bought

    orange_table = [['Fruits' , 'Quantity' , 'Prices'],
                   ['Oranges' ,  f'{orange_order}pcs' , 'PHP 25'],
                   ['Total', '' , f'PHP {orange_bought}'],
                   ['Cash', '' , f'PHP {orange_money_input}'],
                   ['Change Due' , '' , f'PHP {orange_cash_left}']]
    
    print(f"{Fore.GREEN}{Back.BLACK}This is your receipt:")
    print(f"{Fore.WHITE}" , (tabulate(orange_table, headers="firstrow", tablefmt="fancy_grid")))
    return orange_bought

def compute_total_amount(apple_purchase_order, orange_purchase_order, both_money_input):
    orange_price = 25
    apple_price = 20
    both_bought = (apple_purchase_order * apple_price) + (orange_purchase_order*orange_price) 
    both_cash_left = both_money_input - both_bought
    both_data_table = [['Fruits' , 'Quantity' , 'Prices'],
                       ['Apples' , f'{apple_purchase_order}pcs' , 'PHP 20'],
                       ['Orange' , f'{orange_purchase_order}pcs' , 'PHP 25'],
                       ['Total' , '' ,  f' PHP{both_bought}'],
                       ['Cash' , '' , f' PHP{both_money_input}'],
                       ['Change Due' , '' , f' PHP{both_cash_left}']]
    print(f"{Fore.GREEN}{Back.BLACK}This is your receipt:")
    print(f"{Fore.WHITE}" , (tabulate(both_data_table, headers="firstrow", tablefmt="fancy_grid")))
    return both_bought

into_mssg = print(Fore.GREEN , Style.BRIGHT + f.renderText("WELCOME TO ALING NENA'S FRUIT SHOP!"))
offer_mssg = print(f"{Fore.WHITE}{Style.BRIGHT}The products that we are offer:")


table_data = [['Fruits' , 'Prices'], 
              [f'{Fore.RED}Apple' , 'PHP20.00'],
              [f'{Fore.YELLOW}Orange' , 'PHP25.00']]

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

while True:
    order_selection = input(f"{Fore.WHITE}{Style.BRIGHT}Do you want to proceed to your transaction"
                            f" {Fore.GREEN}(yes{Fore.WHITE} or {Fore.RED}no){Fore.WHITE}? Enter here: ")
    if order_selection == "yes":
        fruit_selection = input(f"{Fore.WHITE}What fruit do you like to buy " f"{Fore.RED}(apple/" f"{Fore.YELLOW}orange/" f"{Fore.BLUE}both?) " f"{Fore.WHITE}Enter here: ")
    
        if fruit_selection == "apple":
            apple_money_input = int(input("Enter your amount: PHP "))
            apple_order = int(input(f"{Fore.WHITE}How many " f"{Fore.RED}apples " f"{Fore.WHITE}would you like to buy? Enter here: "))
            apple_bought = compute_total_apples(apple_order, apple_money_input) 
            print("Thank you for your choosing our shop! Your transaction is complete") 
        
        if fruit_selection == "orange":
            orange_money_input = int(input("Enter your amount: PHP "))
            orange_order = int(input(f"{Fore.WHITE}How many " f"{Fore.YELLOW}oranges " f"{Fore.WHITE}would you like to buy? Enter here: "))
            orange_bought = compute_total_oranges(orange_order, orange_money_input) 
            print("Thank you for your choosing our shop! Your transaction is complete") 
        
        if fruit_selection == "both":
            both_money_input = float(input("Enter your amount: PHP "))
            apple_purchase_order = int(input(f"{Fore.WHITE}How many " f"{Fore.RED}apples " f"{Fore.WHITE}would you like to buy? Enter here: "))
            orange_purchase_order = int(input(f"{Fore.WHITE}How many " f"{Fore.YELLOW}oranges " f"{Fore.WHITE}would you like to buy? Enter here: "))
            both_bought = compute_total_amount(apple_purchase_order, orange_purchase_order, both_money_input)
            print("Thank you for your choosing our shop! Your transaction is complete") 
        
    other_transaction = input("Do you want another transaction?" f" {Fore.GREEN}(yes{Fore.WHITE} or {Fore.RED}no) ")
    if other_transaction == "no":
        print(f"{Fore.MAGENTA}That's sad, we hope you'll check out our shop next time! Thank you for your choosing our shop!")
        break
    
    

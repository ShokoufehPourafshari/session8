products = []

def read_data() :
    f = open("ShoppingAssignment.txt","r" )
    for l in f :
        product = l.split(',')
        dic = {'ID': product[0],'Name': product[1],'Price':product[2] ,'Count':product[3]}
        products.append(dic)


def show_menu () :
    while True:
        print("MENU: ")
        print('1- Add')
        print('2- Delete ')
        print('3- Search')
        print('4- Buy')
        print('5- Edit')
        print('6- View all products')
        print('7- Exit')


        user_choice = int(input("your choise: "))
        if user_choice == 1:
            add()

        elif user_choice == 2:
            delete() 

        elif user_choice == 3:
            search()

        elif user_choice == 4:
            buy()

        elif user_choice == 5:
            edit()

        elif user_choice == 6:
            show_products()

        elif user_choice == 7:
            print("Done!")
            break

        else:
            print('try again')

def add():
    while True:
        id = input('enter the ID(Enter exit to finish):')
        if id == 'exit': 
            break
        name =input('Enter Name:')
        for p in products:
            if p['ID'] == id and p['Name'] == name:
                print(f"product {id}  already exists!")
                return
            if p['ID'] == id and p['Name'] != name:
                print(f"product '{id}' already exists with other name!")
                return
            if p['ID'] != id and p['Name'] == name:
                print(f"product '{name}' already exists with other ID!")
                return
            

        price =input('Enter Price:')
        count =input('Enter Count:')
        dic = {'ID':id, 'Name':name, 'Price':price, 'Count': count}
        products.append(dic)
        with open('C:\Users\Shokufeh\Desktop\run\ShoppingAssignment.txt', 'a') as f:  
            line = f"{id},{name},{price},{count}\n"
            f.write(line)
        print('product added succesfuly!')



def delete():
    while True:
        id = input('Enter the ID you wanna remove (Enter exit to finish):')
        if id == 'exit': 
            break
        with open('C:\Users\Shokufeh\Desktop\run\ShoppingAssignment.txt', 'r') as f:
            lines = f.readlines()
        with open('C:\Users\Shokufeh\Desktop\run\ShoppingAssignment.txt', 'w') as f:
            for line in lines:
                if line.split(',')[0] != id:
                    f.write(line)
        print('product removed succesfuly!')



def search():
    while True:
        key = input('Enter your key (Enter exit to finish):')
        if key == 'exit': 
            break
        for product in products :
            if key == product['ID'] or key == product['Name'] or key == product['Price'] or key == product['Count']:
                print(product)
                break
        else:
            print('invalid')



def buy():
    cart = []
    total_price = 0
    while True: 
        item_id = input("Enter the ID of your purcheses (Enter 'exit' to finish):")
        if item_id == 'exit': 
            break
        item_found = False
        for product in products:
            if product["ID"] == item_id:
                item_found = True
                count = int(input("Enter the amount of what you need:"))
                if int(product["Count"]) >= count:
                    product["Count"] = str(int(product["Count"]) - count)
                    cart.append({"Name":product["Name"],
                                 "Price":product["Price"],
                                 "Count":count})
                    print("Added to cart!")
                    total_price += int(product["Price"]) * count

                else:
                    print("we are out of source.")
                    print("source:", product["Count"])



        if not item_found:
                print("wrong id!.")

    print("Cart:", cart)
    print("Total price:", total_price, "Dollor")

    with open("C:\Users\Shokufeh\Desktop\run\ShoppingAssignment.txt", "w") as f:
        for product in products:
            f.write(product["ID"]+","+product["Name"]+","+product["Price"]+","+product["Count"]+"\n")


        
def edit():
    while True:
        id = input("Enter the ID of the product you wanna edit (Enter exit to finish):")
        if id == 'exit':
            return
        

        for product in products:
            if product['ID'] == id:
                print(" ")
                print('product:')
                print('ID\t Name \t Price \t Count')
                print(product['ID'],'\t',product['Name'],'\t',product['Price'],'\t',product['Count'])
                print(" ")

                while True:
                    print('1- Name')
                    print('2- Price')
                    print('3- Count')
                    choice = input('choose the part you wish to edit:')

                    if choice == '1':
                        new_name = input('new name:')
                        product['Name'] = new_name
                        break

                    elif choice == '2':
                        new_price = input('new price:')
                        product['Price'] = new_price
                        break

                    elif choice == '3':
                        new_count = input('new amount:')
                        product['Count'] = new_count
                        break

                    else:
                        print('Think again.')

                with open('C:\Users\Shokufeh\Desktop\run\ShoppingAssignment.txt', 'w') as f:
                    for product in products:
                        line = f"{product['ID']},{product['Name']},{product['Price']},{product['Count']}\n"
                        f.write(line)
                
                print('The List Uptadet Succesfuly!')
                break
            
        else:
            print('Your Request is Unvalid!.')

def show_products() :
    print('ID \t Name \t Price \t Count')
    for product in products :
        print(product['ID'],'\t',product['Name'],'\t',product['Price'],'\t',product['Count'])
read_data()
show_menu()
import json



with open('menu.json', 'r') as f:
    data = json.load(f)


items = data.get('items', [])

while True:
    print('-'*50)
    print('Super Famous Restaturant')
    print('-'*50)
    print("""
            1. Show Menu
            2. Order Items
            3. Update Menu
            4. Add Review
            5. Exit!
        """)
    print('-'*50)
    print('Enter choice_____')
    choice = int(input())

    if choice == 1:
        print('----MENU ITEMS----')
        print('ID\tName\t\tPrice')
        print('-'*40)
        for item in items:
            print(f'{item.get("id")}\t{item.get("name")}\t{item.get("price")}')
        print('-'*40)
    elif choice == 2: 
        order_items = list(map(int, input("What you want to try today> ").split(',')))
        print('-'*40) 
        print('ID\tName\t\tPrice')
        print('-'*40)
        total_bill =0
        for order_item in order_items:
            for item in items: 
                if item['id'] == order_item:
                    print(f'{item.get('id')}\t{item.get('name')}\t{item.get('price')}')
                    total_bill = total_bill + int(item.get('price'))
                    break

        print('-'*40) 
        print(f'Total Bill: {total_bill}')
        print('-'*40)              
        

    elif choice == 3:
        name = input("Enter item name:")
        item_price = int(input('Price of item? '))
        item_type = input('veg or non-veg? ')
        items.append({
            'id':len(items) +1,
            'name' : name, 
            'price': item_price,
            'veg' : True if item_type == 'veg' else False,
            'reviews': []

        })
        data['items'] = items
        with open('menu.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Item is added.")
    elif choice == 4:
        print('Add Review')
    else:
        print('Thank you')
        break

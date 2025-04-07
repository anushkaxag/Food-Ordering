from database.get_all_restaurants import getRestaurantList
from database.dishes import getDishesByRestaurant
from database.user import getUser
from database.orders import placeOrder
from database.orderItem import addOrderItems


def orderFood():
    print("Select restaurant:")
    restaurantsList = getRestaurantList()
    for restaurant in restaurantsList:
        print(restaurant[0],".\t" +restaurant[1]) 

    selected_restaurant_id=input("Enter your restaurant choice: ")
    if not selected_restaurant_id.isnumeric() or int(selected_restaurant_id)<1 or int(selected_restaurant_id)>len(restaurantsList):
        print("Incorrect Choice")
        return
    
    items = getDishesByRestaurant(selected_restaurant_id)

    for i in range(len(items)):
        item = items[i]
        print(i+1,item[2],item[3], sep="\t")

    orders = {}

    while True:
        option_chosen = input("Enter item number to order or any other key to conitnue:")
        if not option_chosen.isnumeric() or int(option_chosen)<0 or int(option_chosen)>len(items):
            break 
        while True:
            option_chosen_int = int(option_chosen)
            item_id = items[option_chosen_int-1][0]
            quantity = input("Enter quantity: ")
            if  quantity.isnumeric():
                if not item_id in orders:
                    orders[item_id] = [items[option_chosen_int-1][2], items[option_chosen_int-1][3], 0]
                orders[item_id][2] += int(quantity)
                break 
            print("Invalid Quantity")
            print(orders)
    print("**************")
    print("Final Order Summary: ")
    total = 0
    for item_id in orders:
        print(item_id,*orders[item_id],orders[item_id][1]*orders[item_id][2], sep="\t" )
        total+=orders[item_id][1]*orders[item_id][2]
    print("\n\n Total: ",total)
    print("**************")


    print("\n\n\n\n")
    user = None
    while True:
        user_email = input("Enter User email: ")
        user_password = input("Enter password: ")
        user = getUser(user_email, user_password)
        print(user)
        if len(user)==1:
            break 
        print("Invalid Credentials, Try again: ")
    
    deliveryAdress = input("Enter Delivery Address: ")

    print("Placing Order......")

    order_id = placeOrder(user[0][0], selected_restaurant_id, total, deliveryAdress)
    addOrderItems(order_id, orders)

    print("THANK YOU")
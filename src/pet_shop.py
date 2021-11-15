# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"] 
    
def increase_pets_sold(pet_shop, number_of_pets):
    pet_shop["admin"]["pets_sold"] += number_of_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_breed=[]
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_breed.append(pet)
    return pet_breed

def find_pet_by_name(cc_pet_shop,pet_name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet ["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer ["cash"]

def remove_customer_cash(customer,cash):
    customer["cash"] -=cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)



# -----optional----------



def customer_can_afford_pet(customer,new_pet):
    return customer["cash"] >= new_pet["price"]
    

# ---------- INTEGRATION ------- 


def sell_pet_to_customer(pet_shop,pet,customer):
    if pet == None:
        print("No pet at the store")
    elif customer_can_afford_pet(customer,pet) == False:
        return "customer_can't_afford_pet"
    else: 
        remove_customer_cash(customer,pet["price"])
        add_or_remove_cash(pet_shop,pet["price"])
        remove_pet_by_name(pet_shop,pet["name"])
        add_pet_to_customer(customer,pet)
        increase_pets_sold(pet_shop,1)

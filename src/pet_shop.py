# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

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





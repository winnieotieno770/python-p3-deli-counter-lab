import ipdb
def line(customer_list):
    if len(customer_list) == 0:
        print("The line is currently empty.")
        return
    customers = " ".join(f"{index + 1}. {name}" for index, name in enumerate(customer_list))
    print(f'The line is currently: {customers}')
    
def take_a_number(customer_list, customer_name):
    customer_list.append(customer_name)
    num = customer_list.index(customer_name) + 1
    print(f"Welcome, {customer_name}. You are number {num} in line.")

take_a_number(['e','f'],'g')
def now_serving(customer_list):
    if len(customer_list) == 0:
        print("There is nobody waiting to be served!")
        return
    c  =  customer_list.pop(0)
    print(f"Currently serving {c}.")
    
now_serving(['Logan', 'Avi', 'Spencer'])
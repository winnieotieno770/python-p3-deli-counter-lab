import ipdb
def line(customer_list):
    if len(customer_list) == 0:
        print("The line is currently empty.")
        return
    customers = " ".join(f"{index + 1}. {name}" for index, name in enumerate(customer_list))
    print(f'The line is currently: {customers}')
    
def take_a_number(customer_list, customer_name):
    customer_list.append(customer_name)
    num = len(customer_list)
    print(f"Welcome, {customer_name}. You are number {num} in line.")


def now_serving():
    pass
take_a_number(["Brenda", "Anna"], "Clark")
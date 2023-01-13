katz_deli = []

def line(line_list):
    if len(line_list) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(line_list)):
            message += f' {i + 1}. {line_list[i]}'
        print(message)
            

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
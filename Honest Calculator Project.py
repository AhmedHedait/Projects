msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
result = 0
memory = 0
temp_memory = 0

msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

# msg_index[0] = "Are you sure? It is only one digit! (y / n)"
# msg_index[1] = "Don't be silly! It's just one number! Add to the memory? (y / n)"
# msg_index[2] = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_index = ["Are you sure? It is only one digit! (y / n)", "Don't be silly! It's just one number! Add to the memory? (y / n)", "Last chance! Do you really want to embarrass yourself? (y / n)"]

msg = ""

def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    else:
        return False

def my_check(v1, v2, v3):
    global msg
    if is_one_digit(x) == True and is_one_digit(y) == True:
        msg = msg_6
        #print(msg)  # msg_6 = " ... lazy"
        pass
    if x == 1 or y == 1 and oper == oper_list[2]:
        msg = msg + msg_7
        #print(msg)  # msg_7 = " ... very lazy"
        pass
    if (x == 0 or y == 0) and (oper == oper_list[2] or oper == oper_list[1] or oper == oper_list[1]):
        msg = msg + msg_8
        #print(msg)  # msg_8 = " ... very, very lazy"
        pass
    if msg != "":
        msg = msg_9 + msg
        print(msg)
        msg = ""


m_counter = 0
while True:
    try:
        memory
        result
        print(msg_0)
        # print(str(m_counter)+ "counter")
        # print(str(memory) + " memory")
        # print(str(result) + " result")
        calc = input()
        calc_list = calc.split()
        if calc_list[0] == "M" and calc_list[2] == "M":
            calc_list[0] = memory
            calc_list[2] = memory
        elif calc_list[0] == "M":
            calc_list[0] = memory
        elif calc_list[2] == "M":
            calc_list[2] = memory

        oper_list = ["+", "-", "*", "/"]
        x = float(calc_list[0])          # test
        oper = calc_list[1]              # test
        y = float(calc_list[2])          # test
        oper_count = oper_list.count(oper)
        my_check(x, y, oper)        # test
        pass
        if type(x) == float and type(y) == float and oper_count > 0:
            if oper == oper_list[0]:
                result = x + y
            elif oper == oper_list[1]:
                result = x - y
            elif oper == oper_list[2]:
                result = x * y
            elif oper != oper_list[3] or y != 0:
                result = x / y
            elif oper == oper_list[3] and y == 0:
                print(msg_3)
                continue
            print(result)
            pass
        elif type(x) == float and type(y) == float and oper_count == 0:
            print(msg_2)

        print(msg_4)  #  "Do you want to store the result? (y / n):"
        mem_answer = input("") #  "Do you want to store the result? (y / n):"
        if mem_answer == "y":
            is_one_digit(result)
            if is_one_digit(result) == True:
                print(msg_index[0])
                msg_input_0 = input("") # input_0
                if msg_input_0 == "y":
                    print(msg_index[1])
                    msg_input_1 = input("")  # input_1
                    if msg_input_1 == "y":
                        print(msg_index[2])
                        msg_input_2 = input("")  # input_2
                        if msg_input_2 == "y":
                            memory = result
                            print(msg_5)
                        elif msg_input_2 == "n":
                            print(msg_5)
                    elif msg_input_1 == "n":
                        print(msg_5)
                elif msg_input_0 == "n":
                    print(msg_5)
            elif is_one_digit(result) == False:
                memory = result
                print(msg_5)
        elif mem_answer == "n":
            print(msg_5)

        con_answer = input("")
        if con_answer == "y":
            # m_counter += 1
            # print("loop1")
            continue
        elif con_answer == "n":
            break

    except ValueError:
        print(msg_1)
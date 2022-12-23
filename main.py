import voice
import operator

voice = voice.voice_command()

def arith_begin(num1, num2, op):
    if op == '+':
        result = operator.add(int(num1), int(num2))
    elif op == '+' or 'plus':
        result = operator.add(int(num1), int(num2))
    elif op == '-' or 'minus':
        result = operator.sub(int(num1), int(num2))
    elif op == '*' or 'multiply' or 'multiplied by' or 'into':
        result = operator.mul(int(num1), int(num2))
    elif op == '/' or 'multiply' or 'multiplied by' or 'into':
        result = operator.truediv(int(num1), int(num2))
    elif op == 'power':
        result = operator.pow(int(num1), int(num2))
    return(result)

def arith_add_on(op, num3, previous_result):
    if op == '+' or 'plus':
            current_result = operator.add(int(previous_result), int(num3))
    elif op == '-' or 'minus':
            current_result = operator.sub(int(previous_result), int(num3))
    elif op == '*' or 'multiply' or 'multiplied by' or 'into':
            current_result = operator.mul(int(previous_result), int(num3))
    elif op == '/' or 'multiply' or 'multiplied by' or 'into':
            current_result = operator.truediv(int(previous_result), int(num3))     
    elif op == 'power':
            current_result = operator.pow(int(previous_result), int(num3))
    return(current_result)

def oper_sep(op1, oper, op2):
    global result1
    op1,op2 = int(op1), int(op2)
    result1 = arith_begin(op1, op2, oper) 
    return result1
def oper_sep_2(oper, op2, previous_result):
    op2 = int(op2)
    return arith_add_on(oper, op2, previous_result) 

def end_func(value):
    print(value)
    exit()
def simple_calc():
    command = voice.take_command()
    voice.talk(command)
    print(command)
    result = oper_sep(*(command.split()))
    print(result)
def arithmetic_calc():
    
    try:
        global final_result
        global command
        global value
        voice.talk('Please say two value for example 1 + 1')
        #command = voice.take_command()
        command = '12 + 12'
        voice.talk(command)
        print(command)
        result1 = oper_sep(*(command.split()))
        print(result1)
        
        value = True
        while value:
            #command = voice.take_command()
            command = input()
            voice.talk(command)
            print(command)
            op , num3 = command
            result2 = oper_sep_2(op, num3, result1)
            print(result2)
            final_result = result2
            value = True
            return final_result
            
    except(ValueError):
        print(command)
        if command == 'equal to' or 'equal':
            print(final_result)
            voice.talk(final_result)
            value = False
        else:
            print('Wrong value entered')
            voice.talk('Wrong value entered')
voice.talk('Welcome Sir. I\'m an AI calculator specially designed for Blind People')
voice.talk('You currently have 3 options')
voice.talk('1. You can do normal calculations with two integers.')
voice.talk('2. You can do arithmetic calculations with n number of integers')
voice.talk('3. You cand do scientific calculations')
#command = voice.take_command()
command = 'option two'
if command == 'option one':
    simple_calc()
elif command == 'option two':
    arithmetic_calc()
voice.talk('Do you want to calculate another value or exit the app')
#command = voice.take_command()
command = input()
if command == 'exit':
    exit()
elif command == 'calculate':
    arithmetic_calc()


    

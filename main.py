####### Home work No. 4
### Calculator
# import madules
from src.add import add
from src.sub import sub
import os


PATH = '/home/farid/Documents/hw4/python_hw_4/src/file.txt'
# mani Function
def main():
    
    # inputes
    input_1, input_2 = map(int, input("Enter your numbers and split them with ',' : ").split(','))

    if not os.path.exists(PATH):
        print('Oops! Created a file.txt in directory: ' + PATH)
        with open(PATH, 'w+') as f:
            pass

    with open(PATH, 'a+') as f:
        f.write(f'{input_1} + {input_2} = {add(input_1, input_2)}\n')
        f.write(f'{input_1} - {input_2} = {sub(input_1, input_2)}\n')
    
    with open(PATH, 'r') as file:
        for line in file:
            print(line.strip())


    print('Your calculations saved in file.txt...')


main()
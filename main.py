####### Home work No. 4
### Calculator

from src.add import add
from src.sub import sub


def main():
    
    input_1, input_2 = map(int,input("Enter your numbers and split them with ',' : "))

    print(f'{input_1} + {input_2} = ' + add(input_1, input_2))

    print(f'{input_1} + {input_2} = ' + sub(input_1, input_2))




main()
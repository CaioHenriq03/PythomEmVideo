def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\n\033[31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return

def leiaFloat(msg):
    while True:
        user_input = input(msg)
        try:
            return float(user_input)
        except ValueError:
            if user_input == '':
                print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
                return 0
            else:
                print("\033[31mERRO: por favor, digite um número real válido.\033[m")

n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
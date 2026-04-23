def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erreur: Division par zéro"
    return x / y

def calculator():
    print("Calculatrice simple")
    print("Opérations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Entrez le premier nombre: "))
            op = input("Entrez l'opération (+, -, *, /): ")
            num2 = float(input("Entrez le deuxième nombre: "))
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Opération invalide")
                continue
            
            print(f"Résultat: {result}")
            
            again = input("Voulez-vous continuer? (oui/non): ").lower()
            if again != 'oui':
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer des nombres.")

if __name__ == "__main__":
    calculator()
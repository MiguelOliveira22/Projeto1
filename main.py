import os, tkinter, classes

def main():
    selected = "Start"
    while selected != 0:
        options()
        selected = int(input(""))
        match selected:
            case 1:
                func1()
                os.system("cls") or None
            case 2:
                func2()
                os.system("cls") or None
            case 3:
                func3()
                os.system("cls") or None
            case 4:
                func4()
                os.system("cls") or None

def options():
    print("1. Cadastro de obras de arte")
    print("2. Listagem de obras de arte")
    print("3. Página web de obras de arte")
    print("4. Triangulo de Pascal")
    print("0. Terminar a execução do programa")

def func1():
    print("Pressione [ENTER] Para Continuar!")

def func2():
    print("Pressione [ENTER] Para Continuar!")

def func3():
    print("Pressione [ENTER] Para Continuar!")

def func4():
    print("Pressione [ENTER] Para Continuar!")

if __name__ == "__main__":
    main()  
import tkinter, classes

def main():
    selected = "Start"
    while selected != 0:
        options()
        selected = int(input(""))
        match selected:
            case 1:
                func1()
            case 2:
                func2()
            case 3:
                func3()
            case 4:
                func4()

def options():
    print("1. Cadastro de obras de arte")
    print("2. Listagem de obras de arte")
    print("3. Página web de obras de arte")
    print("4. Triangulo de Pascal")
    print("0. Terminar a execução do programa")

def func1():
    pass

def func2():
    pass

def func3():
    pass

def func4():
    pass

if __name__ == "__main__":
    main()  
import os, classes
from tkinter import filedialog

def main():
    selected = "Start"
    while selected != 0:
        options()
        selected = int(input("Selecione um: "))
        match selected:
            case 1:
                func1()
            case 2:
                func2()
            case 3:
                func3()
            case 4:
                func4()
        os.system("cls") or None
    print("Muito Obrigado Pelo Uso!")

def options():
    print("1. Cadastro de obras de arte")
    print("2. Listagem de obras de arte")
    print("3. Página web de obras de arte")
    print("4. Triangulo de Pascal")
    print("0. Terminar a execução do programa")

def func1():
    ask = filedialog.askopenfilename(title="James", initialdir="C:/Documents/", multiple=False, filetypes=[("Arquivo de Texto", "*.txt")])
    if ask == "":
        print("Erro Na Abertura De Arquivo!")
        return 1
    call = classes.Obra(ask, 1)
    askb = 0
    call.preencherCampos()
    call.gravarCamposNoArquivo()
    input("Pressione [ENTER] Para Continuar!")

def func2():
    ask = filedialog.askopenfilename(title="James", initialdir="C:/Documents/", multiple=False, filetypes=[("Arquivo de Texto", "*.txt")])
    if ask == "":
        print("Erro Na Abertura De Arquivo!")
        return 1
    call = classes.Obra(ask, 0)
    call.lerCamposDoArquivo()
    input("Pressione [ENTER] Para Continuar!")

def func3():
    input("Pressione [ENTER] Para Continuar!")

def func4():
    input("Pressione [ENTER] Para Continuar!")

if __name__ == "__main__":
    main()  
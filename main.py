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
    ask = filedialog.askopenfilename(title="Selecione Um Arquivo De Obras", multiple=False, filetypes=[("Arquivo de Texto", "*.txt")])
    if len(ask) == 0:
        print("Erro Na Abertura De Arquivo!")
        input("Pressione [ENTER] Para Continuar!")
        return 1
    call = classes.Obra(ask, 1)
    ano = input("Ano da Obra: ")
    while ano != "0":
        mes = input("Mês da Obra: ")
        autor = input("Autor da Obra: ")
        nome = input("Nome da Obra: ")
        estilo = input("Estilo da Obra: ")
        valor = float(input("Valor da Obra: "))
        url = input("Arquivo de Imagem da Obra: ")
        call.preencherCampos(ano, mes, estilo, nome, autor, valor, url)
        call.gravarCamposNoArquivo()
        print()
        ano = input("Ano da Obra: ")
    call.fecharArquivo()
    input("Pressione [ENTER] Para Continuar!")

def func2():
    ask = filedialog.askopenfilename(title="Selecione Um Arquivo De Obras", multiple=False, filetypes=[("Arquivo de Texto", "*.txt")])
    if len(ask) == 0:
        print("Erro Na Abertura De Arquivo!")
        input("Pressione [ENTER] Para Continuar!")
        return 1
    call = classes.Obra(ask, 0)
    print("Ano  Mes  Estilo           Nome da Obra          Nome do Autor         Valor Est.  Arquivo de Imagem")
    i = 0
    valorobra = 0
    info = call.lerCamposDoArquivo()
    while info != 1:
        i += 1
        valorobra += call.valor_estimado
        stringbuffer = call.__str__()
        print(stringbuffer, end = "\n")
        info = call.lerCamposDoArquivo()
    print(f"Itens Listados: {i}          Valor Total Das Obras: {valorobra:.2f}")
    call.fecharArquivo()
    input("Pressione [ENTER] Para Continuar!")

def func3():
    ask = filedialog.askopenfilename(title="Selecione Um Arquivo De Obras", multiple=False, filetypes=[("Arquivo de Texto", "*.txt")])
    if len(ask) == 0:
        print("Erro Na Abertura De Arquivo!")
        input("Pressione [ENTER] Para Continuar!")
        return 1
    call = classes.Obra(ask, 0)
    arquivo = open("obras.html", "w")
    arquivo.write("<!DOCTYPE html>\n")
    arquivo.write("<html lang = ""pt-br"">\n")
    arquivo.write("<head>\n")
    arquivo.write("<title>James</title>\n")
    arquivo.write("</head>\n")
    arquivo.write("<body>\n")
    arquivo.write("<table>\n")
    arquivo.write("<tr><th>Relatório De Obras Da Galeria Virtual</th></tr>\n")
    info = "0"
    while info != 1:
        info = call.lerCamposDoArquivo()
        arquivo.write(f"<tr><td>{call.ano_obra} / {call.mes_obra}</td><td>{call.nome_obra}</td><td>{call.estilo_obra}</td><td>{call.autor_obra}</td><td>{call.valor_estimado:.2f}</td><td><img src='{call.url_obra}' alt='{call.nome_obra} por {call.autor_obra}'></td></tr>\n")
    arquivo.write("</html>\n")
    arquivo.close()
    call.fecharArquivo()
    input("Pressione [ENTER] Para Continuar!")

def func4():
    input("Pressione [ENTER] Para Continuar!")

if __name__ == "__main__":
    main()  
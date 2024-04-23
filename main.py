import os, classes, webbrowser
from tkinter import filedialog, Tk

tipos : tuple = [("Arquivo de Texto", "*.txt")]

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
    os.system("cls") or None
    root = Tk()
    ask = filedialog.askopenfilename(parent=root, title="Selecione Um Arquivo De Obras", initialdir=rf"{os.getcwd()}", multiple=False, filetypes=tipos)
    root.destroy()
    if len(ask) == 0:
        print("Erro Na Abertura De Arquivo!")
        input("Pressione [ENTER] Para Continuar!")
        return 1
    print("Para Sair Da Tela De Cadastro, Insira O Valor 0 No Campo [Ano Da Obra]!")
    call = classes.Obra(ask, 1)
    ano = input("Ano da Obra: ")
    while ano != "0":
        mes = input("Mês da Obra: ")
        autor = input("Autor da Obra: ")
        nome = input("Nome da Obra: ")
        estilo = input("Estilo da Obra: ")
        valor = float(input("Valor da Obra: "))
        url = input("Arquivo de Imagem da Obra (Dentro Da Pasta ./imagem): ")
        call.preencherCampos(ano, mes, estilo, nome, autor, valor, url)
        call.gravarCamposNoArquivo()
        print("\nPara Sair Da Tela De Cadastro, Insira O Valor 0 No Campo [Ano Da Obra]!")
        ano = input("Ano da Obra: ")
    call.fecharArquivo()
    input("Pressione [ENTER] Para Continuar!")

def func2():
    os.system("cls") or None
    root = Tk()
    ask = filedialog.askopenfilename(parent=root, title="Selecione Um Arquivo De Obras", initialdir=rf"{os.getcwd()}", multiple=False, filetypes=tipos)
    root.destroy()
    if len(ask) == 0:
        print("Erro Na Abertura De Arquivo!")
        input("Pressione [ENTER] Para Continuar!")
        return 1
    call = classes.Obra(ask, 0)
    print("Ano  Mes  Estilo           Nome da Obra          Nome do Autor              Valor Est.  Arquivo de Imagem")
    i = 0
    valorobra = 0
    info = call.lerCamposDoArquivo()
    while info != 1:
        i += 1
        valorobra += call.valor_estimado
        stringbuffer = call.__str__()
        print(stringbuffer.rstrip(), end = "\n")
        info = call.lerCamposDoArquivo()
    valorobra = f"{valorobra:.2f}".rjust(15)
    print(f"\n                           Itens Listados: {i}                    Valor: {valorobra}")
    call.fecharArquivo()
    input("\nPressione [ENTER] Para Continuar!")

def func3():
    os.system("cls") or None
    root = Tk()
    ask = filedialog.askopenfilename(parent=root, title="Selecione Um Arquivo De Obras", initialdir=rf"{os.getcwd()}", multiple=False, filetypes=tipos)
    root.destroy()
    if len(ask) == 0:
        print("Erro Na Abertura De Arquivo!")
        input("Pressione [ENTER] Para Continuar!")
        return 1
    call = classes.Obra(ask, 0)
    compare = classes.Obra(ask, 0)
    arquivo = open("obras.html", "w")
    arquivo.write("<!DOCTYPE html>\n")
    arquivo.write("<html lang = ""pt-br"">\n")
    arquivo.write("<head>\n")
    arquivo.write("<title>James</title>\n")
    arquivo.write("<link rel='stylesheet' href='obras.css'>\n")
    arquivo.write("</head>\n")
    arquivo.write("<body>\n")
    arquivo.write("<table>\n")
    arquivo.write(f"<tr><th colspan='6'>Relatório De Obras Da Galeria Virtual</th></tr>\n")
    arquivo.write(f"<tr><th class='half'>Ano / Mês</th><th class='wide'>Nome Obras</th><th class='wide'>Estilo</th><th class='wide'>Autor</th><th>Valor Estimado</th><th>Imagem</th></tr>")

    valortotal = 0
    while call.lerCamposDoArquivo() != 1:
        valorparcial = 0
        valortotal += call.valor_estimado
        info2 = compare
        while info2.lerCamposDoArquivo() != 1:
            string = info2.valor_estimado
            if call.compararCom(compare) == -1:
                string = info2.valor_estimado
        valorparcial += string
        arquivo.write(f"<tr><td>{call.ano_obra} / {call.mes_obra}</td><td>{(call.nome_obra).strip()}</td><td>{(call.estilo_obra).strip()}</td><td>{(call.autor_obra).strip()}</td><td>{call.valor_estimado:.2f}</td><td><img src='{os.getcwd() + (call.url_obra).strip()}' alt='{(call.nome_obra).strip()} por {(call.autor_obra).strip()}'></td></tr>\n")
        arquivo.write(f"<tr><th colspan='4'>Total</th><th>{valorparcial:.2f}</th></tr>")
    arquivo.write(f"<tr><th colspan='4'>Total Geral</th><th>{valortotal:.2f}</th></tr>")
    arquivo.write("</html>\n")

    arquivo.close()
    call.fecharArquivo()
    opener = webbrowser.open("obras.html")
    if opener == None:
        print("Nenhum Navegador Ou Caminho Para O Navegador Foi Encontrado (Chrome / Microsoft Edge)")
    else:
        print("Pronto!")
    input("Pressione [ENTER] Para Continuar!")

def func4():
    os.system("cls") or None
    numero = int(input("Digite até qual linha o triângulo irá: "))
    call = classes.Matematica(numero)
    triangulo = call.triangulo_de_Pascal()
    print("\n" + triangulo)
    input("Pressione [ENTER] Para Continuar!")

if __name__ == "__main__":
    main()  
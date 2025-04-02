from tkinter import *
import os

app=Tk()
app.title("Biblioteca")
app.geometry("500x300")
app.configure(background="#dde")
def sem_comando():
     print("Escrito nada")

def novo_contato():
     exec(open())
#            #executa um comando que eu quero executar
c=os.path.dirname(__file__)
nome_arquivo=c+"\\livros.txt"

def gravar_dados_livro(ctitulo, cautor, cstatus):
    with open(nome_arquivo,"a") as arquivo:
        arquivo.write("\nId........:%s" % Livro.id)
        arquivo.write("\nTitulo....:%s" % ctitulo.get())
        arquivo.write("\nAutor.....:%s" % cautor.get())
        arquivo.write("\nStatus....:%s" % cstatus.get(1.0, END))
        arquivo.write("\n")
        arquivo.write()

class Livro:
    def __init__(self, titulo:str, autor:str, status:bool):
        global contador_livro 
        self.titulo = titulo
        self.autor = autor
        self.id = contador_livro
        self.status = status
        contador_livro += 1

    def janela_cadastro():
        cad = Toplevel(app)
        cad.title("Cadastro de Livro")
        cad.geometry("400x300")
        Label(cad,text="Titulo",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
        ctitulo=Entry(cad)
        ctitulo.place(x=10, y=30, width=200, height=20)
        
        Label(cad,text="Autor",background="#dde",foreground="#009",anchor=W).place(x=10, y=60, width=100, height=20)
        cautor=Entry(cad)
        cautor.place(x=10, y=80, width=100, height=20)

        Label(cad,text="Status",background="#dde",foreground="#009",anchor=W).place(x=10, y=110, width=100, height=20)
        cstatus=Entry(cad)
        cstatus.place(x=10, y=130, width=300, height=20)
        
        Button(cad, text="Imprimir", command=lambda: gravar_dados_livro(ctitulo,cautor,cstatus)).place(x=10, y=270,width=100,height=20)    #place = posiciona


def janela_cadastro_membro():
    memb = Toplevel(app)
    memb.title("Cadastro Membro")
    memb.geometry("400x300")
    Label(memb,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
    vnome=Entry(memb)
    vnome.place(x=10, y=30, width=200, height=20)

    Button(memb, text="Imprimir", command=gravar_dados).place(x=10, y=270,width=100,height=20)

def janela_emprestar_livro():
    liv = Toplevel(app)
    liv.title("Emprestar Livro")
    liv.geometry("400x300")
    Label(liv,text="Titulo",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
    vnome=Entry(liv)
    vnome.place(x=10, y=30, width=200, height=20)

    Label(liv,text="Autor",background="#dde",foreground="#009",anchor=W).place(x=10, y=60, width=100, height=20)
    vfone=Entry(liv)
    vfone.place(x=10, y=80, width=100, height=20)

    Label(liv,text="Status",background="#dde",foreground="#009",anchor=W).place(x=10, y=110, width=100, height=20)
    vemail=Entry(liv)
    vemail.place(x=10, y=130, width=300, height=20)

    Button(liv, text="Imprimir", command=gravar_dados).place(x=10, y=270,width=100,height=20)  

def janela_devolver():
    dev = Toplevel(app)
    dev.title("Devolver Livro")
    dev.geometry("400x300")
    Label(dev,text="Titulo",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
    vnome=Entry(dev)
    vnome.place(x=10, y=30, width=200, height=20)

    Label(dev,text="Autor",background="#dde",foreground="#009",anchor=W).place(x=10, y=60, width=100, height=20)
    vfone=Entry(dev)
    vfone.place(x=10, y=80, width=100, height=20)

    Label(dev,text="Status",background="#dde",foreground="#009",anchor=W).place(x=10, y=110, width=100, height=20)
    vemail=Entry(dev)
    vemail.place(x=10, y=130, width=300, height=20)

    Button(dev, text="Imprimir", command=gravar_dados).place(x=10, y=270,width=100,height=20)

def janela_pesquisar_livros():
    pes = Toplevel(app)
    pes.title("Pesquisar Livro")
    pes.geometry("400x300")

    Label(pes,text="Informe o Nome",background="#dde",foreground="#009",anchor=W).place(x=10, y=60, width=100, height=20)
    vfone=Entry(pes)
    vfone.place(x=10, y=80, width=100, height=20)

    Button(pes, text="Pesquisar", command=gravar_dados).place(x=10, y=270,width=100,height=20)


barra_de_menu=Menu(app)
menu_contatos=Menu(barra_de_menu, tearoff=0)
menu_contatos.add_command(label="Cadastrar Livro", command=Livro.janela_cadastro)
menu_contatos.add_command(label="Cadastrar Membro", command=janela_cadastro_membro)
menu_contatos.add_command(label="Emprestar Livro", command=janela_emprestar_livro)
menu_contatos.add_command(label="Devolver Livro", command=janela_devolver)
menu_contatos.add_separator()
menu_contatos.add_command(label="Fechar", command=app.quit)
barra_de_menu.add_cascade(label="Menu", menu=menu_contatos)

menu_manutençao=Menu(barra_de_menu, tearoff=0)
menu_manutençao.add_command(label="Livros Disponiveis", command=sem_comando)
menu_manutençao.add_command(label="Livros Emprestados", command=sem_comando)
menu_manutençao.add_command(label="Todos os Livros", command=sem_comando)
barra_de_menu.add_cascade(label="Livros", menu=menu_manutençao)

menu_sobre=Menu(barra_de_menu, tearoff=0)
menu_sobre.add_command(label="Pesquisar Livro", command=janela_pesquisar_livros)
menu_sobre.add_command(label="Mostrar Membros", command=sem_comando)
barra_de_menu.add_cascade(label="Pesquisa", menu=menu_sobre)

#anchor -> N=norte, S=sul, E=leste, W=oeste
#NE=nordeste, SE=sudeste, SO=sudoeste, NO=noroeste


app.config(menu=barra_de_menu)
app.mainloop()
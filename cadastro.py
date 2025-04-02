from tkinter import *
import os

app1=Tk()
app1.title("Biblioteca")
app1.geometry("500x300")
app1.configure(background="#dde")

c=os.path.dirname(__file__)
nome_arquivo=c+"\\nomes.txt"

def gravar_dados():
    arquivo=open(nome_arquivo,"a")
    arquivo.write("\nNome......:%s" % vnome.get())
    arquivo.write("\nTelefone..:%s" % vfone.get())
    arquivo.write("\nE-mail....:%s" % vemail.get())
    arquivo.write("\nObs.......:%s" % vobs.get(1.0, END))
    arquivo.write("\n")
    arquivo.write()

Label(app1,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome=Entry(app1)
vnome.place(x=10, y=30, width=200, height=20)

Label(app1,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10, y=60, width=100, height=20)
vfone=Entry(app1)
vfone.place(x=10, y=80, width=100, height=20)

Label(app1,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10, y=110, width=100, height=20)
vemail=Entry(app1)
vemail.place(x=10, y=130, width=300, height=20)

Label(app1,text="Obs",background="#dde",foreground="#009",anchor=W).place(x=10, y=160, width=160, height=20)
vobs=Text(app1)
vobs.place(x=10, y=180, width=300, height=80)

Button(app1, text="Imprimir", command=gravar_dados).place(x=10, y=270,width=100,height=20)

app1.mainloop()


    # print('Menu Biblioteca:')
    # print('1 -- Cadastrar livro')
    # print('2 -- Cadastrar membro')
    # print('3 -- Emprestar livro')
    # print('4 -- Devolver Livro')
    # print('5 -- Livros disponiveis')
    # print('6 -- Livros emprestados')
    # print('7 -- Pesquisar livro')
    # print('8 -- Mostrar membros')
    # print('9 -- Mostrar todos livros')
    # print('10 -- Histórico de emprestimos')
    # print('11 -- Sair')
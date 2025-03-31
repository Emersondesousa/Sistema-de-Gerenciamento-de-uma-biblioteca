
# [PY-A14] ENTREGUE SEU PROJETO ABAIXO SEGUINDO AS OBSERVAÇÕES
# SUGESTÃO DE PROJETO: 
# APLICATIVO DE GERENCIAMENTO DE BIBLIOTECA COM CLASSES E POO
# Criação de Classes:
# Crie as classes Livro, Membro e Biblioteca para representar os elementos da biblioteca.
# Classe Livro:
# Esta classe deve conter atributos como título, autor, ID e status de empréstimo (disponível ou emprestado).
# Classe Membro:
# A classe Membro deve incluir atributos como nome, número de membro e histórico de livros emprestados.
# Classe Biblioteca:
# A classe Biblioteca deve manter um catálogo de livros disponíveis, um registro de membros e métodos para operações como empréstimo,
# devolução e pesquisa de livros.
# Operações da Biblioteca:
# Implemente métodos na classe Biblioteca para adicionar livros ao catálogo, adicionar membros à biblioteca, 
# permitir empréstimo de livros por membros, registrar a devolução de livros e pesquisar livros por título, autor ou ID.
# Interatividade com o Usuário:
# Desenvolva uma interface de linha de comando ou uma interface gráfica simples usando tkinter para permitir que os usuários
# interajam com a biblioteca. Esta interface deve oferecer funcionalidades como adicionar livros, adicionar membros, 
# emprestar e devolver livros, e pesquisar livros por diferentes critérios.
# O projeto será estruturado em classes e utilizará conceitos de programação orientada a objetos para criar uma aplicação 
# de gerenciamento de biblioteca funcional e interativa.




import time
from tkinter import *
import tkinter as tk

lista_biblioteca = []
membros = []
livros_emprestados = []
historico_livros = []

contador_livro = 0
contador_membro = 0

class Livro:
    def __init__(self, titulo:str, autor:str, status:bool):
        global contador_livro 
        self.titulo = titulo
        self.autor = autor
        self.id = contador_livro
        self.status = status
        contador_livro += 1

    def cadastrar_livro(self):
        if self.titulo.strip() == "" or self.autor.strip() == "":
            print('Verifique o título ou o autor, não pode estar vazio...')
        else:    
            cadastrar = {'título': self.titulo, 'autor':self.autor, 'id':self.id, 'status empréstimo':True }
            lista_biblioteca.append(cadastrar)
            print(f'Livro {self.titulo} cadastrado com sucesso!')

class Membro:
    def __init__(self,nome:str):
        global contador_membro
        self.nome = nome
        self.id_membro = contador_membro
        contador_membro += 1

    def cadastrar_membro(self):
        if self.nome.strip() == "":
            print('Nome não pode ser vazio, verifique o nome..')
        else:
            cadastro = {'nome':self.nome, 'id': self.id_membro}
            membros.append(cadastro)
            print(f'Membro cadastrado com sucesso.')

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome

    def emprestar_livro(self, nome_membro, titulo_livro):
        for membro in membros:
            if nome_membro == membro["nome"]:
                for livro in lista_biblioteca:
                    if titulo_livro == livro["título"] and livro["status empréstimo"] == True:
                        livro["status empréstimo"] = False
                        cadastrar = {'nome':nome_membro, 'livro emprestado': titulo_livro }
                        livros_emprestados.append(cadastrar)
                        for i in historico_livros:
                            if i["nome"] == nome_membro:
                                i["historico"].append(titulo_livro)
                                return
                        historico = {'nome':nome_membro, 'historico': [titulo_livro]}
                        historico_livros.append(historico)
                        print(f'Livro {titulo_livro} emprestado para {nome_membro}')    
                        return
                    print('Este livro já está emprestado')
                    return
        print('Membro não encontrado na lista de membros.')

    def devolver_livro(self, livro_devolucao):
        for livro in livros_emprestados:
            if livro_devolucao == livro["livro emprestado"]:
                livros_emprestados.remove(livro)
                for i in lista_biblioteca:
                    if livro_devolucao == i["título"]:
                        i["status empréstimo"] = True
                        print(f'Livro {livro_devolucao} devolvido.')
                        return
        print(f'O livro {livro_devolucao} não foi encontrado.')
    
    def historico_de_emprestimos(self):
        if not historico_livros:
            print('Não há livros no histórico.')
        for historico in historico_livros:
            print(historico)

    def livros_disponiveis(self):
        if not lista_biblioteca:
            print('Não há livros disponiveis.')
        else:    
            for i in lista_biblioteca:
                if i["status empréstimo"] == True:
                    print(f'Título: {i["título"]}, Autor: {i["autor"]}, Id: {i["id"]}')
                
    def mostrar_livros_emprestados(self):
        if not livros_emprestados:
            print('Não há livros emprestados.')
        else:
            for i in livros_emprestados:
                    print(f'Livro: {i["livro emprestado"]}, Membro: {i["nome"]}')

    def pesquisar_livro(self, x):
        for i in lista_biblioteca:
            if x == i["título"] or x == i["autor"] or x == str(i["id"]):
                print(i)
                return
        print('Nenhuma infomação encontrada.')

    def mostrar_membros(self):
        if not membros:
            print('Não há membros cadastrados.')
        for i in membros:
            print(f'Nome: {i["nome"]}, Id: {i["id"]}')

    def mostrar_todos_livros(self):
        if not lista_biblioteca:
            print('Não há livros cadastrados.')
        for i in lista_biblioteca:
            print(f'Título: {i["título"]}, Autor: {i["autor"]}, Id: {i["id"]}, Status: {i["status empréstimo"]}')       


janela = Tk()
janela.title("Biblioteca")

texto_menu = Label(janela, text="Menu")
texto_menu.grid(column=0, row=0)

botao = Button(janela, text="Cadastrar livro", command=Livro.cadastrar_livro)
botao.grid(column=0, row=1)
texto_cadastros = Label(janela, text="")
botao.grid(column=0, row=2)
label = tk.Label(janela, text="Digite algo:")
label.pack(pady=10)

janela.mainloop() 

biblioteca = Biblioteca('')
while True:

    print('Menu Biblioteca:')
    print('1 -- Cadastrar livro')
    print('2 -- Cadastrar membro')
    print('3 -- Emprestar livro')
    print('4 -- Devolver Livro')
    print('5 -- Livros disponiveis')
    print('6 -- Livros emprestados')
    print('7 -- Pesquisar livro')
    print('8 -- Mostrar membros')
    print('9 -- Mostrar todos livros')
    print('10 -- Histórico de emprestimos')
    print('11 -- Sair')
    opcao = input('Informe a opção desejada: ')

    match opcao:

        case '1':
            titulo = input('Informe o titulo: ')
            autor = input('Informe o autor: ')
            livro = Livro(titulo, autor, True)
            livro.cadastrar_livro()
            time.sleep(1)

        case '2':
            nome = input('Informe o nome: ')
            membro = Membro(nome)
            membro.cadastrar_membro()
            time.sleep(1)

        case '3':
            nome_membro = input('Informe o nome do membro: ')
            titulo_livro = input('Informe o título do livro: ')
            biblioteca.emprestar_livro(nome_membro, titulo_livro)
            time.sleep(1)

        case '4':
            nome_livro = input('Informe o nome do livro para devolução: ')
            biblioteca.devolver_livro(nome_livro)
            time.sleep(1)

        case '5':
            biblioteca.livros_disponiveis()
            time.sleep(1)

        case '6':
            biblioteca.mostrar_livros_emprestados()
            time.sleep(1)

        case '7':
            pesquisa = input('Informe o título, autor ou id do livro: ')
            biblioteca.pesquisar_livro(pesquisa)
            time.sleep(1)

        case '8':
            biblioteca.mostrar_membros()
            time.sleep(1)

        case '9':
            biblioteca.mostrar_todos_livros()
            time.sleep(1)    

        case '10':
            biblioteca.historico_de_emprestimos()
            time.sleep(1)

        case '11':
            print('Programa finalizado.')
            break

        case _:
            print('Opção inválida, tente novamente...')
            time.sleep(1)    



    # menu = tk.Menu(janela)
    # janela.config(menu=menu)
    # file_menu = tk.Menu(menu)
    # menu.add_cascade(label="Arquivo", menu=file_menu)
    # file_menu.add_command(label="Abrir")
    # file_menu.add_command(label="Salvar")
    # file_menu.add_separator()
    # file_menu.add_command(label="Sair")
from tkinter import *
from factories import *

# Tela principal

tela = Tk()
tela.geometry('770x400')
tela.title('CRUD clientes')
tela.configure(background='#5084BC')

# notebook e abas

nb = ttk.Notebook(tela)
nb.place(x=10, y=10, width=750, height=380)

t1 = Frame(nb)
t2 = Frame(nb)
t3 = Frame(nb)
nb.add(t1, text='cadastrar novo')
nb.add(t2, text='atualizar cadastro')
nb.add(t3, text='Consultar e Apagar')


# Aba Cadastro

te1 = Display(t1)
te1.update(pesquisa())

camp = LabelFrame(t1, text='cadastrar novo', borderwidth=1, relief='solid')
camp.place(x=10, y=220, width='730', height='110')

cad = Button(t1, text='Cadastrar', command=lambda: salvar(vnome.get(), vcpf.get(), vend.get(), vtel.get()))
cad.place(x=650, y=180, width='60', height='20')

# nome
Label(camp, text='NOME:').place(x=10, y=10, width='50', height='20')
vnome = Entry(camp)
vnome.place(x=70, y=10, width='250', height='20')

# cpf
Label(camp, text='CPF:').place(x=450, y=10, width='50', height='20')
vcpf = Entry(camp)
vcpf.place(x=500, y=10, width='100', height='20')

# endereço
Label(camp, text='ENDEREÇO:').place(x=10, y=50, width='70', height='20')
vend = Entry(camp)
vend.place(x=100, y=50, width='400', height='20')

# telefone
Label(camp, text='TELEFONE:').place(x=510, y=50, width='70', height='20')
vtel = Entry(camp)
vtel.place(x=590, y=50, width='100', height='20')

# Aba Atualizar cadastro

te2 = Display(t2)
te2.update(pesquisa())

camp2 = LabelFrame(t2, text='atualizar', borderwidth=1, relief='solid')
camp2.place(x=10, y=220, width='730', height='110')

# Entrada de dados

Label(camp2, text='NOME:').place(x=10, y=10, width='50', height='20')
atNome = Entry(camp2)
atNome.place(x=70, y=10, width='250', height='20')
Label(camp2, text='CPF:').place(x=450, y=10, width='50', height='20')
atCpf = Entry(camp2)
atCpf.place(x=500, y=10, width='100', height='20')
Label(camp2, text='ENDEREÇO:').place(x=10, y=50, width='70', height='20')
atEnd = Entry(camp2)
atEnd.place(x=100, y=50, width='400', height='20')
Label(camp2, text='TELEFONE:').place(x=510, y=50, width='70', height='20')
atTel = Entry(camp2)
atTel.place(x=590, y=50, width='100', height='20')

# seleção de dados para a atualização

nome = StringVar()
cpf = StringVar()
end = StringVar()
tel = StringVar()

cb_n = Checkbutton(t2, text='nome', variable=nome, onvalue='s', offvalue='n')
cb_n.place(x=620, y=110)
cb_c = Checkbutton(t2, text='cpf', variable=cpf, onvalue='s', offvalue='n')
cb_c.place(x=620, y=130)
cb_e = Checkbutton(t2, text='endereço', variable=end, onvalue='s', offvalue='n')
cb_e.place(x=620, y=150)
cb_t = Checkbutton(t2, text='telefone', variable=tel, onvalue='s', offvalue='n')
cb_t.place(x=620, y=170)

atualizar = Button(t2, text='Atualizar', command=lambda: atualizar(atNome.get(), atCpf.get(), atEnd.get(), atTel.get(), es_nome=cb_n, es_cpf=cb_c, es_end=cb_e, es_tel=cb_t))
atualizar.place(x=650, y=60, width='60', height='20')

# Aba Consultar e Apagar

te3 = Display(t3)
te3.update(pesquisa())

camp3 = LabelFrame(t3, text='Consultar', borderwidth=1, relief='solid')
camp3.place(x=10, y=220, width='730', height='110')

# seleção de pesquisa

p_nome = StringVar()
p_cpf = StringVar()

c_nome = Checkbutton(camp3, text='nome', variable=p_nome, onvalue='s', offvalue='n')
c_cpf = Checkbutton(camp3, text='cpf', variable=p_cpf, onvalue='s', offvalue='n')
c_nome.place(x=100, y=20)
c_cpf.place(x=100, y=50)

Label(camp3, text='nome ou cpf').place(x=250, y=20)

# Entrada

cons = Entry(camp3)
cons.place(x=250, y=50, width='200', height='20')

pesquisar = Button(camp3, text='pesquisar', command=lambda: pesquisa(cons, p_nome, p_cpf))
showall = Button(camp3, text='mostrar tudo')
deletar = Button(camp3, text='apagar')
pesquisar.place(x=600, y=35, width='60', height='20')
showall.place(x=600, y=5, width='80', height='20')
deletar.place(x=600, y=60, width='60', height='20')


tela.mainloop()

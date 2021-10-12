from tkinter import ttk
from banco import *
from tkinter import messagebox


# construtor do treeview


class Display:
    def __init__(self, pai):
        self.tdados = ttk.Treeview(pai, columns=('Nome', 'cpf', 'endereço', 'telefone'), show='headings')
        self.tdados.column('Nome', minwidth=0, width=50)
        self.tdados.column('cpf', minwidth=0, width=50)
        self.tdados.column('endereço', minwidth=0, width=50)
        self.tdados.column('telefone', minwidth=0, width=50)
        self.tdados.heading('Nome', text='nome')
        self.tdados.heading('cpf', text='cpf')
        self.tdados.heading('endereço', text='endereço')
        self.tdados.heading('telefone', text='telefone')
        self.tdados.place(x=10, y=10, width=600, height=200)

    def update(self, dado):
        for (nome, cpf, end, tel) in dado:
            self.tdados.insert("", "end", values=(nome, cpf, end, tel))

    def intenselicionado(self):
        return self.tdados.selection()[0]


# comandos

def salvar(nome, cpf, end, tel):
    if nome or cpf or end or tel == '':
        messagebox.showinfo(title='alerta', message='você precisa preecher todos os campos')
    else:
        vinsert = """
            insert into clientes 
            (nome, cpf, endereco, telefone)
            VALUES ('{}','{}','{}','{}')
        """.format(nome, cpf, end, tel)
        dml(vcon, vinsert)


def atualizar(*args, es_nome, es_cpf, es_end, es_tel):
    dd = list(*args)
    dd2 = []
    for valor in dd:
        if not valor == '':
            dd2.append(valor)


def pesquisa(n_c=None, est1=None, est2=None):
    consulta1 = """
                select nome, cpf, endereco, telefone from clientes
                where nome = '{}'
            """.format(n_c)
    consulta2 = """
                select nome, cpf, endereco, telefone from clientes
                where cpf = '{}'
            """.format(n_c)
    if est1 == 's' and est2 == 'n':
        res = busca(vcon, consulta1)
    elif est1 == 'n' and est2 == 's':
        res = busca(vcon, consulta2)
    else:
        res = busca(vcon, vbusca)
    return res

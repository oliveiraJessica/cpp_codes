from tkinter import *
from pymysql import *
import tkinter.messagebox


# Funcao chamada ao clicar no botao
def efetuar_login():
    connection = connect(host='localhost',
                         user='root',
                         password='',
                         db='cadastro',
                         port=3307)
    cursor = connection.cursor()

    try:
        query = 'select * from users where login = %s'
        rows_affected = cursor.execute(query, login.get())
        if rows_affected <= 0:
            tkinter.messagebox.showinfo('Informação de login', 'Seu usuário ou senha está incorreto')
        else:
            row = cursor.fetchone()
            if row[2] == password.get():
                print('Tudo certo')
            else:
                print('Senha errada')

    finally:
        connection.close()


#    print('Login: ' + login.get())
#    print('Senha: ' + password.get())
#    print('O usuário deseja lembrar o login? %r' % bool(stateLembrarLogin.get()))
#    if stateLembrarLogin.get():
#        print('\tLogin salvo')
#    else:
#        print('\tLogin não salvo')


root = Tk()
root.title('Protótipo v.0.1')

main_frame = Frame(root)
main_frame.grid(
                column=0, row=0,
                sticky=(N, W, E, S))

# Título na primeira linha da tela, expandido para todas as colunas
Label(main_frame,
      text='Acesso ao sistema',
      font=('Courier', 20)
      ).grid(row=0, column=0, columnspan=3, padx=10, pady=3)

# Segunda linha com label de Usuário, seguindo de campo para usuário digitar o login
Label(main_frame,
      text='Usuário:',
      font=('Courier', 12)
      ).grid(row=1, column=0, sticky=E)

login = StringVar()
login_entry = Entry(main_frame,
                    width=20,
                    textvariable=login)
login_entry.focus()
login_entry.grid(row=1, column=1, columnspan=2, padx=10)

# Segunda linha com label de senha, seguindo de campo para usuário digitar o password
Label(main_frame,
      text='Senha:',
      font=('Courier', 12)
      ).grid(row=2, column=0, sticky=E)

password = StringVar()
password_entry = Entry(main_frame,  # Password com caracteres escondidos
                       width=20,
                       show="*",
                       textvariable=password
                       ).grid(row=2, column=1, columnspan=2)

# Check button para o programa lembrar o usuário (nao implementado)
state_remember_login = BooleanVar()
state_button = Checkbutton(main_frame,
                           text='Lembrar usuário',
                           offvalue=False,
                           onvalue=True,
                           variable=state_remember_login,
                           font=('Courier', 12),
                           ).grid(row=3, column=0, columnspan=2)

# Botão para efetuar o login
login_button = Button(main_frame,
                      text='Entrar',
                      font=('Courier', 12),
                      command=efetuar_login
                      ).grid(row=3, column=2)

root.mainloop()

from tkinter import *


# Funcao chamada ao clicar no botao
def efetuar_login():
    print('Login: ' + login.get())
    print('Senha: ' + password.get())
    print('O usuário deseja lembrar o login? %r' % bool(stateLembrarLogin.get()))
    if stateLembrarLogin.get():
        print('\tLogin salvo')
    else:
        print('\tLogin não salvo')


root = Tk()
root.title('Protótipo v.0.1')

mainFrame = Frame(root)
mainFrame.grid(
    column=0, row=0,
    sticky=(N, W, E, S)
)

# Título na primeira linha da tela, espandido para todas as colunas
Label(mainFrame,
      text='Acesso ao sistema',
      font=('Courier', 20)
      ).grid(row=0, column=0, columnspan=3)

# Segunda linha com label de Usuário, seguindo de campo para usuário digitar o login
Label(mainFrame,
      text='Usuário:',
      font=('Courier', 12)
      ).grid(row=1, column=0)

login = StringVar()
loginEntry = Entry(mainFrame,
                   width=20,
                   textvariable=login
                   ).grid(row=1, column=1, columnspan=2)

# Segunda linha com label de senha, seguindo de campo para usuário digitar o password
Label(mainFrame,
      text='Senha:',
      font=('Courier', 12)
      ).grid(row=2, column=0)

password = StringVar()
passwordEntry = Entry(mainFrame,    #Password com caracteres escondidos
                      width=20,
                      show="*",
                      textvariable=password
                      ).grid(row=2, column=1, columnspan=2)

# Check button para o programa lembrar o usuário (nao implementado)
stateLembrarLogin = BooleanVar()
stateButton = Checkbutton(mainFrame,
                          text='Lembrar usuário',
                          offvalue=False,
                          onvalue=True,
                          variable=stateLembrarLogin,
                          font=('Courier', 12),
                          ).grid(row=3, column=0, columnspan=2)

# Botão para efetuar o login
loginButton = Button(mainFrame,
                     text='Entrar',
                     font=('Courier', 12),
                     command=efetuar_login
                     ).grid(row=3, column=2)

root.mainloop()

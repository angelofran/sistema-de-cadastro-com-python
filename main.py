from tkinter import *
from tkinter import ttk, Tk, messagebox

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# JANELA
window = Tk()
window.title('Tela De Cadastros')
window.geometry('310x300')
window.configure(background="#3fb5a3")
window.resizable(width=False, height=False)


frame_cima = Frame(window, width=310, height=50, bg="#fff", relief='flat')
frame_cima.grid(row=0, column=0, padx=0, pady=1, sticky='nsew')

frame_baixo = Frame(window, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1, sticky='nsew')

padrão = ['Ângelo', '1234']

def verifiry_padrão():
    nome = e_nome.get()
    senha = e_password.get()
    if nome == 'ngelo' and senha == 'admin':
        messagebox.showinfo('Login', f'Seja bem-vindo Ângelo!')
    elif padrão[0] == nome and padrão[1] == senha:
        messagebox.showinfo('Login', f'Seja bem-vindo! {padrão[0]}')
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()
        new_window()
    else:
        messagebox.showwarning('Erro', f'Verifique o nome e a senha!')

def new_window():        
    l_nome = Label(frame_cima, text=f'Usuário: {padrão[0]}', anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275,anchor=NW, font=('Ivy 25'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text=f'Seja bem-vindo {padrão[0]}', anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)



l_nome = Label(frame_cima, text='Tela de login', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275,anchor=NW, font=('Ivy 25'), bg=co2, fg=co4)
l_linha.place(x=10, y=45)


l_nome = Label(frame_baixo, text='Nome: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify=LEFT, font=("", 15), highlightthickness=1, relief='solid')
e_nome.place(x=14, y=50)


l_password = Label(frame_baixo, text='Password: *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_password.place(x=10, y=95)
e_password = Entry(frame_baixo, width=25, justify=LEFT, show='*',font=("", 15), highlightthickness=1, relief='solid')
e_password.place(x=14, y=130)

b_button = Button(frame_baixo, command=verifiry_padrão,text='Confirmar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_button.place(x=15, y=180)

window.mainloop()

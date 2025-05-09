import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import re

# Configurações do tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Função de validação e cadastro
def cadastrar_usuario():
    email_valor = entry_email.get().strip()
    senha_valor = entry_senha.get().strip()
    telefone_valor = entry_telefone.get().strip()
    usuario_valor = entry_usuario.get().strip()
    cpf_valor = entry_cpf.get().strip()
    data_valor = entry_data.get().strip()

    if not all([email_valor, senha_valor, telefone_valor, usuario_valor, cpf_valor, data_valor]):
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_valor):
        messagebox.showerror("Erro", "E-mail inválido.")
        return

    if len(senha_valor) < 6:
        messagebox.showerror("Erro", "A senha deve conter pelo menos 6 caracteres.")
        return

    if not telefone_valor.isdigit():
        messagebox.showerror("Erro", "Telefone deve conter apenas números.")
        return

    if not cpf_valor.isdigit() or len(cpf_valor) != 11:
        messagebox.showerror("Erro", "CPF inválido. Deve conter 11 dígitos.")
        return

    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    limpar_campos()

# Função para limpar campos
def limpar_campos():
    for entry in [entry_email, entry_senha, entry_telefone, entry_usuario, entry_cpf, entry_data]:
        entry.delete(0, ctk.END)

# Interface
app = ctk.CTk()
app.title("MatchBike")
app.geometry("360x640")
app.resizable(False, False)
app.configure(fg_color="#3AAFFF")  # fundo azul aproximado



# Título
titulo = ctk.CTkLabel(app, text="CADASTRO", font=ctk.CTkFont(size=24, weight="bold"), text_color="black")
titulo.pack(pady=10)

# Entradas
entry_email = ctk.CTkEntry(app, placeholder_text="E-mail", width=280, height=40,
                           corner_radius=20, fg_color="#A8D6FF", text_color="black")
entry_email.pack(pady=5)
entry_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*", width=280, height=40,
                           corner_radius=20, fg_color="#A8D6FF", text_color="black")
entry_senha.pack(pady=5)

entry_telefone = ctk.CTkEntry(app, placeholder_text="Telefone", width=280, height=40,
                              corner_radius=20, fg_color="#A8D6FF", text_color="black")
entry_telefone.pack(pady=5)

entry_usuario = ctk.CTkEntry(app, placeholder_text="Usuário", width=280, height=40,
                             corner_radius=20, fg_color="#A8D6FF", text_color="black")
entry_usuario.pack(pady=5)

entry_cpf = ctk.CTkEntry(app, placeholder_text="CPF", width=280, height=40,
                         corner_radius=20, fg_color="#A8D6FF", text_color="black")
entry_cpf.pack(pady=5)

entry_data = ctk.CTkEntry(app, placeholder_text="Data de Nascimento (DD/MM/AAAA)", width=280, height=40,
                          corner_radius=20, fg_color="#A8D6FF", text_color="black")
entry_data.pack(pady=5)

# Botão de cadastro
botao = ctk.CTkButton(app,
                      text="Cadastrar",
                      command=cadastrar_usuario,
                      width=280,
                      height=40,
                      corner_radius=20,
                      fg_color="#89C2F7",     # azul mais escuro
                      text_color="black",
                      hover_color="#5FA8D3")  # cor ao passar o mouse
botao.pack(pady=30)

# Logo 
try:
    logo_imagem = ctk.CTkImage(Image.open("Logo.png"), size=(300, 250))
    logo_label = ctk.CTkLabel(app, image=logo_imagem, text="")
    logo_label.pack(pady=10)
except Exception:
    pass  # Não falha se o logo não existir



app.mainloop()

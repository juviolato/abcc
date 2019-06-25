from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
import base

class ABCC(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.title('Sistema de Trocas - ABCC')
		self.geometry('600x400')
		self.resizable(0,0)

		container = Frame(self)
		container.pack(side='top', fill=BOTH, expand=True)
		container.grid(row=0,column=0)

		self.frames = {}

		for F in (StartPage, LoginPage, RegisterPage, CollectionPage, SearchPage, ManagerPage):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0,column=0,sticky='nsew')

		self.show_frame(StartPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		butFrame = Frame(self)
#		butFrame.grid(row=0,column=0)
		butFrame.pack(fill=BOTH, expand=True)
		self.buttonQuit				= Button(butFrame, text='Sair',		 			 command=self.quit)
		self.buttonLogin			= Button(butFrame, text='Login',				 command=lambda: controller.show_frame(LoginPage))
		self.buttonRegister			= Button(butFrame, text='Cadastrar Instituição', command=lambda: controller.show_frame(RegisterPage))
		self.buttonEditCollection	= Button(butFrame, text='Arquivo', 				 command=lambda: controller.show_frame(CollectionPage))
		self.buttonSearchPieces		= Button(butFrame, text='Pesquisar peças',		 command=lambda: controller.show_frame(SearchPage))
		self.buttonManager 			= Button(butFrame, text='Área de gerência',		 command=lambda: controller.show_frame(ManagerPage))
		
		self.buttonQuit.pack(fill=BOTH, expand=True)
		self.buttonLogin.pack(fill=BOTH, expand=True)
		self.buttonRegister.pack(fill=BOTH, expand=True)
		self.buttonEditCollection.pack(fill=BOTH, expand=True)
		self.buttonSearchPieces.pack(fill=BOTH, expand=True)
		self.buttonManager.pack(fill=BOTH, expand=True)

class LoginPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		cnpjLabel = Label(self, text='CNPJ:')
		cnpjLabel.grid(row=0, sticky='e')
		self.cnpjEntry = Entry(self)
		self.cnpjEntry.grid(row=0,column=1)
		passwordLabel = Label(self, text='Senha:')
		passwordLabel.grid(row=1, sticky='e')
		self.passwordEntry = Entry(self, show='*')
		self.passwordEntry.grid(row=1,column=1)

		self.buttonLogin = Button(self, text='Realizar Login', command=self.login)
		self.buttonLogin.grid(row=2,columnspan=2)

		self.buttonBack = Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage))
		self.buttonBack.grid(row=3,columnspan=2)

	def login(self):
		cnpj = self.cnpjEntry.get()
		password = self.passwordEntry.get()
		g.login(cnpj, password)
		messagebox.showinfo('LOGIN REALIZADO','O login foi realizado com sucesso')

class RegisterPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		nameLabel = Label(self, text='Nome:')
		cnpjLabel = Label(self, text='CNPJ:')
		passwordLabel = Label(self, text='Senha:')
		addressLabel = Label(self, text='Endereço:')
		telephoneLabel = Label(self, text='Telefone:')
		emailLabel = Label(self, text='E-mail:')
		
		nameLabel.grid(row=0, sticky='e')
		cnpjLabel.grid(row=1, sticky='e')
		passwordLabel.grid(row=2, sticky='e')
		addressLabel.grid(row=3, sticky='e')
		telephoneLabel.grid(row=4, sticky='e')
		emailLabel.grid(row=5, sticky='e')

		self.nameEntry = Entry(self)
		self.cnpjEntry = Entry(self)
		self.passwordEntry = Entry(self, show='*')
		self.addressEntry = Entry(self)
		self.telephoneEntry = Entry(self)
		self.emailEntry = Entry(self)

		self.nameEntry.grid(row=0,column=1)
		self.cnpjEntry.grid(row=1,column=1)
		self.passwordEntry.grid(row=2,column=1)
		self.addressEntry.grid(row=3,column=1)
		self.telephoneEntry.grid(row=4,column=1)
		self.emailEntry.grid(row=5,column=1)

		self.buttonLogin = Button(self, text='Cadastrar Instituição', command=self.register)
		self.buttonLogin.grid(row=6,columnspan=2)

		self.buttonBack = Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage))
		self.buttonBack.grid(row=7,columnspan=2)

	def register(self):
		name = self.nameEntry.get()
		cnpj = self.cnpjEntry.get()
		password = self.passwordEntry.get()
		address = self.addressEntry.get()
		telephone = self.telephoneEntry.get()
		email = self.emailEntry.get()
		g.registerInstitution(name, cnpj, address, telephone, email, password)
		messagebox.showinfo('REGISTRO CONCLUÍDO','O registro da instituição foi feito com sucesso')

class CollectionPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text='this is the collection page').pack()

		self.buttonBack = Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage))
		self.buttonBack.pack()

class SearchPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text='this is search page').pack()

		self.buttonBack = Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage))
		self.buttonBack.pack()

class ManagerPage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text='this is manager page').pack()

		self.buttonBack = Button(self, text='Voltar', command=lambda: controller.show_frame(StartPage))
		self.buttonBack.pack()

if __name__ == '__main__':
	g = base.Communicator()
	abcc = ABCC()
	abcc.mainloop()

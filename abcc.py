from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
#import PIL.Image, PIL.ImageTk
import base

class GUI(Tk):

	def __init__(self):
		Tk.__init__(self)
		self.title('Sistema de Trocas - ABCC')
		self.resizable(0,0)

		self.loggedIn = False;		

		butFrame = Frame(self)
		butFrame.grid(row=0,column=0)
		self.buttonQuit			= Button(butFrame, text='Sair',		 		command=self.quit			).pack(fill=BOTH, expand=1)
		self.buttonLogin		= Button(butFrame, text='Login / Cadastro',	command=self.login			).pack(fill=BOTH, expand=1)
		self.buttonEditArchive	= Button(butFrame, text='Editar arquivo', 	command=self.editArchive	).pack(fill=BOTH, expand=1)
		self.buttonSearchPieces	= Button(butFrame, text='Pesquisar peças',	command=self.searchPieces	).pack(fill=BOTH, expand=1)
		self.buttonManager 		= Button(butFrame, text='Área de gerência',	command=self.managerArea	).pack(fill=BOTH, expand=1)
		
	def login(self): # estender para aceitar criacao de conta
		cnpj = simpledialog.askstring('Login', 'Insira o seu CNPJ')
		password = simpledialog.askstring('Login', 'Insira a sua senha')
		General.login(cnpj, password)
		self.loggedIn = True;

	def editArchive(self):
		if self.loggedIn:
			print('aaa')
			# fazer coisas aqui
		else:
			messagebox.showerror('Indisponível','Esta ação está disponível apenas para usuários cadastrados')

	def searchPieces(self):
		if self.loggedIn:
			print('aaa')
			# fazer coisas aqui
		else:
			messagebox.showerror('Indisponível','Esta ação está disponível apenas para usuários cadastrados')

	def managerArea(self):
		pass

if __name__ == '__main__':
	gui = GUI()
	gui.mainloop()

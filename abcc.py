from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
#import PIL.Image, PIL.ImageTk
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

		for F in (StartPage, LoginPage, ArchivePage):#, SearchPage, ManagerPage):
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
		butFrame.grid(row=0,column=0)
#		butFrame.pack(fill=BOTH, expand=True)
		self.buttonQuit			= Button(butFrame, text='Sair',		 		command=self.quit)
		self.buttonLogin		= Button(butFrame, text='Login / Cadastro',	command=lambda: controller.show_frame(LoginPage))
		self.buttonEditArchive	= Button(butFrame, text='Arquivo', 			command=lambda: controller.show_frame(ArchivePage))
		self.buttonSearchPieces	= Button(butFrame, text='Pesquisar peças',	command=lambda: controller.show_frame(SearchPage))
		self.buttonManager 		= Button(butFrame, text='Área de gerência',	command=lambda: controller.show_frame(ManagerPage))
		
		self.buttonQuit.pack(fill=BOTH, expand=True)
		self.buttonLogin.pack(fill=BOTH, expand=True)
		self.buttonEditArchive.pack(fill=BOTH, expand=True)
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

	def login(self):
		cnpj = self.cnpjEntry.get()
		password = self.passwordEntry.get()
		g.login(cnpj, password)

class ArchivePage(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text='this is archive page').pack()

if __name__ == '__main__':
	g = base.General('institutions.xml','pieces.xml')
	abcc = ABCC()
	abcc.mainloop()

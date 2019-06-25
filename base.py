from institution import Institution
from piece import Piece
from loan_requests import LoanRequest
from storage_handling import StorageHandler

  
class Communicator:
	def __init__( self ):
		self.storage_handler = StorageHandler()

	def registerInstitution( self, institution_name, cnpj, address, phone_number, email, access_password ):
		new_institution = Institution( cnpj, access_password, address, phone_number, email, institution_name )
		new_institution.registerToStorage( access_password )

	def updateInstitutionInformation( self, cnpj, old_password, institution_name=None, address=None, phone_number=None, email=None, new_password=None ):
		# cnpj não é editável então utilizamos ele para encontrar a instituição que queremos utilizar
		new_institution = Intitution( cnpj, old_password )
		if institution_name is not None: new_institution.name = institution_name
		if address is not None: new_institution.address = address
		if phone_number is not None: new_institution.phone_number = phone_number
		if email is not None: new_institution.email = email
		if new_password is not None: new_institution.password = new_password
		new_institution.registerToStorage( old_password )

	def removeInstitution( self, institution_cnpj, password ):
		institution = Institution( institution_cnpj, password )
		institution.deleteFromStorage()

	def registerPiece( self, name, artist, state, year, owning_institution_cnpj ):
		new_piece = Piece( name, artist, year, state, owning_institution_cnpj )
		new_piece.registerToStorage()

	def updatePieceInformation(self):
		pass

	def removePiece( self, name, artist, year ):
		piece = Piece( name, artist, year )
		piece.deleteFromStorage()

	def createLoanRequest( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece, from_date, to_date ):
		new_loan_request = LoanRequest( loaning_institution, lending_institution, piece, from_date, to_date )

	def removeLoanRequest(self):
		pass

	def acceptLoanRequest(self):
		pass

	def refuseLoanRequest(self):
		pass

	def login( self, institution_cnpj, password ):
		new_institution = Institution( institution_cnpj, password )

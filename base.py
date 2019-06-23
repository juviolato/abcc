from xml.dom import minidom
from xml.etree import ElementTree
from datetime import date

class Piece:
    def __init__( self, name, artist, state, year ):
        self.name = name
        self.artist = artist
        self.state = state
        self.year = year

    def saveToXml( path ):
        # salva a obra

class Institution:
    def __init__( self, name, cnpj, address, phone_number, email, access_password ):
        self.name = name
        self.cnpj = cnpj
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.access_password = access_password
        self.pieces_owned = list( Piece )

    def saveToXml( path ):
        # salva a instituição

class LoanRequest:
    def __init__( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece )
        self.loaning_institution = loaning_institution
        self.lending_institution = lending_institution
        self.piece = piece

class NSeiUmNome:
    def __init__( institution_storage, pieces_storage ):
        self.institution_storage_path = institution_storage
        self.pieces_storage_path = pieces_storage
        initializeStorages()

    def initializeStorages():
        # inicializar arquivos xml

    def registerInstitution( institution_name, cnpj, address, phone_number, email, access_password ):
        new_institution = Institution( institution_name, cnpj, address, phone_number, email )
        new_institution.saveToXml( self.institution_storage_path )

    def removeInstitution( institution_name ):
        # achar a institutição no arquivo e excluir

    def registerPiece( name, artist, state, year ):
        new_piece = Piece( name, artist, state, year )
        new_piece.saveToXml( self.pieces_storage_path )

    def removePiece( name, artist, year ):
        # achar a obra no arquivo e excluir

    def requestLoan( loaning_institution: Institution, lending_institution: Institution, piece: Piece ):


    def login( institution_cnpj, password ):

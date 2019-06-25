from xml.dom import minidom
from xml.etree import ElementTree
from datetime import date

class Utils:
    def validateFilename( self, filename ) -> str:
        if filename.lower().endswith( '.xml' ):
            return filename
        else:
            return filename + ".xml"


class Piece:
    def __init__( self, name, artist, year, state=None, owning_institution_cnpj=None, path=None ):
        if state is None or owning_institution_cnpj is None:
            if path is None:
                raise Exception
            else:
                self.readFromXml( name, artist, year, path )
        else:
            self.name = name
            self.artist = artist
            self.state = state
            self.year = year
            self.owned_by = owning_institution_cnpj
            # estender para checar se existe uma instituição com esse cnpj e se a obra já existe

    def saveToXml( self, path ):
        path = Utils().validateFilename( path )
        pieces = ElementTree.parse( path )
        root = pieces.getroot()
        attributes = { 'name': self.name, 'artist': self.artist, 'state': self.state,
                       'year': self.year, 'owned-by': self.owned_by }
        new_piece = ElementTree.SubElement( root, 'piece', attributes )
        pieces.write( path )
        # estender para checar se a obra já existe

    def readFromXml( self, name, artist, year, path ) -> "Piece":
        path = Utils().validateFilename( path )
        pieces = ElementTree.parse( path )
        root = pieces.getroot()
        for piece in root:
            piece_name = piece.attrib['name']
            piece_artist = piece.attrib['artist']
            piece_year = piece.attrib['year']
            if ( piece_name == name and piece_artist == artist and piece_year == year ):
                self.name = piece_name
                self.artist = piece_artist
                self.year = piece_year
                self.state = piece.attrib['state']
                self.owned_by = piece.attrib['owned-by']
                # estender para checar se existe uma instituição com esse cnpj e se a obra já existe
                return self
        print( "This piece is not currently registered" )
        raise Exception

    def deleteFromXml( self, path ):
        path = Utils().validateFilename( path )
        pieces = ElementTree.parse( path )
        root = pieces.getroot()
        for piece in root:
            piece_name = piece.attrib['name']
            piece_artist = piece.attrib['artist']
            piece_year = piece.attrib['year']
            if ( piece_name == self.name and piece_artist == self.artist and piece_year == self.year ):
                root.remove( piece )
                pieces.write( path )
                return
            

class Institution:
    def __init__( self, cnpj, access_password, address=None, phone_number=None, email=None, name=None, path=None ):
        if address is None or phone_number is None or email is None or name is None:
            if path is None:
                raise Exception
            else:
                self.readFromXml( cnpj, access_password, path )
        else:
            self.name = name
            self.cnpj = cnpj
            self.address = address
            self.phone_number = phone_number
            self.email = email
            self.access_password = access_password
            # estender para checar se a instituição já existe

    def saveToXml( self, path ):
        path = Utils().validateFilename( path )
        institutions = ElementTree.parse( path )
        root = institutions.getroot()
        attributes = { 'name': self.name, 'cnpj': self.cnpj, 'address': self.address,
                       'phone-number': self.phone_number, 'email': self.email, 'password': self.access_password }
        new_institution = ElementTree.SubElement( root, 'institution', attributes )
        institutions.write( path )
        # estender para checar se a instituição já existe

    def readFromXml( self, cnpj, password, path ) -> "Institution":
        path = Utils().validateFilename( path )
        institutions = ElementTree.parse( path )
        root = institutions.getroot()
        for institution in root.findall( "./institution" ):
            if institution.attrib['password'] == password and institution.attrib['cnpj'] == cnpj:
                self.name = institution.attrib['name']
                self.cnpj = cnpj
                self.address = institution.attrib['address']
                self.phone_number = institution.attrib['phone-number']
                self.email = institution.attrib['email']
                self.access_password = password
                return self
        raise Exception

    def deleteFromXml( self, path ):
        path = Utils().validateFilename( path )
        institutions = ElementTree.parse( path )
        root = institutions.getroot()
        institution = root.find(".//institution[@cnpj='"+self.cnpj+"']")
        root.remove( institution )
        institutions.write( path )
        # extender para remover todas as obras que pertencem a essa instituição


class LoanRequest:
    def __init__( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece, from_date, to_date ):
        self.loaning_institution = loaning_institution
        self.lending_institution = lending_institution
        self.piece = piece
        self.starting_date = from_date
        self.ending_date = to_date
        self.request_time = date.today()


class Communicator:
    def __init__( self, institution_storage, pieces_storage ):
        self.institution_storage_path = Utils().validateFilename( institution_storage )
        self.pieces_storage_path = Utils().validateFilename( pieces_storage )
        self.initializeStorages()

    def initializeStorages( self ):
        institution = ElementTree.Element( 'data' )
        storage = open( self.institution_storage_path, "wb" )
        storage.write( ElementTree.tostring( institution ) )
        piece = ElementTree.Element( 'data' )
        storage = open( self.pieces_storage_path, "wb" )
        storage.write( ElementTree.tostring( piece ) )

    def registerInstitution( self, institution_name, cnpj, address, phone_number, email, access_password ):
        new_institution = Institution( cnpj, access_password, address, phone_number, email, institution_name )
        new_institution.saveToXml( self.institution_storage_path )

    def removeInstitution( self, institution_cnpj, password ):
        institution = Institution( institution_cnpj, password, path=self.institution_storage_path )
        institution.deleteFromXml( self.institution_storage_path )

    def registerPiece( self, name, artist, state, year, owning_institution_cnpj ):
        new_piece = Piece( name, artist, year, state, owning_institution_cnpj )
        new_piece.saveToXml( self.pieces_storage_path )

    def removePiece( self, name, artist, year ):
        piece = Piece( name, artist, year, path=self.pieces_storage_path )
        piece.deleteFromXml( self.pieces_storage_path )

    def requestLoan( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece, from_date, to_date ):
        new_loan_request = LoanRequest( loaning_institution, lending_institution, piece, from_date, to_date )

    def login( self, institution_cnpj, password ):
        new_institution = Institution( institution_cnpj, password, path=self.institution_storage_path )

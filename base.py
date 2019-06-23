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
    def __init__( self, name, artist, state, year, owning_institution_cnpj ):
        self.name = name
        self.artist = artist
        self.state = state
        self.year = year
        self.owned_by = owning_institution_cnpj

    def saveToXml( self, path ):
        path = Utils.validateFilename( path )
        pieces = ElementTree.parse( path )
        root = pieces.getroot()
        new_piece = ElementTree.SubElement( root, 'piece' )
        ElementTree.SubElement( new_piece, 'name' ).text( self.name )
        ElementTree.SubElement( new_piece, 'artist' ).text( self.artist )
        ElementTree.SubElement( new_piece, 'state' ).text( self.state )
        ElementTree.SubElement( new_piece, 'year' ).text( self.year )
        ElementTree.SubElement( new_piece, 'owned-by' ).text( self.owned_by )
        pieces.write()

    def readFromXml( self, path, name, artist, year ) -> Piece:
        path = Utils.validateFilename( path )
        pieces = ElementTree.parse( path )
        root = pieces.getroot()
        for piece in root:
            piece_name = piece.findtext( 'name' )
            piece_artist = piece.findtext( 'artist' )
            piece_year = piece.findtext( 'year' )
            if ( piece_name == name and piece_artist == artist and piece_year == year ):
                self.name = piece_name
                self.artist = piece_artist
                self.year = piece_year
                self.state = piece.findtext( 'state' )
                self.owned_by = piece.findtext( 'owned-by' )
                return self
        print( "This piece is not currently registered" )
        raise Exception

    def deleteFromXml( self, path ):
        path = Utils.validateFilename( path )
        pieces = ElementTree.parse( path )
        root = pieces.getroot()
        for piece in root:
            piece_name = piece.findtext( 'name' )
            piece_artist = piece.findtext( 'artist' )
            piece_year = piece.findtext( 'year' )
            if ( piece_name == name and piece_artist == artist and piece_year == year ):
                root.remove( piece )
                return
            

class Institution:
    def __init__( self, name, cnpj, address, phone_number, email, access_password ):
        self.name = name
        self.cnpj = cnpj
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.access_password = access_password

    def saveToXml( self, path ):
        path = Utils.validateFilename( path )
        institutions = ElementTree.parse( path )
        root = institutions.getroot()
        new_institution = ElementTree.SubElement( root, 'institution' ).set( 'cnpj', self.cnpj )
        ElementTree.SubElement( new_institution, 'name' ).text( self.name )
        ElementTree.SubElement( new_institution, 'address' ).text( self.address )
        ElementTree.SubElement( new_institution, 'phone-number' ).text( self.phone_number )
        ElementTree.SubElement( new_institution, 'email' ).text( self.email )
        ElementTree.SubElement( new_institution, 'password' ).text( self.access_password )
        institutions.write()

    def readFromXml( self, path, cnpj, password ) -> Institution:
        path = Utils.validateFilename( path )
        institutions = ElementTree.parse( path )
        root = institutions.getroot()
        institution = root.find("//institution[@cnpj="+cnpj+"]")
        if institution.findtext( 'password' ) == password:
            self.name = institution.findtext( 'name' )
            self.cnpj = cnpj
            self.address = institution.findtext( 'address' )
            self.phone_number = institution.findtext( 'phone-number' )
            self.email = institution.findtext( 'email' )
            self.access_password = password
            return self
        else:
            raise Exception

    def deleteFromXml( self, path ):
        path = Utils.validateFilename( path )
        institutions = ElementTree.parse( path )
        root = institutions.getroot()
        institution = root.find("//institution[@cnpj="+self.cnpj+"]")
        root.remove( institution )
        institutions.write()


class LoanRequest:
    def __init__( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece, from_date, to_date )
        self.loaning_institution = loaning_institution
        self.lending_institution = lending_institution
        self.piece = piece
        self.starting_date = from_date
        self.ending_date = to_date
        self.request_time = date.today()


class NSeiUmNome:
    def __init__( self, institution_storage, pieces_storage ):
        self.institution_storage_path = Utils.validateFilename( institution_storage )
        self.pieces_storage_path = Utils.validateFilename( pieces_storage )
        self.initializeStorages()

    def initializeStorages( self ):
        institution = ElementTree.Element( 'data' )
        storage = open( self.institution_storage_path, "w" )
        storage.write( ElementTree.tostring( institution ) )
        piece = ElementTree.Element( 'data' )
        storage = open( self.pieces_storage_path, "w" )
        storage.write( ElementTree.tostring( piece ) )

    def registerInstitution( self, institution_name, cnpj, address, phone_number, email, access_password ):
        new_institution = Institution( institution_name, cnpj, address, phone_number, email )
        new_institution.saveToXml( self.institution_storage_path )

    def removeInstitution( self, institution_cnpj, password ):
        institution = Institution.readFromXml( self.institution_storage_path, institution_cnpj, password )
        institution.deleteFromXml( self.institution_storage_path )

    def registerPiece( self, name, artist, state, year, owning_institution_cnpj ):
        new_piece = Piece( name, artist, state, year, owned_by )
        new_piece.saveToXml( self.pieces_storage_path )

    def removePiece( self, name, artist, year ):
        piece = Piece.readFromXml( self.pieces_storage_path, name, artist, year )
        piece.deleteFromXml( self.pieces_storage_path )

    def requestLoan( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece, from_date, to_date ):
        new_loan_request = LoanRequest( loaning_institution, lending_institution, piece, from_date, to_date )

    def login( self, institution_cnpj, password ):
        new_institution = Institution.readFromXml( self.institution_storage_path, institution_cnpj, password )
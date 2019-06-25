from xml.dom import minidom
from xml.etree import ElementTree
from datetime import date

LOANS_PATH = 'requests.xml'

class LoanRequest:
    def __init__( self, loaning_institution: Institution, lending_institution: Institution, piece: Piece, from_date, to_date ):
        self.loaning_institution = loaning_institution
        self.lending_institution = lending_institution
        self.piece = piece
        self.starting_date = from_date
        self.ending_date = to_date
        self.request_time = date.today()

    def registerToStorage( self ):
        requests = ElementTree.parse( LOANS_PATH )
        root = requests.getroot()
        # adaptar para checar se a requisição já existe
        attributes =  { 'loaning-institution': self.loaning_institution, 'lending-institution': self.lending_institution,
                        'piece-name': self.piece.name, 'piece-artist': self.piece.artist, 'starting-date': self.starting_date,
                        'ending-date': self.ending_date, 'request-time': self.request_time }
        new_request = ElementTree.SubElement( root, 'loan-request', attributes )
        requests.write( LOANS_PATH )
from xml.dom import minidom
from xml.etree import ElementTree

PIECES_PATH = 'pieces.xml'

class Piece:
	def __init__( self, name, artist, year, state=None, owning_institution_cnpj=None ):

		if state is None or owning_institution_cnpj is None:
			self.retrieveFromStorage( name, artist, year )
		else:
			self.name = name
			self.artist = artist
			self.state = state
			self.year = year
			self.owned_by = owning_institution_cnpj

	def registerToStorage( self ):
		pieces = ElementTree.parse( PIECES_PATH )
		root = pieces.getroot()
        # adaptar para checar se existe uma instituição com esse cnpj e se a obra já não existe
		attributes = { 'name': self.name, 'artist': self.artist, 'state': self.state,
						'year': self.year, 'owned-by': self.owned_by }
		new_piece = ElementTree.SubElement( root, 'piece', attributes )
		pieces.write( PIECES_PATH )

	def retrieveFromStorage( self, name, artist, year ) -> "Piece":
		pieces = ElementTree.parse( PIECES_PATH )
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
				return self
		print( "This piece is not currently registered" )
		raise Exception

	def deleteFromStorage( self ):
		pieces = ElementTree.parse( PIECES_PATH )
		root = pieces.getroot()
		for piece in root:
			piece_name = piece.attrib['name']
			piece_artist = piece.attrib['artist']
			piece_year = piece.attrib['year']
			if ( piece_name == self.name and piece_artist == self.artist and piece_year == self.year ):
				root.remove( piece )
				pieces.write( PIECES_PATH )
				return
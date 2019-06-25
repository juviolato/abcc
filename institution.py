from xml.dom import minidom
from xml.etree import ElementTree

INSTIT_PATH = 'institutions.xml'

class Institution:
	def __init__( self, cnpj, access_password, address=None, phone_number=None, email=None, name=None ):
		if address is None or phone_number is None or email is None or name is None:
		    self.retrieveFromStorage( cnpj, access_password )
		else:
		    self.name = name
		    self.cnpj = cnpj
		    self.address = address
		    self.phone_number = phone_number
		    self.email = email

	def registerToStorage( self, access_password ):
		institutions = ElementTree.parse( INSTIT_PATH )
		root = institutions.getroot()
        # adaptar para checar se a instituição já existe
		attributes = { 'name': self.name, 'cnpj': self.cnpj, 'address': self.address,
		               'phone-number': self.phone_number, 'email': self.email, 'password': access_password }
		new_institution = ElementTree.SubElement( root, 'institution', attributes )
		institutions.write( INSTIT_PATH )

	def retrieveFromStorage( self, cnpj, password ) -> "Institution":
		institutions = ElementTree.parse( INSTIT_PATH )
		root = institutions.getroot()
        # adaptar para checar se a instituição existe
        self.validatePassword( cnpj, password )
        institution = root.find( ".//institution[@cnpj='" + cnpj + "']" )
	    self.name = institution.attrib['name']
	    self.cnpj = cnpj
		self.address = institution.attrib['address']
		self.phone_number = institution.attrib['phone-number']
		self.email = institution.attrib['email']
	    return self

	def deleteFromStorage( self ):
		institutions = ElementTree.parse( INSTIT_PATH )
		root = institutions.getroot()
		institution = root.find( ".//institution[@cnpj='"+self.cnpj+"']" )
		root.remove( institution )
		institutions.write( INSTIT_PATH )
		# extender para remover todas as obras que pertencem a essa instituição

    def validatePassword( self, cnpj, password ):
        institutions = ElementTree.parse( INSTIT_PATH )
        root = institutions.getroot()
        insitution = root.find( ".//institution[@cnpj='" + cnpj + "']" )
        if ( insitution.attrib['password'] != password ):
            raise Exception
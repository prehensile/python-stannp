import requests
import base64

class StannpClient():

    def __init__( self, api_key ):
        self.api_key = api_key

    def perform_request( self, endpoint_url, payload=None ):
        r = requests.post( endpoint_url, data=payload, auth=(self.api_key,"") )
        return r.json()

    def get_balance( self ):
        return self.perform_request( "https://stannp.com/api/v2/balance/get" )

    def get_postcards( self ):
        return self.perform_request( "https://stannp.com/api/v2/postcards/get" )

    def send_postcard( self, addressee, address_1, postcode, iso_country, image,
        address_2=None, address_3=None, city=None, county=None ):
        payload = { "name" : addressee, "address1" : address_1, \
            "postcode" : postcode, "country" : iso_country }
        if address_2 is not None:
            payload[ "address2" ] = address2
        if address_3 is not None:
            payload[ "address3" ] = address3
        if city is not None:
            payload[ "city" ] = city
        if county is not None:
            payload[ "county" ] = county
        if isinstance( image, basestring ):
            # image is already a string, just add it to the payload
            payload[ "image" ] = image
        else:
            # assume image is a file-like object
            try:
                payload[ "image" ] = base64.b64encode( image.read() )
            except Exception, e:
                raise e

        return self.perform_request( "https://stannp.com/api/v2/postcards/create", payload )
  
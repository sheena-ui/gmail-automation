import jwt
import cryptography # for rs256
import jsonschema
# import pytest


class JWTValidator:
    """
    The JWT validator is designed to validate the JWT string issued from UI
    services is correct or not.

    - Check if the string is JWT format (if not, raise DecodeError)
    - Check if the string contains certain key-value pairs (uses options)
    - Check if the string signature is correct (if verify=true and secret is provided)
    - Check if the header, payload schema is correct (uses jsonschema)
    """
    def __init__(self,
                 secret,
                 algorithm='RS256',
                 verify=False,
                 options=None,
                 jwt_header_schema=None,
                 jwt_payload_schema=None):

        self.secret = secret
        self.algorithm = algorithm
        self.verify = verify
        if not options:
            self.options = {}
        self.options['verify_signature'] = self.verify
        self.jwt_header_schema = jwt_header_schema
        self.jwt_payload_schema = jwt_payload_schema

    def is_valid_jwt(self, jwt_token):
        try:
            # decode_kwargs = {
            #     'algorithms': self.algorithm,
            #     'options': self.options,
            #     # 'verify': self.verify
            #     # verify is removed since 2.0.0 to verify_signature inside options
            #     # need to check which version our SSO is using
            # }
            #
            # if self.secret and self.verify:
            #     decode_kwargs['key'] = self.secret
            # elif not self.secret and self.verify:
            #     raise ValueError('Secret key must be provided for JWT verification')
            #
            # decoded_payload = jwt.api_jwt.decode_complete(jwt_token, **decode_kwargs)
            decode_kwargs = {
                'jwt': jwt_str,
                'key': self.secret,
                'algorithms': self.algorithm,
                'options': {'verify_signature': self.verify}
            }
            decoded_payload = jwt.api_jwt.decode_complete(**decode_kwargs)
        except jwt.exceptions.DecodeError as decode_error:
            raise ValueError(f'Invalid JWT token: {decode_error}')
        else:
            try:
                if self.jwt_header_schema:
                    jsonschema.validate(decoded_payload['header'],
                                        self.jwt_header_schema)
                if self.jwt_payload_schema:
                    jsonschema.validate(decoded_payload['payload'],
                                        self.jwt_payload_schema)
            except jsonschema.exceptions.ValidationError as e:
                # TODO make the exception error shorter
                raise ValueError(f'Invalid header schema: {e}')

            return decoded_payload


if __name__ == '__main__':
    secret = '##5v4*!q-_&5$vny9=l4pgrdlu72+(ucafoenez-8_i+f!wlyv'
    # secret = None
    header_schema = {

    }
    payload_schema = {
      "type": "object",
      "properties": {
        "UUID": {"type": "string"},
        "expiry": {"type": "integer"},
        "is_verified": {"type": "boolean"},
        "session": {"type": "string"},
        "ttl_seconds": {"type": "integer"},
        "sub": {"type": "string"},
        "iss": {"type": "string"},
        "exp": {"type": "integer"},
      },
      "required": ["UUID", "expiry", "is_verified", "session", "ttl_seconds", "sub", "iss", "exp"]
    }
    jwt_validator = JWTValidator(secret,
                                 algorithm='RS256',
                                 verify=False,
                                 options=None,
                                 jwt_header_schema=None,
                                 jwt_payload_schema=payload_schema)

    jwt_str = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IlRpMjhIYXJQeDJUSTFEZ3Q4QTdOS0xoTzRKR3I3RnQ0ZFNWbWt5TWhuTVUiLCJ0eXAiOiJKV1QifQ.eyJVVUlEIjoiNGRiMmZkZDYtMTIxYS00YjFhLWI5ZmItZmIyMTc4YzhkMmY1IiwiZXhwaXJ5IjoxNzE2NjIwODczLCJpc192ZXJpZmllZCI6dHJ1ZSwic2Vzc2lvbiI6IjM4MTZkNTk2LWY5NjMtNDU0My04NWJlLWEyZjVhZWZhZTM4MiIsInR0bF9zZWNvbmRzIjo4NjQwMCwic3ViIjoiNGRiMmZkZDYtMTIxYS00YjFhLWI5ZmItZmIyMTc4YzhkMmY1IiwiaXNzIjoiaHR0cHM6Ly9zc28uc3RnLnVpLmNvbSIsImV4cCI6MTcxNjYyMDg3M30.pwzGllZ3icNASYH8wNHWz5r1x0YO4KDDYsGMGFyhDar2iHapu-5rDp6wbWf_T17kXugXmfUMAhtivSaBEB_K4Y6NS6E0REPNnKYTOWHzTKJ9UpSJI6Ecld7zcZiZdthz66cu53SIpNoFNcXS5tvmqVbr3NySI2LeEN0L3HAIMgmOOohtzN5-qETOg3M6Iqfa_IEKz-E83wjoiiwQscU7TSfHtJHQryVIzCqqLWRa7kRRNaS2PoitGINWwsm2yL-QyyO_yFnMouF7ZmWCX1yw8zw6oCaTEoGH1NdndeBDijPhXNuNwmEF5PIgoGlIEDU5EJLHxOK53yyhcvJO1k6rrMykmB39eIHeH4IGd4fW9YvoHZ0fpVmVEw1R5bNRUamFPQamvYN4s_TKjEGbxkfuSB-4yPvb8yJIv7QhQ3sz5CxsaqZ1Iy2Z0AAY3wa42Qdtz0iaXdgq8FRluzWnSV9eQXOGN0YiLJ2qkHB-yh1_Z8aOesFWeVlI0w8kEe3_CXvLSbGMaXBGMx2zXRnj8Z5eq61wllNgbgiAN2WYavY7uWuJvptNOTi0b61Py9mASzSLV0jqL68TBXX_vzEOtF60DGDCn_ANorT_3dCJ2HPaYYTrncvVNKxcLxw249h6DHLNhU3LfTjJtfkBrwMrCKSePKtMetNW4IfnlGIhP_1DsuQ'
    resp = jwt_validator.is_valid_jwt(jwt_str)
    print(resp)


import jwt
import cryptography # for rs256
import jsonschema


class JWTValidator:

    def __init__(self,
                 secret = None,
                 algorithm='RS256',
                 verify_signature=False):
        self.secret = secret
        self.algorithm = algorithm
        self.verify_signature = verify_signature

    def is_valid_cookie_auth(self, jwt_str):
        header_schema = {}  # define header schema
        payload_schema = {}  # define payload schema
        try:
            decoded_payload = self._jwt_decode_handler(jwt_str)
            self._json_schema_check_handler(decoded_payload['header'], header_schema)
            self._json_schema_check_handler(decoded_payload['payload'], payload_schema)
            return True
        except ValueError:
            return False

    def is_valid_oauth_openid(self):
        pass

    def _jwt_decode_handler_v2(self, jwt_str):
        decode_kwargs = {
            'jwt': jwt_str,
            'key': self.secret,
            'algorithms': self.algorithm,
            'options': {'verify_signature': self.verify_signature}
        }
        decoded_payload = jwt.api_jwt.decode_complete(jwt_str, **decode_kwargs)
        return decoded_payload

    def _jwt_decode_handler(self, jwt_str):
        try:
            decode_kwargs = {
                'algorithms': self.algorithm,
                'options': {'verify_signature': self.verify_signature}
            }

            if self.secret and self.verify_signature:
                decode_kwargs['key'] = self.secret
            elif not self.secret and self.verify_signature:
                raise ValueError('Secret key must be provided for JWT verification')
            decoded_payload = jwt.api_jwt.decode_complete(jwt_str, **decode_kwargs)
            return decoded_payload
        except jwt.exceptions.DecodeError as decode_error:
            raise ValueError(f'Invalid JWT token: {decode_error}')

    def _json_schema_check_handler(self, target, target_schema):
        try:
            jsonschema.validate(target,target_schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValueError(f'Invalid JSON schema: {e}')
        return True



# if __name__ == '__main__':
#     jwt_validator = JWTValidator()
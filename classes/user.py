import json
import datetime
from classes.aws import AWS


class User:

    def __init__(self, body):
        self.body = body
        # Load config settings into self.data
        with open('config.json') as json_file:
            self.data = json.load(json_file)
        # Create dynamoDB resource
        aws_object = AWS()
        self.dynamodb_client = aws_object.create_dynamodb_client()

    #########################################################################################################
    # Public method declarations
    #########################################################################################################

    def login(self):
        # Validate email and password. If validated, return JWT
        email = self.body['email']
        password = self.body['password'].encode('utf-8')
        # Check if user exists first
        user_details = self.__return_user(email)
        if user_details == 0:
            return self.custom_400('ERROR: User not found')
        else:
            hashed_password = user_details['password']['B']
            # Check if password matches
            if bcrypt.checkpw(password + self.data['hash_secret'].encode('utf-8'), hashed_password):
                expiry_time = datetime.utcnow() + timedelta(seconds=60 * 30)
                encoded_jwt = jwt.encode(
                    {'email': email, 'exp': expiry_time}, self.data['jwt_encode'], algorithm='HS256').decode('utf-8')
                return_body = {}
                return_body["firstname"] = user_details['first_name']['S']
                return_body["surname"] = user_details['surname']['S']
                return_body["email"] = email
                cookie_string = self.set_cookie(encoded_jwt)
                return {'cookie': cookie_string, 'statusCode': 200, 'response': str(return_body)}
            else:
                return self.custom_400('PASSWORD DID NOT MATCH')

    #########################################################################################################
    # Private method declarations
    #########################################################################################################

    def __return_user(self, email_address):
        response = self.dynamodb_client.get_item(
            TableName='User', Key={'email_address': {'S': email_address}})
        # Check if an user exists
        try:
            user = response['Item']
            return user
        except:
            return 0

    def __set_cookie(jwt):
        # Delete the cookie after 1 day
        expires = (datetime.utcnow() +
                   timedelta(seconds=60 * 60 * 24)).strftime("%a, %d %b %Y %H:%MM:%S GMT")
        # Will remove HttpOnly and see if that works
        # Will take out secure for now, doesn't work in dev
        cookie_string = 'jwt=' + \
            str(jwt) + ';  expires=' + \
            str(expires) + \
            "; Path=/; Max-Age=3600; Domain=www.meetadoo.com; HttpOnly; Secure"
        return cookie_string

    def __custom_400(self, message):
        return {'statusCode': 400, 'response': message}

import json

from rest_framework.test                  import APITestCase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User

class UserSignUpTest(APITestCase):
    
    def test_success_user_signup(self):
        data = {
            'email'    : 'DGK-test-01@gmail.com',
            'nickname' : 'DGK-01',
            'password' : 'DGK12345678'
        }
        
        response = self.client.post('/users/signup', data=json.dumps(data), content_type='application/json')
        
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data,
            {
                'email'    : 'DGK-test-01@gmail.com',
                'nickname' : 'DGK-01'
            }
        )
    

class UserSignInTest(APITestCase):
    def setUp(self):
        User.objects.create(
            id = 1,
            email = 'DGK-test@gmail.com',
            nickname = 'DGK01',
            password = 'DGK12345678'
        )
        
    def tearDown(self):
        User.objects.all().delete()

    def test_success_user_signin(self):
        data = {
            'email' : 'DGK-test@gmail.com',
            'nickname' : 'DGK01',
            'password' : 'DGK12345678'
        }
        
        # print(User.objects.values())
        user  = User.objects.get(email='DGK-test@gmail.com')
        # print(user.id, user.nickname, user.email, user.password)
        token = TokenObtainPairSerializer.get_token(user)
        
        refresh_token = str(token)
        access_token  = str(token.access_token)
        
        # signup_res = self.client.post('/users/signup', data=json.dumps(data), content_type='application/json')
        signin_res = self.client.post('/users/signin', data=json.dumps(data), content_type='application/json')
        
        
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(
            signin_res.json(),
            {
                'refresh' : refresh_token,
                'access'  : access_token
            }
        )
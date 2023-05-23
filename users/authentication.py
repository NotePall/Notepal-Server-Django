from rest_framework.authentication import TokenAuthentication as BaseAuthentication

#  we define our base 
class TokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'
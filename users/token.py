# from django.contrib.auth.tokens import PasswordResetTokenGenerator 
# import six 


# class TokenGenerator(PasswordResetTokenGenerator): 
#     def _make_hash_value(self, user, timestamp): 
#         return( 
#             six.text_type(user.pk) + six.text_type(timestamp) + 
#             six.text_type(user.is_active) 
#         ) 
    

# account_activation_token = TokenGenerator() 

from users.models import CustomUser

from django.shortcuts import get_object_or_404

import uuid


TOKEN = uuid.uuid4().hex

print(TOKEN)


f = get_object_or_404(CustomUser, id=1)

print(f)
# import sqlite3

# dbfile = 'C:/Users/Константин/Desktop/Dev/Django5_Blog/db.sqlite3'

# conn = sqlite3.connect(dbfile)

# cursor = conn.cursor()

# cursor.execute("SELECT email FROM users_customuser ORDER BY id DESC;")

# results = cursor.fetchall()

# a = len(results)

# print(results[0])


# if any('dddddaaa@gmail.com' in code for code in results[0]):
#     print(True)
# else:
#     print(False)


# conn.close()
from rest_framework.test import APITestCase
from django.urls import reverse
from . import models


class AutoTestCases(APITestCase):
    def create_initial_data(self):
        # User Data
        self.user_json={
            "username": "test",
            "email": "test@test.com",
            "first_name": "test",
            "last_name": "test",
            "phone":"+9151452125",
            "password": "test",
            "rank": "STF"
        }

        self.user_obj=models.BaseUser.objects.create(**self.user_json)

        self.edited_user_json={
        "id":self.user_obj.id,
        "username": "edited",
        "email": "edited@edited.com",
        "first_name": "edited",
        "last_name": "edited",
        "rank": "MAN"
        }

        # Change Password
        self.change_pass_json={
            "old_password":"test1234mrct",
            "new_password": "test1234mrct"
        }

        # Letter Data
        self.letter_json={
            "id": "V3omNvMn",
            "priority": "H",
            "created_at": "2022-12-26T14:35:25.613268Z",
            "updated_at": "null",
            "owner": "HEz8lFVC",
            "departman": "0bE1T8Gd"
        }

        self.letter_obj=models.Letter.objects.create(**self.letter_json)

        self.editedletter_json={
            "id": self.letter_obj.id,
            "priority": "H",
            "created_at": "2022-12-26T14:35:25.613268Z",
            "updated_at": "null",
            "owner": "HEz8lFVC",
            "departman": "0bE1T8Gd"
        }

        # Initial letter 
        self.initial_letter_json={
            "priority": "M",
            "owner": "HEz8lFVC",
            "departman": "0bE1T8Gd",
            "comment": [
                {
                "sender": "HEz8lFVC",
                "receiver": "HEz8lFVC",
                "title": "test",
                "description": "test",
                "status": "US",
                "created_at": "2022-12-26T13:50:07.828766Z",
                "updated_at": "null",
                "comment_file": [
                    #"file": "http://127.0.0.1:8000/media/content_file/643e4fe1-09f8-4648-b3e1-e41afd883871.png",
                    ]
                }
            ]
        }

        # Comment
        self.comment_json={
            "id": "kCIIXSZX",
            "comment_file": [
                #"file": "http://127.0.0.1:8000/media/content_file/643e4fe1-09f8-4648-b3e1-e41afd883871.png",
                ],
            "title": "test",
            "description": "test",
            "status": "US",
            "created_at": "2022-12-26T15:00:35.598855Z",
            "updated_at": "null",
            "letter": self.letter_obj.id,
            "sender": self.user_obj.id,
            "receiver": self.user_obj.id
        }

        self.comment_obj=models.Comment.objects.create(**self.comment_json,letter=self.letter_obj,
                                                sender=self.user_obj,receiver=self.user_obj)
        
        self.edited_comment_json={
            "id": self.comment_obj.id,
            "comment_file": [
                #"file": "http://127.0.0.1:8000/media/content_file/643e4fe1-09f8-4648-b3e1-e41afd883871.png",
                ],
            "title": "test_edited",
            "description": "test_edited",
            "status": "US",
            "created_at": "2022-12-26T15:00:35.598855Z",
            "updated_at": "null",
            "letter": self.letter_obj.id,
            "sender": self.user_obj.id,
            "receiver": self.user_obj.id
        }

        # Comment status just put request
        self.comment_status_json={
        "comment":self.comment_obj.id
        }

        # History
        self.history_json={
            "history_file": [
                #"file": "http://127.0.0.1:8000/media/content_file/643e4fe1-09f8-4648-b3e1-e41afd883871.png",
            ],
            "title": "test",
            "description": "test",
            "owner": "HEz8lFVC",
            "departman": "0bE1T8Gd"
        }


    def get_cridential_token(self):
        pass #TODO set authorization for testing 

        
    def test_user_detail(self):
        pass

    def setUp(self) -> None:
        return super().setUp()

    def test_create_user(self):
        url=reverse('user-detail',kwargs={'pk':'asdwadW'})

    def test_change_password(self):
        pass

    def test_get_departman(self):
        pass
    
    def test_get_letters(self):
        pass

    def test_create_letter(self):
        pass
    
    def test_retreive_letter(self):
        pass

    def test_update_letter(self):
        pass

    def test_delete_letter(self):
        pass

    def test_create_initial_letter(self):
        pass

    def test_list_user_comment(self):
        pass

    def test_create_user_comment(self):
        pass

    def test_get_letter_comment(self):
        pass

    def test_create_letter_comment(self):
        pass

    def test_retreive_comment(self):
        pass

    def test_get_history(self):
        pass

    def test_create_history(self):
        pass

    def test_retreive_hsitory(self):
        pass

    def test_delete_history(self):
        pass

    def test_update_history(self):
        pass

    def test_delete_history(self):
        pass

    

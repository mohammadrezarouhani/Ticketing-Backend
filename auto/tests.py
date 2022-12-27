from rest_framework.test import APITestCase
from django.urls import reverse
from . import models


class AutoTestCases(APITestCase):
    def create_initial_data(self):
        # cridential data
        self.cridential_data={
            'username':'admin',
            'password':'admin'
        }

        self.departman_json_obj={
            'title':'test',
            'description':'test'
        }
        self.departman_obj=models.Departman.objects.create(**self.departman_json_obj)

        # User Data
        self.user_json={
            "username": "admin",
            "email": "admin@admin.com",
            "first_name": "test",
            "last_name": "test",
            "departman":self.departman_obj,
            "phone":"+9151452125",
            "password": "admin",
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
            "owner": "HEz8lFVC",
            "departman": "0bE1T8Gd"
        }

        self.letter_json_obj={
            "id": "V3omNvMn",
            "priority": "H",
            "owner": self.user_obj,
            "departman": self.departman_obj
        }

        self.letter_obj=models.Letter.objects.create(**self.letter_json_obj)

        self.editedletter_json={
            "id": self.letter_obj.id,
            "priority": "H",
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
            "title": "test",
            "description": "test",
            "status": "US",
            "letter": self.letter_obj.id,
            "sender": self.user_obj.id,
            "receiver": self.user_obj.id
        }

        self.comment_json_obj={
            "title": "test",
            "description": "test",
            "status": "US",
            "letter": self.letter_obj,
            "sender": self.user_obj,
            "receiver": self.user_obj
        }

        self.comment_obj=models.Comment.objects.create(**self.comment_json_obj)

        self.edited_comment_json={
            "id": self.comment_obj.id,
            "title": "test_edited",
            "description": "test_edited",
            "status": "US",
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

    def set_routing_url(self):
        self.token_obtain=reverse('token-obtain')
        self.token_obtain=reverse('token-refresh')
        self.user_list=reverse('user-list')
        self.user_detail=reverse('user-detail',kwargs={'pk':self.user_obj.id})
        self.change_password=reverse('change-password',kwargs={'pk':self.user_obj.id})
        self.departman_list=reverse('departman-list')
        self.letter_list=reverse('letter-list')
        self.letter_detail=reverse('letter-detail',kwargs={'pk':self.letter_obj.id})
        self.initial_letter=reverse('initial-letter-list')
        self.comment_list=reverse('comment-list')
        self.comment_detail=reverse('comment-detail',kwargs={'pk':self.comment_obj.id})
        self.comment_status=reverse('comment-status',kwargs={'pk':self.user_obj.id})

    def authorise(self):
        response=self.client.post(self.token_obtain,data=self.cridential_data) 
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(response.data.get('access')))

    def setUp(self) -> None:
        self.create_initial_data()
        self.set_routing_url()
        return super().setUp()

    def test_create_user(self):
        pass

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

    def test_retreive_history(self):
        pass

    def test_delete_history(self):
        pass

    def test_update_history(self):
        pass

    def test_delete_history(self):
        pass

    

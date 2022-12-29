from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from . import models
import pdb

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
        self.user_json_obj={
            "username": "admin",
            "email": "admin@admin.com",
            "first_name": "admin",
            "last_name": "test",
            "departman":self.departman_obj,
            "phone":"+9151452125",
            "password": make_password("admin"),
            "rank": "STF"
        }

        self.user_json={
            "username": "test",
            "email": "test@test.com",
            "first_name": "test",
            "last_name": "test",
            "departman":self.departman_obj.id,
            "phone":"+9151452125",
            "password": "test",
            "rank": "STF"
        }

        self.user_obj=models.BaseUser.objects.create(**self.user_json_obj)

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
            "old_password":"admin",
            "new_password": "admin12345678910"
        }

        # Letter Data
        self.letter_json={
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

        self.edited_letter_json={
            "id": self.letter_obj.id,
            "priority": "H",
            "owner": self.user_obj.id,
            "departman": self.departman_obj.id
        }

        # Initial letter 
        self.initial_letter_json={
            "comment": [
                {
                "comment_file": [],
                "title": "test",
                "description": "test",
                "status": "US",
                "sender": self.user_obj.id,
                "receiver": self.user_obj.id
                }
            ],
            "priority": "M",
            "owner": self.user_obj.id,
            "departman": self.departman_obj.id
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
        self.token_obtain_url=reverse('token-obtain')
        self.token_refresh_url=reverse('token-refresh')
        self.user_list_url=reverse('user-list')
        self.user_detail_url=reverse('user-detail',kwargs={'pk':self.user_obj.id})
        self.change_password_url=reverse('change-password',kwargs={'pk':self.user_obj.id})
        self.departman_list_url=reverse('departman-list')
        self.letter_list_url=reverse('letter-list')+"?owner={}".format(self.user_obj.id)
        self.letter_detail_url=reverse('letter-detail',kwargs={'pk':self.letter_obj.id})
        self.initial_letter_url=reverse('initial-letter-list')
        self.comment_list_url=reverse('comment-list')
        self.comment_detail_url=reverse('comment-detail',kwargs={'pk':self.comment_obj.id})
        self.comment_status_url=reverse('comment-status',kwargs={'pk':self.user_obj.id})

    def authorise(self):
        response=self.client.post(self.token_obtain_url,data=self.cridential_data) 
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(response.data.get('access')))

    def setUp(self) -> None:
        self.create_initial_data()
        self.set_routing_url()
        self.authorise()
        return super().setUp()

    def test_create_user(self):
        response=self.client.post(self.user_list_url,data=self.user_json)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertTrue(models.BaseUser.objects.filter(id=response.data.get('id')).exists())

    def test_change_password(self):
        response=self.client.put(self.change_password_url,self.change_pass_json)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(models.BaseUser.objects.get(id=self.user_obj.id).check_password(self.change_pass_json['new_password']))

    def test_get_departman(self):
        response=self.client.get(self.departman_list_url)
        self.assertTrue(models.Departman.objects.filter(id=self.departman_obj.id).exists())
        self.assertTrue(response.data)

    def test_get_letters(self):
        response=self.client.get(self.letter_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(response.data)


    def test_create_letter(self):
        response=self.client.post(self.letter_list_url,self.letter_json)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_retreive_letter(self):
        response=self.client.get(self.letter_detail_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_update_letter(self):
        response=self.client.put(self.letter_detail_url,self.edited_letter_json)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_delete_letter(self):
        response=self.client.delete(self.letter_detail_url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

    def test_create_initial_letter(self): # TODO write next test in time
        # response=self.client.post(self.initial_letter_url,self.initial_letter_json)
        # self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        # self.assertTrue(response.data)

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

    

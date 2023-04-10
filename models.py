# -*- coding: utf-8 -*-

# from google.appengine.ext import client

import webapp2_extras.appengine.auth.models as auth_models

from google.cloud import ndb

client = ndb.Client()

class PostUser(auth_models.User):
    nickname = client.StringProperty()
    mates = client.KeyProperty(repeated=True)

class ImageBlob(client.Model):
    file_name = client.StringProperty()
    content_type = client.StringProperty()
    file_size = client.IntegerProperty()
    upload_date = client.DateTimeProperty(auto_now_add=True)
    image_url = client.StringProperty()
    proprietor = client.StringProperty()

    # @property
    def getting(self):
        article_objs = ExplainArticle.query(ExplainArticle.blob_key == self.key, ancestor=self.key).fetch()
        return article_objs[0]

    @classmethod
    def query_content(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key)

class ExplainArticle(client.Model):
    articles = client.StringProperty(repeated=True)
    update_date = client.DateTimeProperty(auto_now_add=True)
    blob_key = client.KeyProperty(kind=ImageBlob)

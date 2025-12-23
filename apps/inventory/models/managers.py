from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class ProductManager():

    def _create_product(self, **extra_fields):
        product = self.model(**extra_fields)
        product.save(using=self._db)
        return product

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_active", True)
        return self._create_product(email, password, **extra_fields)




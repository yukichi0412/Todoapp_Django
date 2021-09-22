from datetime import datetime
from django.db import models
from django.conf import settings
from django.db.models.fields import IntegerField
from django.utils import timezone

from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from datetime import datetime
import sqlalchemy
from sqlalchemy.sql.sqltypes import Date
from config.db import Base, create_engine, make_session

from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

"""
class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
"""

Base = declarative_base()

class DjangoLikeModelMixin(object):
    id = Column(Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

class Category(Base, DjangoLikeModelMixin):
    __tablename__ = 'category'

    id = Column(Integer, Sequence('category_ud_seq'), primary_key=True)
    title = Column(String(20))
    created_at = Column('created', DateTime, default=timezone.now, nullable=False)

    def __str__(self):
        return self.title

"""
class Task(models.Model):
    STATUS_CHOICES = [(1, '未完了'), (2, '作業中'), (3, '完了')]

    title = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    due_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
"""

class Task(Base, DjangoLikeModelMixin):
    STATUS_CHOICES = [(1, '未完了'), (2, '作業中'), (3, '完了')]

    title = Column(String(100))
    status = Column('status', Integer(), default=1)
    due_date = Column('due', DateTime, default=timezone.now, nullable=False)
    created_at = Column('created', DateTime, default=timezone.now)
    updated_at = Column('updated', DateTime, default=timezone.now)
    category_id = Column(Integer,ForeignKey('Category.id', ondelete='CASCADE'))

    def publish(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


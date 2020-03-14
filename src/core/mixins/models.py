import uuid as uuid
from functools import reduce

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.remotes import BaseRemoteObjectMixin


class BaseModel(models.Model):
    """
    Abstract Base Model
    """

    class Meta:
        abstract = True
        ordering = ("-created_timestamp",)
        default_permissions = ('view', 'add', 'change', 'delete')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_timestamp = models.DateTimeField(_("Created At"), auto_now_add=True, 
                                             editable=False)
    updated_timestamp = models.DateTimeField(_("Updated At"), auto_now=True, 
                                             editable=False)


class RemoteObjectModelMixin(models.Model):
    """
    Abstract RemoteObjectModelMixin
    """
    field_mapping = {
        'id': 'remote_id'
    }
    remote_manager = BaseRemoteObjectMixin()
    children = []

    class Meta:
        abstract = True

    remote_id = models.CharField(
        _("Remote Object Id"), max_length=1024, unique=True, null=True, blank=True)


    def update_model_from_remote(self, **kwargs):
        """
        model1.model2.model3.name = x
        geattr(model1, 'model2', object), 'name', x)
        :return: remote object
        """
        remote = self.remote_manager.get_remote_attrs(**kwargs)
        kwargs.update(remote)
        for field, value in kwargs.items():
            setattr(self, self.field_mapping.get(field, field), value)

        self.save()
        return self

    def update_children_model_from_remote(self, **kwargs):
        """
        :return:
        """
        for child in self.children:
            model = getattr(getattr(self, child, object), 'model', None)
            if not model:
                continue
            parent_field_name = str(getattr(
                getattr(self, child, object), 'field', None).name)
            child_objects = getattr(self, child, []).all().values('remote_id')
            child_remotes = self.remote_manager.get_children(child, **kwargs)
            child_objects_list = [k['remote_id'] for k in child_objects]

            for child_remote in child_remotes:
                atts = {
                    'id': child_remote,
                    parent_field_name: self
                }

                if child_remote not in child_objects_list:
                    instance = model()
                else:
                    instance = model.objects.get(remote_id=child_remote)
                instance.update_model_from_remote(**atts)

    
    def update_remote_from_model(self, **kwargs):
        field_mapping_reverse = { 
            k: v for k, v in self.field_mapping.items()
        }
        data = { 
            field_mapping_reverse.get(v, v): 
                getattr(self, field_mapping_reverse.get()) 
            for v in self.remote_manager.fields
        }
        kwargs['data'] = data
        remote = self.remote_manager.update(**kwargs)
        return remote

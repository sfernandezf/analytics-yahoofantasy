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


class BaseStats(models.Model):
    class Meta:
        abstract = True

    g = models.FloatField(_("Games"), blank=True, null=True)
    pa = models.FloatField(_("Plate Appareances"), blank=True, null=True)
    ab = models.FloatField(_("At Bat"), blank=True, null=True)
    h = models.FloatField(_("Hits"), blank=True, null=True)
    double = models.FloatField(_("Doubles"), blank=True, null=True)
    triple = models.FloatField(_("Triples"), blank=True, null=True)
    hr = models.FloatField(_("Home Run"), blank=True, null=True)
    r = models.FloatField(_("Runs"), blank=True, null=True)
    rbi = models.FloatField(_("Runs Bat in"), blank=True, null=True)
    bb = models.FloatField(_("Base Balls"), blank=True, null=True)
    so = models.FloatField(_("Strike Out"), blank=True, null=True)
    hbp = models.FloatField(_("Hit By Pitch"), blank=True, null=True)
    sb = models.FloatField(_("Stolen Base"), blank=True, null=True)
    cs = models.FloatField(_("Caught Stolen"), blank=True, null=True)
    avg = models.FloatField(_("Average"), blank=True, null=True)
    obp = models.FloatField(_("Obp"), blank=True, null=True)
    slg = models.FloatField(_("Slugging"), blank=True, null=True)
    ops = models.FloatField(_("OPS"), blank=True, null=True)
    woba = models.FloatField(_("wOBA"), blank=True, null=True)
    wrcplus = models.FloatField(_("wRC+"), blank=True, null=True)
    bsr = models.FloatField(_("BsR"), blank=True, null=True)
    fld = models.FloatField(_("Fld"), blank=True, null=True)
    off = models.FloatField(_("Off"), blank=True, null=True)
    _def = models.FloatField(_("Def"), blank=True, null=True)
    war = models.FloatField(_("WAR"), blank=True, null=True)
    w = models.FloatField(_("Win"), blank=True, null=True)
    l = models.FloatField(_("Loses"), blank=True, null=True)
    era = models.FloatField(_("Earned Run Average"), blank=True, null=True)
    gs = models.FloatField(_("Game Started"), blank=True, null=True)
    ip = models.FloatField(_("Innings Pitched"), blank=True, null=True)
    ha = models.FloatField(_("Hits Allowed"), blank=True, null=True)
    er = models.FloatField(_("Earned Run"), blank=True, null=True)
    hra = models.FloatField(_("Home Run Allowed"), blank=True, null=True)
    soa = models.FloatField(_("Strike Out Allowed"), blank=True, null=True)
    bba = models.FloatField(_("Base Balls Allowed"), blank=True, null=True)
    whip = models.FloatField(_("WHIP"), blank=True, null=True)
    k9 = models.FloatField(_("Strike Out in 9 Inns"), blank=True, null=True)
    bb9 = models.FloatField(_("Base Balls in ( Inns"), blank=True, null=True)
    fip = models.FloatField(_("FIP"), blank=True, null=True)
    adp = models.FloatField(_("WAR"), blank=True, null=True)



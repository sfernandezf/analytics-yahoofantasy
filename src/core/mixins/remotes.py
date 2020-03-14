from django.conf import settings

class BaseRemoteObjectMixin:
    def __init__(self, **kwargs):
        self.fields = []
        self.attrs = {}
        self.children_map = {}

    def get_remote_attrs(self, **kwargs):
        return self.attrs

    def update(self, **kwargs):
        raise NotImplementedError

    def get_children(self, child, **kwargs):
        if not child in self.children_map:
            return []
        
        return getattr(self, self.children_map[child])(**kwargs)
        

class YahooBaseRemoteObjectMixin(BaseRemoteObjectMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields = ['id', 'name']




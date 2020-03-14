from rest_framework import mixins, viewsets
from rest_framework.settings import api_settings


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    """
    queryset = None
    serializer_class = None

    lookup_field = 'pk'

    # The filter backend classes to use for queryset filtering
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS

    # The style to use for queryset pagination.
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES

    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

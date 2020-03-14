import os
from django.conf import settings

from yahoo_oauth import OAuth2

def get_oauth():
    file_path = os.path.join(settings.BASE_DIR, "core", "settings",
                             "yahoo.json")
    oauth = settings.YAHOO_OAUTH
    if not oauth:
        oauth = OAuth2(None, None, from_file=file_path)
        
    if not oauth.token_is_valid():
        oauth.refresh_access_token()
    
    settings.YAHOO_OAUTH = oauth
    return oauth

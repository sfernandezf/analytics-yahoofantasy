from split_settings.tools import include


INSTALLED_APPS = ["users"]
include(
    "base.py", 
    "rest.py", 
    "storage.py", 
    "auth.py", 
    "email.py", 
    "swagger.py",
    "others.py",
    "yahoo.py",
    "project_apps.py"
)

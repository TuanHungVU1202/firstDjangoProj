from django.urls import path
from . import views

'''
from django.db import connections
from django.db.utils import OperationalError
db_conn = connections['default']
try:
    c = db_conn.cursor()
except OperationalError:
    connected = False
else:
    connected = True
'''
import socket

def test_connection():
    """Test whether the postgres database is available. Usage:

        if "--offline" in sys.argv:
            os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings.offline'
        else:
            os.environ['DJANGO_SETTINGS_MODULE'] = 'myapp.settings.standard'
            from myapp.functions.connection import test_connection
            test_connection()
    """
    try:
        s = socket.create_connection(("example.net", 5432), 5)
        s.close()
    except socket.timeout:
        msg = """Can't detect the postgres server. If you're outside the
        intranet, you might need to turn the VPN on."""
        raise socket.timeout(msg)

urlpatterns = {
    path ('', views.index),
    path ('contact/', views.contact)
}


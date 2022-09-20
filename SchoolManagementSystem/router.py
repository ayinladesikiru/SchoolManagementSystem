from sms.viewset import StudentViewset
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('studentz', StudentViewset)
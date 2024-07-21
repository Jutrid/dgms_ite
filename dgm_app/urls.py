from django.urls import path
from .views import more, one, form_demanede, dashboard, gst_user, gst_new, gst_place, add_place
urlpatterns = [
    path('more/', more, name='more'),
    path('one<int:id>/', one, name='one'),
    path('form_demande/', form_demanede, name='form_demande'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/gestion user/', gst_user, name='gst_user'),
    path('dashboard/gestion new/', gst_new, name='gst_new'),
    path('dashboard/gestion new/add', gst_new),
    path('dashboard/gestion place/', gst_place, name='gst_place'),
    path('dashboard/gestion place/add', add_place),
]

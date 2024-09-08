from django.urls import path
from .views import delete_place, delete_new, get_result, more, one, form_demanede, dashboard, gst_user, gst_new, gst_place, add_place, add_new, gst_demande, detail, demande_a, demande_n
urlpatterns = [
    path('more/', more, name='more'),
    path('one<int:id>/', one, name='one'),
    path('form_demande/', form_demanede, name='form_demande'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/gestion user/', gst_user, name='gst_user'),
    path('dashboard/gestion new/', gst_new, name='gst_new'),
    path('dashboard/gestion new/add', add_new, name='add_new'),
    path('dashboard/gestion new/delete<int:id>', delete_new),
    path('dashboard/gestion place/', gst_place, name='gst_place'),
    path('dashboard/gestion place/add', add_place),
    path('dashboard/gestion place/delete<int:id>', delete_place),
    path('dashboard/gestion demande/', gst_demande, name='gst_demande'),
    path('dashboard/gestion demande/appouver<int:id>', demande_a),
    path('dashboard/gestion demande/desappouver<int:id>', demande_n),
    path('dashboard/gestion demande/detail<int:id>', detail),
    path('dashboard/gestion demande/get_pdf_file<int:id>', get_result),
]


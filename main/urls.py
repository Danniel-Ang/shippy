from django.urls import path
from main.views import make_entry_product
from main.views import *
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('edit_product/<uuid:id>', edit_product, name='edit_product'),
    path('delete_product/<uuid:id>', delete_product, name='delete_product'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'), 
    path('create-product-entry', make_entry_product, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]


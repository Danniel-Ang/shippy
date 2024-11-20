from django.urls import path
from main.views import *
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    
    # Authentication
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', user_logout, name='logout'), 
    
    # Modify Product Entry
    path('add-product-entry', add_product_entry, name='add_product_entry'),
    path('add-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>', delete_product, name='delete_product'),
    
    # Show XML JSON
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('json_user', show_user_product, name='show_user_product'),
    
    # Flutter
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]


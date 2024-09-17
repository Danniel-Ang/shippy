from django.urls import path
from main.views import make_entry_product
from main.views import show_main
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', make_entry_product, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]


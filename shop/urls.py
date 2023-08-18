from django.urls import path
from django.utils.regex_helper import normalize
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),

    # ===activar==desactivar shop/iluminacion
    path('shop/<slug:subcategory_slug>/<slug:category_slug>/', views.shop, name='categries'),
    path('shop/<slug:subcategory_slug>/', views.shop, name='subcategries'),

    # path('shop/<slug:subcategory_slug>/<slug:category_slug>/', views.shop, name='subcategries'),
    path('shop/<slug:subcategory_slug>/<slug:category_slug>/<slug:product_details_slug>/', views.product_details, name='product_details'),
    path('search/', views.search, name='search'),
    path('review/<int:product_id>/', views.review, name='review'),
    # path('shop/<slug:subcategory_slug', views.shop2 ,name ='subcategries')
    path('shop/<slug:category_slug', views.shop2 )

]




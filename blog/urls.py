from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('about', views.about, name='about'),
    path('about/edit', views.about_edit, name='about_edit'),
    path('contact', views.contact, name='contact'),
    path('newsletter-add', views.newsletter_add, name='newsletter_add'),
    path('newsletter-confirm/<str:code>', views.newsletter_confirm, name='newsletter_confirm'),
    path('newsletter-remove/<str:code>', views.newsletter_remove, name='newsletter_remove'),
    path('newsletter-send', views.newsletter_send, name='newsletter_send'),
    path('media/uploads/<str:year>/<str:month>/<str:day>/<str:name>', views.media, name='media'),
      path('help', views.help, name='help'),
]

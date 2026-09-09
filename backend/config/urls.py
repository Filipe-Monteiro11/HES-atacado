from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from produtos import views

admin.site.site_header = 'HES Atacado — Painel Administrativo'
admin.site.site_title = 'HES Atacado'
admin.site.index_title = 'Gerenciamento'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('api/categorias/', views.api_categorias, name='api_categorias'),
    path('api/produtos/', views.api_produtos, name='api_produtos'),
]

# Serve os arquivos do frontend (css, js, img) direto da pasta frontend
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^(?P<path>(?:css|js|img)/.*)$', serve, {'document_root': settings.FRONTEND_DIR}),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
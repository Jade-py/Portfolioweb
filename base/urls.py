from django.urls import path, include
from .views import resume, workspace, home, DeleteSkills, DeleteCertification,DeleteProjects, moveup, movedown
from django.conf.urls.static import static
from portfolio.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', home, name='home'),
    path('resume/', resume, name='resume'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('workspace/', workspace, name='workspace'),
    path('delete_skill/<int:pk>/', DeleteSkills.as_view(), name='DeleteSkill'),
    path('delete_certificate/<int:pk>/', DeleteCertification.as_view(), name='DeleteCertificate'),
    path('delete_project/<int:pk>/', DeleteProjects.as_view(), name='DeleteProject'),
    path('up/<str:model>/<int:pk>', moveup, name='up'),
    path('down/<str:model>/<int:pk>', movedown, name='down'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

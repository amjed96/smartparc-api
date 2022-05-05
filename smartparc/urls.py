"""smartparc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from personnel.views import UserViewset, PermisViewset, PasseportViewset, VisiteViewset
from flotte.views import VehiculeViewset, AffectationViewset, ContratLocationFlotteViewset, ContratAchatViewset, ConsommationViewset
from achatstock.views import DocumentViewset, DemandeAchatViewset, StockViewset
from location.views import ContratLocationViewset
from maintenance.views import DemandeInterventionViewset, InterventionViewset, PieceRechangeViewset, PlanEntretienViewset
from transport.views import FicheTrajetViewset
from tiers.views import TiersViewset, ContactViewset
from transport.views import DossierVoyage, FicheTrajet

router = routers.SimpleRouter()

# Personnel
router.register(r'personnel', UserViewset, basename='personnel')
router.register(r'permis', PermisViewset, basename='permis')
router.register(r'passeport', PasseportViewset, basename='passeport')
router.register(r'visite', VisiteViewset, basename='visite')

# Flotte
router.register(r'vehicule', VehiculeViewset, basename='vehicule')
router.register(r'affectation', AffectationViewset, basename='affectation')
router.register(r'contrat-location-flotte', ContratLocationFlotteViewset, basename='contrat-location-flotte')
router.register(r'contrat-achat', ContratAchatViewset, basename='contrat-achat')
router.register(r'consommation', ConsommationViewset, basename='consommation')

# AchatStock
router.register(r'document', DocumentViewset, basename='document')
router.register(r'demande-achat', DemandeAchatViewset, basename='demande-achat')
router.register(r'stock', StockViewset, basename='stock')

# Location
router.register(r'contrat-location', ContratLocationViewset, basename='contrat-location')

# Maintenance
router.register(r'demande-intervention', DemandeInterventionViewset, basename='demande-intervention')
router.register(r'intervention', InterventionViewset, basename='intervention')
router.register(r'piece-rechange', PieceRechangeViewset, basename='piece-rechange')
router.register(r'plan-entretien', PlanEntretienViewset, basename='plan-entretien')

# Tiers
router.register(r'tiers', TiersViewset, basename='tiers')
router.register(r'contact', ContactViewset, basename='contact')

# Transport
router.register(r'dossier-voyage', DemandeAchatViewset, basename='dossier-voyage')
router.register(r'fiche-trajet', FicheTrajetViewset, basename='fiche-trajet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]

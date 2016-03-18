
__author__ = 'mrk2'

from django.conf.urls import url

from gastos import views
urlpatterns = [

    url(r'^tipo-de-gasto/$', views.tipoGasto, name='tipo-gasto'),
    url(r'^gastos/$', views.misGastos, name='misGastos'),



]

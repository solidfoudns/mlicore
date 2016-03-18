from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from ecomerce.orders.models import Orden

def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        #el pago fue correctamente procesado
        order = get_object_or_404(Orden, id=ipn_obj.invoice)
        #marca la orden como pagada
        order.paid = True
        order.save()
    valid_ipn_received.connect(payment_notification)


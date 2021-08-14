# Create your tasks here

from celery import shared_task
from order.models import Order
from django.core.mail import send_mail


@shared_task
def message_to_clients(order_id):
    order=Order.objects.get(id=order_id)

    subject=f"Hello Dear{order.first_name} "
    message=f"Your shopping in our website and your cart have {order.orderitems} , and your order id is {order.id}"

    sender="mostafa.xw@gmail.com"
    reciver=f"{order.email}"

    send_mail(subject=subject,
              message=message,
              from_email=sender,
              to=reciver  )

    return send_mail

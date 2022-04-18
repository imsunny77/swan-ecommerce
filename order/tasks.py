from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from .utils import mail_order_detail
from datetime import datetime, timedelta

@task(name="task_mail_order_detail")
def task_mail_order_detail(mail_to, receipt, branch_email):
    mail_order_detail(mail_to, receipt, branch_email)
    return 'Order detail has been sent successfully to the mail %s' % (mail_to,)
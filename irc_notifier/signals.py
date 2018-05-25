import logging
from django.dispatch import receiver
from xmodule.modulestore.django import modulestore, SignalHandler

from . import tasks

log = logging.getLogger()

@receiver(SignalHandler.course_published)
def notify_on_course_publish(sender, course_key, **kwargs):
    log.info("Sending notification of course publish.")
    tasks.notify_on_irc.delay(sender, course_key)

import irc.client

from django.conf import settings
from celery.task import task
from operator import itemgetter

DEFAULT_SETTINGS = {
    "SERVER": "irc.freenode.net",
    "PORT": 6667,
    "CHANNEL": "##edxcon2018workshop",
    "NICKNAME": "edxircnotifier"
}

class IRCNotifierClient(irc.client.SimpleIRCClient):
    def __init__(self, target, message):
        super(IRCNotifierClient, self).__init__()
        self.target = target
        self.message = message

    def on_welcome(self, connection, event):
        if irc.client.is_channel(self.target):
            connection.join(self.target)
        else:
            self.send_message()

    def on_join(self, connection, event):
        self.send_message()

    def send_message(self):
        self.connection.privmsg(self.target, self.message)
        self.connection.quit("")


@task()
def notify_on_irc(sender, course_key):
    message = "Course Published: %s" % (course_key,)
    ircsettings = getattr(settings, "IRC_NOTIFIER", DEFAULT_SETTINGS)
    server, port, channel, nickname = itemgetter("SERVER", "PORT", "CHANNEL", "NICKNAME")(ircsettings)
    client = IRCNotifierClient(channel, message)
    client.connect(server, port, nickname)
    client.start()

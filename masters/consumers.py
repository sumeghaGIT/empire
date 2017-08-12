from channels import Channel
from channels.sessions import channel_session
from .models import Notifications
from channels import Group

# Connected to websocket.connect
@channel_session
def ws_connect(message):
    # Add to reader group
    Group("notification").add(message.reply_channel)
    # Accept the connection request
    message.reply_channel.send({"accept": True})

# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    # Remove from reader group on clean disconnect
    Group("notification").discard(message.reply_channel)
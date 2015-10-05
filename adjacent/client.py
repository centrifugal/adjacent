# coding: utf-8
from django.conf import settings
from cent.core import Client as RawClient


class Client(object):

    def __init__(self, address=None, secret=None, timeout=10, json_encoder=None):
        self.address = address or settings.CENTRIFUGE_ADDRESS
        self.secret = secret or settings.CENTRIFUGE_SECRET
        self.timeout = timeout or settings.CENTRIFUGE_TIMEOUT
        self.api_address = self.address
        self._client = RawClient(
            self.api_address, self.secret,
            timeout=self.timeout, json_encoder=json_encoder
        )

    def publish(self, channel, data, client=None):
        params = {
            "channel": channel,
            "data": data
        }
        if client:
            params["client"] = client
        self._client.add("publish", params)

    def unsubscribe(self, user, channel=None):
        params = {"user": user}
        if channel:
            params["channel"] = channel
        self._client.add("unsubscribe", params)

    def disconnect(self, user):
        self._client.add("disconnect", {
            "user": user
        })

    def presence(self, channel):
        self._client.add("presence", {
            "channel": channel
        })

    def history(self, channel):
        self._client.add("history", {
            "channel": channel
        })

    def channels(self):
        self._client.add("channels", {})

    def stats(self):
        self._client.add("stats", {})

    def send(self):
        return self._client.send()

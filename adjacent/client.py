# coding: utf-8
from django.conf import settings
from cent.core import Client as RawClient


class Client(object):

    def __init__(self, address=None, project_id=None, secret_key=None, timeout=10):
        self.address = address or settings.CENTRIFUGE_ADDRESS
        self.project_id = project_id or settings.CENTRIFUGE_PROJECT_ID
        self.secret_key = secret_key or settings.CENTRIFUGE_PROJECT_SECRET
        self.timeout = timeout or settings.CENTRIFUGE_TIMEOUT
        self.api_address = self.address + '/api'
        self._client = RawClient(
            self.api_address, self.project_id, self.secret_key, timeout=self.timeout
        )

    def publish(self, channel, data):
        self._client.add("publish", {
            "channel": channel,
            "data": data
        })

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

    def send(self):
        return self._client.send()

Centrifugo server integration with Django framework.

Installation:

```bash
pip install adjacent
```

Add `adjacent` into INSTALLED_APPS

Add some settings to your `settings.py` file:

```python
CENTRIFUGE_ADDRESS = 'http://centrifuge.example.com'
CENTRIFUGE_SECRET = 'your secret key from Centrifugo'
CENTRIFUGE_TIMEOUT = 10
```

After this you get the follows:

1) Function to create connection parameters for user:

```python
from adjacent import get_connection_parameters

params = get_connection_parameters(user)
```

2) Client wrapper to send messages into Centrifuge

```python
from adjacent import Client

client = Client()

# add some messages to publish
client.publish("channel", {"data": "first"})
client.publish("channel", {"data": "second"})

# actually send request with 2 publish messages added above to Centrifuge
response = client.send()
```

Client methods:

* `client.publish(channel, data, client=None)`
* `client.disconnect(user)`
* `client.unsubscribe(user, channel)`
* `client.presence(channel)`
* `client.history(channel)`
* `client.channels()`
* `client.stats()`

In template
===========

When you passed connection parameters to template you can initialize Centrifuge javascript object in this way:

```javascript
var centrifuge = new Centrifuge({
    url: '{{ params.sockjs_endpoint }}',
    user: '{{ params.user }}',
    timestamp: '{{ params.timestamp }}',
    info: '{{ params.info|safe }}',
    token: '{{ params.token }}'
});
```

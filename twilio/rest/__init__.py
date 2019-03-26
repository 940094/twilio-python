# coding=utf-8
import os
import platform
from twilio import __version__
from twilio.base.exceptions import TwilioException
from twilio.base.obsolete import obsolete_client
from twilio.http.http_client import TwilioHttpClient


class Client(object):

    def __init__(self, username=None, password=None, account_sid=None, region=None,
                 http_client=None, environment=None):

        environment = environment or os.environ

        self.username = username or environment.get('TWILIO_ACCOUNT_SID')

        self.password = password or environment.get('TWILIO_AUTH_TOKEN')

        self.account_sid = account_sid or self.username

        self.region = region


        if not self.username or not self.password:
            raise TwilioException("Credentials are required to create a TwilioClient")

        self.auth = (self.username, self.password)

        self.http_client = http_client or TwilioHttpClient()


        # Domains
        self._accounts = None
        self._api = None
        self._authy = None
        self._autopilot = None
        self._chat = None
        self._fax = None
        self._flex_api = None
        self._ip_messaging = None
        self._lookups = None
        self._monitor = None
        self._notify = None
        self._preview = None
        self._pricing = None
        self._proxy = None
        self._taskrouter = None
        self._trunking = None
        self._video = None
        self._messaging = None
        self._wireless = None
        self._sync = None
        self._studio = None
        self._verify = None
        self._voice = None
        self._insights = None

    def request(self, method, uri, params=None, data=None, headers=None, auth=None,
                timeout=None, allow_redirects=False):

        auth = auth or self.auth
        headers = headers or {}

        headers['User-Agent'] = 'twilio-python/{} (Python {})'.format(
            __version__,
            platform.python_version(),
        )
        headers['X-Twilio-Client'] = 'python-{}'.format(__version__)
        headers['Accept-Charset'] = 'utf-8'

        if method == 'POST' and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        if 'Accept' not in headers:
            headers['Accept'] = 'application/json'

        if self.region:
            head, tail = uri.split('.', 1)

            if not tail.startswith(self.region):
                uri = '.'.join([head, self.region, tail])

        return self.http_client.request(
            method,
            uri,
            params=params,
            data=data,
            headers=headers,
            auth=auth,
            timeout=timeout,
            allow_redirects=allow_redirects
        )

    @property
    def accounts(self):

        if self._accounts is None:
            from twilio.rest.accounts import Accounts
            self._accounts = Accounts(self)
        return self._accounts

    @property
    def api(self):

        if self._api is None:
            from twilio.rest.api import Api
            self._api = Api(self)
        return self._api

    @property
    def authy(self):

        if self._authy is None:
            from twilio.rest.authy import Authy
            self._authy = Authy(self)
        return self._authy

    @property
    def autopilot(self):

        if self._autopilot is None:
            from twilio.rest.autopilot import Autopilot
            self._autopilot = Autopilot(self)
        return self._autopilot

    @property
    def chat(self):

        if self._chat is None:
            from twilio.rest.chat import Chat
            self._chat = Chat(self)
        return self._chat

    @property
    def fax(self):

        if self._fax is None:
            from twilio.rest.fax import Fax
            self._fax = Fax(self)
        return self._fax

    @property
    def flex_api(self):

        if self._flex_api is None:
            from twilio.rest.flex_api import FlexApi
            self._flex_api = FlexApi(self)
        return self._flex_api

    @property
    def ip_messaging(self):

        if self._ip_messaging is None:
            from twilio.rest.ip_messaging import IpMessaging
            self._ip_messaging = IpMessaging(self)
        return self._ip_messaging

    @property
    def lookups(self):

        if self._lookups is None:
            from twilio.rest.lookups import Lookups
            self._lookups = Lookups(self)
        return self._lookups

    @property
    def monitor(self):

        if self._monitor is None:
            from twilio.rest.monitor import Monitor
            self._monitor = Monitor(self)
        return self._monitor

    @property
    def notify(self):

        if self._notify is None:
            from twilio.rest.notify import Notify
            self._notify = Notify(self)
        return self._notify

    @property
    def preview(self):

        if self._preview is None:
            from twilio.rest.preview import Preview
            self._preview = Preview(self)
        return self._preview

    @property
    def pricing(self):

        if self._pricing is None:
            from twilio.rest.pricing import Pricing
            self._pricing = Pricing(self)
        return self._pricing

    @property
    def proxy(self):
        if self._proxy is None:
            from twilio.rest.proxy import Proxy
            self._proxy = Proxy(self)
        return self._proxy

    @property
    def taskrouter(self):

        if self._taskrouter is None:
            from twilio.rest.taskrouter import Taskrouter
            self._taskrouter = Taskrouter(self)
        return self._taskrouter

    @property
    def trunking(self):

        if self._trunking is None:
            from twilio.rest.trunking import Trunking
            self._trunking = Trunking(self)
        return self._trunking

    @property
    def video(self):

        if self._video is None:
            from twilio.rest.video import Video
            self._video = Video(self)
        return self._video

    @property
    def messaging(self):

        if self._messaging is None:
            from twilio.rest.messaging import Messaging
            self._messaging = Messaging(self)
        return self._messaging

    @property
    def wireless(self):

        if self._wireless is None:
            from twilio.rest.wireless import Wireless
            self._wireless = Wireless(self)
        return self._wireless

    @property
    def sync(self):

        if self._sync is None:
            from twilio.rest.sync import Sync
            self._sync = Sync(self)
        return self._sync

    @property
    def studio(self):

        if self._studio is None:
            from twilio.rest.studio import Studio
            self._studio = Studio(self)
        return self._studio

    @property
    def verify(self):

        if self._verify is None:
            from twilio.rest.verify import Verify
            self._verify = Verify(self)
        return self._verify

    @property
    def voice(self):

        if self._voice is None:
            from twilio.rest.voice import Voice
            self._voice = Voice(self)
        return self._voice

    @property
    def insights(self):

        if self._insights is None:
            from twilio.rest.insights import Insights
            self._insights = Insights(self)
        return self._insights

    @property
    def addresses(self):

        return self.api.account.addresses

    @property
    def applications(self):

        return self.api.account.applications

    @property
    def authorized_connect_apps(self):

        return self.api.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):

        return self.api.account.available_phone_numbers

    @property
    def balance(self):

        return self.api.account.balance

    @property
    def calls(self):

        return self.api.account.calls

    @property
    def conferences(self):

        return self.api.account.conferences

    @property
    def connect_apps(self):

        return self.api.account.connect_apps

    @property
    def incoming_phone_numbers(self):

        return self.api.account.incoming_phone_numbers

    @property
    def keys(self):

        return self.api.account.keys

    @property
    def messages(self):

        return self.api.account.messages

    @property
    def new_keys(self):

        return self.api.account.new_keys

    @property
    def new_signing_keys(self):

        return self.api.account.new_signing_keys

    @property
    def notifications(self):

        return self.api.account.notifications

    @property
    def outgoing_caller_ids(self):

        return self.api.account.outgoing_caller_ids

    @property
    def queues(self):

        return self.api.account.queues

    @property
    def recordings(self):

        return self.api.account.recordings

    @property
    def signing_keys(self):

        return self.api.account.signing_keys

    @property
    def sip(self):

        return self.api.account.sip

    @property
    def short_codes(self):

        return self.api.account.short_codes

    @property
    def tokens(self):

        return self.api.account.tokens

    @property
    def transcriptions(self):

        return self.api.account.transcriptions

    @property
    def usage(self):

        return self.api.account.usage

    @property
    def validation_requests(self):

        return self.api.account.validation_requests

    def __repr__(self):

        return '<Twilio {}>'.format(self.account_sid)


@obsolete_client
class TwilioClient(object):


    def __init__(self, *args):
        pass


@obsolete_client
class TwilioRestClient(object):


    def __init__(self, *args):
        pass


@obsolete_client
class TwilioIpMessagingClient(object):


    def __init__(self, *args):
        pass


@obsolete_client
class TwilioLookupsClient(object):

    def __init__(self, *args):
        pass


@obsolete_client
class TwilioMonitorClient(object):


    def __init__(self, *args):
        pass


@obsolete_client
class TwilioPricingClient(object):


    def __init__(self, *args):
        pass


@obsolete_client
class TwilioTaskRouterClient(object):


    def __init__(self, *args):
        pass


@obsolete_client
class TwilioTrunkingClient(object):


    def __init__(self, *args):
        pass

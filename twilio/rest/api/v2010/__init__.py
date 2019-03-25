# coding=utf-8

from twilio.base.version import Version
from twilio.rest.api.v2010.account import AccountContext
from twilio.rest.api.v2010.account import AccountList


class V2010(Version):

    def __init__(self, domain):

        super(V2010, self).__init__(domain)
        self.version = '2010-04-01'
        self._accounts = None
        self._account = None

    @property
    def accounts(self):
 
        if self._accounts is None:
            self._accounts = AccountList(self)
        return self._accounts

    @property
    def account(self):

        if self._account is None:
            self._account = AccountContext(self, self.domain.twilio.account_sid)
        return self._account

    @account.setter
    def account(self, value):

        self._account = value

    @property
    def addresses(self):

        return self.account.addresses

    @property
    def applications(self):

        return self.account.applications

    @property
    def authorized_connect_apps(self):

        return self.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):

        return self.account.available_phone_numbers

    @property
    def balance(self):

        return self.account.balance

    @property
    def calls(self):

        return self.account.calls

    @property
    def conferences(self):

        return self.account.conferences

    @property
    def connect_apps(self):

        return self.account.connect_apps

    @property
    def incoming_phone_numbers(self):

        return self.account.incoming_phone_numbers

    @property
    def keys(self):

        return self.account.keys

    @property
    def messages(self):

        return self.account.messages

    @property
    def new_keys(self):

        return self.account.new_keys

    @property
    def new_signing_keys(self):
        return self.account.new_signing_keys

    @property
    def notifications(self):

        return self.account.notifications

    @property
    def outgoing_caller_ids(self):

        return self.account.outgoing_caller_ids

    @property
    def queues(self):

        return self.account.queues

    @property
    def recordings(self):

        return self.account.recordings

    @property
    def signing_keys(self):

        return self.account.signing_keys

    @property
    def sip(self):

        return self.account.sip

    @property
    def short_codes(self):

        return self.account.short_codes

    @property
    def tokens(self):

        return self.account.tokens

    @property
    def transcriptions(self):

        return self.account.transcriptions

    @property
    def usage(self):

        return self.account.usage

    @property
    def validation_requests(self):

        return self.account.validation_requests

    def __repr__(self):

        return '<Twilio.Api.V2010>'

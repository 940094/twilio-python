# coding=utf-8

from twilio.base.domain import Domain
from twilio.rest.api.v2010 import V2010


class Api(Domain):

    def __init__(self, twilio):
 
        super(Api, self).__init__(twilio)

        self.base_url = 'https://api.twilio.com'

        # Versions
        self._v2010 = None

    @property
    def v2010(self):

        if self._v2010 is None:
            self._v2010 = V2010(self)
        return self._v2010

    @property
    def account(self):
 
        return self.v2010.account

    @property
    def accounts(self):
 
        return self.v2010.accounts

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
        """
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestList
        """
        return self.account.validation_requests

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api>'

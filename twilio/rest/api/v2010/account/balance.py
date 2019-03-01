# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class BalanceList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the BalanceList

        :param Version version: Version that contains the resource
        :param account_sid: Account Sid.

        :returns: twilio.rest.api.v2010.account.balance.BalanceList
        :rtype: twilio.rest.api.v2010.account.balance.BalanceList
        """
        super(BalanceList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/Balance.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a BalanceInstance

        :returns: Fetched BalanceInstance
        :rtype: twilio.rest.api.v2010.account.balance.BalanceInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return BalanceInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.BalanceList>'


class BalancePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the BalancePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: Account Sid.

        :returns: twilio.rest.api.v2010.account.balance.BalancePage
        :rtype: twilio.rest.api.v2010.account.balance.BalancePage
        """
        super(BalancePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BalanceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.balance.BalanceInstance
        :rtype: twilio.rest.api.v2010.account.balance.BalanceInstance
        """
        return BalanceInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.BalancePage>'


class BalanceInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid):
        """
        Initialize the BalanceInstance

        :returns: twilio.rest.api.v2010.account.balance.BalanceInstance
        :rtype: twilio.rest.api.v2010.account.balance.BalanceInstance
        """
        super(BalanceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'balance': payload['balance'],
            'currency': payload['currency'],
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, }

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def balance(self):
        """
        :returns: Account balance
        :rtype: unicode
        """
        return self._properties['balance']

    @property
    def currency(self):
        """
        :returns: Currency units
        :rtype: unicode
        """
        return self._properties['currency']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.BalanceInstance>'
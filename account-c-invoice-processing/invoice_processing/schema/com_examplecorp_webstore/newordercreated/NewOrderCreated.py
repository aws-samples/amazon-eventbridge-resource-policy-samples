# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.com_examplecorp_webstore.newordercreated.NewOrderCreatedItem import NewOrderCreatedItem  # noqa: F401,E501

class NewOrderCreated(object):


    _types = {
        'customerId': 'str',
        'lineItems': 'list[NewOrderCreatedItem]',
        'orderDate': 'datetime',
        'orderNo': 'str'
    }

    _attribute_map = {
        'customerId': 'customerId',
        'lineItems': 'lineItems',
        'orderDate': 'orderDate',
        'orderNo': 'orderNo'
    }

    def __init__(self, customerId=None, lineItems=None, orderDate=None, orderNo=None):  # noqa: E501
        self._customerId = None
        self._lineItems = None
        self._orderDate = None
        self._orderNo = None
        self.discriminator = None
        self.customerId = customerId
        self.lineItems = lineItems
        self.orderDate = orderDate
        self.orderNo = orderNo


    @property
    def customerId(self):

        return self._customerId

    @customerId.setter
    def customerId(self, customerId):


        self._customerId = customerId


    @property
    def lineItems(self):

        return self._lineItems

    @lineItems.setter
    def lineItems(self, lineItems):


        self._lineItems = lineItems


    @property
    def orderDate(self):

        return self._orderDate

    @orderDate.setter
    def orderDate(self, orderDate):


        self._orderDate = orderDate


    @property
    def orderNo(self):

        return self._orderNo

    @orderNo.setter
    def orderNo(self, orderNo):


        self._orderNo = orderNo

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NewOrderCreated, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, NewOrderCreated):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


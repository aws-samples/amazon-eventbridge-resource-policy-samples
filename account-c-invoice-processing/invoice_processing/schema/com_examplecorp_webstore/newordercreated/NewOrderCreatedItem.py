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

class NewOrderCreatedItem(object):


    _types = {
        'currency': 'str',
        'productCode': 'str',
        'quantityOrdered': 'float',
        'unitPrice': 'float'
    }

    _attribute_map = {
        'currency': 'currency',
        'productCode': 'productCode',
        'quantityOrdered': 'quantityOrdered',
        'unitPrice': 'unitPrice'
    }

    def __init__(self, currency=None, productCode=None, quantityOrdered=None, unitPrice=None):  # noqa: E501
        self._currency = None
        self._productCode = None
        self._quantityOrdered = None
        self._unitPrice = None
        self.discriminator = None
        self.currency = currency
        self.productCode = productCode
        self.quantityOrdered = quantityOrdered
        self.unitPrice = unitPrice


    @property
    def currency(self):

        return self._currency

    @currency.setter
    def currency(self, currency):


        self._currency = currency


    @property
    def productCode(self):

        return self._productCode

    @productCode.setter
    def productCode(self, productCode):


        self._productCode = productCode


    @property
    def quantityOrdered(self):

        return self._quantityOrdered

    @quantityOrdered.setter
    def quantityOrdered(self, quantityOrdered):


        self._quantityOrdered = quantityOrdered


    @property
    def unitPrice(self):

        return self._unitPrice

    @unitPrice.setter
    def unitPrice(self, unitPrice):


        self._unitPrice = unitPrice

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
        if issubclass(NewOrderCreatedItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, NewOrderCreatedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other


# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.


class AccountingUnit(object):
    """Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.
    """

    def __init__(self, multiplier="M", energyUnit=0.0, monetaryUnit="CAD", value=0.0):
        """Initialises a new 'AccountingUnit' instance.

        @param multiplier: Multiplier for the 'energyUnit' or 'monetaryUnit'. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param energyUnit: Unit of service. 
        @param monetaryUnit: Unit of currency. Values are: "CAD", "EUR", "CHF", "INR", "AUD", "USD", "RUR", "GBP", "CNY", "SEK", "JPY", "other", "NOK", "DKK"
        @param value: Value expressed in applicable units. 
        """
        #: Multiplier for the 'energyUnit' or 'monetaryUnit'. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.multiplier = multiplier

        #: Unit of service.
        self.energyUnit = energyUnit

        #: Unit of currency. Values are: "CAD", "EUR", "CHF", "INR", "AUD", "USD", "RUR", "GBP", "CNY", "SEK", "JPY", "other", "NOK", "DKK"
        self.monetaryUnit = monetaryUnit

        #: Value expressed in applicable units.
        self.value = value


    _attrs = ["multiplier", "energyUnit", "monetaryUnit", "value"]
    _attr_types = {"multiplier": str, "energyUnit": float, "monetaryUnit": str, "value": float}
    _defaults = {"multiplier": "M", "energyUnit": 0.0, "monetaryUnit": "CAD", "value": 0.0}
    _enums = {"multiplier": "UnitMultiplier", "monetaryUnit": "Currency"}
    _refs = []
    _many_refs = []


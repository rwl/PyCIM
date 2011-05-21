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

from CIM14.Element import Element

class AccountingUnit(Element):
    """Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.
    """

    def __init__(self, multiplier="k", monetaryUnit="CNY", energyUnit=0.0, value=0.0, *args, **kw_args):
        """Initialises a new 'AccountingUnit' instance.

        @param multiplier: Multiplier for the 'energyUnit' or 'monetaryUnit'. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param monetaryUnit: Unit of currency. Values are: "CNY", "EUR", "INR", "AUD", "CHF", "DKK", "other", "RUR", "SEK", "GBP", "JPY", "NOK", "CAD", "USD"
        @param energyUnit: Unit of service. 
        @param value: Value expressed in applicable units. 
        """
        #: Multiplier for the 'energyUnit' or 'monetaryUnit'. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.multiplier = multiplier

        #: Unit of currency. Values are: "CNY", "EUR", "INR", "AUD", "CHF", "DKK", "other", "RUR", "SEK", "GBP", "JPY", "NOK", "CAD", "USD"
        self.monetaryUnit = monetaryUnit

        #: Unit of service.
        self.energyUnit = energyUnit

        #: Value expressed in applicable units.
        self.value = value

        super(AccountingUnit, self).__init__(*args, **kw_args)

    _attrs = ["multiplier", "monetaryUnit", "energyUnit", "value"]
    _attr_types = {"multiplier": str, "monetaryUnit": str, "energyUnit": float, "value": float}
    _defaults = {"multiplier": "k", "monetaryUnit": "CNY", "energyUnit": 0.0, "value": 0.0}
    _enums = {"multiplier": "UnitMultiplier", "monetaryUnit": "Currency"}
    _refs = []
    _many_refs = []


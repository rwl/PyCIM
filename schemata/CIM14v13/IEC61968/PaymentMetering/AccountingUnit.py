# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.Element import Element

class AccountingUnit(Element):
    """Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.
    """

    def __init__(self, monetaryUnit='EUR', multiplier='m', energyUnit=0.0, value=0.0, **kw_args):
        """Initializes a new 'AccountingUnit' instance.

        @param monetaryUnit: Unit of currency. Values are: "EUR", "other", "JPY", "DKK", "NOK", "CNY", "USD", "INR", "SEK", "AUD", "CHF", "CAD", "RUR", "GBP"
        @param multiplier: Multiplier for the 'energyUnit' or 'monetaryUnit'. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param energyUnit: Unit of service. 
        @param value: Value expressed in applicable units. 
        """
        #: Unit of currency.Values are: "EUR", "other", "JPY", "DKK", "NOK", "CNY", "USD", "INR", "SEK", "AUD", "CHF", "CAD", "RUR", "GBP"
        self.monetaryUnit = monetaryUnit

        #: Multiplier for the 'energyUnit' or 'monetaryUnit'.Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.multiplier = multiplier

        #: Unit of service.
        self.energyUnit = energyUnit

        #: Value expressed in applicable units.
        self.value = value

        super(AccountingUnit, self).__init__(**kw_args)


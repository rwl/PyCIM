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

from CIM14.Element import Element

class AccountMovement(Element):
    """Credit/debit movements for an account.
    """

    def __init__(self, dateTime='', amount=0.0, reason='', *args, **kw_args):
        """Initialises a new 'AccountMovement' instance.

        @param dateTime: Date and time when the credit/debit transaction was performed. 
        @param amount: Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears. 
        @param reason: Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied. 
        """
        #: Date and time when the credit/debit transaction was performed.
        self.dateTime = dateTime

        #: Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears.
        self.amount = amount

        #: Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied.
        self.reason = reason

        super(AccountMovement, self).__init__(*args, **kw_args)

    _attrs = ["dateTime", "amount", "reason"]
    _attr_types = {"dateTime": str, "amount": float, "reason": str}
    _defaults = {"dateTime": '', "amount": 0.0, "reason": ''}
    _enums = {}
    _refs = []
    _many_refs = []


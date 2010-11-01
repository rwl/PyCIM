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

class AccountMovement(Element):
    """Credit/debit movements for an account.
    """

    def __init__(self, amount=0.0, dateTime='', reason='', *args, **kw_args):
        """Initializes a new 'AccountMovement' instance.

        @param amount: Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears. 
        @param dateTime: Date and time when the credit/debit transaction was performed. 
        @param reason: Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied. 
        """
        #: Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears. 
        self.amount = amount

        #: Date and time when the credit/debit transaction was performed. 
        self.dateTime = dateTime

        #: Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied. 
        self.reason = reason

        super(AccountMovement, self).__init__(*args, **kw_args)


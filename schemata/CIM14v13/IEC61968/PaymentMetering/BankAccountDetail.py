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

class BankAccountDetail(Element):
    """Details of a bank account.
    """

    def __init__(self, branchCode='', holderID='', holderName='', accountNumber='', bankName='', *args, **kw_args):
        """Initializes a new 'BankAccountDetail' instance.

        @param branchCode: Branch of bank where account is held. 
        @param holderID: National identity number (or equivalent) of account holder. 
        @param holderName: Name of account holder. 
        @param accountNumber: Operational account reference number. 
        @param bankName: Name of bank where account is held. 
        """
        #: Branch of bank where account is held.
        self.branchCode = branchCode

        #: National identity number (or equivalent) of account holder.
        self.holderID = holderID

        #: Name of account holder.
        self.holderName = holderName

        #: Operational account reference number.
        self.accountNumber = accountNumber

        #: Name of bank where account is held.
        self.bankName = bankName

        super(BankAccountDetail, self).__init__(*args, **kw_args)


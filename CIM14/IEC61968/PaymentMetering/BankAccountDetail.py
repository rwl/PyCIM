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

class BankAccountDetail(Element):
    """Details of a bank account.
    """

    def __init__(self, holderName='', accountNumber='', bankName='', branchCode='', holderID='', *args, **kw_args):
        """Initialises a new 'BankAccountDetail' instance.

        @param holderName: Name of account holder. 
        @param accountNumber: Operational account reference number. 
        @param bankName: Name of bank where account is held. 
        @param branchCode: Branch of bank where account is held. 
        @param holderID: National identity number (or equivalent) of account holder. 
        """
        #: Name of account holder.
        self.holderName = holderName

        #: Operational account reference number.
        self.accountNumber = accountNumber

        #: Name of bank where account is held.
        self.bankName = bankName

        #: Branch of bank where account is held.
        self.branchCode = branchCode

        #: National identity number (or equivalent) of account holder.
        self.holderID = holderID

        super(BankAccountDetail, self).__init__(*args, **kw_args)

    _attrs = ["holderName", "accountNumber", "bankName", "branchCode", "holderID"]
    _attr_types = {"holderName": str, "accountNumber": str, "bankName": str, "branchCode": str, "holderID": str}
    _defaults = {"holderName": '', "accountNumber": '', "bankName": '', "branchCode": '', "holderID": ''}
    _enums = {}
    _refs = []
    _many_refs = []


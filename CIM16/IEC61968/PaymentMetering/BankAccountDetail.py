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


class BankAccountDetail(object):
    """Details of a bank account.Details of a bank account.
    """

    def __init__(self, holderID='', holderName='', bankName='', branchCode='', accountNumber=''):
        """Initialises a new 'BankAccountDetail' instance.

        @param holderID: National identity number (or equivalent) of account holder. 
        @param holderName: Name of account holder. 
        @param bankName: Name of bank where account is held. 
        @param branchCode: Branch of bank where account is held. 
        @param accountNumber: Operational account reference number. 
        """
        #: National identity number (or equivalent) of account holder.
        self.holderID = holderID

        #: Name of account holder.
        self.holderName = holderName

        #: Name of bank where account is held.
        self.bankName = bankName

        #: Branch of bank where account is held.
        self.branchCode = branchCode

        #: Operational account reference number.
        self.accountNumber = accountNumber


    _attrs = ["holderID", "holderName", "bankName", "branchCode", "accountNumber"]
    _attr_types = {"holderID": str, "holderName": str, "bankName": str, "branchCode": str, "accountNumber": str}
    _defaults = {"holderID": '', "holderName": '', "bankName": '', "branchCode": '', "accountNumber": ''}
    _enums = {}
    _refs = []
    _many_refs = []


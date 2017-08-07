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


class AccountMovement(object):
    """Credit/debit movements for an account.Credit/debit movements for an account.
    """

    def __init__(self, dateTime='', reason='', amount=0.0):
        """Initialises a new 'AccountMovement' instance.

        @param dateTime: Date and time when the credit/debit transaction was performed. 
        @param reason: Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied. 
        @param amount: Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears. 
        """
        #: Date and time when the credit/debit transaction was performed.
        self.dateTime = dateTime

        #: Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied.
        self.reason = reason

        #: Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears.
        self.amount = amount


    _attrs = ["dateTime", "reason", "amount"]
    _attr_types = {"dateTime": str, "reason": str, "amount": float}
    _defaults = {"dateTime": '', "reason": '', "amount": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []


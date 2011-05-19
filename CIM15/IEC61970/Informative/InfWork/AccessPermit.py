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

from CIM15.IEC61968.Common.Document import Document

class AccessPermit(Document):
    """A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.
    """

    def __init__(self, applicationNumber='', payment=0.0, effectiveDate='', expirationDate='', permitID='', *args, **kw_args):
        """Initialises a new 'AccessPermit' instance.

        @param applicationNumber: Permit application number that is used by municipality, state, province, etc. 
        @param payment: Total cost of permit. 
        @param effectiveDate: Date that permit became official. 
        @param expirationDate: Permit expiration date. 
        @param permitID: Permit identifier. 
        """
        #: Permit application number that is used by municipality, state, province, etc.
        self.applicationNumber = applicationNumber

        #: Total cost of permit.
        self.payment = payment

        #: Date that permit became official.
        self.effectiveDate = effectiveDate

        #: Permit expiration date.
        self.expirationDate = expirationDate

        #: Permit identifier.
        self.permitID = permitID

        super(AccessPermit, self).__init__(*args, **kw_args)

    _attrs = ["applicationNumber", "payment", "effectiveDate", "expirationDate", "permitID"]
    _attr_types = {"applicationNumber": str, "payment": float, "effectiveDate": str, "expirationDate": str, "permitID": str}
    _defaults = {"applicationNumber": '', "payment": 0.0, "effectiveDate": '', "expirationDate": '', "permitID": ''}
    _enums = {}
    _refs = []
    _many_refs = []


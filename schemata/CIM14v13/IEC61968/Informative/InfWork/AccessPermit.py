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

from CIM14v13.IEC61968.Common.Document import Document

class AccessPermit(Document):
    """A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.
    """

    def __init__(self, payment=0.0, applicationNumber='', expirationDate='', effectiveDate='', permitID='', *args, **kw_args):
        """Initializes a new 'AccessPermit' instance.

        @param payment: Total cost of permit. 
        @param applicationNumber: Permit application number that is used by municipality, state, province, etc. 
        @param expirationDate: Permit expiration date. 
        @param effectiveDate: Date that permit became official. 
        @param permitID: Permit identifier. 
        """
        #: Total cost of permit. 
        self.payment = payment

        #: Permit application number that is used by municipality, state, province, etc. 
        self.applicationNumber = applicationNumber

        #: Permit expiration date. 
        self.expirationDate = expirationDate

        #: Date that permit became official. 
        self.effectiveDate = effectiveDate

        #: Permit identifier. 
        self.permitID = permitID

        super(AccessPermit, self).__init__(*args, **kw_args)


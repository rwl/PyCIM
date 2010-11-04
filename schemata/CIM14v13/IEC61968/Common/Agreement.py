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

class Agreement(Document):
    """Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.
    """

    def __init__(self, signDate='', validityInterval=None, *args, **kw_args):
        """Initializes a new 'Agreement' instance.

        @param signDate: Date this agreement was consummated among associated persons and/or organisations. 
        @param validityInterval: Date and time interval this agreement is valid (from going into effect to termination).
        """
        #: Date this agreement was consummated among associated persons and/or organisations.
        self.signDate = signDate

        self.validityInterval = validityInterval

        super(Agreement, self).__init__(*args, **kw_args)

    # Date and time interval this agreement is valid (from going into effect to termination).
    validityInterval = None


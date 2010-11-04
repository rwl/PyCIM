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

class Regulation(Document):
    """Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.
    """

    def __init__(self, referenceNumber='', *args, **kw_args):
        """Initializes a new 'Regulation' instance.

        @param referenceNumber: External reference to regulation, if applicable. 
        """
        #: External reference to regulation, if applicable.
        self.referenceNumber = referenceNumber

        super(Regulation, self).__init__(*args, **kw_args)


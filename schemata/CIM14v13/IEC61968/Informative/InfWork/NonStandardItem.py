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

class NonStandardItem(Document):
    """This document provides information for non-standard items like customer contributions (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids.
    """

    def __init__(self, amount=0.0, code='', *args, **kw_args):
        """Initializes a new 'NonStandardItem' instance.

        @param amount: The projected cost for this item. 
        @param code: The category of non-standard work. 
        """
        #: The projected cost for this item.
        self.amount = amount

        #: The category of non-standard work.
        self.code = code

        super(NonStandardItem, self).__init__(*args, **kw_args)


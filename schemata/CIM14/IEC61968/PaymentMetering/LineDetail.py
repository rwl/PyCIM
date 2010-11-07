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

from CIM14.Element import Element

class LineDetail(Element):
    """Details on an amount line, with rounding, date and note.
    """

    def __init__(self, dateTime='', rounding=0.0, note='', amount=0.0, **kw_args):
        """Initializes a new 'LineDetail' instance.

        @param dateTime: Date and time when this line was created in the application process. 
        @param rounding: Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'. 
        @param note: Free format note relevant to this line. 
        @param amount: Amount for this line item. 
        """
        #: Date and time when this line was created in the application process.
        self.dateTime = dateTime

        #: Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'.
        self.rounding = rounding

        #: Free format note relevant to this line.
        self.note = note

        #: Amount for this line item.
        self.amount = amount

        super(LineDetail, self).__init__(**kw_args)


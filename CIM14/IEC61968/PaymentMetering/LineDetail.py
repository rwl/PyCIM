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

class LineDetail(Element):
    """Details on an amount line, with rounding, date and note.
    """

    def __init__(self, dateTime='', rounding=0.0, note='', amount=0.0, *args, **kw_args):
        """Initialises a new 'LineDetail' instance.

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

        super(LineDetail, self).__init__(*args, **kw_args)

    _attrs = ["dateTime", "rounding", "note", "amount"]
    _attr_types = {"dateTime": str, "rounding": float, "note": str, "amount": float}
    _defaults = {"dateTime": '', "rounding": 0.0, "note": '', "amount": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []


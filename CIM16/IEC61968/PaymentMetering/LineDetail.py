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


class LineDetail(object):
    """Details on an amount line, with rounding, date and note.Details on an amount line, with rounding, date and note.
    """

    def __init__(self, amount=0.0, rounding=0.0, dateTime='', note=''):
        """Initialises a new 'LineDetail' instance.

        @param amount: Amount for this line item. 
        @param rounding: Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'. 
        @param dateTime: Date and time when this line was created in the application process. 
        @param note: Free format note relevant to this line. 
        """
        #: Amount for this line item.
        self.amount = amount

        #: Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'.
        self.rounding = rounding

        #: Date and time when this line was created in the application process.
        self.dateTime = dateTime

        #: Free format note relevant to this line.
        self.note = note


    _attrs = ["amount", "rounding", "dateTime", "note"]
    _attr_types = {"amount": float, "rounding": float, "dateTime": str, "note": str}
    _defaults = {"amount": 0.0, "rounding": 0.0, "dateTime": '', "note": ''}
    _enums = {}
    _refs = []
    _many_refs = []


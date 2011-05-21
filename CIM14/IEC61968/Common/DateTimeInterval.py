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

class DateTimeInterval(Element):
    """Interval of date and time.
    """

    def __init__(self, end='', start='', *args, **kw_args):
        """Initialises a new 'DateTimeInterval' instance.

        @param end: Date and time that this interval ended. 
        @param start: Date and time that this interval started. 
        """
        #: Date and time that this interval ended.
        self.end = end

        #: Date and time that this interval started.
        self.start = start

        super(DateTimeInterval, self).__init__(*args, **kw_args)

    _attrs = ["end", "start"]
    _attr_types = {"end": str, "start": str}
    _defaults = {"end": '', "start": ''}
    _enums = {}
    _refs = []
    _many_refs = []


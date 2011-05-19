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

class ErpTimeSheet(Document):
    """Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.Time sheet for employees and contractors. Note that ErpTimeSheet inherits the relationship to ErpPerson from Document.
    """

    def __init__(self, ErpTimeEntries=None, *args, **kw_args):
        """Initialises a new 'ErpTimeSheet' instance.

        @param ErpTimeEntries:
        """
        self._ErpTimeEntries = []
        self.ErpTimeEntries = [] if ErpTimeEntries is None else ErpTimeEntries

        super(ErpTimeSheet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpTimeEntries"]
    _many_refs = ["ErpTimeEntries"]

    def getErpTimeEntries(self):
        
        return self._ErpTimeEntries

    def setErpTimeEntries(self, value):
        for x in self._ErpTimeEntries:
            x.ErpTimeSheet = None
        for y in value:
            y._ErpTimeSheet = self
        self._ErpTimeEntries = value

    ErpTimeEntries = property(getErpTimeEntries, setErpTimeEntries)

    def addErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj.ErpTimeSheet = self

    def removeErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj.ErpTimeSheet = None


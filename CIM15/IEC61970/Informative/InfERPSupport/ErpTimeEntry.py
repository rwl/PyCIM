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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpTimeEntry(IdentifiedObject):
    """An individual entry on an ErpTimeSheet.An individual entry on an ErpTimeSheet.
    """

    def __init__(self, ErpProjectAccounting=None, status=None, ErpTimeSheet=None, *args, **kw_args):
        """Initialises a new 'ErpTimeEntry' instance.

        @param ErpProjectAccounting:
        @param status:
        @param ErpTimeSheet:
        """
        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self.status = status

        self._ErpTimeSheet = None
        self.ErpTimeSheet = ErpTimeSheet

        super(ErpTimeEntry, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpProjectAccounting", "status", "ErpTimeSheet"]
    _many_refs = []

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.ErpTimeEntries if x != self]
            self._ErpProjectAccounting._ErpTimeEntries = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            if self not in self._ErpProjectAccounting._ErpTimeEntries:
                self._ErpProjectAccounting._ErpTimeEntries.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

    status = None

    def getErpTimeSheet(self):
        
        return self._ErpTimeSheet

    def setErpTimeSheet(self, value):
        if self._ErpTimeSheet is not None:
            filtered = [x for x in self.ErpTimeSheet.ErpTimeEntries if x != self]
            self._ErpTimeSheet._ErpTimeEntries = filtered

        self._ErpTimeSheet = value
        if self._ErpTimeSheet is not None:
            if self not in self._ErpTimeSheet._ErpTimeEntries:
                self._ErpTimeSheet._ErpTimeEntries.append(self)

    ErpTimeSheet = property(getErpTimeSheet, setErpTimeSheet)


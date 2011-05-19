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

class OutageHistory(Document):
    """A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.
    """

    def __init__(self, OutageReports=None, *args, **kw_args):
        """Initialises a new 'OutageHistory' instance.

        @param OutageReports: OutageReports per customer for which this OutageHistory is created.
        """
        self._OutageReports = []
        self.OutageReports = [] if OutageReports is None else OutageReports

        super(OutageHistory, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["OutageReports"]
    _many_refs = ["OutageReports"]

    def getOutageReports(self):
        """OutageReports per customer for which this OutageHistory is created.
        """
        return self._OutageReports

    def setOutageReports(self, value):
        for x in self._OutageReports:
            x.OutageHistory = None
        for y in value:
            y._OutageHistory = self
        self._OutageReports = value

    OutageReports = property(getOutageReports, setOutageReports)

    def addOutageReports(self, *OutageReports):
        for obj in OutageReports:
            obj.OutageHistory = self

    def removeOutageReports(self, *OutageReports):
        for obj in OutageReports:
            obj.OutageHistory = None


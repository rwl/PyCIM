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

class IncidentCode(IdentifiedObject):
    """Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in association end 'Names'.Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in association end 'Names'.
    """

    def __init__(self, subCode='', IncidentRecords=None, *args, **kw_args):
        """Initialises a new 'IncidentCode' instance.

        @param subCode: Additional level of classification detail (as extension to the main code found in association to Name). 
        @param IncidentRecords:
        """
        #: Additional level of classification detail (as extension to the main code found in association to Name).
        self.subCode = subCode

        self._IncidentRecords = []
        self.IncidentRecords = [] if IncidentRecords is None else IncidentRecords

        super(IncidentCode, self).__init__(*args, **kw_args)

    _attrs = ["subCode"]
    _attr_types = {"subCode": str}
    _defaults = {"subCode": ''}
    _enums = {}
    _refs = ["IncidentRecords"]
    _many_refs = ["IncidentRecords"]

    def getIncidentRecords(self):
        
        return self._IncidentRecords

    def setIncidentRecords(self, value):
        for p in self._IncidentRecords:
            filtered = [q for q in p.IncidentCodes if q != self]
            self._IncidentRecords._IncidentCodes = filtered
        for r in value:
            if self not in r._IncidentCodes:
                r._IncidentCodes.append(self)
        self._IncidentRecords = value

    IncidentRecords = property(getIncidentRecords, setIncidentRecords)

    def addIncidentRecords(self, *IncidentRecords):
        for obj in IncidentRecords:
            if self not in obj._IncidentCodes:
                obj._IncidentCodes.append(self)
            self._IncidentRecords.append(obj)

    def removeIncidentRecords(self, *IncidentRecords):
        for obj in IncidentRecords:
            if self in obj._IncidentCodes:
                obj._IncidentCodes.remove(self)
            self._IncidentRecords.remove(obj)


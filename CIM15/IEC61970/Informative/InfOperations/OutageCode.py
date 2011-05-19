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

class OutageCode(IdentifiedObject):
    """Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in 'OutageRecord.outageType'. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical outage code is in the inherited association to Name. The code is described in the inherited 'description' attribute.Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in 'OutageRecord.outageType'. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical outage code is in the inherited association to Name. The code is described in the inherited 'description' attribute.
    """

    def __init__(self, subCode='', OutageRecords=None, OutageSteps=None, *args, **kw_args):
        """Initialises a new 'OutageCode' instance.

        @param subCode: The main code is stored in the inherited association to Name. This sub-code provides an additional level of classification detail. 
        @param OutageRecords:
        @param OutageSteps:
        """
        #: The main code is stored in the inherited association to Name. This sub-code provides an additional level of classification detail.
        self.subCode = subCode

        self._OutageRecords = []
        self.OutageRecords = [] if OutageRecords is None else OutageRecords

        self._OutageSteps = []
        self.OutageSteps = [] if OutageSteps is None else OutageSteps

        super(OutageCode, self).__init__(*args, **kw_args)

    _attrs = ["subCode"]
    _attr_types = {"subCode": str}
    _defaults = {"subCode": ''}
    _enums = {}
    _refs = ["OutageRecords", "OutageSteps"]
    _many_refs = ["OutageRecords", "OutageSteps"]

    def getOutageRecords(self):
        
        return self._OutageRecords

    def setOutageRecords(self, value):
        for p in self._OutageRecords:
            filtered = [q for q in p.OutageCodes if q != self]
            self._OutageRecords._OutageCodes = filtered
        for r in value:
            if self not in r._OutageCodes:
                r._OutageCodes.append(self)
        self._OutageRecords = value

    OutageRecords = property(getOutageRecords, setOutageRecords)

    def addOutageRecords(self, *OutageRecords):
        for obj in OutageRecords:
            if self not in obj._OutageCodes:
                obj._OutageCodes.append(self)
            self._OutageRecords.append(obj)

    def removeOutageRecords(self, *OutageRecords):
        for obj in OutageRecords:
            if self in obj._OutageCodes:
                obj._OutageCodes.remove(self)
            self._OutageRecords.remove(obj)

    def getOutageSteps(self):
        
        return self._OutageSteps

    def setOutageSteps(self, value):
        for p in self._OutageSteps:
            filtered = [q for q in p.OutageCodes if q != self]
            self._OutageSteps._OutageCodes = filtered
        for r in value:
            if self not in r._OutageCodes:
                r._OutageCodes.append(self)
        self._OutageSteps = value

    OutageSteps = property(getOutageSteps, setOutageSteps)

    def addOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            if self not in obj._OutageCodes:
                obj._OutageCodes.append(self)
            self._OutageSteps.append(obj)

    def removeOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            if self in obj._OutageCodes:
                obj._OutageCodes.remove(self)
            self._OutageSteps.remove(obj)


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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class OutageCode(IdentifiedObject):
    """Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in OutageRecord.outageType. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical 'outage code' is in the inherited 'name' attribute. The code is described in the inherited 'description' attribute.
    """

    def __init__(self, subCode='', OutageRecords=None, OutageSteps=None, *args, **kw_args):
        """Initializes a new 'OutageCode' instance.

        @param subCode: The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail. 
        @param OutageRecords:
        @param OutageSteps:
        """
        #: The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail. 
        self.subCode = subCode

        self._OutageRecords = []
        self.OutageRecords = [] if OutageRecords is None else OutageRecords

        self._OutageSteps = []
        self.OutageSteps = [] if OutageSteps is None else OutageSteps

        super(OutageCode, self).__init__(*args, **kw_args)

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


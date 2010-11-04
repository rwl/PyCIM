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

class IncidentCode(IdentifiedObject):
    """Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in 'name'.
    """

    def __init__(self, subCode='', IncidentRecords=None, *args, **kw_args):
        """Initializes a new 'IncidentCode' instance.

        @param subCode: Additional level of classification detail (as extension to the main code found in 'name'). 
        @param IncidentRecords:
        """
        #: Additional level of classification detail (as extension to the main code found in 'name').
        self.subCode = subCode

        self._IncidentRecords = []
        self.IncidentRecords = [] if IncidentRecords is None else IncidentRecords

        super(IncidentCode, self).__init__(*args, **kw_args)

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


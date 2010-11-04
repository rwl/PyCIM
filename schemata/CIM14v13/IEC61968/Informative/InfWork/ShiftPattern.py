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

class ShiftPattern(IdentifiedObject):
    """The patterns of shifts worked by people or crews.
    """

    def __init__(self, cycleCount=0, assignmentType='', validityInterval=None, Crews=None, status=None, **kw_args):
        """Initializes a new 'ShiftPattern' instance.

        @param cycleCount: Number of cycles for a temporary shift. 
        @param assignmentType: Type of assignement intended to be worked on this shift, for example, temporary, standard, etc. 
        @param validityInterval: Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
        @param Crews:
        @param status:
        """
        #: Number of cycles for a temporary shift.
        self.cycleCount = cycleCount

        #: Type of assignement intended to be worked on this shift, for example, temporary, standard, etc.
        self.assignmentType = assignmentType

        self.validityInterval = validityInterval

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.status = status

        super(ShiftPattern, self).__init__(**kw_args)

    # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
    validityInterval = None

    def getCrews(self):
        
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.ShiftPatterns if q != self]
            self._Crews._ShiftPatterns = filtered
        for r in value:
            if self not in r._ShiftPatterns:
                r._ShiftPatterns.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._ShiftPatterns:
                obj._ShiftPatterns.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._ShiftPatterns:
                obj._ShiftPatterns.remove(self)
            self._Crews.remove(obj)

    status = None


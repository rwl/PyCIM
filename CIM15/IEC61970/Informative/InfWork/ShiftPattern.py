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

class ShiftPattern(IdentifiedObject):
    """The patterns of shifts worked by people or crews.The patterns of shifts worked by people or crews.
    """

    def __init__(self, cycleCount=0, assignmentType='', Crews=None, status=None, validityInterval=None, *args, **kw_args):
        """Initialises a new 'ShiftPattern' instance.

        @param cycleCount: Number of cycles for a temporary shift. 
        @param assignmentType: Type of assignement intended to be worked on this shift, for example, temporary, standard, etc. 
        @param Crews:
        @param status:
        @param validityInterval: Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
        """
        #: Number of cycles for a temporary shift.
        self.cycleCount = cycleCount

        #: Type of assignement intended to be worked on this shift, for example, temporary, standard, etc.
        self.assignmentType = assignmentType

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.status = status

        self.validityInterval = validityInterval

        super(ShiftPattern, self).__init__(*args, **kw_args)

    _attrs = ["cycleCount", "assignmentType"]
    _attr_types = {"cycleCount": int, "assignmentType": str}
    _defaults = {"cycleCount": 0, "assignmentType": ''}
    _enums = {}
    _refs = ["Crews", "status", "validityInterval"]
    _many_refs = ["Crews"]

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

    # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
    validityInterval = None


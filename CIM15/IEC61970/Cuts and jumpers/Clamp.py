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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class Clamp(ConductingEquipment):
    """A Clamp is a galvanic connection at a line segment where other equipment is connected. A Clamp does not cut the line segment.  A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode. Any other ConductingEquipment can be connected to the Clamp ConnectivityNode.A Clamp is a galvanic connection at a line segment where other equipment is connected. A Clamp does not cut the line segment.  A Clamp is ConductingEquipment and has one Terminal with an associated ConnectivityNode. Any other ConductingEquipment can be connected to the Clamp ConnectivityNode.
    """

    def __init__(self, lengthFromTerminal1=0.0, ACLineSegment=None, *args, **kw_args):
        """Initialises a new 'Clamp' instance.

        @param lengthFromTerminal1: The length to the place where the cut is located starting from side one of the cut line segment, i.e. the line segment Terminal with sequenceNumber = 1. 
        @param ACLineSegment:
        """
        #: The length to the place where the cut is located starting from side one of the cut line segment, i.e. the line segment Terminal with sequenceNumber = 1.
        self.lengthFromTerminal1 = lengthFromTerminal1

        self._ACLineSegment = None
        self.ACLineSegment = ACLineSegment

        super(Clamp, self).__init__(*args, **kw_args)

    _attrs = ["lengthFromTerminal1"]
    _attr_types = {"lengthFromTerminal1": float}
    _defaults = {"lengthFromTerminal1": 0.0}
    _enums = {}
    _refs = ["ACLineSegment"]
    _many_refs = []

    def getACLineSegment(self):
        
        return self._ACLineSegment

    def setACLineSegment(self, value):
        if self._ACLineSegment is not None:
            filtered = [x for x in self.ACLineSegment.Clamp if x != self]
            self._ACLineSegment._Clamp = filtered

        self._ACLineSegment = value
        if self._ACLineSegment is not None:
            if self not in self._ACLineSegment._Clamp:
                self._ACLineSegment._Clamp.append(self)

    ACLineSegment = property(getACLineSegment, setACLineSegment)


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

from CIM15.IEC61970.Wires.Switch import Switch

class Cut(Switch):
    """A Cut separates a line segment into two parts. The Cut appears as a Switch inserted between these two parts and connects them together. As the Cut is normally &ldquo;open&rdquo; there is no galvanic connection between the two line segment parts. But it is possible to 'close' the Cut to get galvanic connection. The Cut Terminals are oriented towards the line segment Terminals with the same sequenceNumber. Hence the Cut Terminal with sequenceNumber=1 is oriented to the line segment with Terminal.sequenceNumber=1. The Cut Terminals also act as connection points for jumpers and other equipment, e.g. a mobile generator. To enable this ConnectivityNoces are placed at the Cut Terminals. Once the ConnectivityNodes are in place any ConductingEquipment can be connected at them.A Cut separates a line segment into two parts. The Cut appears as a Switch inserted between these two parts and connects them together. As the Cut is normally &ldquo;open&rdquo; there is no galvanic connection between the two line segment parts. But it is possible to 'close' the Cut to get galvanic connection. The Cut Terminals are oriented towards the line segment Terminals with the same sequenceNumber. Hence the Cut Terminal with sequenceNumber=1 is oriented to the line segment with Terminal.sequenceNumber=1. The Cut Terminals also act as connection points for jumpers and other equipment, e.g. a mobile generator. To enable this ConnectivityNoces are placed at the Cut Terminals. Once the ConnectivityNodes are in place any ConductingEquipment can be connected at them.
    """

    def __init__(self, lengthFromTerminal1=0.0, ACLineSegment=None, *args, **kw_args):
        """Initialises a new 'Cut' instance.

        @param lengthFromTerminal1: The length to the place where the cut is located starting from side one of the cut line segment, i.e. the line segment Terminal with sequenceNumber = 1. 
        @param ACLineSegment:
        """
        #: The length to the place where the cut is located starting from side one of the cut line segment, i.e. the line segment Terminal with sequenceNumber = 1.
        self.lengthFromTerminal1 = lengthFromTerminal1

        self._ACLineSegment = None
        self.ACLineSegment = ACLineSegment

        super(Cut, self).__init__(*args, **kw_args)

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
            filtered = [x for x in self.ACLineSegment.Cut if x != self]
            self._ACLineSegment._Cut = filtered

        self._ACLineSegment = value
        if self._ACLineSegment is not None:
            if self not in self._ACLineSegment._Cut:
                self._ACLineSegment._Cut.append(self)

    ACLineSegment = property(getACLineSegment, setACLineSegment)


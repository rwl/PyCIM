# Copyright (C) 2017 Emily Ma
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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource


class ACLineSegmentPhase(PowerSystemResource):

    def __init__(self, phase=None, ACLineSegment=None, *args, **kw_args):
        """Initialises a new 'ACLineSegmentPhase' instance.

        @param phase: 'A', 'B', 'C', 'N'
        @param ACLineSegment:
        """

        self.phase = phase
        self._ACLineSegment = None
        self.ACLineSegment = ACLineSegment

        super(ACLineSegmentPhase, self).__init__(*args, **kw_args)

    _attrs = ["phase"]
    _attr_types = {"phase": str}
    _defaults = {"phase": "C"}
    _enums = {"phase": "SinglePhaseKind"}
    _refs = ["ACLineSegment"]
    _many_refs = []

    def getACLineSegment(self):
        return self._ACLineSegment

    def setACLineSegment(self, value):
        if self._ACLineSegment is not None:
            filtered = [x for x in self.ACLineSegment.ACLineSegmentPhases if x != self]
            self._ACLineSegment._ACLineSegmentPhases = filtered

        self._ACLineSegment = value
        if self._ACLineSegment is not None:
            if self not in self._ACLineSegment._ACLineSegmentPhases:
                self._ACLineSegment._ACLineSegmentPhases.append(self)

    ACLineSegment = property(getACLineSegment, setACLineSegment)

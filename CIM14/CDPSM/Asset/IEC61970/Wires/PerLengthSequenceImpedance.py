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

from CIM15.CDPSM.Asset.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PerLengthSequenceImpedance(IdentifiedObject):
    """Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.
    """

    def __init__(self, LineSegments=None, *args, **kw_args):
        """Initialises a new 'PerLengthSequenceImpedance' instance.

        @param LineSegments: All line segments described by this sequence impedance.
        """
        self._LineSegments = []
        self.LineSegments = [] if LineSegments is None else LineSegments

        super(PerLengthSequenceImpedance, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LineSegments"]
    _many_refs = ["LineSegments"]

    def getLineSegments(self):
        """All line segments described by this sequence impedance.
        """
        return self._LineSegments

    def setLineSegments(self, value):
        for x in self._LineSegments:
            x.SequenceImpedance = None
        for y in value:
            y._SequenceImpedance = self
        self._LineSegments = value

    LineSegments = property(getLineSegments, setLineSegments)

    def addLineSegments(self, *LineSegments):
        for obj in LineSegments:
            obj.SequenceImpedance = self

    def removeLineSegments(self, *LineSegments):
        for obj in LineSegments:
            obj.SequenceImpedance = None


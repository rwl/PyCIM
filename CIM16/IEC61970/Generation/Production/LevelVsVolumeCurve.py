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

from CIM16.IEC61970.Core.Curve import Curve

class LevelVsVolumeCurve(Curve):
    """Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.
    """

    def __init__(self, Reservoir=None, *args, **kw_args):
        """Initialises a new 'LevelVsVolumeCurve' instance.

        @param Reservoir: A reservoir may have a level versus volume relationship.
        """
        self._Reservoir = None
        self.Reservoir = Reservoir

        super(LevelVsVolumeCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Reservoir"]
    _many_refs = []

    def getReservoir(self):
        """A reservoir may have a level versus volume relationship.
        """
        return self._Reservoir

    def setReservoir(self, value):
        if self._Reservoir is not None:
            filtered = [x for x in self.Reservoir.LevelVsVolumeCurves if x != self]
            self._Reservoir._LevelVsVolumeCurves = filtered

        self._Reservoir = value
        if self._Reservoir is not None:
            if self not in self._Reservoir._LevelVsVolumeCurves:
                self._Reservoir._LevelVsVolumeCurves.append(self)

    Reservoir = property(getReservoir, setReservoir)


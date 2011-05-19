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

from CIM15.Element import Element

class PhaseTapChangerTabularPoint(Element):
    """PhaseTapChangerTabularPoint describe each tap step in the curve.PhaseTapChangerTabularPoint describe each tap step in the curve.
    """

    def __init__(self, x=0.0, step=0, angle=0.0, PhaseTapChangerTabular=None, *args, **kw_args):
        """Initialises a new 'PhaseTapChangerTabularPoint' instance.

        @param x: The reactance deviation in percent of nominal value. The actual reactance is calculated as follows xcal = xnom(1 + x/100). 
        @param step: The tap step. 
        @param angle: The angle difference in degrees. 
        @param PhaseTapChangerTabular:
        """
        #: The reactance deviation in percent of nominal value. The actual reactance is calculated as follows xcal = xnom(1 + x/100).
        self.x = x

        #: The tap step.
        self.step = step

        #: The angle difference in degrees.
        self.angle = angle

        self._PhaseTapChangerTabular = None
        self.PhaseTapChangerTabular = PhaseTapChangerTabular

        super(PhaseTapChangerTabularPoint, self).__init__(*args, **kw_args)

    _attrs = ["x", "step", "angle"]
    _attr_types = {"x": float, "step": int, "angle": float}
    _defaults = {"x": 0.0, "step": 0, "angle": 0.0}
    _enums = {}
    _refs = ["PhaseTapChangerTabular"]
    _many_refs = []

    def getPhaseTapChangerTabular(self):
        
        return self._PhaseTapChangerTabular

    def setPhaseTapChangerTabular(self, value):
        if self._PhaseTapChangerTabular is not None:
            filtered = [x for x in self.PhaseTapChangerTabular.PhaseTapChangerTabularPoint if x != self]
            self._PhaseTapChangerTabular._PhaseTapChangerTabularPoint = filtered

        self._PhaseTapChangerTabular = value
        if self._PhaseTapChangerTabular is not None:
            if self not in self._PhaseTapChangerTabular._PhaseTapChangerTabularPoint:
                self._PhaseTapChangerTabular._PhaseTapChangerTabularPoint.append(self)

    PhaseTapChangerTabular = property(getPhaseTapChangerTabular, setPhaseTapChangerTabular)


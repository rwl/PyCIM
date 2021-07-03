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

from CIM16.Element import Element

class RatioTapChangerTabularPoint(Element):
    """RatioTapChangerTabularPoint describe each tap step in the curve.RatioTapChangerTabularPoint describe each tap step in the curve.
    """

    def __init__(self, x=0.0, ratio=0.0, step=0, RatioTapChangerTabular=None, *args, **kw_args):
        """Initialises a new 'RatioTapChangerTabularPoint' instance.

        @param x: The reactance deviation in percent of nominal value. The actual reactance is calculated as follows xcal = xnom(1 + x/100). 
        @param ratio: The voltage ratio in per unit. Hence this is a value close to one. 
        @param step: The tap step. 
        @param RatioTapChangerTabular:
        """
        #: The reactance deviation in percent of nominal value. The actual reactance is calculated as follows xcal = xnom(1 + x/100).
        self.x = x

        #: The voltage ratio in per unit. Hence this is a value close to one.
        self.ratio = ratio

        #: The tap step.
        self.step = step

        self._RatioTapChangerTabular = None
        self.RatioTapChangerTabular = RatioTapChangerTabular

        super(RatioTapChangerTabularPoint, self).__init__(*args, **kw_args)

    _attrs = ["x", "ratio", "step"]
    _attr_types = {"x": float, "ratio": float, "step": int}
    _defaults = {"x": 0.0, "ratio": 0.0, "step": 0}
    _enums = {}
    _refs = ["RatioTapChangerTabular"]
    _many_refs = []

    def getRatioTapChangerTabular(self):
        
        return self._RatioTapChangerTabular

    def setRatioTapChangerTabular(self, value):
        if self._RatioTapChangerTabular is not None:
            filtered = [x for x in self.RatioTapChangerTabular.RatioTapChangerTabularPoint if x != self]
            self._RatioTapChangerTabular._RatioTapChangerTabularPoint = filtered

        self._RatioTapChangerTabular = value
        if self._RatioTapChangerTabular is not None:
            if self not in self._RatioTapChangerTabular._RatioTapChangerTabularPoint:
                self._RatioTapChangerTabular._RatioTapChangerTabularPoint.append(self)

    RatioTapChangerTabular = property(getRatioTapChangerTabular, setRatioTapChangerTabular)


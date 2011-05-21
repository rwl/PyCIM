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

from CIM14.ENTSOE.Equipment.Element import Element

class CurveData(Element):
    """Multi-purpose data points for defining a curve.-  The CurveData class is used to represent points for various curves that derive from the Curve class.  The curves defined in this profile are:       GrossToNetActivePowerCurve      ReactiveCapabilityCurve  
    """

    def __init__(self, y1value=0.0, xvalue=0.0, y2value=0.0, Curve=None, *args, **kw_args):
        """Initialises a new 'CurveData' instance.

        @param y1value: The data value of the  first Y-axis variable, depending on the Y-axis units 
        @param xvalue: The data value of the X-axis variable,  depending on the X-axis units 
        @param y2value: The data value of the second Y-axis variable (if present), depending on the Y-axis units 
        @param Curve: The Curve defined by this CurveData.
        """
        #: The data value of the  first Y-axis variable, depending on the Y-axis units
        self.y1value = y1value

        #: The data value of the X-axis variable,  depending on the X-axis units
        self.xvalue = xvalue

        #: The data value of the second Y-axis variable (if present), depending on the Y-axis units
        self.y2value = y2value

        self._Curve = None
        self.Curve = Curve

        super(CurveData, self).__init__(*args, **kw_args)

    _attrs = ["y1value", "xvalue", "y2value"]
    _attr_types = {"y1value": float, "xvalue": float, "y2value": float}
    _defaults = {"y1value": 0.0, "xvalue": 0.0, "y2value": 0.0}
    _enums = {}
    _refs = ["Curve"]
    _many_refs = []

    def getCurve(self):
        """The Curve defined by this CurveData.
        """
        return self._Curve

    def setCurve(self, value):
        if self._Curve is not None:
            filtered = [x for x in self.Curve.CurveDatas if x != self]
            self._Curve._CurveDatas = filtered

        self._Curve = value
        if self._Curve is not None:
            if self not in self._Curve._CurveDatas:
                self._Curve._CurveDatas.append(self)

    Curve = property(getCurve, setCurve)


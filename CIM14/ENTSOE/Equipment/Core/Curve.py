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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.
    """

    def __init__(self, y1Unit="A", curveStyle="straightLineYValues", xUnit="A", CurveDatas=None, *args, **kw_args):
        """Initialises a new 'Curve' instance.

        @param y1Unit: The Y1-axis units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        @param curveStyle: The style or shape of the curve. Values are: "straightLineYValues", "rampYValue", "constantYValue", "formula"
        @param xUnit: The X-axis units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        @param CurveDatas: The point data values that define a curve
        """
        #: The Y1-axis units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        self.y1Unit = y1Unit

        #: The style or shape of the curve. Values are: "straightLineYValues", "rampYValue", "constantYValue", "formula"
        self.curveStyle = curveStyle

        #: The X-axis units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        self.xUnit = xUnit

        self._CurveDatas = []
        self.CurveDatas = [] if CurveDatas is None else CurveDatas

        super(Curve, self).__init__(*args, **kw_args)

    _attrs = ["y1Unit", "curveStyle", "xUnit"]
    _attr_types = {"y1Unit": str, "curveStyle": str, "xUnit": str}
    _defaults = {"y1Unit": "A", "curveStyle": "straightLineYValues", "xUnit": "A"}
    _enums = {"y1Unit": "UnitSymbol", "curveStyle": "CurveStyle", "xUnit": "UnitSymbol"}
    _refs = ["CurveDatas"]
    _many_refs = ["CurveDatas"]

    def getCurveDatas(self):
        """The point data values that define a curve
        """
        return self._CurveDatas

    def setCurveDatas(self, value):
        for x in self._CurveDatas:
            x.Curve = None
        for y in value:
            y._Curve = self
        self._CurveDatas = value

    CurveDatas = property(getCurveDatas, setCurveDatas)

    def addCurveDatas(self, *CurveDatas):
        for obj in CurveDatas:
            obj.Curve = self

    def removeCurveDatas(self, *CurveDatas):
        for obj in CurveDatas:
            obj.Curve = None


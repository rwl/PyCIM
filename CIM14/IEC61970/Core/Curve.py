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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.
    """

    def __init__(self, y2Multiplier="k", y3Multiplier="k", y1Unit="N", xMultiplier="k", y3Unit="N", xUnit="N", y1Multiplier="k", curveStyle="rampYValue", y2Unit="N", CurveDatas=None, *args, **kw_args):
        """Initialises a new 'Curve' instance.

        @param y2Multiplier: Multiplier for Y2-axis. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param y3Multiplier: Multiplier for Y3-axis. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param y1Unit: The Y1-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param xMultiplier: Multiplier for X-axis. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param y3Unit: The Y3-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param xUnit: The X-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param y1Multiplier: Multiplier for Y1-axis Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param curveStyle: The style or shape of the curve. Values are: "rampYValue", "straightLineYValues", "formula", "constantYValue"
        @param y2Unit: The Y2-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param CurveDatas: The point data values that define a curve
        """
        #: Multiplier for Y2-axis. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.y2Multiplier = y2Multiplier

        #: Multiplier for Y3-axis. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.y3Multiplier = y3Multiplier

        #: The Y1-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.y1Unit = y1Unit

        #: Multiplier for X-axis. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.xMultiplier = xMultiplier

        #: The Y3-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.y3Unit = y3Unit

        #: The X-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.xUnit = xUnit

        #: Multiplier for Y1-axis Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.y1Multiplier = y1Multiplier

        #: The style or shape of the curve. Values are: "rampYValue", "straightLineYValues", "formula", "constantYValue"
        self.curveStyle = curveStyle

        #: The Y2-axis units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.y2Unit = y2Unit

        self._CurveDatas = []
        self.CurveDatas = [] if CurveDatas is None else CurveDatas

        super(Curve, self).__init__(*args, **kw_args)

    _attrs = ["y2Multiplier", "y3Multiplier", "y1Unit", "xMultiplier", "y3Unit", "xUnit", "y1Multiplier", "curveStyle", "y2Unit"]
    _attr_types = {"y2Multiplier": str, "y3Multiplier": str, "y1Unit": str, "xMultiplier": str, "y3Unit": str, "xUnit": str, "y1Multiplier": str, "curveStyle": str, "y2Unit": str}
    _defaults = {"y2Multiplier": "k", "y3Multiplier": "k", "y1Unit": "N", "xMultiplier": "k", "y3Unit": "N", "xUnit": "N", "y1Multiplier": "k", "curveStyle": "rampYValue", "y2Unit": "N"}
    _enums = {"y2Multiplier": "UnitMultiplier", "y3Multiplier": "UnitMultiplier", "y1Unit": "UnitSymbol", "xMultiplier": "UnitMultiplier", "y3Unit": "UnitSymbol", "xUnit": "UnitSymbol", "y1Multiplier": "UnitMultiplier", "curveStyle": "CurveStyle", "y2Unit": "UnitSymbol"}
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


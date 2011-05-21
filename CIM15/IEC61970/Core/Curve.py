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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.
    """

    def __init__(self, xUnit="N", y1Multiplier="M", y2Unit="N", y3Multiplier="M", y1Unit="N", xMultiplier="M", y3Unit="N", y2Multiplier="M", curveStyle="formula", CurveDatas=None, *args, **kw_args):
        """Initialises a new 'Curve' instance.

        @param xUnit: The X-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param y1Multiplier: Multiplier for Y1-axis Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param y2Unit: The Y2-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param y3Multiplier: Multiplier for Y3-axis. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param y1Unit: The Y1-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param xMultiplier: Multiplier for X-axis. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param y3Unit: The Y3-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param y2Multiplier: Multiplier for Y2-axis. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param curveStyle: The style or shape of the curve. Values are: "formula", "constantYValue", "straightLineYValues", "rampYValue"
        @param CurveDatas: The point data values that define a curve
        """
        #: The X-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.xUnit = xUnit

        #: Multiplier for Y1-axis Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.y1Multiplier = y1Multiplier

        #: The Y2-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.y2Unit = y2Unit

        #: Multiplier for Y3-axis. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.y3Multiplier = y3Multiplier

        #: The Y1-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.y1Unit = y1Unit

        #: Multiplier for X-axis. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.xMultiplier = xMultiplier

        #: The Y3-axis units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.y3Unit = y3Unit

        #: Multiplier for Y2-axis. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.y2Multiplier = y2Multiplier

        #: The style or shape of the curve. Values are: "formula", "constantYValue", "straightLineYValues", "rampYValue"
        self.curveStyle = curveStyle

        self._CurveDatas = []
        self.CurveDatas = [] if CurveDatas is None else CurveDatas

        super(Curve, self).__init__(*args, **kw_args)

    _attrs = ["xUnit", "y1Multiplier", "y2Unit", "y3Multiplier", "y1Unit", "xMultiplier", "y3Unit", "y2Multiplier", "curveStyle"]
    _attr_types = {"xUnit": str, "y1Multiplier": str, "y2Unit": str, "y3Multiplier": str, "y1Unit": str, "xMultiplier": str, "y3Unit": str, "y2Multiplier": str, "curveStyle": str}
    _defaults = {"xUnit": "N", "y1Multiplier": "M", "y2Unit": "N", "y3Multiplier": "M", "y1Unit": "N", "xMultiplier": "M", "y3Unit": "N", "y2Multiplier": "M", "curveStyle": "formula"}
    _enums = {"xUnit": "UnitSymbol", "y1Multiplier": "UnitMultiplier", "y2Unit": "UnitSymbol", "y3Multiplier": "UnitMultiplier", "y1Unit": "UnitSymbol", "xMultiplier": "UnitMultiplier", "y3Unit": "UnitSymbol", "y2Multiplier": "UnitMultiplier", "curveStyle": "CurveStyle"}
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


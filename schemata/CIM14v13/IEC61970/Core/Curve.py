# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Curve(IdentifiedObject):
    """A multi-purpose curve or functional relationship between an independent variable (X-axis) and dependent (Y-axis) variables.
    """

    def __init__(self, y3Multiplier='m', y2Multiplier='m', xMultiplier='m', y2Unit='m2', curveStyle='constantYValue', y1Unit='m2', y1Multiplier='m', y3Unit='m2', xUnit='m2', CurveDatas=None, *args, **kw_args):
        """Initializes a new 'Curve' instance.

        @param y3Multiplier: Multiplier for Y3-axis. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param y2Multiplier: Multiplier for Y2-axis. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param xMultiplier: Multiplier for X-axis. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param y2Unit: The Y2-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param curveStyle: The style or shape of the curve. Values are: "constantYValue", "rampYValue", "formula", "straightLineYValues"
        @param y1Unit: The Y1-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param y1Multiplier: Multiplier for Y1-axis Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param y3Unit: The Y3-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param xUnit: The X-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param CurveDatas: The point data values that define a curve
        """
        #: Multiplier for Y3-axis. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.y3Multiplier = y3Multiplier

        #: Multiplier for Y2-axis. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.y2Multiplier = y2Multiplier

        #: Multiplier for X-axis. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.xMultiplier = xMultiplier

        #: The Y2-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.y2Unit = y2Unit

        #: The style or shape of the curve. Values are: "constantYValue", "rampYValue", "formula", "straightLineYValues"
        self.curveStyle = curveStyle

        #: The Y1-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.y1Unit = y1Unit

        #: Multiplier for Y1-axis Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.y1Multiplier = y1Multiplier

        #: The Y3-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.y3Unit = y3Unit

        #: The X-axis units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.xUnit = xUnit

        self._CurveDatas = []
        self.CurveDatas = [] if CurveDatas is None else CurveDatas

        super(Curve, self).__init__(*args, **kw_args)

    def getCurveDatas(self):
        """The point data values that define a curve
        """
        return self._CurveDatas

    def setCurveDatas(self, value):
        for x in self._CurveDatas:
            x._Curve = None
        for y in value:
            y._Curve = self
        self._CurveDatas = value

    CurveDatas = property(getCurveDatas, setCurveDatas)

    def addCurveDatas(self, *CurveDatas):
        for obj in CurveDatas:
            obj._Curve = self
            self._CurveDatas.append(obj)

    def removeCurveDatas(self, *CurveDatas):
        for obj in CurveDatas:
            obj._Curve = None
            self._CurveDatas.remove(obj)


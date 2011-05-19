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

from CIM15.IEC61970.Core.Curve import Curve

class HeatInputCurve(Curve):
    """Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.
    """

    def __init__(self, isNetGrossP=False, heatInputEff=0.0, heatInputOffset=0.0, auxPowerOffset=0.0, auxPowerMult=0.0, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'HeatInputCurve' instance.

        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param heatInputEff: Heat input - efficiency multiplier adjustment factor. 
        @param heatInputOffset: Heat input - offset adjustment factor. 
        @param auxPowerOffset: Power output - auxiliary power offset adjustment factor 
        @param auxPowerMult: Power output - auxiliary power multiplier adjustment factor. 
        @param ThermalGeneratingUnit: A thermal generating unit may have a heat input curve
        """
        #: Flag is set to true when output is expressed in net active power
        self.isNetGrossP = isNetGrossP

        #: Heat input - efficiency multiplier adjustment factor.
        self.heatInputEff = heatInputEff

        #: Heat input - offset adjustment factor.
        self.heatInputOffset = heatInputOffset

        #: Power output - auxiliary power offset adjustment factor
        self.auxPowerOffset = auxPowerOffset

        #: Power output - auxiliary power multiplier adjustment factor.
        self.auxPowerMult = auxPowerMult

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(HeatInputCurve, self).__init__(*args, **kw_args)

    _attrs = ["isNetGrossP", "heatInputEff", "heatInputOffset", "auxPowerOffset", "auxPowerMult"]
    _attr_types = {"isNetGrossP": bool, "heatInputEff": float, "heatInputOffset": float, "auxPowerOffset": float, "auxPowerMult": float}
    _defaults = {"isNetGrossP": False, "heatInputEff": 0.0, "heatInputOffset": 0.0, "auxPowerOffset": 0.0, "auxPowerMult": 0.0}
    _enums = {}
    _refs = ["ThermalGeneratingUnit"]
    _many_refs = []

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a heat input curve
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._HeatInputCurve = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit.HeatInputCurve = None
            self._ThermalGeneratingUnit._HeatInputCurve = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)


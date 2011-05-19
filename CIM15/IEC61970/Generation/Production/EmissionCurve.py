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

class EmissionCurve(Curve):
    """Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.
    """

    def __init__(self, emissionContent=0.0, isNetGrossP=False, emissionType="carbonDisulfide", ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'EmissionCurve' instance.

        @param emissionContent: The emission content per quantity of fuel burned 
        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param emissionType: The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "carbonDisulfide", "sulfurDioxide", "hydrogenSulfide", "chlorine", "carbonDioxide", "nitrogenOxide"
        @param ThermalGeneratingUnit: A thermal generating unit may have  one or more emission curves
        """
        #: The emission content per quantity of fuel burned
        self.emissionContent = emissionContent

        #: Flag is set to true when output is expressed in net active power
        self.isNetGrossP = isNetGrossP

        #: The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "carbonDisulfide", "sulfurDioxide", "hydrogenSulfide", "chlorine", "carbonDioxide", "nitrogenOxide"
        self.emissionType = emissionType

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(EmissionCurve, self).__init__(*args, **kw_args)

    _attrs = ["emissionContent", "isNetGrossP", "emissionType"]
    _attr_types = {"emissionContent": float, "isNetGrossP": bool, "emissionType": str}
    _defaults = {"emissionContent": 0.0, "isNetGrossP": False, "emissionType": "carbonDisulfide"}
    _enums = {"emissionType": "EmissionType"}
    _refs = ["ThermalGeneratingUnit"]
    _many_refs = []

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have  one or more emission curves
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            filtered = [x for x in self.ThermalGeneratingUnit.EmissionCurves if x != self]
            self._ThermalGeneratingUnit._EmissionCurves = filtered

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            if self not in self._ThermalGeneratingUnit._EmissionCurves:
                self._ThermalGeneratingUnit._EmissionCurves.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)


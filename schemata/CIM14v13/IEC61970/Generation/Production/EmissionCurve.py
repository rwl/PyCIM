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

from CIM14v13.IEC61970.Core.Curve import Curve

class EmissionCurve(Curve):
    """Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.
    """

    def __init__(self, emissionType='nitrogenOxide', isNetGrossP=False, emissionContent=0.0, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'EmissionCurve' instance.

        @param emissionType: The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "nitrogenOxide", "carbonDisulfide", "hydrogenSulfide", "sulfurDioxide", "chlorine", "carbonDioxide"
        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param emissionContent: The emission content per quantity of fuel burned 
        @param ThermalGeneratingUnit: A thermal generating unit may have  one or more emission curves
        """
        #: The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "nitrogenOxide", "carbonDisulfide", "hydrogenSulfide", "sulfurDioxide", "chlorine", "carbonDioxide"
        self.emissionType = emissionType

        #: Flag is set to true when output is expressed in net active power 
        self.isNetGrossP = isNetGrossP

        #: The emission content per quantity of fuel burned 
        self.emissionContent = emissionContent

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(EmissionCurve, self).__init__(*args, **kw_args)

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
            self._ThermalGeneratingUnit._EmissionCurves.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)


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

from CIM14.IEC61970.Core.Curve import Curve

class EmissionAccount(Curve):
    """Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.
    """

    def __init__(self, emissionType="chlorine", emissionValueSource="measured", ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'EmissionAccount' instance.

        @param emissionType: The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "chlorine", "carbonDioxide", "hydrogenSulfide", "nitrogenOxide", "sulfurDioxide", "carbonDisulfide"
        @param emissionValueSource: The source of the emission value. Values are: "measured", "calculated"
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more emission allowance accounts
        """
        #: The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "chlorine", "carbonDioxide", "hydrogenSulfide", "nitrogenOxide", "sulfurDioxide", "carbonDisulfide"
        self.emissionType = emissionType

        #: The source of the emission value. Values are: "measured", "calculated"
        self.emissionValueSource = emissionValueSource

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(EmissionAccount, self).__init__(*args, **kw_args)

    _attrs = ["emissionType", "emissionValueSource"]
    _attr_types = {"emissionType": str, "emissionValueSource": str}
    _defaults = {"emissionType": "chlorine", "emissionValueSource": "measured"}
    _enums = {"emissionType": "EmissionType", "emissionValueSource": "EmissionValueSource"}
    _refs = ["ThermalGeneratingUnit"]
    _many_refs = []

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have one or more emission allowance accounts
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            filtered = [x for x in self.ThermalGeneratingUnit.EmmissionAccounts if x != self]
            self._ThermalGeneratingUnit._EmmissionAccounts = filtered

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            if self not in self._ThermalGeneratingUnit._EmmissionAccounts:
                self._ThermalGeneratingUnit._EmmissionAccounts.append(self)

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)


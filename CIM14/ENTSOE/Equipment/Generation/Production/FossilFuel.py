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

class FossilFuel(IdentifiedObject):
    """The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """

    def __init__(self, fossilFuelType="oil", ThermalGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'FossilFuel' instance.

        @param fossilFuelType: The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        @param ThermalGeneratingUnit: A thermal generating unit may have one or more fossil fuels
        """
        #: The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        self.fossilFuelType = fossilFuelType

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(FossilFuel, self).__init__(*args, **kw_args)

    _attrs = ["fossilFuelType"]
    _attr_types = {"fossilFuelType": str}
    _defaults = {"fossilFuelType": "oil"}
    _enums = {"fossilFuelType": "FuelType"}
    _refs = ["ThermalGeneratingUnit"]
    _many_refs = []

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have one or more fossil fuels
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._FossilFuels = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit.FossilFuels = None
            self._ThermalGeneratingUnit._FossilFuels = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)


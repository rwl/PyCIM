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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CombinedCyclePlant(PowerSystemResource):
    """A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiencyA set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency
    """

    def __init__(self, combCyclePlantRating=0.0, ThermalGeneratingUnits=None, *args, **kw_args):
        """Initialises a new 'CombinedCyclePlant' instance.

        @param combCyclePlantRating: The combined cycle plant's active power output rating 
        @param ThermalGeneratingUnits: A thermal generating unit may be a member of a combined cycle plant
        """
        #: The combined cycle plant's active power output rating
        self.combCyclePlantRating = combCyclePlantRating

        self._ThermalGeneratingUnits = []
        self.ThermalGeneratingUnits = [] if ThermalGeneratingUnits is None else ThermalGeneratingUnits

        super(CombinedCyclePlant, self).__init__(*args, **kw_args)

    _attrs = ["combCyclePlantRating"]
    _attr_types = {"combCyclePlantRating": float}
    _defaults = {"combCyclePlantRating": 0.0}
    _enums = {}
    _refs = ["ThermalGeneratingUnits"]
    _many_refs = ["ThermalGeneratingUnits"]

    def getThermalGeneratingUnits(self):
        """A thermal generating unit may be a member of a combined cycle plant
        """
        return self._ThermalGeneratingUnits

    def setThermalGeneratingUnits(self, value):
        for x in self._ThermalGeneratingUnits:
            x.CombinedCyclePlant = None
        for y in value:
            y._CombinedCyclePlant = self
        self._ThermalGeneratingUnits = value

    ThermalGeneratingUnits = property(getThermalGeneratingUnits, setThermalGeneratingUnits)

    def addThermalGeneratingUnits(self, *ThermalGeneratingUnits):
        for obj in ThermalGeneratingUnits:
            obj.CombinedCyclePlant = self

    def removeThermalGeneratingUnits(self, *ThermalGeneratingUnits):
        for obj in ThermalGeneratingUnits:
            obj.CombinedCyclePlant = None


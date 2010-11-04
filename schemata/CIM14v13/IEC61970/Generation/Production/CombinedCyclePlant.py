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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CombinedCyclePlant(PowerSystemResource):
    """A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency
    """

    def __init__(self, combCyclePlantRating=0.0, ThermalGeneratingUnits=None, **kw_args):
        """Initializes a new 'CombinedCyclePlant' instance.

        @param combCyclePlantRating: The combined cycle plant's active power output rating 
        @param ThermalGeneratingUnits: A thermal generating unit may be a member of a combined cycle plant
        """
        #: The combined cycle plant's active power output rating
        self.combCyclePlantRating = combCyclePlantRating

        self._ThermalGeneratingUnits = []
        self.ThermalGeneratingUnits = [] if ThermalGeneratingUnits is None else ThermalGeneratingUnits

        super(CombinedCyclePlant, self).__init__(**kw_args)

    def getThermalGeneratingUnits(self):
        """A thermal generating unit may be a member of a combined cycle plant
        """
        return self._ThermalGeneratingUnits

    def setThermalGeneratingUnits(self, value):
        for x in self._ThermalGeneratingUnits:
            x._CombinedCyclePlant = None
        for y in value:
            y._CombinedCyclePlant = self
        self._ThermalGeneratingUnits = value

    ThermalGeneratingUnits = property(getThermalGeneratingUnits, setThermalGeneratingUnits)

    def addThermalGeneratingUnits(self, *ThermalGeneratingUnits):
        for obj in ThermalGeneratingUnits:
            obj._CombinedCyclePlant = self
            self._ThermalGeneratingUnits.append(obj)

    def removeThermalGeneratingUnits(self, *ThermalGeneratingUnits):
        for obj in ThermalGeneratingUnits:
            obj._CombinedCyclePlant = None
            self._ThermalGeneratingUnits.remove(obj)


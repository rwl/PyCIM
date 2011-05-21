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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class PowerCutZone(PowerSystemResource):
    """An area or zone of the power system which is used for load shedding purposes.
    """

    def __init__(self, cutLevel1=0.0, cutLevel2=0.0, EnergyConsumers=None, *args, **kw_args):
        """Initialises a new 'PowerCutZone' instance.

        @param cutLevel1: First level (amount) of load to cut as a percentage of total zone load 
        @param cutLevel2: Second level (amount) of load to cut as a percentage of total zone load 
        @param EnergyConsumers: An energy consumer is assigned to a power cut zone
        """
        #: First level (amount) of load to cut as a percentage of total zone load
        self.cutLevel1 = cutLevel1

        #: Second level (amount) of load to cut as a percentage of total zone load
        self.cutLevel2 = cutLevel2

        self._EnergyConsumers = []
        self.EnergyConsumers = [] if EnergyConsumers is None else EnergyConsumers

        super(PowerCutZone, self).__init__(*args, **kw_args)

    _attrs = ["cutLevel1", "cutLevel2"]
    _attr_types = {"cutLevel1": float, "cutLevel2": float}
    _defaults = {"cutLevel1": 0.0, "cutLevel2": 0.0}
    _enums = {}
    _refs = ["EnergyConsumers"]
    _many_refs = ["EnergyConsumers"]

    def getEnergyConsumers(self):
        """An energy consumer is assigned to a power cut zone
        """
        return self._EnergyConsumers

    def setEnergyConsumers(self, value):
        for x in self._EnergyConsumers:
            x.PowerCutZone = None
        for y in value:
            y._PowerCutZone = self
        self._EnergyConsumers = value

    EnergyConsumers = property(getEnergyConsumers, setEnergyConsumers)

    def addEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj.PowerCutZone = self

    def removeEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj.PowerCutZone = None


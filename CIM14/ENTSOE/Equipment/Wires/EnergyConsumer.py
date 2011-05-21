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

from CIM14.ENTSOE.Equipment.Core.ConductingEquipment import ConductingEquipment

class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system model-  [R8.2] is satisfied by navigation to ConnectivityNode and Substation -  The definition of the real and reactive power injections for an EnergyConsumer can be done using different sets of attributes.  In the simplest case, the injections can be defined directly using only the attributes “pfixed” and “qfixed”. -  To specify conforming and nonconforming loads, the classes ConformLoad, NonConformLoad, or their subtypes should be used. -  The attributes defining the affect of voltage and frequency on the injection defined by an associated LoadResponseCharacteristic should be supplied, if they are available, but are not required. 
    """

    def __init__(self, pfixed=0.0, pfixedPct=0.0, qfixedPct=0.0, qfixed=0.0, LoadResponse=None, *args, **kw_args):
        """Initialises a new 'EnergyConsumer' instance.

        @param pfixed: Active power of the load that is a fixed quantity. 
        @param pfixedPct: Fixed active power as per cent of load group fixed active power 
        @param qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. 
        @param qfixed: Reactive power of the load that is a fixed quantity. 
        @param LoadResponse: The load response characteristic of this load.
        """
        #: Active power of the load that is a fixed quantity.
        self.pfixed = pfixed

        #: Fixed active power as per cent of load group fixed active power
        self.pfixedPct = pfixedPct

        #: Fixed reactive power as per cent of load group fixed reactive power.
        self.qfixedPct = qfixedPct

        #: Reactive power of the load that is a fixed quantity.
        self.qfixed = qfixed

        self._LoadResponse = None
        self.LoadResponse = LoadResponse

        super(EnergyConsumer, self).__init__(*args, **kw_args)

    _attrs = ["pfixed", "pfixedPct", "qfixedPct", "qfixed"]
    _attr_types = {"pfixed": float, "pfixedPct": float, "qfixedPct": float, "qfixed": float}
    _defaults = {"pfixed": 0.0, "pfixedPct": 0.0, "qfixedPct": 0.0, "qfixed": 0.0}
    _enums = {}
    _refs = ["LoadResponse"]
    _many_refs = []

    def getLoadResponse(self):
        """The load response characteristic of this load.
        """
        return self._LoadResponse

    def setLoadResponse(self, value):
        if self._LoadResponse is not None:
            filtered = [x for x in self.LoadResponse.EnergyConsumer if x != self]
            self._LoadResponse._EnergyConsumer = filtered

        self._LoadResponse = value
        if self._LoadResponse is not None:
            if self not in self._LoadResponse._EnergyConsumer:
                self._LoadResponse._EnergyConsumer.append(self)

    LoadResponse = property(getLoadResponse, setLoadResponse)


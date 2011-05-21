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

from CIM15.CDPSM.Connectivity.IEC61970.Wires.Conductor import Conductor

class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system. For symmetrical, transposed 3ph lines, it is sufficient to use ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment. If per lenght impedance data is available from a library of standard types, impedances and admittances can be calculated in one of the following ways: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model.
    """

    def __init__(self, BaseVoltage=None, *args, **kw_args):
        """Initialises a new 'ACLineSegment' instance.

        @param BaseVoltage: Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        super(ACLineSegment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BaseVoltage"]
    _many_refs = []

    def getBaseVoltage(self):
        """Use association to ConductingEquipment only when there is no VoltageLevel container used.
        """
        return self._BaseVoltage

    def setBaseVoltage(self, value):
        if self._BaseVoltage is not None:
            filtered = [x for x in self.BaseVoltage.ConductingEquipment if x != self]
            self._BaseVoltage._ConductingEquipment = filtered

        self._BaseVoltage = value
        if self._BaseVoltage is not None:
            if self not in self._BaseVoltage._ConductingEquipment:
                self._BaseVoltage._ConductingEquipment.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)


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

from CIM15.IEC61970.AuxiliaryEquipment.Sensor import Sensor

class PotentialTransformer(Sensor):
    """Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.
    """

    def __init__(self, nominalRatio=0.0, accuracyClass='', ptClass='', PTInfo=None, *args, **kw_args):
        """Initialises a new 'PotentialTransformer' instance.

        @param nominalRatio: Nominal ratio between the primary and secondary voltage. 
        @param accuracyClass: PT accuracy classification. 
        @param ptClass: PT classification. 
        @param PTInfo: Potential (voltage) transformer data.
        """
        #: Nominal ratio between the primary and secondary voltage.
        self.nominalRatio = nominalRatio

        #: PT accuracy classification.
        self.accuracyClass = accuracyClass

        #: PT classification.
        self.ptClass = ptClass

        self._PTInfo = None
        self.PTInfo = PTInfo

        super(PotentialTransformer, self).__init__(*args, **kw_args)

    _attrs = ["nominalRatio", "accuracyClass", "ptClass"]
    _attr_types = {"nominalRatio": float, "accuracyClass": str, "ptClass": str}
    _defaults = {"nominalRatio": 0.0, "accuracyClass": '', "ptClass": ''}
    _enums = {}
    _refs = ["PTInfo"]
    _many_refs = []

    def getPTInfo(self):
        """Potential (voltage) transformer data.
        """
        return self._PTInfo

    def setPTInfo(self, value):
        if self._PTInfo is not None:
            filtered = [x for x in self.PTInfo.PTs if x != self]
            self._PTInfo._PTs = filtered

        self._PTInfo = value
        if self._PTInfo is not None:
            if self not in self._PTInfo._PTs:
                self._PTInfo._PTs.append(self)

    PTInfo = property(getPTInfo, setPTInfo)


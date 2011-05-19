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

class CurrentTransformer(Sensor):
    """Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """

    def __init__(self, ctClass='', accuracyLimit='', usage='', accuracyClass='', coreCount=0, maxRatio=0.0, CTInfo=None, *args, **kw_args):
        """Initialises a new 'CurrentTransformer' instance.

        @param ctClass: CT classification; i.e. class 10P. 
        @param accuracyLimit: Percent of rated current for which the CT remains accurate within specified limits. 
        @param usage: Intended usage of the CT; i.e. metering, protection. 
        @param accuracyClass: CT accuracy classification. 
        @param coreCount: Number of cores. 
        @param maxRatio: For multi-ratio CT's, the maximum permissable ratio attainable. 
        @param CTInfo: Current transformer data.
        """
        #: CT classification; i.e. class 10P.
        self.ctClass = ctClass

        #: Percent of rated current for which the CT remains accurate within specified limits.
        self.accuracyLimit = accuracyLimit

        #: Intended usage of the CT; i.e. metering, protection.
        self.usage = usage

        #: CT accuracy classification.
        self.accuracyClass = accuracyClass

        #: Number of cores.
        self.coreCount = coreCount

        #: For multi-ratio CT's, the maximum permissable ratio attainable.
        self.maxRatio = maxRatio

        self._CTInfo = None
        self.CTInfo = CTInfo

        super(CurrentTransformer, self).__init__(*args, **kw_args)

    _attrs = ["ctClass", "accuracyLimit", "usage", "accuracyClass", "coreCount", "maxRatio"]
    _attr_types = {"ctClass": str, "accuracyLimit": str, "usage": str, "accuracyClass": str, "coreCount": int, "maxRatio": float}
    _defaults = {"ctClass": '', "accuracyLimit": '', "usage": '', "accuracyClass": '', "coreCount": 0, "maxRatio": 0.0}
    _enums = {}
    _refs = ["CTInfo"]
    _many_refs = []

    def getCTInfo(self):
        """Current transformer data.
        """
        return self._CTInfo

    def setCTInfo(self, value):
        if self._CTInfo is not None:
            filtered = [x for x in self.CTInfo.CTs if x != self]
            self._CTInfo._CTs = filtered

        self._CTInfo = value
        if self._CTInfo is not None:
            if self not in self._CTInfo._CTs:
                self._CTInfo._CTs.append(self)

    CTInfo = property(getCTInfo, setCTInfo)


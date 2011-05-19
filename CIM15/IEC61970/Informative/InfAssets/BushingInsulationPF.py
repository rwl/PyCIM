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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BushingInsulationPF(IdentifiedObject):
    """Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    """

    def __init__(self, testKind="c2", status=None, TransformerObservation=None, BushingInfo=None, *args, **kw_args):
        """Initialises a new 'BushingInsulationPF' instance.

        @param testKind: Kind of test for this bushing. Values are: "c2", "c1"
        @param status:
        @param TransformerObservation:
        @param BushingInfo:
        """
        #: Kind of test for this bushing. Values are: "c2", "c1"
        self.testKind = testKind

        self.status = status

        self._TransformerObservation = None
        self.TransformerObservation = TransformerObservation

        self._BushingInfo = None
        self.BushingInfo = BushingInfo

        super(BushingInsulationPF, self).__init__(*args, **kw_args)

    _attrs = ["testKind"]
    _attr_types = {"testKind": str}
    _defaults = {"testKind": "c2"}
    _enums = {"testKind": "BushingInsulationPfTestKind"}
    _refs = ["status", "TransformerObservation", "BushingInfo"]
    _many_refs = []

    status = None

    def getTransformerObservation(self):
        
        return self._TransformerObservation

    def setTransformerObservation(self, value):
        if self._TransformerObservation is not None:
            filtered = [x for x in self.TransformerObservation.BushingInsultationPFs if x != self]
            self._TransformerObservation._BushingInsultationPFs = filtered

        self._TransformerObservation = value
        if self._TransformerObservation is not None:
            if self not in self._TransformerObservation._BushingInsultationPFs:
                self._TransformerObservation._BushingInsultationPFs.append(self)

    TransformerObservation = property(getTransformerObservation, setTransformerObservation)

    def getBushingInfo(self):
        
        return self._BushingInfo

    def setBushingInfo(self, value):
        if self._BushingInfo is not None:
            filtered = [x for x in self.BushingInfo.BushingInsulationPFs if x != self]
            self._BushingInfo._BushingInsulationPFs = filtered

        self._BushingInfo = value
        if self._BushingInfo is not None:
            if self not in self._BushingInfo._BushingInsulationPFs:
                self._BushingInfo._BushingInsulationPFs.append(self)

    BushingInfo = property(getBushingInfo, setBushingInfo)


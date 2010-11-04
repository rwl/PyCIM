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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BushingInsulationPF(IdentifiedObject):
    """Bushing insulation power factor condition as a result of a test. Typical status values are: Acceptable, Minor Deterioration or Moisture Absorption, Major Deterioration or Moisture Absorption, Failed.
    """

    def __init__(self, testKind='c1', BushingAsset=None, TransformerObservation=None, status=None, **kw_args):
        """Initializes a new 'BushingInsulationPF' instance.

        @param testKind: Kind of test for this bushing. Values are: "c1", "c2"
        @param BushingAsset:
        @param TransformerObservation:
        @param status:
        """
        #: Kind of test for this bushing.Values are: "c1", "c2"
        self.testKind = testKind

        self._BushingAsset = None
        self.BushingAsset = BushingAsset

        self._TransformerObservation = None
        self.TransformerObservation = TransformerObservation

        self.status = status

        super(BushingInsulationPF, self).__init__(**kw_args)

    def getBushingAsset(self):
        
        return self._BushingAsset

    def setBushingAsset(self, value):
        if self._BushingAsset is not None:
            filtered = [x for x in self.BushingAsset.BushingInsulationPFs if x != self]
            self._BushingAsset._BushingInsulationPFs = filtered

        self._BushingAsset = value
        if self._BushingAsset is not None:
            self._BushingAsset._BushingInsulationPFs.append(self)

    BushingAsset = property(getBushingAsset, setBushingAsset)

    def getTransformerObservation(self):
        
        return self._TransformerObservation

    def setTransformerObservation(self, value):
        if self._TransformerObservation is not None:
            filtered = [x for x in self.TransformerObservation.BushingInsultationPFs if x != self]
            self._TransformerObservation._BushingInsultationPFs = filtered

        self._TransformerObservation = value
        if self._TransformerObservation is not None:
            self._TransformerObservation._BushingInsultationPFs.append(self)

    TransformerObservation = property(getTransformerObservation, setTransformerObservation)

    status = None


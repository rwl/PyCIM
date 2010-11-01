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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class PotentialTransformer(Equipment):
    """Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.
    """

    def __init__(self, accuracyClass='', ptClass='', nominalRatio=0.0, PotentialTransformerAsset=None, PotentialTransformerTypeAsset=None, *args, **kw_args):
        """Initializes a new 'PotentialTransformer' instance.

        @param accuracyClass: PT accuracy classification. 
        @param ptClass: PT classification. 
        @param nominalRatio: Nominal ratio between the primary and secondary voltage. 
        @param PotentialTransformerAsset:
        @param PotentialTransformerTypeAsset:
        """
        #: PT accuracy classification. 
        self.accuracyClass = accuracyClass

        #: PT classification. 
        self.ptClass = ptClass

        #: Nominal ratio between the primary and secondary voltage. 
        self.nominalRatio = nominalRatio

        self._PotentialTransformerAsset = None
        self.PotentialTransformerAsset = PotentialTransformerAsset

        self._PotentialTransformerTypeAsset = None
        self.PotentialTransformerTypeAsset = PotentialTransformerTypeAsset

        super(PotentialTransformer, self).__init__(*args, **kw_args)

    def getPotentialTransformerAsset(self):
        
        return self._PotentialTransformerAsset

    def setPotentialTransformerAsset(self, value):
        if self._PotentialTransformerAsset is not None:
            self._PotentialTransformerAsset._PotentialTransformer = None

        self._PotentialTransformerAsset = value
        if self._PotentialTransformerAsset is not None:
            self._PotentialTransformerAsset._PotentialTransformer = self

    PotentialTransformerAsset = property(getPotentialTransformerAsset, setPotentialTransformerAsset)

    def getPotentialTransformerTypeAsset(self):
        
        return self._PotentialTransformerTypeAsset

    def setPotentialTransformerTypeAsset(self, value):
        if self._PotentialTransformerTypeAsset is not None:
            filtered = [x for x in self.PotentialTransformerTypeAsset.PotentialTransformers if x != self]
            self._PotentialTransformerTypeAsset._PotentialTransformers = filtered

        self._PotentialTransformerTypeAsset = value
        if self._PotentialTransformerTypeAsset is not None:
            self._PotentialTransformerTypeAsset._PotentialTransformers.append(self)

    PotentialTransformerTypeAsset = property(getPotentialTransformerTypeAsset, setPotentialTransformerTypeAsset)


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

from CIM14v13.IEC61968.Assets.Asset import Asset

class ConductorAsset(Asset):
    """Physical asset used to perform the conductor's role.
    """

    def __init__(self, groundingMethod='', isHorizontal=False, insulated=False, CircuitSection=None, ConductorAssetModel=None, ConductorSegment=None, **kw_args):
        """Initializes a new 'ConductorAsset' instance.

        @param groundingMethod: Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other. 
        @param isHorizontal: True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service). 
        @param insulated: True if conductor asset has an insulator around the core material. 
        @param CircuitSection:
        @param ConductorAssetModel:
        @param ConductorSegment:
        """
        #: Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other.
        self.groundingMethod = groundingMethod

        #: True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service).
        self.isHorizontal = isHorizontal

        #: True if conductor asset has an insulator around the core material.
        self.insulated = insulated

        self._CircuitSection = None
        self.CircuitSection = CircuitSection

        self._ConductorAssetModel = None
        self.ConductorAssetModel = ConductorAssetModel

        self._ConductorSegment = None
        self.ConductorSegment = ConductorSegment

        super(ConductorAsset, self).__init__(**kw_args)

    def getCircuitSection(self):
        
        return self._CircuitSection

    def setCircuitSection(self, value):
        if self._CircuitSection is not None:
            filtered = [x for x in self.CircuitSection.ConductorAssets if x != self]
            self._CircuitSection._ConductorAssets = filtered

        self._CircuitSection = value
        if self._CircuitSection is not None:
            self._CircuitSection._ConductorAssets.append(self)

    CircuitSection = property(getCircuitSection, setCircuitSection)

    def getConductorAssetModel(self):
        
        return self._ConductorAssetModel

    def setConductorAssetModel(self, value):
        if self._ConductorAssetModel is not None:
            filtered = [x for x in self.ConductorAssetModel.ConductorAssets if x != self]
            self._ConductorAssetModel._ConductorAssets = filtered

        self._ConductorAssetModel = value
        if self._ConductorAssetModel is not None:
            self._ConductorAssetModel._ConductorAssets.append(self)

    ConductorAssetModel = property(getConductorAssetModel, setConductorAssetModel)

    def getConductorSegment(self):
        
        return self._ConductorSegment

    def setConductorSegment(self, value):
        if self._ConductorSegment is not None:
            filtered = [x for x in self.ConductorSegment.ConductorAssets if x != self]
            self._ConductorSegment._ConductorAssets = filtered

        self._ConductorSegment = value
        if self._ConductorSegment is not None:
            self._ConductorSegment._ConductorAssets.append(self)

    ConductorSegment = property(getConductorSegment, setConductorSegment)


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

class ConductorInfo(IdentifiedObject):
    """Conductor data.
    """

    def __init__(self, usage='secondary', insulationMaterial='highPressureFluidFilled', phaseCount=0, insulated=False, insulationThickness=0.0, ConductorSegments=None, ConductorAssetModel=None, WireArrangements=None, *args, **kw_args):
        """Initializes a new 'ConductorInfo' instance.

        @param usage: Usage of this conductor. Values are: "secondary", "transmission", "other", "distribution"
        @param insulationMaterial: (if insulated conductor) Material used for insulation. Values are: "highPressureFluidFilled", "lowCapacitanceRubber", "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "treeRetardantCrosslinkedPolyethylene", "oilPaper", "butyl", "beltedPilc", "rubber", "ethylenePropyleneRubber", "varnishedCambricCloth", "asbestosAndVarnishedCambric", "treeResistantHighMolecularWeightPolyethylene", "other", "siliconRubber", "unbeltedPilc", "varnishedDacronGlass"
        @param phaseCount: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        @param insulated: True if conductor is insulated. 
        @param insulationThickness: (if insulated conductor) Thickness of the insulation. 
        @param ConductorSegments: All conductor segments described by this conductor data.
        @param ConductorAssetModel:
        @param WireArrangements: All wire arrangements (single wires) that make this conductor.
        """
        #: Usage of this conductor. Values are: "secondary", "transmission", "other", "distribution"
        self.usage = usage

        #: (if insulated conductor) Material used for insulation. Values are: "highPressureFluidFilled", "lowCapacitanceRubber", "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "treeRetardantCrosslinkedPolyethylene", "oilPaper", "butyl", "beltedPilc", "rubber", "ethylenePropyleneRubber", "varnishedCambricCloth", "asbestosAndVarnishedCambric", "treeResistantHighMolecularWeightPolyethylene", "other", "siliconRubber", "unbeltedPilc", "varnishedDacronGlass"
        self.insulationMaterial = insulationMaterial

        #: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        self.phaseCount = phaseCount

        #: True if conductor is insulated. 
        self.insulated = insulated

        #: (if insulated conductor) Thickness of the insulation. 
        self.insulationThickness = insulationThickness

        self._ConductorSegments = []
        self.ConductorSegments = [] if ConductorSegments is None else ConductorSegments

        self._ConductorAssetModel = None
        self.ConductorAssetModel = ConductorAssetModel

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        super(ConductorInfo, self).__init__(*args, **kw_args)

    def getConductorSegments(self):
        """All conductor segments described by this conductor data.
        """
        return self._ConductorSegments

    def setConductorSegments(self, value):
        for x in self._ConductorSegments:
            x._ConductorInfo = None
        for y in value:
            y._ConductorInfo = self
        self._ConductorSegments = value

    ConductorSegments = property(getConductorSegments, setConductorSegments)

    def addConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj._ConductorInfo = self
            self._ConductorSegments.append(obj)

    def removeConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj._ConductorInfo = None
            self._ConductorSegments.remove(obj)

    def getConductorAssetModel(self):
        
        return self._ConductorAssetModel

    def setConductorAssetModel(self, value):
        if self._ConductorAssetModel is not None:
            self._ConductorAssetModel._ConductorInfo = None

        self._ConductorAssetModel = value
        if self._ConductorAssetModel is not None:
            self._ConductorAssetModel._ConductorInfo = self

    ConductorAssetModel = property(getConductorAssetModel, setConductorAssetModel)

    def getWireArrangements(self):
        """All wire arrangements (single wires) that make this conductor.
        """
        return self._WireArrangements

    def setWireArrangements(self, value):
        for x in self._WireArrangements:
            x._ConductorInfo = None
        for y in value:
            y._ConductorInfo = self
        self._WireArrangements = value

    WireArrangements = property(getWireArrangements, setWireArrangements)

    def addWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj._ConductorInfo = self
            self._WireArrangements.append(obj)

    def removeWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj._ConductorInfo = None
            self._WireArrangements.remove(obj)


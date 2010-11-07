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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ConductorInfo(IdentifiedObject):
    """Conductor data.
    """

    def __init__(self, usage='distribution', insulationMaterial='crosslinkedPolyethylene', insulated=False, insulationThickness=0.0, phaseCount=0, ConductorSegments=None, WireArrangements=None, **kw_args):
        """Initializes a new 'ConductorInfo' instance.

        @param usage: Usage of this conductor. Values are: "distribution", "secondary", "transmission", "other"
        @param insulationMaterial: (if insulated conductor) Material used for insulation. Values are: "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "unbeltedPilc", "treeRetardantCrosslinkedPolyethylene", "butyl", "rubber", "asbestosAndVarnishedCambric", "beltedPilc", "varnishedDacronGlass", "other", "treeResistantHighMolecularWeightPolyethylene", "lowCapacitanceRubber", "varnishedCambricCloth", "highPressureFluidFilled", "ethylenePropyleneRubber", "siliconRubber", "oilPaper"
        @param insulated: True if conductor is insulated. 
        @param insulationThickness: (if insulated conductor) Thickness of the insulation. 
        @param phaseCount: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        @param ConductorSegments: All conductor segments described by this conductor data.
        @param WireArrangements: All wire arrangements (single wires) that make this conductor.
        """
        #: Usage of this conductor.Values are: "distribution", "secondary", "transmission", "other"
        self.usage = usage

        #: (if insulated conductor) Material used for insulation.Values are: "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "unbeltedPilc", "treeRetardantCrosslinkedPolyethylene", "butyl", "rubber", "asbestosAndVarnishedCambric", "beltedPilc", "varnishedDacronGlass", "other", "treeResistantHighMolecularWeightPolyethylene", "lowCapacitanceRubber", "varnishedCambricCloth", "highPressureFluidFilled", "ethylenePropyleneRubber", "siliconRubber", "oilPaper"
        self.insulationMaterial = insulationMaterial

        #: True if conductor is insulated.
        self.insulated = insulated

        #: (if insulated conductor) Thickness of the insulation.
        self.insulationThickness = insulationThickness

        #: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.
        self.phaseCount = phaseCount

        self._ConductorSegments = []
        self.ConductorSegments = [] if ConductorSegments is None else ConductorSegments

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        super(ConductorInfo, self).__init__(**kw_args)

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


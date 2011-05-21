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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ConductorInfo(IdentifiedObject):
    """Conductor data.
    """

    def __init__(self, phaseCount=0, insulationMaterial="crosslinkedPolyethylene", insulationThickness=0.0, insulated=False, usage="secondary", WireArrangements=None, ConductorSegments=None, *args, **kw_args):
        """Initialises a new 'ConductorInfo' instance.

        @param phaseCount: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        @param insulationMaterial: (if insulated conductor) Material used for insulation. Values are: "crosslinkedPolyethylene", "butyl", "treeRetardantCrosslinkedPolyethylene", "asbestosAndVarnishedCambric", "highPressureFluidFilled", "ethylenePropyleneRubber", "ozoneResistantRubber", "oilPaper", "varnishedDacronGlass", "highMolecularWeightPolyethylene", "other", "varnishedCambricCloth", "treeResistantHighMolecularWeightPolyethylene", "unbeltedPilc", "beltedPilc", "rubber", "lowCapacitanceRubber", "siliconRubber"
        @param insulationThickness: (if insulated conductor) Thickness of the insulation. 
        @param insulated: True if conductor is insulated. 
        @param usage: Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        @param WireArrangements: All wire arrangements (single wires) that make this conductor.
        @param ConductorSegments: All conductor segments described by this conductor data.
        """
        #: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.
        self.phaseCount = phaseCount

        #: (if insulated conductor) Material used for insulation. Values are: "crosslinkedPolyethylene", "butyl", "treeRetardantCrosslinkedPolyethylene", "asbestosAndVarnishedCambric", "highPressureFluidFilled", "ethylenePropyleneRubber", "ozoneResistantRubber", "oilPaper", "varnishedDacronGlass", "highMolecularWeightPolyethylene", "other", "varnishedCambricCloth", "treeResistantHighMolecularWeightPolyethylene", "unbeltedPilc", "beltedPilc", "rubber", "lowCapacitanceRubber", "siliconRubber"
        self.insulationMaterial = insulationMaterial

        #: (if insulated conductor) Thickness of the insulation.
        self.insulationThickness = insulationThickness

        #: True if conductor is insulated.
        self.insulated = insulated

        #: Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        self.usage = usage

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        self._ConductorSegments = []
        self.ConductorSegments = [] if ConductorSegments is None else ConductorSegments

        super(ConductorInfo, self).__init__(*args, **kw_args)

    _attrs = ["phaseCount", "insulationMaterial", "insulationThickness", "insulated", "usage"]
    _attr_types = {"phaseCount": int, "insulationMaterial": str, "insulationThickness": float, "insulated": bool, "usage": str}
    _defaults = {"phaseCount": 0, "insulationMaterial": "crosslinkedPolyethylene", "insulationThickness": 0.0, "insulated": False, "usage": "secondary"}
    _enums = {"insulationMaterial": "ConductorInsulationKind", "usage": "ConductorUsageKind"}
    _refs = ["WireArrangements", "ConductorSegments"]
    _many_refs = ["WireArrangements", "ConductorSegments"]

    def getWireArrangements(self):
        """All wire arrangements (single wires) that make this conductor.
        """
        return self._WireArrangements

    def setWireArrangements(self, value):
        for x in self._WireArrangements:
            x.ConductorInfo = None
        for y in value:
            y._ConductorInfo = self
        self._WireArrangements = value

    WireArrangements = property(getWireArrangements, setWireArrangements)

    def addWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj.ConductorInfo = self

    def removeWireArrangements(self, *WireArrangements):
        for obj in WireArrangements:
            obj.ConductorInfo = None

    def getConductorSegments(self):
        """All conductor segments described by this conductor data.
        """
        return self._ConductorSegments

    def setConductorSegments(self, value):
        for x in self._ConductorSegments:
            x.ConductorInfo = None
        for y in value:
            y._ConductorInfo = self
        self._ConductorSegments = value

    ConductorSegments = property(getConductorSegments, setConductorSegments)

    def addConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj.ConductorInfo = self

    def removeConductorSegments(self, *ConductorSegments):
        for obj in ConductorSegments:
            obj.ConductorInfo = None


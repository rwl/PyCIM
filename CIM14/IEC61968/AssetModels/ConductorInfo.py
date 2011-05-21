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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ConductorInfo(IdentifiedObject):
    """Conductor data.
    """

    def __init__(self, usage="distribution", insulationMaterial="crosslinkedPolyethylene", insulated=False, insulationThickness=0.0, phaseCount=0, ConductorSegments=None, WireArrangements=None, *args, **kw_args):
        """Initialises a new 'ConductorInfo' instance.

        @param usage: Usage of this conductor. Values are: "distribution", "secondary", "transmission", "other"
        @param insulationMaterial: (if insulated conductor) Material used for insulation. Values are: "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "unbeltedPilc", "treeRetardantCrosslinkedPolyethylene", "butyl", "rubber", "asbestosAndVarnishedCambric", "beltedPilc", "varnishedDacronGlass", "other", "treeResistantHighMolecularWeightPolyethylene", "lowCapacitanceRubber", "varnishedCambricCloth", "highPressureFluidFilled", "ethylenePropyleneRubber", "siliconRubber", "oilPaper"
        @param insulated: True if conductor is insulated. 
        @param insulationThickness: (if insulated conductor) Thickness of the insulation. 
        @param phaseCount: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        @param ConductorSegments: All conductor segments described by this conductor data.
        @param WireArrangements: All wire arrangements (single wires) that make this conductor.
        """
        #: Usage of this conductor. Values are: "distribution", "secondary", "transmission", "other"
        self.usage = usage

        #: (if insulated conductor) Material used for insulation. Values are: "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "unbeltedPilc", "treeRetardantCrosslinkedPolyethylene", "butyl", "rubber", "asbestosAndVarnishedCambric", "beltedPilc", "varnishedDacronGlass", "other", "treeResistantHighMolecularWeightPolyethylene", "lowCapacitanceRubber", "varnishedCambricCloth", "highPressureFluidFilled", "ethylenePropyleneRubber", "siliconRubber", "oilPaper"
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

        super(ConductorInfo, self).__init__(*args, **kw_args)

    _attrs = ["usage", "insulationMaterial", "insulated", "insulationThickness", "phaseCount"]
    _attr_types = {"usage": str, "insulationMaterial": str, "insulated": bool, "insulationThickness": float, "phaseCount": int}
    _defaults = {"usage": "distribution", "insulationMaterial": "crosslinkedPolyethylene", "insulated": False, "insulationThickness": 0.0, "phaseCount": 0}
    _enums = {"usage": "ConductorUsageKind", "insulationMaterial": "ConductorInsulationKind"}
    _refs = ["ConductorSegments", "WireArrangements"]
    _many_refs = ["ConductorSegments", "WireArrangements"]

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


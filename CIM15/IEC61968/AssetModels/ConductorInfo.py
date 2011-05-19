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

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class ConductorInfo(AssetInfo):
    """Conductor data.Conductor data.
    """

    def __init__(self, insulated=False, usage="secondary", insulationMaterial="treeRetardantCrosslinkedPolyethylene", phaseCount=0, insulationThickness=0.0, WireArrangements=None, LineSegments=None, *args, **kw_args):
        """Initialises a new 'ConductorInfo' instance.

        @param insulated: True if conductor is insulated. 
        @param usage: Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        @param insulationMaterial: (if insulated conductor) Material used for insulation. Values are: "treeRetardantCrosslinkedPolyethylene", "butyl", "highPressureFluidFilled", "other", "varnishedCambricCloth", "siliconRubber", "beltedPilc", "crosslinkedPolyethylene", "oilPaper", "lowCapacitanceRubber", "asbestosAndVarnishedCambric", "treeResistantHighMolecularWeightPolyethylene", "unbeltedPilc", "ozoneResistantRubber", "ethylenePropyleneRubber", "highMolecularWeightPolyethylene", "varnishedDacronGlass", "rubber"
        @param phaseCount: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return. 
        @param insulationThickness: (if insulated conductor) Thickness of the insulation. 
        @param WireArrangements: All wire arrangements (single wires) that make this conductor.
        @param LineSegments: All line segments described by this conductor data.
        """
        #: True if conductor is insulated.
        self.insulated = insulated

        #: Usage of this conductor. Values are: "secondary", "other", "distribution", "transmission"
        self.usage = usage

        #: (if insulated conductor) Material used for insulation. Values are: "treeRetardantCrosslinkedPolyethylene", "butyl", "highPressureFluidFilled", "other", "varnishedCambricCloth", "siliconRubber", "beltedPilc", "crosslinkedPolyethylene", "oilPaper", "lowCapacitanceRubber", "asbestosAndVarnishedCambric", "treeResistantHighMolecularWeightPolyethylene", "unbeltedPilc", "ozoneResistantRubber", "ethylenePropyleneRubber", "highMolecularWeightPolyethylene", "varnishedDacronGlass", "rubber"
        self.insulationMaterial = insulationMaterial

        #: Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.
        self.phaseCount = phaseCount

        #: (if insulated conductor) Thickness of the insulation.
        self.insulationThickness = insulationThickness

        self._WireArrangements = []
        self.WireArrangements = [] if WireArrangements is None else WireArrangements

        self._LineSegments = []
        self.LineSegments = [] if LineSegments is None else LineSegments

        super(ConductorInfo, self).__init__(*args, **kw_args)

    _attrs = ["insulated", "usage", "insulationMaterial", "phaseCount", "insulationThickness"]
    _attr_types = {"insulated": bool, "usage": str, "insulationMaterial": str, "phaseCount": int, "insulationThickness": float}
    _defaults = {"insulated": False, "usage": "secondary", "insulationMaterial": "treeRetardantCrosslinkedPolyethylene", "phaseCount": 0, "insulationThickness": 0.0}
    _enums = {"usage": "ConductorUsageKind", "insulationMaterial": "ConductorInsulationKind"}
    _refs = ["WireArrangements", "LineSegments"]
    _many_refs = ["WireArrangements", "LineSegments"]

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

    def getLineSegments(self):
        """All line segments described by this conductor data.
        """
        return self._LineSegments

    def setLineSegments(self, value):
        for x in self._LineSegments:
            x.ConductorInfo = None
        for y in value:
            y._ConductorInfo = self
        self._LineSegments = value

    LineSegments = property(getLineSegments, setLineSegments)

    def addLineSegments(self, *LineSegments):
        for obj in LineSegments:
            obj.ConductorInfo = self

    def removeLineSegments(self, *LineSegments):
        for obj in LineSegments:
            obj.ConductorInfo = None


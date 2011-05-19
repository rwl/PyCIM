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

from CIM15.IEC61968.Assets.AssetContainer import AssetContainer

class Structure(AssetContainer):
    """Construction holding assets such as conductors, transformers, switchgear, etc.Construction holding assets such as conductors, transformers, switchgear, etc.
    """

    def __init__(self, ratedVoltage=0.0, fumigantAppliedDate='', weedRemovedDate='', removeWeed=False, height=0.0, fumigantName='', materialKind="wood", StructureSupportInfos=None, MountingConnections=None, *args, **kw_args):
        """Initialises a new 'Structure' instance.

        @param ratedVoltage: Maximum rated voltage of the equipment that can be mounted on/contained within the structure. 
        @param fumigantAppliedDate: Date fumigant was last applied. 
        @param weedRemovedDate: Date weed were last removed. 
        @param removeWeed: True if weeds are to be removed around asset. 
        @param height: Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions. 
        @param fumigantName: Name of fumigant. 
        @param materialKind: Material this structure is made of. Values are: "wood", "concrete", "steel", "other"
        @param StructureSupportInfos:
        @param MountingConnections:
        """
        #: Maximum rated voltage of the equipment that can be mounted on/contained within the structure.
        self.ratedVoltage = ratedVoltage

        #: Date fumigant was last applied.
        self.fumigantAppliedDate = fumigantAppliedDate

        #: Date weed were last removed.
        self.weedRemovedDate = weedRemovedDate

        #: True if weeds are to be removed around asset.
        self.removeWeed = removeWeed

        #: Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions.
        self.height = height

        #: Name of fumigant.
        self.fumigantName = fumigantName

        #: Material this structure is made of. Values are: "wood", "concrete", "steel", "other"
        self.materialKind = materialKind

        self._StructureSupportInfos = []
        self.StructureSupportInfos = [] if StructureSupportInfos is None else StructureSupportInfos

        self._MountingConnections = []
        self.MountingConnections = [] if MountingConnections is None else MountingConnections

        super(Structure, self).__init__(*args, **kw_args)

    _attrs = ["ratedVoltage", "fumigantAppliedDate", "weedRemovedDate", "removeWeed", "height", "fumigantName", "materialKind"]
    _attr_types = {"ratedVoltage": float, "fumigantAppliedDate": str, "weedRemovedDate": str, "removeWeed": bool, "height": float, "fumigantName": str, "materialKind": str}
    _defaults = {"ratedVoltage": 0.0, "fumigantAppliedDate": '', "weedRemovedDate": '', "removeWeed": False, "height": 0.0, "fumigantName": '', "materialKind": "wood"}
    _enums = {"materialKind": "StructureMaterialKind"}
    _refs = ["StructureSupportInfos", "MountingConnections"]
    _many_refs = ["StructureSupportInfos", "MountingConnections"]

    def getStructureSupportInfos(self):
        
        return self._StructureSupportInfos

    def setStructureSupportInfos(self, value):
        for x in self._StructureSupportInfos:
            x.SecuredStructure = None
        for y in value:
            y._SecuredStructure = self
        self._StructureSupportInfos = value

    StructureSupportInfos = property(getStructureSupportInfos, setStructureSupportInfos)

    def addStructureSupportInfos(self, *StructureSupportInfos):
        for obj in StructureSupportInfos:
            obj.SecuredStructure = self

    def removeStructureSupportInfos(self, *StructureSupportInfos):
        for obj in StructureSupportInfos:
            obj.SecuredStructure = None

    def getMountingConnections(self):
        
        return self._MountingConnections

    def setMountingConnections(self, value):
        for p in self._MountingConnections:
            filtered = [q for q in p.StructureInfos if q != self]
            self._MountingConnections._StructureInfos = filtered
        for r in value:
            if self not in r._StructureInfos:
                r._StructureInfos.append(self)
        self._MountingConnections = value

    MountingConnections = property(getMountingConnections, setMountingConnections)

    def addMountingConnections(self, *MountingConnections):
        for obj in MountingConnections:
            if self not in obj._StructureInfos:
                obj._StructureInfos.append(self)
            self._MountingConnections.append(obj)

    def removeMountingConnections(self, *MountingConnections):
        for obj in MountingConnections:
            if self in obj._StructureInfos:
                obj._StructureInfos.remove(self)
            self._MountingConnections.remove(obj)


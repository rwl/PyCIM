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

from CIM14v13.IEC61968.Assets.AssetContainer import AssetContainer

class Structure(AssetContainer):
    """Construction holding assets such as conductors, transformers, switchgear, etc.
    """

    def __init__(self, materialKind='concrete', height=0.0, removeWeed=False, weedRemovedDate='', fumigantAppliedDate='', fumigantName='', StructureSupports=None, **kw_args):
        """Initializes a new 'Structure' instance.

        @param materialKind: Material this structure is made of. Values are: "concrete", "wood", "other", "steel"
        @param height: Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions. 
        @param removeWeed: True if weeds are to be removed around asset. 
        @param weedRemovedDate: Date weed were last removed. 
        @param fumigantAppliedDate: Date fumigant was last applied. 
        @param fumigantName: Name of fumigant. 
        @param StructureSupports:
        """
        #: Material this structure is made of.Values are: "concrete", "wood", "other", "steel"
        self.materialKind = materialKind

        #: Visible height of structure above ground level for overhead construction (e.g., Pole or Tower) or below ground level for an underground vault, manhole, etc. Refer to associated DimensionPropertiesInfo for other types of dimensions.
        self.height = height

        #: True if weeds are to be removed around asset.
        self.removeWeed = removeWeed

        #: Date weed were last removed.
        self.weedRemovedDate = weedRemovedDate

        #: Date fumigant was last applied.
        self.fumigantAppliedDate = fumigantAppliedDate

        #: Name of fumigant.
        self.fumigantName = fumigantName

        self._StructureSupports = []
        self.StructureSupports = [] if StructureSupports is None else StructureSupports

        super(Structure, self).__init__(**kw_args)

    def getStructureSupports(self):
        
        return self._StructureSupports

    def setStructureSupports(self, value):
        for x in self._StructureSupports:
            x._SecuredStructure = None
        for y in value:
            y._SecuredStructure = self
        self._StructureSupports = value

    StructureSupports = property(getStructureSupports, setStructureSupports)

    def addStructureSupports(self, *StructureSupports):
        for obj in StructureSupports:
            obj._SecuredStructure = self
            self._StructureSupports.append(obj)

    def removeStructureSupports(self, *StructureSupports):
        for obj in StructureSupports:
            obj._SecuredStructure = None
            self._StructureSupports.remove(obj)


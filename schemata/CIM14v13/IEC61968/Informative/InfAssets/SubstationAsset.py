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

class SubstationAsset(AssetContainer):
    """A grouping of assets such as conductors, transformers, switchgear, etc. When located on the ground surface, it is usually surrounded by some kind of fence with a locked gate. It may also be located inside buildings, in underground vaults, and on structures. Use 'category' for utility-specific categorisation (such as Air Cooled, Gas Insultated, etc.).
    """

    def __init__(self, function='industrial', Substation=None, *args, **kw_args):
        """Initializes a new 'SubstationAsset' instance.

        @param function: Function of this substation asset. Values are: "industrial", "subTransmission", "generation", "distribution", "transmission", "other"
        @param Substation:
        """
        #: Function of this substation asset.Values are: "industrial", "subTransmission", "generation", "distribution", "transmission", "other"
        self.function = function

        self._Substation = None
        self.Substation = Substation

        super(SubstationAsset, self).__init__(*args, **kw_args)

    def getSubstation(self):
        
        return self._Substation

    def setSubstation(self, value):
        if self._Substation is not None:
            self._Substation._SubstationAsset = None

        self._Substation = value
        if self._Substation is not None:
            self._Substation._SubstationAsset = self

    Substation = property(getSubstation, setSubstation)


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

class Cabinet(AssetContainer):
    """Enclosure that offers protection to the equipment it contains and/or safety to people/animals outside it.
    """

    def __init__(self, CabinetModel=None, **kw_args):
        """Initializes a new 'Cabinet' instance.

        @param CabinetModel:
        """
        self._CabinetModel = None
        self.CabinetModel = CabinetModel

        super(Cabinet, self).__init__(**kw_args)

    def getCabinetModel(self):
        
        return self._CabinetModel

    def setCabinetModel(self, value):
        if self._CabinetModel is not None:
            filtered = [x for x in self.CabinetModel.Cabinets if x != self]
            self._CabinetModel._Cabinets = filtered

        self._CabinetModel = value
        if self._CabinetModel is not None:
            self._CabinetModel._Cabinets.append(self)

    CabinetModel = property(getCabinetModel, setCabinetModel)


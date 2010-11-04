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

class ComEquipmentAsset(AssetContainer):
    """Communicaiton equipment, other than media, such as gateways, routers, controllers, etc.
    """

    def __init__(self, DeviceFunctions=None, **kw_args):
        """Initializes a new 'ComEquipmentAsset' instance.

        @param DeviceFunctions: All device functions of this communication equipment asset.
        """
        self._DeviceFunctions = []
        self.DeviceFunctions = [] if DeviceFunctions is None else DeviceFunctions

        super(ComEquipmentAsset, self).__init__(**kw_args)

    def getDeviceFunctions(self):
        """All device functions of this communication equipment asset.
        """
        return self._DeviceFunctions

    def setDeviceFunctions(self, value):
        for x in self._DeviceFunctions:
            x._ComEquipmentAsset = None
        for y in value:
            y._ComEquipmentAsset = self
        self._DeviceFunctions = value

    DeviceFunctions = property(getDeviceFunctions, setDeviceFunctions)

    def addDeviceFunctions(self, *DeviceFunctions):
        for obj in DeviceFunctions:
            obj._ComEquipmentAsset = self
            self._DeviceFunctions.append(obj)

    def removeDeviceFunctions(self, *DeviceFunctions):
        for obj in DeviceFunctions:
            obj._ComEquipmentAsset = None
            self._DeviceFunctions.remove(obj)


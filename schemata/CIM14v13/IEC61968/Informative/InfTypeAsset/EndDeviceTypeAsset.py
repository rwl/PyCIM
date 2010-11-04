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

from CIM14v13.IEC61968.Informative.InfTypeAsset.TypeAsset import TypeAsset

class EndDeviceTypeAsset(TypeAsset):
    """Documentation for generic End Device that may be used for various purposes such as work planning.
    """

    def __init__(self, EndDeviceModels=None, **kw_args):
        """Initializes a new 'EndDeviceTypeAsset' instance.

        @param EndDeviceModels:
        """
        self._EndDeviceModels = []
        self.EndDeviceModels = [] if EndDeviceModels is None else EndDeviceModels

        super(EndDeviceTypeAsset, self).__init__(**kw_args)

    def getEndDeviceModels(self):
        
        return self._EndDeviceModels

    def setEndDeviceModels(self, value):
        for x in self._EndDeviceModels:
            x._EndDeviceTypeAsset = None
        for y in value:
            y._EndDeviceTypeAsset = self
        self._EndDeviceModels = value

    EndDeviceModels = property(getEndDeviceModels, setEndDeviceModels)

    def addEndDeviceModels(self, *EndDeviceModels):
        for obj in EndDeviceModels:
            obj._EndDeviceTypeAsset = self
            self._EndDeviceModels.append(obj)

    def removeEndDeviceModels(self, *EndDeviceModels):
        for obj in EndDeviceModels:
            obj._EndDeviceTypeAsset = None
            self._EndDeviceModels.remove(obj)


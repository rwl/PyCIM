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

from CIM14v13.IEC61968.Assets.Asset import Asset

class WorkEquipmentAsset(Asset):
    """Various equipment used to perform units of work by crews, office staff, etc.
    """

    def __init__(self, WorkEquipmentAssetModel=None, Crew=None, Usages=None, *args, **kw_args):
        """Initializes a new 'WorkEquipmentAsset' instance.

        @param WorkEquipmentAssetModel:
        @param Crew:
        @param Usages:
        """
        self._WorkEquipmentAssetModel = None
        self.WorkEquipmentAssetModel = WorkEquipmentAssetModel

        self._Crew = None
        self.Crew = Crew

        self._Usages = []
        self.Usages = [] if Usages is None else Usages

        super(WorkEquipmentAsset, self).__init__(*args, **kw_args)

    def getWorkEquipmentAssetModel(self):
        
        return self._WorkEquipmentAssetModel

    def setWorkEquipmentAssetModel(self, value):
        if self._WorkEquipmentAssetModel is not None:
            filtered = [x for x in self.WorkEquipmentAssetModel.WorkEquipmentAssets if x != self]
            self._WorkEquipmentAssetModel._WorkEquipmentAssets = filtered

        self._WorkEquipmentAssetModel = value
        if self._WorkEquipmentAssetModel is not None:
            self._WorkEquipmentAssetModel._WorkEquipmentAssets.append(self)

    WorkEquipmentAssetModel = property(getWorkEquipmentAssetModel, setWorkEquipmentAssetModel)

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.WorkEquipmentAssets if x != self]
            self._Crew._WorkEquipmentAssets = filtered

        self._Crew = value
        if self._Crew is not None:
            self._Crew._WorkEquipmentAssets.append(self)

    Crew = property(getCrew, setCrew)

    def getUsages(self):
        
        return self._Usages

    def setUsages(self, value):
        for x in self._Usages:
            x._WorkEquipmentAsset = None
        for y in value:
            y._WorkEquipmentAsset = self
        self._Usages = value

    Usages = property(getUsages, setUsages)

    def addUsages(self, *Usages):
        for obj in Usages:
            obj._WorkEquipmentAsset = self
            self._Usages.append(obj)

    def removeUsages(self, *Usages):
        for obj in Usages:
            obj._WorkEquipmentAsset = None
            self._Usages.remove(obj)


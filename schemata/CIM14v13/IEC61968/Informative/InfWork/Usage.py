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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Usage(IdentifiedObject):
    """The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.
    """

    def __init__(self, MaterialItem=None, WorkTask=None, status=None, WorkEquipmentAsset=None, *args, **kw_args):
        """Initializes a new 'Usage' instance.

        @param MaterialItem:
        @param WorkTask:
        @param status:
        @param WorkEquipmentAsset:
        """
        self._MaterialItem = None
        self.MaterialItem = MaterialItem

        self._WorkTask = None
        self.WorkTask = WorkTask

        self.status = status

        self._WorkEquipmentAsset = None
        self.WorkEquipmentAsset = WorkEquipmentAsset

        super(Usage, self).__init__(*args, **kw_args)

    def getMaterialItem(self):
        
        return self._MaterialItem

    def setMaterialItem(self, value):
        if self._MaterialItem is not None:
            filtered = [x for x in self.MaterialItem.Usages if x != self]
            self._MaterialItem._Usages = filtered

        self._MaterialItem = value
        if self._MaterialItem is not None:
            self._MaterialItem._Usages.append(self)

    MaterialItem = property(getMaterialItem, setMaterialItem)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.Usages if x != self]
            self._WorkTask._Usages = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._Usages.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    status = None

    def getWorkEquipmentAsset(self):
        
        return self._WorkEquipmentAsset

    def setWorkEquipmentAsset(self, value):
        if self._WorkEquipmentAsset is not None:
            filtered = [x for x in self.WorkEquipmentAsset.Usages if x != self]
            self._WorkEquipmentAsset._Usages = filtered

        self._WorkEquipmentAsset = value
        if self._WorkEquipmentAsset is not None:
            self._WorkEquipmentAsset._Usages.append(self)

    WorkEquipmentAsset = property(getWorkEquipmentAsset, setWorkEquipmentAsset)


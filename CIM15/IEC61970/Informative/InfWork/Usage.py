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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Usage(IdentifiedObject):
    """The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.
    """

    def __init__(self, WorkTask=None, WorkEquipmentAsset=None, status=None, MaterialItem=None, *args, **kw_args):
        """Initialises a new 'Usage' instance.

        @param WorkTask:
        @param WorkEquipmentAsset:
        @param status:
        @param MaterialItem:
        """
        self._WorkTask = None
        self.WorkTask = WorkTask

        self._WorkEquipmentAsset = None
        self.WorkEquipmentAsset = WorkEquipmentAsset

        self.status = status

        self._MaterialItem = None
        self.MaterialItem = MaterialItem

        super(Usage, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["WorkTask", "WorkEquipmentAsset", "status", "MaterialItem"]
    _many_refs = []

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.Usages if x != self]
            self._WorkTask._Usages = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._Usages:
                self._WorkTask._Usages.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getWorkEquipmentAsset(self):
        
        return self._WorkEquipmentAsset

    def setWorkEquipmentAsset(self, value):
        if self._WorkEquipmentAsset is not None:
            filtered = [x for x in self.WorkEquipmentAsset.Usages if x != self]
            self._WorkEquipmentAsset._Usages = filtered

        self._WorkEquipmentAsset = value
        if self._WorkEquipmentAsset is not None:
            if self not in self._WorkEquipmentAsset._Usages:
                self._WorkEquipmentAsset._Usages.append(self)

    WorkEquipmentAsset = property(getWorkEquipmentAsset, setWorkEquipmentAsset)

    status = None

    def getMaterialItem(self):
        
        return self._MaterialItem

    def setMaterialItem(self, value):
        if self._MaterialItem is not None:
            filtered = [x for x in self.MaterialItem.Usages if x != self]
            self._MaterialItem._Usages = filtered

        self._MaterialItem = value
        if self._MaterialItem is not None:
            if self not in self._MaterialItem._Usages:
                self._MaterialItem._Usages.append(self)

    MaterialItem = property(getMaterialItem, setMaterialItem)


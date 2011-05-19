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

from CIM15.IEC61968.Assets.Asset import Asset

class WorkEquipment(Asset):
    """Equipment used to perform units of work by crews, office staff, etc.Equipment used to perform units of work by crews, office staff, etc.
    """

    def __init__(self, Crew=None, Usages=None, *args, **kw_args):
        """Initialises a new 'WorkEquipment' instance.

        @param Crew:
        @param Usages:
        """
        self._Crew = None
        self.Crew = Crew

        self._Usages = []
        self.Usages = [] if Usages is None else Usages

        super(WorkEquipment, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Crew", "Usages"]
    _many_refs = ["Usages"]

    def getCrew(self):
        
        return self._Crew

    def setCrew(self, value):
        if self._Crew is not None:
            filtered = [x for x in self.Crew.WorkEquipmentAssets if x != self]
            self._Crew._WorkEquipmentAssets = filtered

        self._Crew = value
        if self._Crew is not None:
            if self not in self._Crew._WorkEquipmentAssets:
                self._Crew._WorkEquipmentAssets.append(self)

    Crew = property(getCrew, setCrew)

    def getUsages(self):
        
        return self._Usages

    def setUsages(self, value):
        for x in self._Usages:
            x.WorkEquipmentAsset = None
        for y in value:
            y._WorkEquipmentAsset = self
        self._Usages = value

    Usages = property(getUsages, setUsages)

    def addUsages(self, *Usages):
        for obj in Usages:
            obj.WorkEquipmentAsset = self

    def removeUsages(self, *Usages):
        for obj in Usages:
            obj.WorkEquipmentAsset = None


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

from CIM14.IEC61970.LoadModel.EnergyArea import EnergyArea

class SubLoadArea(EnergyArea):
    """The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    def __init__(self, LoadGroups=None, LoadArea=None, *args, **kw_args):
        """Initialises a new 'SubLoadArea' instance.

        @param LoadGroups: The Loadgroups in the SubLoadArea.
        @param LoadArea: The LoadArea where the SubLoadArea belongs.
        """
        self._LoadGroups = []
        self.LoadGroups = [] if LoadGroups is None else LoadGroups

        self._LoadArea = None
        self.LoadArea = LoadArea

        super(SubLoadArea, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LoadGroups", "LoadArea"]
    _many_refs = ["LoadGroups"]

    def getLoadGroups(self):
        """The Loadgroups in the SubLoadArea.
        """
        return self._LoadGroups

    def setLoadGroups(self, value):
        for x in self._LoadGroups:
            x.SubLoadArea = None
        for y in value:
            y._SubLoadArea = self
        self._LoadGroups = value

    LoadGroups = property(getLoadGroups, setLoadGroups)

    def addLoadGroups(self, *LoadGroups):
        for obj in LoadGroups:
            obj.SubLoadArea = self

    def removeLoadGroups(self, *LoadGroups):
        for obj in LoadGroups:
            obj.SubLoadArea = None

    def getLoadArea(self):
        """The LoadArea where the SubLoadArea belongs.
        """
        return self._LoadArea

    def setLoadArea(self, value):
        if self._LoadArea is not None:
            filtered = [x for x in self.LoadArea.SubLoadAreas if x != self]
            self._LoadArea._SubLoadAreas = filtered

        self._LoadArea = value
        if self._LoadArea is not None:
            if self not in self._LoadArea._SubLoadAreas:
                self._LoadArea._SubLoadAreas.append(self)

    LoadArea = property(getLoadArea, setLoadArea)


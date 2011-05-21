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

from CIM14.CPSM.Equipment.LoadModel.EnergyArea import EnergyArea

class LoadArea(EnergyArea):
    """The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.
    """

    def __init__(self, SubLoadAreas=None, *args, **kw_args):
        """Initialises a new 'LoadArea' instance.

        @param SubLoadAreas: The SubLoadAreas in the LoadArea.
        """
        self._SubLoadAreas = []
        self.SubLoadAreas = [] if SubLoadAreas is None else SubLoadAreas

        super(LoadArea, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SubLoadAreas"]
    _many_refs = ["SubLoadAreas"]

    def getSubLoadAreas(self):
        """The SubLoadAreas in the LoadArea.
        """
        return self._SubLoadAreas

    def setSubLoadAreas(self, value):
        for x in self._SubLoadAreas:
            x.LoadArea = None
        for y in value:
            y._LoadArea = self
        self._SubLoadAreas = value

    SubLoadAreas = property(getSubLoadAreas, setSubLoadAreas)

    def addSubLoadAreas(self, *SubLoadAreas):
        for obj in SubLoadAreas:
            obj.LoadArea = self

    def removeSubLoadAreas(self, *SubLoadAreas):
        for obj in SubLoadAreas:
            obj.LoadArea = None


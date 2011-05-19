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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class Ground(ConductingEquipment):
    """A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.
    """

    def __init__(self, WindingInsulations=None, *args, **kw_args):
        """Initialises a new 'Ground' instance.

        @param WindingInsulations:
        """
        self._WindingInsulations = []
        self.WindingInsulations = [] if WindingInsulations is None else WindingInsulations

        super(Ground, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["WindingInsulations"]
    _many_refs = ["WindingInsulations"]

    def getWindingInsulations(self):
        
        return self._WindingInsulations

    def setWindingInsulations(self, value):
        for x in self._WindingInsulations:
            x.Ground = None
        for y in value:
            y._Ground = self
        self._WindingInsulations = value

    WindingInsulations = property(getWindingInsulations, setWindingInsulations)

    def addWindingInsulations(self, *WindingInsulations):
        for obj in WindingInsulations:
            obj.Ground = self

    def removeWindingInsulations(self, *WindingInsulations):
        for obj in WindingInsulations:
            obj.Ground = None


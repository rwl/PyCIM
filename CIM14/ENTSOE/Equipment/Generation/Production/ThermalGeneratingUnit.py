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

from CIM14.ENTSOE.Equipment.Generation.Production.GeneratingUnit import GeneratingUnit

class ThermalGeneratingUnit(GeneratingUnit):
    """A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.-  The association to FossilFuel is not required.
    """

    def __init__(self, FossilFuels=None, *args, **kw_args):
        """Initialises a new 'ThermalGeneratingUnit' instance.

        @param FossilFuels: A thermal generating unit may have one or more fossil fuels
        """
        self._FossilFuels = None
        self.FossilFuels = FossilFuels

        super(ThermalGeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["FossilFuels"]
    _many_refs = []

    def getFossilFuels(self):
        """A thermal generating unit may have one or more fossil fuels
        """
        return self._FossilFuels

    def setFossilFuels(self, value):
        if self._FossilFuels is not None:
            self._FossilFuels._ThermalGeneratingUnit = None

        self._FossilFuels = value
        if self._FossilFuels is not None:
            self._FossilFuels.ThermalGeneratingUnit = None
            self._FossilFuels._ThermalGeneratingUnit = self

    FossilFuels = property(getFossilFuels, setFossilFuels)


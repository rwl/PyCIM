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

from CIM15.IEC61970.Core.Curve import Curve

class GrossToNetActivePowerCurve(Curve):
    """Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """

    def __init__(self, GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'GrossToNetActivePowerCurve' instance.

        @param GeneratingUnit: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(GrossToNetActivePowerCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GeneratingUnit"]
    _many_refs = []

    def getGeneratingUnit(self):
        """A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.GrossToNetActivePowerCurves if x != self]
            self._GeneratingUnit._GrossToNetActivePowerCurves = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            if self not in self._GeneratingUnit._GrossToNetActivePowerCurves:
                self._GeneratingUnit._GrossToNetActivePowerCurves.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)


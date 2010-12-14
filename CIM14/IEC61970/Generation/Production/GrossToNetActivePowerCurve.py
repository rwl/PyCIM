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

from CIM14.IEC61970.Core.Curve import Curve

class GrossToNetActivePowerCurve(Curve):
    """Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
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


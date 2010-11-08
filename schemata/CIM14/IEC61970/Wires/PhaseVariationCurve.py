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

class PhaseVariationCurve(Curve):
    """A Phase Variation Curve describes the phase shift in relationship to tap step changes.  The tap step is represented using the xValue and the phase shift using y1value.
    """

    def __init__(self, PhaseTapChanger=None, *args, **kw_args):
        """Initialises a new 'PhaseVariationCurve' instance.

        @param PhaseTapChanger: A PhaseVariationCurve defines phase shift changes for a PhaseTapChanger.
        """
        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        super(PhaseVariationCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PhaseTapChanger"]
    _many_refs = []

    def getPhaseTapChanger(self):
        """A PhaseVariationCurve defines phase shift changes for a PhaseTapChanger.
        """
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._PhaseVariationCurve = None

        self._PhaseTapChanger = value
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._PhaseVariationCurve = self

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)


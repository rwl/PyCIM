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

class ImpedanceVariationCurve(Curve):
    """An Impedance Variation Curve describes the change in Transformer Winding impedance values in relationship to tap step changes.  The tap step is represented using the xValue, resistance using y1value, reactance using y2value, and magnetizing susceptance using y3value.  The resistance (r), reactance (x), and magnetizing susceptance (b) of the associated TransformerWinding define the impedance when the tap is at neutral step.  The curve values represent the change to the impedance from the neutral step values.  The impedance at a non-neutral step is calculated by adding the neutral step impedance (from the TransformerWinding) to the delta value from the curve.
    """

    def __init__(self, TapChanger=None, **kw_args):
        """Initializes a new 'ImpedanceVariationCurve' instance.

        @param TapChanger: An ImpedanceVariationCurve is defines impedance changes for a TapChanger.
        """
        self._TapChanger = None
        self.TapChanger = TapChanger

        super(ImpedanceVariationCurve, self).__init__(**kw_args)

    def getTapChanger(self):
        """An ImpedanceVariationCurve is defines impedance changes for a TapChanger.
        """
        return self._TapChanger

    def setTapChanger(self, value):
        if self._TapChanger is not None:
            self._TapChanger._ImpedanceVariationCurve = None

        self._TapChanger = value
        if self._TapChanger is not None:
            self._TapChanger._ImpedanceVariationCurve = self

    TapChanger = property(getTapChanger, setTapChanger)


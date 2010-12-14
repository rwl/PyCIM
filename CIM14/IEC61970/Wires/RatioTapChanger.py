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

from CIM14.IEC61970.Wires.TapChanger import TapChanger

class RatioTapChanger(TapChanger):
    """A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """

    def __init__(self, tculControlMode="volt", Winding=None, TransformerWinding=None, RatioVariationCurve=None, *args, **kw_args):
        """Initialises a new 'RatioTapChanger' instance.

        @param tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "volt", "reactive"
        @param Winding: Winding to which this ratio tap changer belongs.
        @param TransformerWinding: The transformer winding to which the ratio tap changer belongs.
        @param RatioVariationCurve: A RatioTapChanger can have an associated RatioVariationCurve to define tap ratio variations with tap step changes.
        """
        #: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "volt", "reactive"
        self.tculControlMode = tculControlMode

        self._Winding = None
        self.Winding = Winding

        self._TransformerWinding = None
        self.TransformerWinding = TransformerWinding

        self._RatioVariationCurve = None
        self.RatioVariationCurve = RatioVariationCurve

        super(RatioTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["tculControlMode"]
    _attr_types = {"tculControlMode": str}
    _defaults = {"tculControlMode": "volt"}
    _enums = {"tculControlMode": "TransformerControlMode"}
    _refs = ["Winding", "TransformerWinding", "RatioVariationCurve"]
    _many_refs = []

    def getWinding(self):
        """Winding to which this ratio tap changer belongs.
        """
        return self._Winding

    def setWinding(self, value):
        if self._Winding is not None:
            self._Winding._RatioTapChanger = None

        self._Winding = value
        if self._Winding is not None:
            self._Winding.RatioTapChanger = None
            self._Winding._RatioTapChanger = self

    Winding = property(getWinding, setWinding)

    def getTransformerWinding(self):
        """The transformer winding to which the ratio tap changer belongs.
        """
        return self._TransformerWinding

    def setTransformerWinding(self, value):
        if self._TransformerWinding is not None:
            self._TransformerWinding._RatioTapChanger = None

        self._TransformerWinding = value
        if self._TransformerWinding is not None:
            self._TransformerWinding.RatioTapChanger = None
            self._TransformerWinding._RatioTapChanger = self

    TransformerWinding = property(getTransformerWinding, setTransformerWinding)

    def getRatioVariationCurve(self):
        """A RatioTapChanger can have an associated RatioVariationCurve to define tap ratio variations with tap step changes.
        """
        return self._RatioVariationCurve

    def setRatioVariationCurve(self, value):
        if self._RatioVariationCurve is not None:
            self._RatioVariationCurve._RatioTapChanger = None

        self._RatioVariationCurve = value
        if self._RatioVariationCurve is not None:
            self._RatioVariationCurve.RatioTapChanger = None
            self._RatioVariationCurve._RatioTapChanger = self

    RatioVariationCurve = property(getRatioVariationCurve, setRatioVariationCurve)


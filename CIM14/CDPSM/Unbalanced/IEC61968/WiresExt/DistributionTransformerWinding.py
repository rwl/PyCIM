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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.ConductingEquipment import ConductingEquipment

class DistributionTransformerWinding(ConductingEquipment):
    """Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. - 'windingType' attribute is replaced by 'sequenceNumber' attribute on WindingInfo class. - all the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """

    def __init__(self, rground=0.0, xground=0.0, grounded=False, WindingInfo=None, Transformer=None, RatioTapChanger=None, PiImpedance=None, *args, **kw_args):
        """Initialises a new 'DistributionTransformerWinding' instance.

        @param rground: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
        @param xground: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
        @param grounded: (for Yn and Zn connections) True if the neutral is solidly grounded. 
        @param WindingInfo: Data for this winding.
        @param Transformer: Transformer this winding belongs to.
        @param RatioTapChanger: Ratio tap changer associated with this winding.
        @param PiImpedance: (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
        """
        #: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.
        self.rground = rground

        #: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.
        self.xground = xground

        #: (for Yn and Zn connections) True if the neutral is solidly grounded.
        self.grounded = grounded

        self._WindingInfo = None
        self.WindingInfo = WindingInfo

        self._Transformer = None
        self.Transformer = Transformer

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        self._PiImpedance = None
        self.PiImpedance = PiImpedance

        super(DistributionTransformerWinding, self).__init__(*args, **kw_args)

    _attrs = ["rground", "xground", "grounded"]
    _attr_types = {"rground": float, "xground": float, "grounded": bool}
    _defaults = {"rground": 0.0, "xground": 0.0, "grounded": False}
    _enums = {}
    _refs = ["WindingInfo", "Transformer", "RatioTapChanger", "PiImpedance"]
    _many_refs = []

    def getWindingInfo(self):
        """Data for this winding.
        """
        return self._WindingInfo

    def setWindingInfo(self, value):
        if self._WindingInfo is not None:
            filtered = [x for x in self.WindingInfo.Windings if x != self]
            self._WindingInfo._Windings = filtered

        self._WindingInfo = value
        if self._WindingInfo is not None:
            if self not in self._WindingInfo._Windings:
                self._WindingInfo._Windings.append(self)

    WindingInfo = property(getWindingInfo, setWindingInfo)

    def getTransformer(self):
        """Transformer this winding belongs to.
        """
        return self._Transformer

    def setTransformer(self, value):
        if self._Transformer is not None:
            filtered = [x for x in self.Transformer.Windings if x != self]
            self._Transformer._Windings = filtered

        self._Transformer = value
        if self._Transformer is not None:
            if self not in self._Transformer._Windings:
                self._Transformer._Windings.append(self)

    Transformer = property(getTransformer, setTransformer)

    def getRatioTapChanger(self):
        """Ratio tap changer associated with this winding.
        """
        return self._RatioTapChanger

    def setRatioTapChanger(self, value):
        if self._RatioTapChanger is not None:
            self._RatioTapChanger._Winding = None

        self._RatioTapChanger = value
        if self._RatioTapChanger is not None:
            self._RatioTapChanger.Winding = None
            self._RatioTapChanger._Winding = self

    RatioTapChanger = property(getRatioTapChanger, setRatioTapChanger)

    def getPiImpedance(self):
        """(accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
        """
        return self._PiImpedance

    def setPiImpedance(self, value):
        if self._PiImpedance is not None:
            filtered = [x for x in self.PiImpedance.Windings if x != self]
            self._PiImpedance._Windings = filtered

        self._PiImpedance = value
        if self._PiImpedance is not None:
            if self not in self._PiImpedance._Windings:
                self._PiImpedance._Windings.append(self)

    PiImpedance = property(getPiImpedance, setPiImpedance)


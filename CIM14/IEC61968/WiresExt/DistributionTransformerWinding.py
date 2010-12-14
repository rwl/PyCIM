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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class DistributionTransformerWinding(ConductingEquipment):
    """Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. - 'windingType' attribute is replaced by 'sequenceNumber' attribute on WindingInfo class. - all the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """

    def __init__(self, grounded=False, xground=0.0, rground=0.0, Transformer=None, WindingInfo=None, RatioTapChanger=None, PiImpedance=None, PhaseTapChanger=None, *args, **kw_args):
        """Initialises a new 'DistributionTransformerWinding' instance.

        @param grounded: (for Yn and Zn connections) True if the neutral is solidly grounded. 
        @param xground: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true. 
        @param rground: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true. 
        @param Transformer: Transformer this winding belongs to.
        @param WindingInfo: Data for this winding.
        @param RatioTapChanger: Ratio tap changer associated with this winding.
        @param PiImpedance: (accurate for 2- or 3-winding transformers only) Pi-model impedances of this winding.
        @param PhaseTapChanger: Phase tap changer associated with this winding.
        """
        #: (for Yn and Zn connections) True if the neutral is solidly grounded.
        self.grounded = grounded

        #: (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded' is true.
        self.xground = xground

        #: (for Yn and Zn connections) Resistance part of neutral impedance where 'grounded' is true.
        self.rground = rground

        self._Transformer = None
        self.Transformer = Transformer

        self._WindingInfo = None
        self.WindingInfo = WindingInfo

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        self._PiImpedance = None
        self.PiImpedance = PiImpedance

        self._PhaseTapChanger = None
        self.PhaseTapChanger = PhaseTapChanger

        super(DistributionTransformerWinding, self).__init__(*args, **kw_args)

    _attrs = ["grounded", "xground", "rground"]
    _attr_types = {"grounded": bool, "xground": float, "rground": float}
    _defaults = {"grounded": False, "xground": 0.0, "rground": 0.0}
    _enums = {}
    _refs = ["Transformer", "WindingInfo", "RatioTapChanger", "PiImpedance", "PhaseTapChanger"]
    _many_refs = []

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

    def getPhaseTapChanger(self):
        """Phase tap changer associated with this winding.
        """
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger._Winding = None

        self._PhaseTapChanger = value
        if self._PhaseTapChanger is not None:
            self._PhaseTapChanger.Winding = None
            self._PhaseTapChanger._Winding = self

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)


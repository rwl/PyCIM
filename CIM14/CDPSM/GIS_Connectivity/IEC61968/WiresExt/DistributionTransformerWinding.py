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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.ConductingEquipment import ConductingEquipment

class DistributionTransformerWinding(ConductingEquipment):
    """Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. - 'windingType' attribute is replaced by 'sequenceNumber' attribute on WindingInfo class. - all the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.
    """

    def __init__(self, WindingInfo=None, Transformer=None, RatioTapChanger=None, *args, **kw_args):
        """Initialises a new 'DistributionTransformerWinding' instance.

        @param WindingInfo: Data for this winding.
        @param Transformer: Transformer this winding belongs to.
        @param RatioTapChanger: Ratio tap changer associated with this winding.
        """
        self._WindingInfo = None
        self.WindingInfo = WindingInfo

        self._Transformer = None
        self.Transformer = Transformer

        self._RatioTapChanger = None
        self.RatioTapChanger = RatioTapChanger

        super(DistributionTransformerWinding, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["WindingInfo", "Transformer", "RatioTapChanger"]
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


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

from CIM14v13.IEC61968.Informative.InfAssets.Structure import Structure

class Pole(Structure):
    """A long, slender piece of wood, metal, etc. usually rounded that stands vertically from the ground and is used for mounting various types of overhead equipment. Dimensions of Pole are specified in associated DimensionsInfo.
    """

    def __init__(self, baseKind='cement', preservativeKind='naphthena', treatmentKind='grayStain', treatedDateTime='', construction='', breastBlock=False, jpaReference='', SupportStreetlights=None, PoleModel=None, *args, **kw_args):
        """Initializes a new 'Pole' instance.

        @param baseKind: Kind of base for this pole. Values are: "cement", "dirt", "unknown", "other", "asphalt"
        @param preservativeKind: Kind of preservative for this pole. Values are: "naphthena", "unknown", "other", "chemonite", "penta", "cellon", "creosote"
        @param treatmentKind: Kind of treatment for this pole. Values are: "grayStain", "other", "natural", "greenStain", "full", "unknown", "butt", "penta"
        @param treatedDateTime: Date and time pole was last treated with preservative. 
        @param construction: The framing structure mounted on the pole. 
        @param breastBlock: True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used. 
        @param jpaReference: Joint pole agreement reference number. 
        @param SupportStreetlights: Streetlight(s) may be attached to a pole.
        @param PoleModel:
        """
        #: Kind of base for this pole. Values are: "cement", "dirt", "unknown", "other", "asphalt"
        self.baseKind = baseKind

        #: Kind of preservative for this pole. Values are: "naphthena", "unknown", "other", "chemonite", "penta", "cellon", "creosote"
        self.preservativeKind = preservativeKind

        #: Kind of treatment for this pole. Values are: "grayStain", "other", "natural", "greenStain", "full", "unknown", "butt", "penta"
        self.treatmentKind = treatmentKind

        #: Date and time pole was last treated with preservative. 
        self.treatedDateTime = treatedDateTime

        #: The framing structure mounted on the pole. 
        self.construction = construction

        #: True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used. 
        self.breastBlock = breastBlock

        #: Joint pole agreement reference number. 
        self.jpaReference = jpaReference

        self._SupportStreetlights = []
        self.SupportStreetlights = [] if SupportStreetlights is None else SupportStreetlights

        self._PoleModel = None
        self.PoleModel = PoleModel

        super(Pole, self).__init__(*args, **kw_args)

    def getSupportStreetlights(self):
        """Streetlight(s) may be attached to a pole.
        """
        return self._SupportStreetlights

    def setSupportStreetlights(self, value):
        for x in self._SupportStreetlights:
            x._AttachedToPole = None
        for y in value:
            y._AttachedToPole = self
        self._SupportStreetlights = value

    SupportStreetlights = property(getSupportStreetlights, setSupportStreetlights)

    def addSupportStreetlights(self, *SupportStreetlights):
        for obj in SupportStreetlights:
            obj._AttachedToPole = self
            self._SupportStreetlights.append(obj)

    def removeSupportStreetlights(self, *SupportStreetlights):
        for obj in SupportStreetlights:
            obj._AttachedToPole = None
            self._SupportStreetlights.remove(obj)

    def getPoleModel(self):
        
        return self._PoleModel

    def setPoleModel(self, value):
        if self._PoleModel is not None:
            filtered = [x for x in self.PoleModel.Poles if x != self]
            self._PoleModel._Poles = filtered

        self._PoleModel = value
        if self._PoleModel is not None:
            self._PoleModel._Poles.append(self)

    PoleModel = property(getPoleModel, setPoleModel)


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

from CIM15.IEC61968.Common.Document import Document

class Specification(Document):
    """Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.
    """

    def __init__(self, AssetPropertyCurves=None, Mediums=None, AssetProperites=None, ReliabilityInfos=None, DimensionsInfos=None, Ratings=None, QualificationRequirements=None, *args, **kw_args):
        """Initialises a new 'Specification' instance.

        @param AssetPropertyCurves:
        @param Mediums:
        @param AssetProperites: UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param ReliabilityInfos:
        @param DimensionsInfos:
        @param Ratings: UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        @param QualificationRequirements:
        """
        self._AssetPropertyCurves = []
        self.AssetPropertyCurves = [] if AssetPropertyCurves is None else AssetPropertyCurves

        self._Mediums = []
        self.Mediums = [] if Mediums is None else Mediums

        self._AssetProperites = []
        self.AssetProperites = [] if AssetProperites is None else AssetProperites

        self._ReliabilityInfos = []
        self.ReliabilityInfos = [] if ReliabilityInfos is None else ReliabilityInfos

        self._DimensionsInfos = []
        self.DimensionsInfos = [] if DimensionsInfos is None else DimensionsInfos

        self._Ratings = []
        self.Ratings = [] if Ratings is None else Ratings

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        super(Specification, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["AssetPropertyCurves", "Mediums", "AssetProperites", "ReliabilityInfos", "DimensionsInfos", "Ratings", "QualificationRequirements"]
    _many_refs = ["AssetPropertyCurves", "Mediums", "AssetProperites", "ReliabilityInfos", "DimensionsInfos", "Ratings", "QualificationRequirements"]

    def getAssetPropertyCurves(self):
        
        return self._AssetPropertyCurves

    def setAssetPropertyCurves(self, value):
        for x in self._AssetPropertyCurves:
            x.Specification = None
        for y in value:
            y._Specification = self
        self._AssetPropertyCurves = value

    AssetPropertyCurves = property(getAssetPropertyCurves, setAssetPropertyCurves)

    def addAssetPropertyCurves(self, *AssetPropertyCurves):
        for obj in AssetPropertyCurves:
            obj.Specification = self

    def removeAssetPropertyCurves(self, *AssetPropertyCurves):
        for obj in AssetPropertyCurves:
            obj.Specification = None

    def getMediums(self):
        
        return self._Mediums

    def setMediums(self, value):
        for x in self._Mediums:
            x.Specification = None
        for y in value:
            y._Specification = self
        self._Mediums = value

    Mediums = property(getMediums, setMediums)

    def addMediums(self, *Mediums):
        for obj in Mediums:
            obj.Specification = self

    def removeMediums(self, *Mediums):
        for obj in Mediums:
            obj.Specification = None

    def getAssetProperites(self):
        """UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._AssetProperites

    def setAssetProperites(self, value):
        for x in self._AssetProperites:
            x.PropertySpecification = None
        for y in value:
            y._PropertySpecification = self
        self._AssetProperites = value

    AssetProperites = property(getAssetProperites, setAssetProperites)

    def addAssetProperites(self, *AssetProperites):
        for obj in AssetProperites:
            obj.PropertySpecification = self

    def removeAssetProperites(self, *AssetProperites):
        for obj in AssetProperites:
            obj.PropertySpecification = None

    def getReliabilityInfos(self):
        
        return self._ReliabilityInfos

    def setReliabilityInfos(self, value):
        for x in self._ReliabilityInfos:
            x.Specification = None
        for y in value:
            y._Specification = self
        self._ReliabilityInfos = value

    ReliabilityInfos = property(getReliabilityInfos, setReliabilityInfos)

    def addReliabilityInfos(self, *ReliabilityInfos):
        for obj in ReliabilityInfos:
            obj.Specification = self

    def removeReliabilityInfos(self, *ReliabilityInfos):
        for obj in ReliabilityInfos:
            obj.Specification = None

    def getDimensionsInfos(self):
        
        return self._DimensionsInfos

    def setDimensionsInfos(self, value):
        for p in self._DimensionsInfos:
            filtered = [q for q in p.Specifications if q != self]
            self._DimensionsInfos._Specifications = filtered
        for r in value:
            if self not in r._Specifications:
                r._Specifications.append(self)
        self._DimensionsInfos = value

    DimensionsInfos = property(getDimensionsInfos, setDimensionsInfos)

    def addDimensionsInfos(self, *DimensionsInfos):
        for obj in DimensionsInfos:
            if self not in obj._Specifications:
                obj._Specifications.append(self)
            self._DimensionsInfos.append(obj)

    def removeDimensionsInfos(self, *DimensionsInfos):
        for obj in DimensionsInfos:
            if self in obj._Specifications:
                obj._Specifications.remove(self)
            self._DimensionsInfos.remove(obj)

    def getRatings(self):
        """UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        """
        return self._Ratings

    def setRatings(self, value):
        for x in self._Ratings:
            x.RatingSpecification = None
        for y in value:
            y._RatingSpecification = self
        self._Ratings = value

    Ratings = property(getRatings, setRatings)

    def addRatings(self, *Ratings):
        for obj in Ratings:
            obj.RatingSpecification = self

    def removeRatings(self, *Ratings):
        for obj in Ratings:
            obj.RatingSpecification = None

    def getQualificationRequirements(self):
        
        return self._QualificationRequirements

    def setQualificationRequirements(self, value):
        for p in self._QualificationRequirements:
            filtered = [q for q in p.Specifications if q != self]
            self._QualificationRequirements._Specifications = filtered
        for r in value:
            if self not in r._Specifications:
                r._Specifications.append(self)
        self._QualificationRequirements = value

    QualificationRequirements = property(getQualificationRequirements, setQualificationRequirements)

    def addQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self not in obj._Specifications:
                obj._Specifications.append(self)
            self._QualificationRequirements.append(obj)

    def removeQualificationRequirements(self, *QualificationRequirements):
        for obj in QualificationRequirements:
            if self in obj._Specifications:
                obj._Specifications.remove(self)
            self._QualificationRequirements.remove(obj)


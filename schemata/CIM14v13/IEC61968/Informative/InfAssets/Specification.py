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

from CIM14v13.IEC61968.Common.Document import Document

class Specification(Document):
    """Specification can be used for various purposes relative to an asset, a logical device (PowerSystemResource), location, etc. Examples include documents supplied by manufacturers such as asset installation instructions, asset maintenance instructions, etc.
    """

    def __init__(self, AssetProperites=None, QualificationRequirements=None, Ratings=None, DimensionsInfos=None, ReliabilityInfos=None, Mediums=None, AssetPropertyCurves=None, **kw_args):
        """Initializes a new 'Specification' instance.

        @param AssetProperites: UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        @param QualificationRequirements:
        @param Ratings: UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        @param DimensionsInfos:
        @param ReliabilityInfos:
        @param Mediums:
        @param AssetPropertyCurves:
        """
        self._AssetProperites = []
        self.AssetProperites = [] if AssetProperites is None else AssetProperites

        self._QualificationRequirements = []
        self.QualificationRequirements = [] if QualificationRequirements is None else QualificationRequirements

        self._Ratings = []
        self.Ratings = [] if Ratings is None else Ratings

        self._DimensionsInfos = []
        self.DimensionsInfos = [] if DimensionsInfos is None else DimensionsInfos

        self._ReliabilityInfos = []
        self.ReliabilityInfos = [] if ReliabilityInfos is None else ReliabilityInfos

        self._Mediums = []
        self.Mediums = [] if Mediums is None else Mediums

        self._AssetPropertyCurves = []
        self.AssetPropertyCurves = [] if AssetPropertyCurves is None else AssetPropertyCurves

        super(Specification, self).__init__(**kw_args)

    def getAssetProperites(self):
        """UserAttributes used to specify further properties of the asset covered with this specification. Use 'name' to specify what kind of property it is, and 'value.value' attribute for the actual value.
        """
        return self._AssetProperites

    def setAssetProperites(self, value):
        for x in self._AssetProperites:
            x._PropertySpecification = None
        for y in value:
            y._PropertySpecification = self
        self._AssetProperites = value

    AssetProperites = property(getAssetProperites, setAssetProperites)

    def addAssetProperites(self, *AssetProperites):
        for obj in AssetProperites:
            obj._PropertySpecification = self
            self._AssetProperites.append(obj)

    def removeAssetProperites(self, *AssetProperites):
        for obj in AssetProperites:
            obj._PropertySpecification = None
            self._AssetProperites.remove(obj)

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

    def getRatings(self):
        """UserAttributes used to specify ratings of the asset covered by this specification. Ratings also can be used to set the initial value of operational measurement limits. Use 'name' to specify what kind of rating it is (e.g., voltage, current), and 'value' attribute for the actual value and unit information of the rating.
        """
        return self._Ratings

    def setRatings(self, value):
        for x in self._Ratings:
            x._RatingSpecification = None
        for y in value:
            y._RatingSpecification = self
        self._Ratings = value

    Ratings = property(getRatings, setRatings)

    def addRatings(self, *Ratings):
        for obj in Ratings:
            obj._RatingSpecification = self
            self._Ratings.append(obj)

    def removeRatings(self, *Ratings):
        for obj in Ratings:
            obj._RatingSpecification = None
            self._Ratings.remove(obj)

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

    def getReliabilityInfos(self):
        
        return self._ReliabilityInfos

    def setReliabilityInfos(self, value):
        for x in self._ReliabilityInfos:
            x._Specification = None
        for y in value:
            y._Specification = self
        self._ReliabilityInfos = value

    ReliabilityInfos = property(getReliabilityInfos, setReliabilityInfos)

    def addReliabilityInfos(self, *ReliabilityInfos):
        for obj in ReliabilityInfos:
            obj._Specification = self
            self._ReliabilityInfos.append(obj)

    def removeReliabilityInfos(self, *ReliabilityInfos):
        for obj in ReliabilityInfos:
            obj._Specification = None
            self._ReliabilityInfos.remove(obj)

    def getMediums(self):
        
        return self._Mediums

    def setMediums(self, value):
        for x in self._Mediums:
            x._Specification = None
        for y in value:
            y._Specification = self
        self._Mediums = value

    Mediums = property(getMediums, setMediums)

    def addMediums(self, *Mediums):
        for obj in Mediums:
            obj._Specification = self
            self._Mediums.append(obj)

    def removeMediums(self, *Mediums):
        for obj in Mediums:
            obj._Specification = None
            self._Mediums.remove(obj)

    def getAssetPropertyCurves(self):
        
        return self._AssetPropertyCurves

    def setAssetPropertyCurves(self, value):
        for x in self._AssetPropertyCurves:
            x._Specification = None
        for y in value:
            y._Specification = self
        self._AssetPropertyCurves = value

    AssetPropertyCurves = property(getAssetPropertyCurves, setAssetPropertyCurves)

    def addAssetPropertyCurves(self, *AssetPropertyCurves):
        for obj in AssetPropertyCurves:
            obj._Specification = self
            self._AssetPropertyCurves.append(obj)

    def removeAssetPropertyCurves(self, *AssetPropertyCurves):
        for obj in AssetPropertyCurves:
            obj._Specification = None
            self._AssetPropertyCurves.remove(obj)


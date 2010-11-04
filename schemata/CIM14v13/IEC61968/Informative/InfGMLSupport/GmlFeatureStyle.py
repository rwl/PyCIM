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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlFeatureStyle(IdentifiedObject):
    """Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.
    """

    def __init__(self, queryGrammar='xpath', version='', featureTypeName='', baseType='', featureType='', semanticTypeIdentifier='', featureConstraint='', GmlGeometryStyles=None, GmlFeatureTypes=None, GmlLabelStyles=None, GmlSymbols=None, GmlTobologyStyles=None, **kw_args):
        """Initializes a new 'GmlFeatureStyle' instance.

        @param queryGrammar: Grammar used in the content of the gml:featureConstraint element. Values are: "xpath", "other", "xquery"
        @param version: Allows version numbers to be identified when the SLD pieces are used independently. 
        @param featureTypeName: Identifies the specific feature type that the feature-type style is for. 
        @param baseType: Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive. 
        @param featureType: The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features. 
        @param semanticTypeIdentifier: The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types. 
        @param featureConstraint: This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'. 
        @param GmlGeometryStyles:
        @param GmlFeatureTypes:
        @param GmlLabelStyles:
        @param GmlSymbols:
        @param GmlTobologyStyles:
        """
        #: Grammar used in the content of the gml:featureConstraint element.Values are: "xpath", "other", "xquery"
        self.queryGrammar = queryGrammar

        #: Allows version numbers to be identified when the SLD pieces are used independently.
        self.version = version

        #: Identifies the specific feature type that the feature-type style is for.
        self.featureTypeName = featureTypeName

        #: Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive.
        self.baseType = baseType

        #: The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features.
        self.featureType = featureType

        #: The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types.
        self.semanticTypeIdentifier = semanticTypeIdentifier

        #: This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'.
        self.featureConstraint = featureConstraint

        self._GmlGeometryStyles = []
        self.GmlGeometryStyles = [] if GmlGeometryStyles is None else GmlGeometryStyles

        self._GmlFeatureTypes = []
        self.GmlFeatureTypes = [] if GmlFeatureTypes is None else GmlFeatureTypes

        self._GmlLabelStyles = []
        self.GmlLabelStyles = [] if GmlLabelStyles is None else GmlLabelStyles

        self._GmlSymbols = []
        self.GmlSymbols = [] if GmlSymbols is None else GmlSymbols

        self._GmlTobologyStyles = []
        self.GmlTobologyStyles = [] if GmlTobologyStyles is None else GmlTobologyStyles

        super(GmlFeatureStyle, self).__init__(**kw_args)

    def getGmlGeometryStyles(self):
        
        return self._GmlGeometryStyles

    def setGmlGeometryStyles(self, value):
        for x in self._GmlGeometryStyles:
            x._GmlFeatureStyle = None
        for y in value:
            y._GmlFeatureStyle = self
        self._GmlGeometryStyles = value

    GmlGeometryStyles = property(getGmlGeometryStyles, setGmlGeometryStyles)

    def addGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj._GmlFeatureStyle = self
            self._GmlGeometryStyles.append(obj)

    def removeGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj._GmlFeatureStyle = None
            self._GmlGeometryStyles.remove(obj)

    def getGmlFeatureTypes(self):
        
        return self._GmlFeatureTypes

    def setGmlFeatureTypes(self, value):
        for p in self._GmlFeatureTypes:
            filtered = [q for q in p.GmlFeatureStyles if q != self]
            self._GmlFeatureTypes._GmlFeatureStyles = filtered
        for r in value:
            if self not in r._GmlFeatureStyles:
                r._GmlFeatureStyles.append(self)
        self._GmlFeatureTypes = value

    GmlFeatureTypes = property(getGmlFeatureTypes, setGmlFeatureTypes)

    def addGmlFeatureTypes(self, *GmlFeatureTypes):
        for obj in GmlFeatureTypes:
            if self not in obj._GmlFeatureStyles:
                obj._GmlFeatureStyles.append(self)
            self._GmlFeatureTypes.append(obj)

    def removeGmlFeatureTypes(self, *GmlFeatureTypes):
        for obj in GmlFeatureTypes:
            if self in obj._GmlFeatureStyles:
                obj._GmlFeatureStyles.remove(self)
            self._GmlFeatureTypes.remove(obj)

    def getGmlLabelStyles(self):
        
        return self._GmlLabelStyles

    def setGmlLabelStyles(self, value):
        for x in self._GmlLabelStyles:
            x._GmlFeatureStyle = None
        for y in value:
            y._GmlFeatureStyle = self
        self._GmlLabelStyles = value

    GmlLabelStyles = property(getGmlLabelStyles, setGmlLabelStyles)

    def addGmlLabelStyles(self, *GmlLabelStyles):
        for obj in GmlLabelStyles:
            obj._GmlFeatureStyle = self
            self._GmlLabelStyles.append(obj)

    def removeGmlLabelStyles(self, *GmlLabelStyles):
        for obj in GmlLabelStyles:
            obj._GmlFeatureStyle = None
            self._GmlLabelStyles.remove(obj)

    def getGmlSymbols(self):
        
        return self._GmlSymbols

    def setGmlSymbols(self, value):
        for p in self._GmlSymbols:
            filtered = [q for q in p.GmlFeatureStyles if q != self]
            self._GmlSymbols._GmlFeatureStyles = filtered
        for r in value:
            if self not in r._GmlFeatureStyles:
                r._GmlFeatureStyles.append(self)
        self._GmlSymbols = value

    GmlSymbols = property(getGmlSymbols, setGmlSymbols)

    def addGmlSymbols(self, *GmlSymbols):
        for obj in GmlSymbols:
            if self not in obj._GmlFeatureStyles:
                obj._GmlFeatureStyles.append(self)
            self._GmlSymbols.append(obj)

    def removeGmlSymbols(self, *GmlSymbols):
        for obj in GmlSymbols:
            if self in obj._GmlFeatureStyles:
                obj._GmlFeatureStyles.remove(self)
            self._GmlSymbols.remove(obj)

    def getGmlTobologyStyles(self):
        
        return self._GmlTobologyStyles

    def setGmlTobologyStyles(self, value):
        for x in self._GmlTobologyStyles:
            x._GmlFeatureStyle = None
        for y in value:
            y._GmlFeatureStyle = self
        self._GmlTobologyStyles = value

    GmlTobologyStyles = property(getGmlTobologyStyles, setGmlTobologyStyles)

    def addGmlTobologyStyles(self, *GmlTobologyStyles):
        for obj in GmlTobologyStyles:
            obj._GmlFeatureStyle = self
            self._GmlTobologyStyles.append(obj)

    def removeGmlTobologyStyles(self, *GmlTobologyStyles):
        for obj in GmlTobologyStyles:
            obj._GmlFeatureStyle = None
            self._GmlTobologyStyles.remove(obj)


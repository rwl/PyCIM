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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlFeatureStyle(IdentifiedObject):
    """Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.
    """

    def __init__(self, semanticTypeIdentifier='', featureType='', version='', featureTypeName='', featureConstraint='', baseType='', queryGrammar="other", GmlGeometryStyles=None, GmlSymbols=None, GmlTobologyStyles=None, GmlLabelStyles=None, GmlFeatureTypes=None, *args, **kw_args):
        """Initialises a new 'GmlFeatureStyle' instance.

        @param semanticTypeIdentifier: The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types. 
        @param featureType: The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features. 
        @param version: Allows version numbers to be identified when the SLD pieces are used independently. 
        @param featureTypeName: Identifies the specific feature type that the feature-type style is for. 
        @param featureConstraint: This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'. 
        @param baseType: Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive. 
        @param queryGrammar: Grammar used in the content of the gml:featureConstraint element. Values are: "other", "xpath", "xquery"
        @param GmlGeometryStyles:
        @param GmlSymbols:
        @param GmlTobologyStyles:
        @param GmlLabelStyles:
        @param GmlFeatureTypes:
        """
        #: The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types.
        self.semanticTypeIdentifier = semanticTypeIdentifier

        #: The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features.
        self.featureType = featureType

        #: Allows version numbers to be identified when the SLD pieces are used independently.
        self.version = version

        #: Identifies the specific feature type that the feature-type style is for.
        self.featureTypeName = featureTypeName

        #: This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'.
        self.featureConstraint = featureConstraint

        #: Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive.
        self.baseType = baseType

        #: Grammar used in the content of the gml:featureConstraint element. Values are: "other", "xpath", "xquery"
        self.queryGrammar = queryGrammar

        self._GmlGeometryStyles = []
        self.GmlGeometryStyles = [] if GmlGeometryStyles is None else GmlGeometryStyles

        self._GmlSymbols = []
        self.GmlSymbols = [] if GmlSymbols is None else GmlSymbols

        self._GmlTobologyStyles = []
        self.GmlTobologyStyles = [] if GmlTobologyStyles is None else GmlTobologyStyles

        self._GmlLabelStyles = []
        self.GmlLabelStyles = [] if GmlLabelStyles is None else GmlLabelStyles

        self._GmlFeatureTypes = []
        self.GmlFeatureTypes = [] if GmlFeatureTypes is None else GmlFeatureTypes

        super(GmlFeatureStyle, self).__init__(*args, **kw_args)

    _attrs = ["semanticTypeIdentifier", "featureType", "version", "featureTypeName", "featureConstraint", "baseType", "queryGrammar"]
    _attr_types = {"semanticTypeIdentifier": str, "featureType": str, "version": str, "featureTypeName": str, "featureConstraint": str, "baseType": str, "queryGrammar": str}
    _defaults = {"semanticTypeIdentifier": '', "featureType": '', "version": '', "featureTypeName": '', "featureConstraint": '', "baseType": '', "queryGrammar": "other"}
    _enums = {"queryGrammar": "QueryGrammarKind"}
    _refs = ["GmlGeometryStyles", "GmlSymbols", "GmlTobologyStyles", "GmlLabelStyles", "GmlFeatureTypes"]
    _many_refs = ["GmlGeometryStyles", "GmlSymbols", "GmlTobologyStyles", "GmlLabelStyles", "GmlFeatureTypes"]

    def getGmlGeometryStyles(self):
        
        return self._GmlGeometryStyles

    def setGmlGeometryStyles(self, value):
        for x in self._GmlGeometryStyles:
            x.GmlFeatureStyle = None
        for y in value:
            y._GmlFeatureStyle = self
        self._GmlGeometryStyles = value

    GmlGeometryStyles = property(getGmlGeometryStyles, setGmlGeometryStyles)

    def addGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj.GmlFeatureStyle = self

    def removeGmlGeometryStyles(self, *GmlGeometryStyles):
        for obj in GmlGeometryStyles:
            obj.GmlFeatureStyle = None

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
            x.GmlFeatureStyle = None
        for y in value:
            y._GmlFeatureStyle = self
        self._GmlTobologyStyles = value

    GmlTobologyStyles = property(getGmlTobologyStyles, setGmlTobologyStyles)

    def addGmlTobologyStyles(self, *GmlTobologyStyles):
        for obj in GmlTobologyStyles:
            obj.GmlFeatureStyle = self

    def removeGmlTobologyStyles(self, *GmlTobologyStyles):
        for obj in GmlTobologyStyles:
            obj.GmlFeatureStyle = None

    def getGmlLabelStyles(self):
        
        return self._GmlLabelStyles

    def setGmlLabelStyles(self, value):
        for x in self._GmlLabelStyles:
            x.GmlFeatureStyle = None
        for y in value:
            y._GmlFeatureStyle = self
        self._GmlLabelStyles = value

    GmlLabelStyles = property(getGmlLabelStyles, setGmlLabelStyles)

    def addGmlLabelStyles(self, *GmlLabelStyles):
        for obj in GmlLabelStyles:
            obj.GmlFeatureStyle = self

    def removeGmlLabelStyles(self, *GmlLabelStyles):
        for obj in GmlLabelStyles:
            obj.GmlFeatureStyle = None

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


#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" The package contains portions of the model defined by graphic standards such as those proposed by OpenGIS Consortium referred to as the Geography Markup Language (GML). It facilitates integration among electric utility applications (CIM) and Geographical Information Systems (GIS) and other applications. Rather than inventing new CIM classes that accomplish similar functionality as in existing GML, the preferred approach is to use and extend 'Gml' classes as appropriate. Note that care has been taken to separate the geometry of features from how features can be graphically represented. GML supports the concept of a geographic feature, which is 'an abstraction of a real world phenomenon; it is a geographic feature if it is associated with a location relative to the Earth'. So a digital representation of the real world can be thought of as a set of features. The state of a feature is defined by a set of properties, where each property can be thought of as a {name, type, value} triple. The number of properties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties that may be geometry-valued.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'A Geographic Feature is 'an abstraction of a real world phenomenon; it is a geographic feature if it can is asociated with a location relative to the Earth. A digital representation of the real world can be thought of as a set of features. He state of a feature is defined by a set of properties, whre each property can be thought of as a (name, type, value) triple. The number of propoerties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties tht may be geometry-valued. Geographic features in GML include coverages and observations as subtypes. A coverage is a type of feature that has a coverage function with a spatial domain and a value  set range of homogeneous 2 to n dimensional tuples. A coverage can represent one feature or a collection of features 'to model and make visible spatial relationships between, and the spatial distribution of, earth phenomena.' A reference system provides a scale of measurement for assigning values to a location, time or other descriptive quantity or quality. A coordinate reference system consists of set of coordinate system axes that are related to the earth through a datum that defines the size and shape of the earth. Geometries in GML indicate the coordinate reference system in which the measurements have ben made. The 'parent' geometry element of a geometric complex or geometric aggregate makes this indication for its constituent geometries.'
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import PositionPoint
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Location
from CIM import Element
from CIM.IEC61970.Domain import FloatQuantity
from CIM.IEC61970.Domain import AngleDegrees



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Float, Date, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of grammar for queries.
QueryGrammarKind = Enum("xpath", "other", "xquery", desc="Kind of grammar for queries.")

#------------------------------------------------------------------------------
#  "GmlPosition" class:
#------------------------------------------------------------------------------

class GmlPosition(PositionPoint):
    """ Position point with a GML coordinate reference system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlCoordinateSystem = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlCoordinateSystem",
        transient=True,
        opposite="GmlPositions",
        editor=InstanceEditor(name="_gmlcoordinatesystems"))

    def _get_gmlcoordinatesystems(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlCoordinateSystem" ]
        else:
            return []

    _gmlcoordinatesystems = Property(fget=_get_gmlcoordinatesystems)

    #--------------------------------------------------------------------------
    #  Begin "GmlPosition" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sequenceNumber", "zPosition", "xPosition", "yPosition",
                label="Attributes"),
            VGroup("Parent", "Location", "GmlCoordinateSystem",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlPosition",
        title="GmlPosition",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlPosition" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlLabelPlacement" class:
#------------------------------------------------------------------------------

class GmlLabelPlacement(IdentifiedObject):
    """ Used to position a label relative to a point or a line.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlTextSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTextSymbol"))

    # Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry.
    type = Str(desc="Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry.")

    # Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0.
    offset = Str(desc="Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0.")

    # X-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
    anchorX = Str(desc="X-coordinate location inside of a label to use for anchoring the label to the main-geometry point.")

    # Clockwise rotation of the label in degrees from the normal direction for a font.
    rotation = Str(desc="Clockwise rotation of the label in degrees from the normal direction for a font.")

    # Y displacement from the main-geometry point to render a text label.
    displacementY = Str(desc="Y displacement from the main-geometry point to render a text label.")

    # X displacement from the main-geometry point to render a text label.
    displacementX = Str(desc="X displacement from the main-geometry point to render a text label.")

    # Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
    anchorY = Str(desc="Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point.")

    #--------------------------------------------------------------------------
    #  Begin "GmlLabelPlacement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "type", "offset", "anchorX", "rotation", "displacementY", "displacementX", "anchorY",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlTextSymbols",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlLabelPlacement",
        title="GmlLabelPlacement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlLabelPlacement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlTopologyStyle" class:
#------------------------------------------------------------------------------

class GmlTopologyStyle(IdentifiedObject):
    """ The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlLableStyle = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlLabelStyle",
        transient=True,
        opposite="GmlTopologyStyles",
        editor=InstanceEditor(name="_gmllabelstyles"))

    def _get_gmllabelstyles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlLabelStyle" ]
        else:
            return []

    _gmllabelstyles = Property(fget=_get_gmllabelstyles)

    GmlFeatureStyle = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle",
        transient=True,
        opposite="GmlTobologyStyles",
        editor=InstanceEditor(name="_gmlfeaturestyles"))

    def _get_gmlfeaturestyles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle" ]
        else:
            return []

    _gmlfeaturestyles = Property(fget=_get_gmlfeaturestyles)

    #--------------------------------------------------------------------------
    #  Begin "GmlTopologyStyle" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlLableStyle", "GmlFeatureStyle",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlTopologyStyle",
        title="GmlTopologyStyle",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlTopologyStyle" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlSvgParameter" class:
#------------------------------------------------------------------------------

class GmlSvgParameter(IdentifiedObject):
    """ Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlStokes = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlStroke"))

    GmlFills = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFill"))

    GmlFonts = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFont"))

    # The SVG/CSS-coded value of the associated SvgAttribute.
    value = Str(desc="The SVG/CSS-coded value of the associated SvgAttribute.")

    # The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported.
    attribute = Str(desc="The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported.")

    #--------------------------------------------------------------------------
    #  Begin "GmlSvgParameter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value", "attribute",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlStokes", "GmlFills", "GmlFonts",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlSvgParameter",
        title="GmlSvgParameter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlSvgParameter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlMark" class:
#------------------------------------------------------------------------------

class GmlMark(IdentifiedObject):
    """ Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFIlls = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFill"))

    GmlGraphics = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlGraphic"))

    GmlStrokes = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlStroke"))

    # Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x.
    wellKnownName = Str(desc="Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x.")

    #--------------------------------------------------------------------------
    #  Begin "GmlMark" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "wellKnownName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFIlls", "GmlGraphics", "GmlStrokes",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlMark",
        title="GmlMark",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlMark" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlFont" class:
#------------------------------------------------------------------------------

class GmlFont(IdentifiedObject):
    """ Identifies a font of a certain family, style, and size.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlTextSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTextSymbol"))

    GmlColour = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlColour",
        transient=True,
        opposite="GmlFonts",
        editor=InstanceEditor(name="_gmlcolours"))

    def _get_gmlcolours(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlColour" ]
        else:
            return []

    _gmlcolours = Property(fget=_get_gmlcolours)

    GmlSvgParameters = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSvgParameter"))

    # True if 'size' is expressed in absolute values. Default is false.
    absoluteSize = Bool(desc="True if 'size' is expressed in absolute values. Default is false.")

    # The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'.
    style = Str(desc="The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'.")

    # The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available.
    size = Str(desc="The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available.")

    # Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order.
    family = Str(desc="Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order.")

    # The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'.
    weight = Str(desc="The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'.")

    #--------------------------------------------------------------------------
    #  Begin "GmlFont" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "absoluteSize", "style", "size", "family", "weight",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlTextSymbols", "GmlColour", "GmlSvgParameters",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlFont",
        title="GmlFont",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlFont" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlSymbol" class:
#------------------------------------------------------------------------------

class GmlSymbol(IdentifiedObject):
    """ Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFeatureStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle"))

    GmlBaseSymbol = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlBaseSymbol",
        transient=True,
        opposite="GmlSymbols",
        editor=InstanceEditor(name="_gmlbasesymbols"))

    def _get_gmlbasesymbols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlBaseSymbol" ]
        else:
            return []

    _gmlbasesymbols = Property(fget=_get_gmlbasesymbols)

    # The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in.
    level = Str(desc="The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in.")

    # The Symbol type.
    type = Str(desc="The Symbol type.")

    # The version of the Symbol.
    version = Str(desc="The version of the Symbol.")

    #--------------------------------------------------------------------------
    #  Begin "GmlSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "level", "type", "version",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles", "GmlBaseSymbol",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlSymbol",
        title="GmlSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlSymbol" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlSelector" class:
#------------------------------------------------------------------------------

class GmlSelector(IdentifiedObject):
    """ A diagram element that allows selection by a user, i.e. as 'hyperNode' for navigating between diagrams, or as composite object representing multiple grouped objects.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    #--------------------------------------------------------------------------
    #  Begin "GmlSelector" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Locations", "ChangeItems",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlSelector",
        title="GmlSelector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlSelector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlGeometryStyle" class:
#------------------------------------------------------------------------------

class GmlGeometryStyle(IdentifiedObject):
    """ The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFeatureStyle = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle",
        transient=True,
        opposite="GmlGeometryStyles",
        editor=InstanceEditor(name="_gmlfeaturestyles"))

    def _get_gmlfeaturestyles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle" ]
        else:
            return []

    _gmlfeaturestyles = Property(fget=_get_gmlfeaturestyles)

    GmlLabelStyle = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlLabelStyle",
        transient=True,
        opposite="GmlGeometryStyles",
        editor=InstanceEditor(name="_gmllabelstyles"))

    def _get_gmllabelstyles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlLabelStyle" ]
        else:
            return []

    _gmllabelstyles = Property(fget=_get_gmllabelstyles)

    # Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing.
    symbol = Str(desc="Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing.")

    # It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value.
    geometryType = Str(desc="It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value.")

    # The name of the geometry property of a feature to which this GeometryStyle applies.
    geometryProperty = Str(desc="The name of the geometry property of a feature to which this GeometryStyle applies.")

    #--------------------------------------------------------------------------
    #  Begin "GmlGeometryStyle" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "symbol", "geometryType", "geometryProperty",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyle", "GmlLabelStyle",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlGeometryStyle",
        title="GmlGeometryStyle",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlGeometryStyle" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlDiagramObject" class:
#------------------------------------------------------------------------------

class GmlDiagramObject(Location):
    """ Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Diagrams = List(Instance("CIM.IEC61968.Informative.InfCommon.Diagram"))

    GmlLineSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlLineSymbol"))

    GmlCoordinateSystems = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlCoordinateSystem"))

    GmlRasterSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlRasterSymbol"))

    GmlPolygonSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlPolygonSymbol"))

    GmlPointSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlPointSymbol"))

    GmlTextSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTextSymbol"))

    #--------------------------------------------------------------------------
    #  Begin "GmlDiagramObject" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "Diagrams", "GmlLineSymbols", "GmlCoordinateSystems", "GmlRasterSymbols", "GmlPolygonSymbols", "GmlPointSymbols", "GmlTextSymbols",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject",
        title="GmlDiagramObject",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlDiagramObject" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlFeatureType" class:
#------------------------------------------------------------------------------

class GmlFeatureType(IdentifiedObject):
    """ Type classification of feature.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFeatureStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle"))

    #--------------------------------------------------------------------------
    #  Begin "GmlFeatureType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureType",
        title="GmlFeatureType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlFeatureType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlHalo" class:
#------------------------------------------------------------------------------

class GmlHalo(IdentifiedObject):
    """ A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlTextSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTextSymbol"))

    # The Radius element gives the absolute size of a halo radius in pixels encoded as a floating-point number. The radius is taken from the outside edge of a font glyph to extend the area of coverage of the glyph (and the inside edge of ?holes? in the glyphs). The default radius is one pixel. Negative values are not allowed.
    radius = Str(desc="The Radius element gives the absolute size of a halo radius in pixels encoded as a floating-point number. The radius is taken from the outside edge of a font glyph to extend the area of coverage of the glyph (and the inside edge of ?holes? in the glyphs). The default radius is one pixel. Negative values are not allowed.")

    # Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = Float(desc="Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0")

    #--------------------------------------------------------------------------
    #  Begin "GmlHalo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "radius", "opacity",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlTextSymbols",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlHalo",
        title="GmlHalo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlHalo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlObservation" class:
#------------------------------------------------------------------------------

class GmlObservation(Element):
    """ A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    GmlValues = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlValue"))

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    # Contains or points to the specimen, region or station which is the object of the observation
    target = Str(desc="Contains or points to the specimen, region or station which is the object of the observation")

    # Contains or points to a description of a sensor, instrument or procedure used for the observation.
    using = Str(desc="Contains or points to a description of a sensor, instrument or procedure used for the observation.")

    dateTime = Date

    # Indicates the result of the observation.
    resultOf = Str(desc="Indicates the result of the observation.")

    #--------------------------------------------------------------------------
    #  Begin "GmlObservation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "target", "using", "dateTime", "resultOf",
                label="Attributes"),
            VGroup("Parent", "ChangeItems", "GmlValues", "Locations",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlObservation",
        title="GmlObservation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlObservation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlBaseSymbol" class:
#------------------------------------------------------------------------------

class GmlBaseSymbol(IdentifiedObject):
    """ Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSymbol"))

    #--------------------------------------------------------------------------
    #  Begin "GmlBaseSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlSymbols",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlBaseSymbol",
        title="GmlBaseSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlBaseSymbol" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlValue" class:
#------------------------------------------------------------------------------

class GmlValue(IdentifiedObject):
    """ Used for direct representation of values.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MeasurementValue = Instance("CIM.IEC61970.Meas.MeasurementValue",
        transient=True,
        opposite="GmlValues",
        editor=InstanceEditor(name="_measurementvalues"))

    def _get_measurementvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Meas.MeasurementValue" ]
        else:
            return []

    _measurementvalues = Property(fget=_get_measurementvalues)

    GmlObservation = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlObservation",
        transient=True,
        opposite="GmlValues",
        editor=InstanceEditor(name="_gmlobservations"))

    def _get_gmlobservations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlObservation" ]
        else:
            return []

    _gmlobservations = Property(fget=_get_gmlobservations)

    value = FloatQuantity

    timePeriod = Str

    dateTime = Date

    #--------------------------------------------------------------------------
    #  Begin "GmlValue" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value", "timePeriod", "dateTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MeasurementValue", "GmlObservation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlValue",
        title="GmlValue",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlValue" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlFill" class:
#------------------------------------------------------------------------------

class GmlFill(IdentifiedObject):
    """ Specifies how the area of the geometry will be filled.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlColour = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlColour",
        transient=True,
        opposite="GmlFills",
        editor=InstanceEditor(name="_gmlcolours"))

    def _get_gmlcolours(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlColour" ]
        else:
            return []

    _gmlcolours = Property(fget=_get_gmlcolours)

    GmlPolygonSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlPolygonSymbol"))

    GmlSvgParameters = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSvgParameter"))

    GmlMarks = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlMark"))

    GmlTextSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTextSymbol"))

    # Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = Float(desc="Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0")

    #--------------------------------------------------------------------------
    #  Begin "GmlFill" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "opacity",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlColour", "GmlPolygonSymbols", "GmlSvgParameters", "GmlMarks", "GmlTextSymbols",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlFill",
        title="GmlFill",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlFill" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlColour" class:
#------------------------------------------------------------------------------

class GmlColour(IdentifiedObject):
    """ The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFills = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFill"))

    GmlFonts = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFont"))

    GmlStrokes = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlStroke"))

    # The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.).
    blue = Str(desc="The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.).")

    # The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)
    green = Str(desc="The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)")

    # The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)
    red = Str(desc="The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.)")

    #--------------------------------------------------------------------------
    #  Begin "GmlColour" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "blue", "green", "red",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFills", "GmlFonts", "GmlStrokes",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlColour",
        title="GmlColour",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlColour" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlLabelStyle" class:
#------------------------------------------------------------------------------

class GmlLabelStyle(IdentifiedObject):
    """ The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlGeometryStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlGeometryStyle"))

    GmlFeatureStyle = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle",
        transient=True,
        opposite="GmlLabelStyles",
        editor=InstanceEditor(name="_gmlfeaturestyles"))

    def _get_gmlfeaturestyles(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle" ]
        else:
            return []

    _gmlfeaturestyles = Property(fget=_get_gmlfeaturestyles)

    GmlTopologyStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTopologyStyle"))

    # Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute).
    transform = Str(desc="Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute).")

    # Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties.
    style = Str(desc="Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties.")

    # Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature.
    labelExpression = Str(desc="Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature.")

    #--------------------------------------------------------------------------
    #  Begin "GmlLabelStyle" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "transform", "style", "labelExpression",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlGeometryStyles", "GmlFeatureStyle", "GmlTopologyStyles",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlLabelStyle",
        title="GmlLabelStyle",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlLabelStyle" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlGraphic" class:
#------------------------------------------------------------------------------

class GmlGraphic(IdentifiedObject):
    """ A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlMarks = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlMark"))

    GmlPointSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlPointSymbol"))

    # Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar).
    xScale = Float(desc="Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar).")

    # Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed.
    size = Int(desc="Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed.")

    # Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars).
    yScale = Float(desc="Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars).")

    # Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = Float(desc="Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0")

    # The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with.
    symbolID = Str(desc="The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with.")

    # Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid.
    rotation = AngleDegrees(desc="Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid.")

    # The minimum symbol size allowed.
    minSize = Int(desc="The minimum symbol size allowed.")

    #--------------------------------------------------------------------------
    #  Begin "GmlGraphic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "xScale", "size", "yScale", "opacity", "symbolID", "rotation", "minSize",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlMarks", "GmlPointSymbols",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlGraphic",
        title="GmlGraphic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlGraphic" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlStroke" class:
#------------------------------------------------------------------------------

class GmlStroke(IdentifiedObject):
    """ The element encapsulating the graphical symbolization parameters for linear geometries.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlSvgParameters = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSvgParameter"))

    GmlLineSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlLineSymbol"))

    GmlMarks = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlMark"))

    GmlColour = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlColour",
        transient=True,
        opposite="GmlStrokes",
        editor=InstanceEditor(name="_gmlcolours"))

    def _get_gmlcolours(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlColour" ]
        else:
            return []

    _gmlcolours = Property(fget=_get_gmlcolours)

    GmlPolygonSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlPolygonSymbol"))

    # Specifies the level of translucency to use when rendering the stroke. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
    opacity = Float(desc="Specifies the level of translucency to use when rendering the stroke. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0")

    # Enumerated values telling how line strings should be joined (between line segments). The values are represented as content strings.  The allowed values for line join are 'mitre', 'round', and 'bevel'. The default values are system-dependent.
    linejoin = Str(desc="Enumerated values telling how line strings should be joined (between line segments). The values are represented as content strings.  The allowed values for line join are 'mitre', 'round', and 'bevel'. The default values are system-dependent.")

    # Specifies the distance as a float into the 'stroke-dasharray' pattern at which to start drawing.
    dashOffset = Str(desc="Specifies the distance as a float into the 'stroke-dasharray' pattern at which to start drawing.")

    # Encodes a dash pattern as a series of space separated floats. The first number gives the length in pixels of dash to draw, the second gives the amount of space to leave, and this pattern repeats. If an odd number of values is given, then the pattern is expanded by repeating it twice to give an even number of values. Decimal values have a system-dependent interpretation (usually depending on whether antialiasing is being used). The default is to draw an unbroken line.
    dashArray = Str(desc="Encodes a dash pattern as a series of space separated floats. The first number gives the length in pixels of dash to draw, the second gives the amount of space to leave, and this pattern repeats. If an odd number of values is given, then the pattern is expanded by repeating it twice to give an even number of values. Decimal values have a system-dependent interpretation (usually depending on whether antialiasing is being used). The default is to draw an unbroken line.")

    # The absolute width (thickness) of a stroke in pixels encoded as a float. The default is 1.0. Fractional numbers are allowed (with a system-dependent interpretation) but negative numbers are not.
    width = Float(desc="The absolute width (thickness) of a stroke in pixels encoded as a float. The default is 1.0. Fractional numbers are allowed (with a system-dependent interpretation) but negative numbers are not.")

    # Enumerated values telling how line strings should be capped (at the two ends of the line string). The values are represented as content strings.  The allowed values for line cap are 'butt', 'round', and 'square'. The default values are system-dependent.
    lineCap = Str(desc="Enumerated values telling how line strings should be capped (at the two ends of the line string). The values are represented as content strings.  The allowed values for line cap are 'butt', 'round', and 'square'. The default values are system-dependent.")

    # The name of a defined line style. Usually will be an enumerated value and will be system-specific.
    lineStyle = Str(desc="The name of a defined line style. Usually will be an enumerated value and will be system-specific.")

    #--------------------------------------------------------------------------
    #  Begin "GmlStroke" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "opacity", "linejoin", "dashOffset", "dashArray", "width", "lineCap", "lineStyle",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlSvgParameters", "GmlLineSymbols", "GmlMarks", "GmlColour", "GmlPolygonSymbols",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlStroke",
        title="GmlStroke",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlStroke" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlCoordinateSystem" class:
#------------------------------------------------------------------------------

class GmlCoordinateSystem(IdentifiedObject):
    """ A coordinate reference system consists of a set of coordinate system axes that is related to the earth through a datum that defines the size and shape of the earth or some abstract reference system such as those used for rendering schemantic diagrams, internal views of items such as cabinets, vaults, etc. Geometries in GML indicate the coordinate reference system in which their measurements have been made.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlPositions = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlPosition"))

    GmlDiagramObjects = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject"))

    Diagrams = List(Instance("CIM.IEC61968.Informative.InfCommon.Diagram"))

    positionUnitName = Str

    # If applicable, the maximum position allowed along the Z axis of the coordinate reference system.
    zMax = Str(desc="If applicable, the maximum position allowed along the Z axis of the coordinate reference system.")

    # The maximum position allowed along the Y axis of the coordinate reference system.
    yMax = Str(desc="The maximum position allowed along the Y axis of the coordinate reference system.")

    # If applicable, the minimum position allowed along the Z axis of the coordinate reference system.
    zMin = Str(desc="If applicable, the minimum position allowed along the Z axis of the coordinate reference system.")

    # The minimum position allowed along the Y axis of the coordinate reference system.
    yMin = Str(desc="The minimum position allowed along the Y axis of the coordinate reference system.")

    # The minimum position allowed along the X axis of the coordinate reference system.
    xMin = Str(desc="The minimum position allowed along the X axis of the coordinate reference system.")

    scale = Str

    # The maximum position allowed along the X axis of the coordinate reference system.
    xMax = Str(desc="The maximum position allowed along the X axis of the coordinate reference system.")

    #--------------------------------------------------------------------------
    #  Begin "GmlCoordinateSystem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "positionUnitName", "zMax", "yMax", "zMin", "yMin", "xMin", "scale", "xMax",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlPositions", "GmlDiagramObjects", "Diagrams",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlCoordinateSystem",
        title="GmlCoordinateSystem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlCoordinateSystem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlFeatureStyle" class:
#------------------------------------------------------------------------------

class GmlFeatureStyle(IdentifiedObject):
    """ Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlGeometryStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlGeometryStyle"))

    GmlFeatureTypes = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureType"))

    GmlLabelStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlLabelStyle"))

    GmlSymbols = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSymbol"))

    GmlTobologyStyles = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlTopologyStyle"))

    # Grammar used in the content of the gml:featureConstraint element.
    queryGrammar = QueryGrammarKind(desc="Grammar used in the content of the gml:featureConstraint element.")

    # Allows version numbers to be identified when the SLD pieces are used independently.
    version = Str(desc="Allows version numbers to be identified when the SLD pieces are used independently.")

    # Identifies the specific feature type that the feature-type style is for.
    featureTypeName = Str(desc="Identifies the specific feature type that the feature-type style is for.")

    # Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive.
    baseType = Str(desc="Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive.")

    # The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features.
    featureType = Str(desc="The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features.")

    # The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types.
    semanticTypeIdentifier = Str(desc="The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types.")

    # This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'.
    featureConstraint = Str(desc="This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'.")

    #--------------------------------------------------------------------------
    #  Begin "GmlFeatureStyle" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "queryGrammar", "version", "featureTypeName", "baseType", "featureType", "semanticTypeIdentifier", "featureConstraint",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlGeometryStyles", "GmlFeatureTypes", "GmlLabelStyles", "GmlSymbols", "GmlTobologyStyles",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlFeatureStyle",
        title="GmlFeatureStyle",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlFeatureStyle" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlPointSymbol" class:
#------------------------------------------------------------------------------

class GmlPointSymbol(GmlSymbol):
    """ Used to draw a 'graphic' at a point.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlGraphic = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlGraphic",
        transient=True,
        opposite="GmlPointSymbols",
        editor=InstanceEditor(name="_gmlgraphics"))

    def _get_gmlgraphics(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlGraphic" ]
        else:
            return []

    _gmlgraphics = Property(fget=_get_gmlgraphics)

    GmlDiagramObject = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject",
        transient=True,
        opposite="GmlPointSymbols",
        editor=InstanceEditor(name="_gmldiagramobjects"))

    def _get_gmldiagramobjects(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject" ]
        else:
            return []

    _gmldiagramobjects = Property(fget=_get_gmldiagramobjects)

    #--------------------------------------------------------------------------
    #  Begin "GmlPointSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "level", "type", "version",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles", "GmlBaseSymbol", "GmlGraphic", "GmlDiagramObject",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlPointSymbol",
        title="GmlPointSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlPointSymbol" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlPolygonGeometry" class:
#------------------------------------------------------------------------------

class GmlPolygonGeometry(GmlDiagramObject):
    """ Used to show the footprint of substations, sites, service territories, tax districts, school districts, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GmlPolygonGeometry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "Diagrams", "GmlLineSymbols", "GmlCoordinateSystems", "GmlRasterSymbols", "GmlPolygonSymbols", "GmlPointSymbols", "GmlTextSymbols",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlPolygonGeometry",
        title="GmlPolygonGeometry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlPolygonGeometry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlPolygonSymbol" class:
#------------------------------------------------------------------------------

class GmlPolygonSymbol(GmlSymbol):
    """ Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFill = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFill",
        transient=True,
        opposite="GmlPolygonSymbols",
        editor=InstanceEditor(name="_gmlfills"))

    def _get_gmlfills(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlFill" ]
        else:
            return []

    _gmlfills = Property(fget=_get_gmlfills)

    GmlDiagramObject = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject",
        transient=True,
        opposite="GmlPolygonSymbols",
        editor=InstanceEditor(name="_gmldiagramobjects"))

    def _get_gmldiagramobjects(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject" ]
        else:
            return []

    _gmldiagramobjects = Property(fget=_get_gmldiagramobjects)

    GmlStroke = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlStroke",
        transient=True,
        opposite="GmlPolygonSymbols",
        editor=InstanceEditor(name="_gmlstrokes"))

    def _get_gmlstrokes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlStroke" ]
        else:
            return []

    _gmlstrokes = Property(fget=_get_gmlstrokes)

    #--------------------------------------------------------------------------
    #  Begin "GmlPolygonSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "level", "type", "version",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles", "GmlBaseSymbol", "GmlFill", "GmlDiagramObject", "GmlStroke",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlPolygonSymbol",
        title="GmlPolygonSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlPolygonSymbol" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlLineSymbol" class:
#------------------------------------------------------------------------------

class GmlLineSymbol(GmlSymbol):
    """ Used to style a 'stroke' along a linear geometry type, such as a string of line segments.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlDiagramObject = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject",
        transient=True,
        opposite="GmlLineSymbols",
        editor=InstanceEditor(name="_gmldiagramobjects"))

    def _get_gmldiagramobjects(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject" ]
        else:
            return []

    _gmldiagramobjects = Property(fget=_get_gmldiagramobjects)

    GmlStroke = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlStroke",
        transient=True,
        opposite="GmlLineSymbols",
        editor=InstanceEditor(name="_gmlstrokes"))

    def _get_gmlstrokes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlStroke" ]
        else:
            return []

    _gmlstrokes = Property(fget=_get_gmlstrokes)

    # For dynamic network update (i.e. colouring) purposes
    sourceSide = Str(desc="For dynamic network update (i.e. colouring) purposes")

    #--------------------------------------------------------------------------
    #  Begin "GmlLineSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "level", "type", "version", "sourceSide",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles", "GmlBaseSymbol", "GmlDiagramObject", "GmlStroke",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlLineSymbol",
        title="GmlLineSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlLineSymbol" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlPointGeometry" class:
#------------------------------------------------------------------------------

class GmlPointGeometry(GmlDiagramObject):
    """ Typically used for rendering power system resources and/or point assets.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GmlPointGeometry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "Diagrams", "GmlLineSymbols", "GmlCoordinateSystems", "GmlRasterSymbols", "GmlPolygonSymbols", "GmlPointSymbols", "GmlTextSymbols",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlPointGeometry",
        title="GmlPointGeometry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlPointGeometry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlRasterSymbol" class:
#------------------------------------------------------------------------------

class GmlRasterSymbol(GmlSymbol):
    """ Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlDiagramObject = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject",
        transient=True,
        opposite="GmlRasterSymbols",
        editor=InstanceEditor(name="_gmldiagramobjects"))

    def _get_gmldiagramobjects(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject" ]
        else:
            return []

    _gmldiagramobjects = Property(fget=_get_gmldiagramobjects)

    # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    greenSourceName = Str(desc="Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.")

    # If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers.
    brighnessOnly = Bool(desc="If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers.")

    # The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent.
    reliefFactor = Str(desc="The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent.")

    # Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes.
    overlapbehaviour = Str(desc="Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes.")

    # A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    graySourcename = Str(desc="A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.")

    # Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0.
    opacity = Float(desc="Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0.")

    # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    redSourcename = Str(desc="Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.")

    # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
    blueSourcename = Str(desc="Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.")

    #--------------------------------------------------------------------------
    #  Begin "GmlRasterSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "level", "type", "version", "greenSourceName", "brighnessOnly", "reliefFactor", "overlapbehaviour", "graySourcename", "opacity", "redSourcename", "blueSourcename",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles", "GmlBaseSymbol", "GmlDiagramObject",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlRasterSymbol",
        title="GmlRasterSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlRasterSymbol" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlLineGeometry" class:
#------------------------------------------------------------------------------

class GmlLineGeometry(GmlDiagramObject):
    """ Typically used for rendering linear assets and/or power system resources.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # For dynamic network update (i.e. colouring) purposes
    sourceSide = Str(desc="For dynamic network update (i.e. colouring) purposes")

    #--------------------------------------------------------------------------
    #  Begin "GmlLineGeometry" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference", "sourceSide",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "Diagrams", "GmlLineSymbols", "GmlCoordinateSystems", "GmlRasterSymbols", "GmlPolygonSymbols", "GmlPointSymbols", "GmlTextSymbols",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlLineGeometry",
        title="GmlLineGeometry",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlLineGeometry" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GmlTextSymbol" class:
#------------------------------------------------------------------------------

class GmlTextSymbol(GmlSymbol):
    """ Used for styling text labels, i.e., for rendering them according to various graphical parameters.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GmlFont = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFont",
        transient=True,
        opposite="GmlTextSymbols",
        editor=InstanceEditor(name="_gmlfonts"))

    def _get_gmlfonts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlFont" ]
        else:
            return []

    _gmlfonts = Property(fget=_get_gmlfonts)

    GmlLabelPlacement = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlLabelPlacement",
        transient=True,
        opposite="GmlTextSymbols",
        editor=InstanceEditor(name="_gmllabelplacements"))

    def _get_gmllabelplacements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlLabelPlacement" ]
        else:
            return []

    _gmllabelplacements = Property(fget=_get_gmllabelplacements)

    GmlFill = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlFill",
        transient=True,
        opposite="GmlTextSymbols",
        editor=InstanceEditor(name="_gmlfills"))

    def _get_gmlfills(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlFill" ]
        else:
            return []

    _gmlfills = Property(fget=_get_gmlfills)

    GmlHalo = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlHalo",
        transient=True,
        opposite="GmlTextSymbols",
        editor=InstanceEditor(name="_gmlhalos"))

    def _get_gmlhalos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlHalo" ]
        else:
            return []

    _gmlhalos = Property(fget=_get_gmlhalos)

    GmlDiagramObject = Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject",
        transient=True,
        opposite="GmlTextSymbols",
        editor=InstanceEditor(name="_gmldiagramobjects"))

    def _get_gmldiagramobjects(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfGMLSupport.GmlDiagramObject" ]
        else:
            return []

    _gmldiagramobjects = Property(fget=_get_gmldiagramobjects)

    # The minimum font size allowed.
    minFontSize = Int(desc="The minimum font size allowed.")

    # Generic method for capturing all unspecified information pertaining to the TextSymbol.
    property = Str(desc="Generic method for capturing all unspecified information pertaining to the TextSymbol.")

    # The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc.
    fieldID = Str(desc="The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc.")

    # Text-label content. If the value is not provided, then no text will be rendered.
    label = Str(desc="Text-label content. If the value is not provided, then no text will be rendered.")

    # The type-classification of a label.
    labelType = Str(desc="The type-classification of a label.")

    #--------------------------------------------------------------------------
    #  Begin "GmlTextSymbol" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "level", "type", "version", "minFontSize", "property", "fieldID", "label", "labelType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "GmlFeatureStyles", "GmlBaseSymbol", "GmlFont", "GmlLabelPlacement", "GmlFill", "GmlHalo", "GmlDiagramObject",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfGMLSupport.GmlTextSymbol",
        title="GmlTextSymbol",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GmlTextSymbol" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------

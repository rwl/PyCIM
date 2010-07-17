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

""" The package contains portions of the model defined by graphic standards such as those proposed by OpenGIS Consortium referred to as the Geography Markup Language (GML). It facilitates integration among electric utility applications (CIM) and Geographical Information Systems (GIS) and other applications. Rather than inventing new CIM classes that accomplish similar functionality as in existing GML, the preferred approach is to use and extend 'Gml' classes as appropriate. Note that care has been taken to separate the geometry of features from how features can be graphically represented. GML supports the concept of a geographic feature, which is 'an abstraction of a real world phenomenon; it is a geographic feature if it is associated with a location relative to the Earth'. So a digital representation of the real world can be thought of as a set of features. The state of a feature is defined by a set of properties, where each property can be thought of as a {name, type, value} triple. The number of properties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties that may be geometry-valued.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'A Geographic Feature is 'an abstraction of a real world phenomenon; it is a geographic feature if it can is asociated with a location relative to the Earth. A digital representation of the real world can be thought of as a set of features. He state of a feature is defined by a set of properties, whre each property can be thought of as a (name, type, value) triple. The number of propoerties a feature may have, together with their names and types, are determined by its type definition. Geographic features with geometry are those with properties tht may be geometry-valued. Geographic features in GML include coverages and observations as subtypes. A coverage is a type of feature that has a coverage function with a spatial domain and a value  set range of homogeneous 2 to n dimensional tuples. A coverage can represent one feature or a collection of features 'to model and make visible spatial relationships between, and the spatial distribution of, earth phenomena.' A reference system provides a scale of measurement for assigning values to a location, time or other descriptive quantity or quality. A coordinate reference system consists of set of coordinate system axes that are related to the earth through a datum that defines the size and shape of the earth. Geometries in GML indicate the coordinate reference system in which the measurements have ben made. The 'parent' geometry element of a geometric complex or geometric aggregate makes this indication for its constituent geometries.'
"""

from cim.iec61968.common import PositionPoint
from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Location
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infgmlsupport"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfGMLSupport"

class GmlPosition(PositionPoint):
    """ Position point with a GML coordinate reference system.
    """
    # <<< gml_position
    # @generated
    def __init__(self, gml_coordinate_system=None, **kw_args):
        """ Initialises a new 'GmlPosition' instance.
        """

        self._gml_coordinate_system = None
        self.gml_coordinate_system = gml_coordinate_system


        super(GmlPosition, self).__init__(**kw_args)
    # >>> gml_position

    # <<< gml_coordinate_system
    # @generated
    def get_gml_coordinate_system(self):
        """ 
        """
        return self._gml_coordinate_system

    def set_gml_coordinate_system(self, value):
        if self._gml_coordinate_system is not None:
            filtered = [x for x in self.gml_coordinate_system.gml_positions if x != self]
            self._gml_coordinate_system._gml_positions = filtered

        self._gml_coordinate_system = value
        if self._gml_coordinate_system is not None:
            self._gml_coordinate_system._gml_positions.append(self)

    gml_coordinate_system = property(get_gml_coordinate_system, set_gml_coordinate_system)
    # >>> gml_coordinate_system


    def __str__(self):
        """ Returns a string representation of the GmlPosition.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_position.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlPosition.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlPosition", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_coordinate_system is not None:
            s += '%s<%s:GmlPosition.gml_coordinate_system rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_coordinate_system.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.location is not None:
            s += '%s<%s:PositionPoint.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        s += '%s<%s:PositionPoint.sequence_number>%s</%s:PositionPoint.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:PositionPoint.z_position>%s</%s:PositionPoint.z_position>' % \
            (indent, ns_prefix, self.z_position, ns_prefix)
        s += '%s<%s:PositionPoint.x_position>%s</%s:PositionPoint.x_position>' % \
            (indent, ns_prefix, self.x_position, ns_prefix)
        s += '%s<%s:PositionPoint.y_position>%s</%s:PositionPoint.y_position>' % \
            (indent, ns_prefix, self.y_position, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlPosition")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_position.serialize


class GmlLabelPlacement(IdentifiedObject):
    """ Used to position a label relative to a point or a line.
    """
    # <<< gml_label_placement
    # @generated
    def __init__(self, type='', offset='', anchor_x='', rotation='', displacement_y='', displacement_x='', anchor_y='', gml_text_symbols=None, **kw_args):
        """ Initialises a new 'GmlLabelPlacement' instance.
        """
        # Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry. 
        self.type = type

        # Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0. 
        self.offset = offset

        # X-coordinate location inside of a label to use for anchoring the label to the main-geometry point. 
        self.anchor_x = anchor_x

        # Clockwise rotation of the label in degrees from the normal direction for a font. 
        self.rotation = rotation

        # Y displacement from the main-geometry point to render a text label. 
        self.displacement_y = displacement_y

        # X displacement from the main-geometry point to render a text label. 
        self.displacement_x = displacement_x

        # Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point. 
        self.anchor_y = anchor_y


        self._gml_text_symbols = []
        if gml_text_symbols is not None:
            self.gml_text_symbols = gml_text_symbols
        else:
            self.gml_text_symbols = []


        super(GmlLabelPlacement, self).__init__(**kw_args)
    # >>> gml_label_placement

    # <<< gml_text_symbols
    # @generated
    def get_gml_text_symbols(self):
        """ 
        """
        return self._gml_text_symbols

    def set_gml_text_symbols(self, value):
        for x in self._gml_text_symbols:
            x._gml_label_placement = None
        for y in value:
            y._gml_label_placement = self
        self._gml_text_symbols = value

    gml_text_symbols = property(get_gml_text_symbols, set_gml_text_symbols)

    def add_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_label_placement = self
            self._gml_text_symbols.append(obj)

    def remove_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_label_placement = None
            self._gml_text_symbols.remove(obj)
    # >>> gml_text_symbols


    def __str__(self):
        """ Returns a string representation of the GmlLabelPlacement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_label_placement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlLabelPlacement.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlLabelPlacement", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlLabelPlacement.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlLabelPlacement.type>%s</%s:GmlLabelPlacement.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlLabelPlacement.offset>%s</%s:GmlLabelPlacement.offset>' % \
            (indent, ns_prefix, self.offset, ns_prefix)
        s += '%s<%s:GmlLabelPlacement.anchor_x>%s</%s:GmlLabelPlacement.anchor_x>' % \
            (indent, ns_prefix, self.anchor_x, ns_prefix)
        s += '%s<%s:GmlLabelPlacement.rotation>%s</%s:GmlLabelPlacement.rotation>' % \
            (indent, ns_prefix, self.rotation, ns_prefix)
        s += '%s<%s:GmlLabelPlacement.displacement_y>%s</%s:GmlLabelPlacement.displacement_y>' % \
            (indent, ns_prefix, self.displacement_y, ns_prefix)
        s += '%s<%s:GmlLabelPlacement.displacement_x>%s</%s:GmlLabelPlacement.displacement_x>' % \
            (indent, ns_prefix, self.displacement_x, ns_prefix)
        s += '%s<%s:GmlLabelPlacement.anchor_y>%s</%s:GmlLabelPlacement.anchor_y>' % \
            (indent, ns_prefix, self.anchor_y, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlLabelPlacement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_label_placement.serialize


class GmlTopologyStyle(IdentifiedObject):
    """ The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.
    """
    # <<< gml_topology_style
    # @generated
    def __init__(self, gml_lable_style=None, gml_feature_style=None, **kw_args):
        """ Initialises a new 'GmlTopologyStyle' instance.
        """

        self._gml_lable_style = None
        self.gml_lable_style = gml_lable_style

        self._gml_feature_style = None
        self.gml_feature_style = gml_feature_style


        super(GmlTopologyStyle, self).__init__(**kw_args)
    # >>> gml_topology_style

    # <<< gml_lable_style
    # @generated
    def get_gml_lable_style(self):
        """ 
        """
        return self._gml_lable_style

    def set_gml_lable_style(self, value):
        if self._gml_lable_style is not None:
            filtered = [x for x in self.gml_lable_style.gml_topology_styles if x != self]
            self._gml_lable_style._gml_topology_styles = filtered

        self._gml_lable_style = value
        if self._gml_lable_style is not None:
            self._gml_lable_style._gml_topology_styles.append(self)

    gml_lable_style = property(get_gml_lable_style, set_gml_lable_style)
    # >>> gml_lable_style

    # <<< gml_feature_style
    # @generated
    def get_gml_feature_style(self):
        """ 
        """
        return self._gml_feature_style

    def set_gml_feature_style(self, value):
        if self._gml_feature_style is not None:
            filtered = [x for x in self.gml_feature_style.gml_tobology_styles if x != self]
            self._gml_feature_style._gml_tobology_styles = filtered

        self._gml_feature_style = value
        if self._gml_feature_style is not None:
            self._gml_feature_style._gml_tobology_styles.append(self)

    gml_feature_style = property(get_gml_feature_style, set_gml_feature_style)
    # >>> gml_feature_style


    def __str__(self):
        """ Returns a string representation of the GmlTopologyStyle.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_topology_style.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlTopologyStyle.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlTopologyStyle", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_lable_style is not None:
            s += '%s<%s:GmlTopologyStyle.gml_lable_style rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_lable_style.uri)
        if self.gml_feature_style is not None:
            s += '%s<%s:GmlTopologyStyle.gml_feature_style rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_feature_style.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlTopologyStyle")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_topology_style.serialize


class GmlSvgParameter(IdentifiedObject):
    """ Refers to an SVG/CSS graphical-formatting parameter. The parameter is identified using the 'name' attribute and the content of the element gives the SVG/CSS-coded value.
    """
    # <<< gml_svg_parameter
    # @generated
    def __init__(self, value='', attribute='', gml_stokes=None, gml_fills=None, gml_fonts=None, **kw_args):
        """ Initialises a new 'GmlSvgParameter' instance.
        """
        # The SVG/CSS-coded value of the associated SvgAttribute. 
        self.value = value

        # The attribute of the GmlSvgParameter. E.g., for 'Stroke', the following SvgParameters may be used: 'stroke' (color), 'stroke-opacity', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-dasharray', and 'stroke-dashoffset'. Others are not officially supported. 
        self.attribute = attribute


        self._gml_stokes = []
        if gml_stokes is not None:
            self.gml_stokes = gml_stokes
        else:
            self.gml_stokes = []

        self._gml_fills = []
        if gml_fills is not None:
            self.gml_fills = gml_fills
        else:
            self.gml_fills = []

        self._gml_fonts = []
        if gml_fonts is not None:
            self.gml_fonts = gml_fonts
        else:
            self.gml_fonts = []


        super(GmlSvgParameter, self).__init__(**kw_args)
    # >>> gml_svg_parameter

    # <<< gml_stokes
    # @generated
    def get_gml_stokes(self):
        """ 
        """
        return self._gml_stokes

    def set_gml_stokes(self, value):
        for p in self._gml_stokes:
            filtered = [q for q in p.gml_svg_parameters if q != self]
            self._gml_stokes._gml_svg_parameters = filtered
        for r in value:
            if self not in r._gml_svg_parameters:
                r._gml_svg_parameters.append(self)
        self._gml_stokes = value

    gml_stokes = property(get_gml_stokes, set_gml_stokes)

    def add_gml_stokes(self, *gml_stokes):
        for obj in gml_stokes:
            if self not in obj._gml_svg_parameters:
                obj._gml_svg_parameters.append(self)
            self._gml_stokes.append(obj)

    def remove_gml_stokes(self, *gml_stokes):
        for obj in gml_stokes:
            if self in obj._gml_svg_parameters:
                obj._gml_svg_parameters.remove(self)
            self._gml_stokes.remove(obj)
    # >>> gml_stokes

    # <<< gml_fills
    # @generated
    def get_gml_fills(self):
        """ 
        """
        return self._gml_fills

    def set_gml_fills(self, value):
        for p in self._gml_fills:
            filtered = [q for q in p.gml_svg_parameters if q != self]
            self._gml_fills._gml_svg_parameters = filtered
        for r in value:
            if self not in r._gml_svg_parameters:
                r._gml_svg_parameters.append(self)
        self._gml_fills = value

    gml_fills = property(get_gml_fills, set_gml_fills)

    def add_gml_fills(self, *gml_fills):
        for obj in gml_fills:
            if self not in obj._gml_svg_parameters:
                obj._gml_svg_parameters.append(self)
            self._gml_fills.append(obj)

    def remove_gml_fills(self, *gml_fills):
        for obj in gml_fills:
            if self in obj._gml_svg_parameters:
                obj._gml_svg_parameters.remove(self)
            self._gml_fills.remove(obj)
    # >>> gml_fills

    # <<< gml_fonts
    # @generated
    def get_gml_fonts(self):
        """ 
        """
        return self._gml_fonts

    def set_gml_fonts(self, value):
        for p in self._gml_fonts:
            filtered = [q for q in p.gml_svg_parameters if q != self]
            self._gml_fonts._gml_svg_parameters = filtered
        for r in value:
            if self not in r._gml_svg_parameters:
                r._gml_svg_parameters.append(self)
        self._gml_fonts = value

    gml_fonts = property(get_gml_fonts, set_gml_fonts)

    def add_gml_fonts(self, *gml_fonts):
        for obj in gml_fonts:
            if self not in obj._gml_svg_parameters:
                obj._gml_svg_parameters.append(self)
            self._gml_fonts.append(obj)

    def remove_gml_fonts(self, *gml_fonts):
        for obj in gml_fonts:
            if self in obj._gml_svg_parameters:
                obj._gml_svg_parameters.remove(self)
            self._gml_fonts.remove(obj)
    # >>> gml_fonts


    def __str__(self):
        """ Returns a string representation of the GmlSvgParameter.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_svg_parameter.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlSvgParameter.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlSvgParameter", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_stokes:
            s += '%s<%s:GmlSvgParameter.gml_stokes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_fills:
            s += '%s<%s:GmlSvgParameter.gml_fills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_fonts:
            s += '%s<%s:GmlSvgParameter.gml_fonts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlSvgParameter.value>%s</%s:GmlSvgParameter.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:GmlSvgParameter.attribute>%s</%s:GmlSvgParameter.attribute>' % \
            (indent, ns_prefix, self.attribute, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlSvgParameter")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_svg_parameter.serialize


class GmlMark(IdentifiedObject):
    """ Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).
    """
    # <<< gml_mark
    # @generated
    def __init__(self, well_known_name='', gml_fills=None, gml_graphics=None, gml_strokes=None, **kw_args):
        """ Initialises a new 'GmlMark' instance.
        """
        # Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x. 
        self.well_known_name = well_known_name


        self._gml_fills = []
        if gml_fills is not None:
            self.gml_fills = gml_fills
        else:
            self.gml_fills = []

        self._gml_graphics = []
        if gml_graphics is not None:
            self.gml_graphics = gml_graphics
        else:
            self.gml_graphics = []

        self._gml_strokes = []
        if gml_strokes is not None:
            self.gml_strokes = gml_strokes
        else:
            self.gml_strokes = []


        super(GmlMark, self).__init__(**kw_args)
    # >>> gml_mark

    # <<< gml_fills
    # @generated
    def get_gml_fills(self):
        """ 
        """
        return self._gml_fills

    def set_gml_fills(self, value):
        for p in self._gml_fills:
            filtered = [q for q in p.gml_marks if q != self]
            self._gml_fills._gml_marks = filtered
        for r in value:
            if self not in r._gml_marks:
                r._gml_marks.append(self)
        self._gml_fills = value

    gml_fills = property(get_gml_fills, set_gml_fills)

    def add_gml_fills(self, *gml_fills):
        for obj in gml_fills:
            if self not in obj._gml_marks:
                obj._gml_marks.append(self)
            self._gml_fills.append(obj)

    def remove_gml_fills(self, *gml_fills):
        for obj in gml_fills:
            if self in obj._gml_marks:
                obj._gml_marks.remove(self)
            self._gml_fills.remove(obj)
    # >>> gml_fills

    # <<< gml_graphics
    # @generated
    def get_gml_graphics(self):
        """ 
        """
        return self._gml_graphics

    def set_gml_graphics(self, value):
        for p in self._gml_graphics:
            filtered = [q for q in p.gml_marks if q != self]
            self._gml_graphics._gml_marks = filtered
        for r in value:
            if self not in r._gml_marks:
                r._gml_marks.append(self)
        self._gml_graphics = value

    gml_graphics = property(get_gml_graphics, set_gml_graphics)

    def add_gml_graphics(self, *gml_graphics):
        for obj in gml_graphics:
            if self not in obj._gml_marks:
                obj._gml_marks.append(self)
            self._gml_graphics.append(obj)

    def remove_gml_graphics(self, *gml_graphics):
        for obj in gml_graphics:
            if self in obj._gml_marks:
                obj._gml_marks.remove(self)
            self._gml_graphics.remove(obj)
    # >>> gml_graphics

    # <<< gml_strokes
    # @generated
    def get_gml_strokes(self):
        """ 
        """
        return self._gml_strokes

    def set_gml_strokes(self, value):
        for p in self._gml_strokes:
            filtered = [q for q in p.gml_marks if q != self]
            self._gml_strokes._gml_marks = filtered
        for r in value:
            if self not in r._gml_marks:
                r._gml_marks.append(self)
        self._gml_strokes = value

    gml_strokes = property(get_gml_strokes, set_gml_strokes)

    def add_gml_strokes(self, *gml_strokes):
        for obj in gml_strokes:
            if self not in obj._gml_marks:
                obj._gml_marks.append(self)
            self._gml_strokes.append(obj)

    def remove_gml_strokes(self, *gml_strokes):
        for obj in gml_strokes:
            if self in obj._gml_marks:
                obj._gml_marks.remove(self)
            self._gml_strokes.remove(obj)
    # >>> gml_strokes


    def __str__(self):
        """ Returns a string representation of the GmlMark.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_mark.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlMark.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlMark", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_fills:
            s += '%s<%s:GmlMark.gml_fills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_graphics:
            s += '%s<%s:GmlMark.gml_graphics rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_strokes:
            s += '%s<%s:GmlMark.gml_strokes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlMark.well_known_name>%s</%s:GmlMark.well_known_name>' % \
            (indent, ns_prefix, self.well_known_name, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlMark")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_mark.serialize


class GmlFont(IdentifiedObject):
    """ Identifies a font of a certain family, style, and size.
    """
    # <<< gml_font
    # @generated
    def __init__(self, absolute_size=False, style='', size='', family='', weight='', gml_text_symbols=None, gml_colour=None, gml_svg_parameters=None, **kw_args):
        """ Initialises a new 'GmlFont' instance.
        """
        # True if 'size' is expressed in absolute values. Default is false. 
        self.absolute_size = absolute_size

        # The style to use for a font. The allowed values are 'normal', 'italic', and 'oblique'. 
        self.style = style

        # The size to use for the font in pixels. The default is defined to be 10 pixels, though various systems may have restrictions on what sizes are available. 
        self.size = size

        # Family name of a font to use. Allowed values are system-dependent. Any number of font-family attributes may be given and they are assumed to be in preferred order. 
        self.family = family

        # The amount of weight or boldness to use for a font. Allowed values are 'normal' and 'bold'. 
        self.weight = weight


        self._gml_text_symbols = []
        if gml_text_symbols is not None:
            self.gml_text_symbols = gml_text_symbols
        else:
            self.gml_text_symbols = []

        self._gml_colour = None
        self.gml_colour = gml_colour

        self._gml_svg_parameters = []
        if gml_svg_parameters is not None:
            self.gml_svg_parameters = gml_svg_parameters
        else:
            self.gml_svg_parameters = []


        super(GmlFont, self).__init__(**kw_args)
    # >>> gml_font

    # <<< gml_text_symbols
    # @generated
    def get_gml_text_symbols(self):
        """ 
        """
        return self._gml_text_symbols

    def set_gml_text_symbols(self, value):
        for x in self._gml_text_symbols:
            x._gml_font = None
        for y in value:
            y._gml_font = self
        self._gml_text_symbols = value

    gml_text_symbols = property(get_gml_text_symbols, set_gml_text_symbols)

    def add_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_font = self
            self._gml_text_symbols.append(obj)

    def remove_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_font = None
            self._gml_text_symbols.remove(obj)
    # >>> gml_text_symbols

    # <<< gml_colour
    # @generated
    def get_gml_colour(self):
        """ 
        """
        return self._gml_colour

    def set_gml_colour(self, value):
        if self._gml_colour is not None:
            filtered = [x for x in self.gml_colour.gml_fonts if x != self]
            self._gml_colour._gml_fonts = filtered

        self._gml_colour = value
        if self._gml_colour is not None:
            self._gml_colour._gml_fonts.append(self)

    gml_colour = property(get_gml_colour, set_gml_colour)
    # >>> gml_colour

    # <<< gml_svg_parameters
    # @generated
    def get_gml_svg_parameters(self):
        """ 
        """
        return self._gml_svg_parameters

    def set_gml_svg_parameters(self, value):
        for p in self._gml_svg_parameters:
            filtered = [q for q in p.gml_fonts if q != self]
            self._gml_svg_parameters._gml_fonts = filtered
        for r in value:
            if self not in r._gml_fonts:
                r._gml_fonts.append(self)
        self._gml_svg_parameters = value

    gml_svg_parameters = property(get_gml_svg_parameters, set_gml_svg_parameters)

    def add_gml_svg_parameters(self, *gml_svg_parameters):
        for obj in gml_svg_parameters:
            if self not in obj._gml_fonts:
                obj._gml_fonts.append(self)
            self._gml_svg_parameters.append(obj)

    def remove_gml_svg_parameters(self, *gml_svg_parameters):
        for obj in gml_svg_parameters:
            if self in obj._gml_fonts:
                obj._gml_fonts.remove(self)
            self._gml_svg_parameters.remove(obj)
    # >>> gml_svg_parameters


    def __str__(self):
        """ Returns a string representation of the GmlFont.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_font.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlFont.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlFont", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlFont.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_colour is not None:
            s += '%s<%s:GmlFont.gml_colour rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_colour.uri)
        for obj in self.gml_svg_parameters:
            s += '%s<%s:GmlFont.gml_svg_parameters rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlFont.absolute_size>%s</%s:GmlFont.absolute_size>' % \
            (indent, ns_prefix, self.absolute_size, ns_prefix)
        s += '%s<%s:GmlFont.style>%s</%s:GmlFont.style>' % \
            (indent, ns_prefix, self.style, ns_prefix)
        s += '%s<%s:GmlFont.size>%s</%s:GmlFont.size>' % \
            (indent, ns_prefix, self.size, ns_prefix)
        s += '%s<%s:GmlFont.family>%s</%s:GmlFont.family>' % \
            (indent, ns_prefix, self.family, ns_prefix)
        s += '%s<%s:GmlFont.weight>%s</%s:GmlFont.weight>' % \
            (indent, ns_prefix, self.weight, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlFont")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_font.serialize


class GmlSymbol(IdentifiedObject):
    """ Describes how a feature is to appear on a map or display. The symbol describes not just the shape that should appear but also such graphical properties as color and opacity.
    """
    # <<< gml_symbol
    # @generated
    def __init__(self, level='', type='', version='', gml_feature_styles=None, gml_base_symbol=None, **kw_args):
        """ Initialises a new 'GmlSymbol' instance.
        """
        # The level (of the map) where the symbol exists or the zoom levels at which this diagram object is displayed. As a way of de-cluttering displays, for example, some symbols and annotations are only shown when zoomed in. 
        self.level = level

        # The Symbol type. 
        self.type = type

        # The version of the Symbol. 
        self.version = version


        self._gml_feature_styles = []
        if gml_feature_styles is not None:
            self.gml_feature_styles = gml_feature_styles
        else:
            self.gml_feature_styles = []

        self._gml_base_symbol = None
        self.gml_base_symbol = gml_base_symbol


        super(GmlSymbol, self).__init__(**kw_args)
    # >>> gml_symbol

    # <<< gml_feature_styles
    # @generated
    def get_gml_feature_styles(self):
        """ 
        """
        return self._gml_feature_styles

    def set_gml_feature_styles(self, value):
        for p in self._gml_feature_styles:
            filtered = [q for q in p.gml_symbols if q != self]
            self._gml_feature_styles._gml_symbols = filtered
        for r in value:
            if self not in r._gml_symbols:
                r._gml_symbols.append(self)
        self._gml_feature_styles = value

    gml_feature_styles = property(get_gml_feature_styles, set_gml_feature_styles)

    def add_gml_feature_styles(self, *gml_feature_styles):
        for obj in gml_feature_styles:
            if self not in obj._gml_symbols:
                obj._gml_symbols.append(self)
            self._gml_feature_styles.append(obj)

    def remove_gml_feature_styles(self, *gml_feature_styles):
        for obj in gml_feature_styles:
            if self in obj._gml_symbols:
                obj._gml_symbols.remove(self)
            self._gml_feature_styles.remove(obj)
    # >>> gml_feature_styles

    # <<< gml_base_symbol
    # @generated
    def get_gml_base_symbol(self):
        """ 
        """
        return self._gml_base_symbol

    def set_gml_base_symbol(self, value):
        if self._gml_base_symbol is not None:
            filtered = [x for x in self.gml_base_symbol.gml_symbols if x != self]
            self._gml_base_symbol._gml_symbols = filtered

        self._gml_base_symbol = value
        if self._gml_base_symbol is not None:
            self._gml_base_symbol._gml_symbols.append(self)

    gml_base_symbol = property(get_gml_base_symbol, set_gml_base_symbol)
    # >>> gml_base_symbol


    def __str__(self):
        """ Returns a string representation of the GmlSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlSymbol", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlSymbol.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_base_symbol is not None:
            s += '%s<%s:GmlSymbol.gml_base_symbol rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_base_symbol.uri)
        s += '%s<%s:GmlSymbol.level>%s</%s:GmlSymbol.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:GmlSymbol.type>%s</%s:GmlSymbol.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlSymbol.version>%s</%s:GmlSymbol.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_symbol.serialize


class GmlSelector(IdentifiedObject):
    """ A diagram element that allows selection by a user, i.e. as 'hyperNode' for navigating between diagrams, or as composite object representing multiple grouped objects.
    """
    # <<< gml_selector
    # @generated
    def __init__(self, locations=None, change_items=None, **kw_args):
        """ Initialises a new 'GmlSelector' instance.
        """

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []


        super(GmlSelector, self).__init__(**kw_args)
    # >>> gml_selector

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.gml_selectors if q != self]
            self._locations._gml_selectors = filtered
        for r in value:
            if self not in r._gml_selectors:
                r._gml_selectors.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._gml_selectors:
                obj._gml_selectors.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._gml_selectors:
                obj._gml_selectors.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._gml_selector = None
        for y in value:
            y._gml_selector = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._gml_selector = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._gml_selector = None
            self._change_items.remove(obj)
    # >>> change_items


    def __str__(self):
        """ Returns a string representation of the GmlSelector.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_selector.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlSelector.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlSelector", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.locations:
            s += '%s<%s:GmlSelector.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:GmlSelector.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlSelector")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_selector.serialize


class GmlGeometryStyle(IdentifiedObject):
    """ The style for one geometry of a feature. Any number of geometry style descriptors can be assigned to one feature style. This is usually required for features with multiple geometry properties.
    """
    # <<< gml_geometry_style
    # @generated
    def __init__(self, symbol='', geometry_type='', geometry_property='', gml_feature_style=None, gml_label_style=None, **kw_args):
        """ Initialises a new 'GmlGeometryStyle' instance.
        """
        # Graphical symbol used to render a geometry or a topology. A symbol is a description of graphical attributes of a graphical object without a particular, implicit meaning. It can be a description of a line, circle, polygon or more complex drawing. 
        self.symbol = symbol

        # It is necessary to specify the geometry type using this attribute as well since the application schema of the geometry property may allow different geometries as its value. 
        self.geometry_type = geometry_type

        # The name of the geometry property of a feature to which this GeometryStyle applies. 
        self.geometry_property = geometry_property


        self._gml_feature_style = None
        self.gml_feature_style = gml_feature_style

        self._gml_label_style = None
        self.gml_label_style = gml_label_style


        super(GmlGeometryStyle, self).__init__(**kw_args)
    # >>> gml_geometry_style

    # <<< gml_feature_style
    # @generated
    def get_gml_feature_style(self):
        """ 
        """
        return self._gml_feature_style

    def set_gml_feature_style(self, value):
        if self._gml_feature_style is not None:
            filtered = [x for x in self.gml_feature_style.gml_geometry_styles if x != self]
            self._gml_feature_style._gml_geometry_styles = filtered

        self._gml_feature_style = value
        if self._gml_feature_style is not None:
            self._gml_feature_style._gml_geometry_styles.append(self)

    gml_feature_style = property(get_gml_feature_style, set_gml_feature_style)
    # >>> gml_feature_style

    # <<< gml_label_style
    # @generated
    def get_gml_label_style(self):
        """ 
        """
        return self._gml_label_style

    def set_gml_label_style(self, value):
        if self._gml_label_style is not None:
            filtered = [x for x in self.gml_label_style.gml_geometry_styles if x != self]
            self._gml_label_style._gml_geometry_styles = filtered

        self._gml_label_style = value
        if self._gml_label_style is not None:
            self._gml_label_style._gml_geometry_styles.append(self)

    gml_label_style = property(get_gml_label_style, set_gml_label_style)
    # >>> gml_label_style


    def __str__(self):
        """ Returns a string representation of the GmlGeometryStyle.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_geometry_style.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlGeometryStyle.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlGeometryStyle", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_feature_style is not None:
            s += '%s<%s:GmlGeometryStyle.gml_feature_style rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_feature_style.uri)
        if self.gml_label_style is not None:
            s += '%s<%s:GmlGeometryStyle.gml_label_style rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_label_style.uri)
        s += '%s<%s:GmlGeometryStyle.symbol>%s</%s:GmlGeometryStyle.symbol>' % \
            (indent, ns_prefix, self.symbol, ns_prefix)
        s += '%s<%s:GmlGeometryStyle.geometry_type>%s</%s:GmlGeometryStyle.geometry_type>' % \
            (indent, ns_prefix, self.geometry_type, ns_prefix)
        s += '%s<%s:GmlGeometryStyle.geometry_property>%s</%s:GmlGeometryStyle.geometry_property>' % \
            (indent, ns_prefix, self.geometry_property, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlGeometryStyle")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_geometry_style.serialize


class GmlDiagramObject(Location):
    """ Any of the magnitudes that serve to define the position of a point by reference to a fixed figure, system of lines, etc.
    """
    # <<< gml_diagram_object
    # @generated
    def __init__(self, diagrams=None, gml_line_symbols=None, gml_coordinate_systems=None, gml_raster_symbols=None, gml_polygon_symbols=None, gml_point_symbols=None, gml_text_symbols=None, **kw_args):
        """ Initialises a new 'GmlDiagramObject' instance.
        """

        self._diagrams = []
        if diagrams is not None:
            self.diagrams = diagrams
        else:
            self.diagrams = []

        self._gml_line_symbols = []
        if gml_line_symbols is not None:
            self.gml_line_symbols = gml_line_symbols
        else:
            self.gml_line_symbols = []

        self._gml_coordinate_systems = []
        if gml_coordinate_systems is not None:
            self.gml_coordinate_systems = gml_coordinate_systems
        else:
            self.gml_coordinate_systems = []

        self._gml_raster_symbols = []
        if gml_raster_symbols is not None:
            self.gml_raster_symbols = gml_raster_symbols
        else:
            self.gml_raster_symbols = []

        self._gml_polygon_symbols = []
        if gml_polygon_symbols is not None:
            self.gml_polygon_symbols = gml_polygon_symbols
        else:
            self.gml_polygon_symbols = []

        self._gml_point_symbols = []
        if gml_point_symbols is not None:
            self.gml_point_symbols = gml_point_symbols
        else:
            self.gml_point_symbols = []

        self._gml_text_symbols = []
        if gml_text_symbols is not None:
            self.gml_text_symbols = gml_text_symbols
        else:
            self.gml_text_symbols = []


        super(GmlDiagramObject, self).__init__(**kw_args)
    # >>> gml_diagram_object

    # <<< diagrams
    # @generated
    def get_diagrams(self):
        """ 
        """
        return self._diagrams

    def set_diagrams(self, value):
        for p in self._diagrams:
            filtered = [q for q in p.gml_diagram_objects if q != self]
            self._diagrams._gml_diagram_objects = filtered
        for r in value:
            if self not in r._gml_diagram_objects:
                r._gml_diagram_objects.append(self)
        self._diagrams = value

    diagrams = property(get_diagrams, set_diagrams)

    def add_diagrams(self, *diagrams):
        for obj in diagrams:
            if self not in obj._gml_diagram_objects:
                obj._gml_diagram_objects.append(self)
            self._diagrams.append(obj)

    def remove_diagrams(self, *diagrams):
        for obj in diagrams:
            if self in obj._gml_diagram_objects:
                obj._gml_diagram_objects.remove(self)
            self._diagrams.remove(obj)
    # >>> diagrams

    # <<< gml_line_symbols
    # @generated
    def get_gml_line_symbols(self):
        """ 
        """
        return self._gml_line_symbols

    def set_gml_line_symbols(self, value):
        for x in self._gml_line_symbols:
            x._gml_diagram_object = None
        for y in value:
            y._gml_diagram_object = self
        self._gml_line_symbols = value

    gml_line_symbols = property(get_gml_line_symbols, set_gml_line_symbols)

    def add_gml_line_symbols(self, *gml_line_symbols):
        for obj in gml_line_symbols:
            obj._gml_diagram_object = self
            self._gml_line_symbols.append(obj)

    def remove_gml_line_symbols(self, *gml_line_symbols):
        for obj in gml_line_symbols:
            obj._gml_diagram_object = None
            self._gml_line_symbols.remove(obj)
    # >>> gml_line_symbols

    # <<< gml_coordinate_systems
    # @generated
    def get_gml_coordinate_systems(self):
        """ 
        """
        return self._gml_coordinate_systems

    def set_gml_coordinate_systems(self, value):
        for p in self._gml_coordinate_systems:
            filtered = [q for q in p.gml_diagram_objects if q != self]
            self._gml_coordinate_systems._gml_diagram_objects = filtered
        for r in value:
            if self not in r._gml_diagram_objects:
                r._gml_diagram_objects.append(self)
        self._gml_coordinate_systems = value

    gml_coordinate_systems = property(get_gml_coordinate_systems, set_gml_coordinate_systems)

    def add_gml_coordinate_systems(self, *gml_coordinate_systems):
        for obj in gml_coordinate_systems:
            if self not in obj._gml_diagram_objects:
                obj._gml_diagram_objects.append(self)
            self._gml_coordinate_systems.append(obj)

    def remove_gml_coordinate_systems(self, *gml_coordinate_systems):
        for obj in gml_coordinate_systems:
            if self in obj._gml_diagram_objects:
                obj._gml_diagram_objects.remove(self)
            self._gml_coordinate_systems.remove(obj)
    # >>> gml_coordinate_systems

    # <<< gml_raster_symbols
    # @generated
    def get_gml_raster_symbols(self):
        """ 
        """
        return self._gml_raster_symbols

    def set_gml_raster_symbols(self, value):
        for x in self._gml_raster_symbols:
            x._gml_diagram_object = None
        for y in value:
            y._gml_diagram_object = self
        self._gml_raster_symbols = value

    gml_raster_symbols = property(get_gml_raster_symbols, set_gml_raster_symbols)

    def add_gml_raster_symbols(self, *gml_raster_symbols):
        for obj in gml_raster_symbols:
            obj._gml_diagram_object = self
            self._gml_raster_symbols.append(obj)

    def remove_gml_raster_symbols(self, *gml_raster_symbols):
        for obj in gml_raster_symbols:
            obj._gml_diagram_object = None
            self._gml_raster_symbols.remove(obj)
    # >>> gml_raster_symbols

    # <<< gml_polygon_symbols
    # @generated
    def get_gml_polygon_symbols(self):
        """ 
        """
        return self._gml_polygon_symbols

    def set_gml_polygon_symbols(self, value):
        for x in self._gml_polygon_symbols:
            x._gml_diagram_object = None
        for y in value:
            y._gml_diagram_object = self
        self._gml_polygon_symbols = value

    gml_polygon_symbols = property(get_gml_polygon_symbols, set_gml_polygon_symbols)

    def add_gml_polygon_symbols(self, *gml_polygon_symbols):
        for obj in gml_polygon_symbols:
            obj._gml_diagram_object = self
            self._gml_polygon_symbols.append(obj)

    def remove_gml_polygon_symbols(self, *gml_polygon_symbols):
        for obj in gml_polygon_symbols:
            obj._gml_diagram_object = None
            self._gml_polygon_symbols.remove(obj)
    # >>> gml_polygon_symbols

    # <<< gml_point_symbols
    # @generated
    def get_gml_point_symbols(self):
        """ 
        """
        return self._gml_point_symbols

    def set_gml_point_symbols(self, value):
        for x in self._gml_point_symbols:
            x._gml_diagram_object = None
        for y in value:
            y._gml_diagram_object = self
        self._gml_point_symbols = value

    gml_point_symbols = property(get_gml_point_symbols, set_gml_point_symbols)

    def add_gml_point_symbols(self, *gml_point_symbols):
        for obj in gml_point_symbols:
            obj._gml_diagram_object = self
            self._gml_point_symbols.append(obj)

    def remove_gml_point_symbols(self, *gml_point_symbols):
        for obj in gml_point_symbols:
            obj._gml_diagram_object = None
            self._gml_point_symbols.remove(obj)
    # >>> gml_point_symbols

    # <<< gml_text_symbols
    # @generated
    def get_gml_text_symbols(self):
        """ 
        """
        return self._gml_text_symbols

    def set_gml_text_symbols(self, value):
        for x in self._gml_text_symbols:
            x._gml_diagram_object = None
        for y in value:
            y._gml_diagram_object = self
        self._gml_text_symbols = value

    gml_text_symbols = property(get_gml_text_symbols, set_gml_text_symbols)

    def add_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_diagram_object = self
            self._gml_text_symbols.append(obj)

    def remove_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_diagram_object = None
            self._gml_text_symbols.remove(obj)
    # >>> gml_text_symbols


    def __str__(self):
        """ Returns a string representation of the GmlDiagramObject.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_diagram_object.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlDiagramObject.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlDiagramObject", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.diagrams:
            s += '%s<%s:GmlDiagramObject.diagrams rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_line_symbols:
            s += '%s<%s:GmlDiagramObject.gml_line_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_coordinate_systems:
            s += '%s<%s:GmlDiagramObject.gml_coordinate_systems rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_raster_symbols:
            s += '%s<%s:GmlDiagramObject.gml_raster_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_polygon_symbols:
            s += '%s<%s:GmlDiagramObject.gml_polygon_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_point_symbols:
            s += '%s<%s:GmlDiagramObject.gml_point_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlDiagramObject.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlDiagramObject")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_diagram_object.serialize


class GmlFeatureType(IdentifiedObject):
    """ Type classification of feature.
    """
    # <<< gml_feature_type
    # @generated
    def __init__(self, gml_feature_styles=None, **kw_args):
        """ Initialises a new 'GmlFeatureType' instance.
        """

        self._gml_feature_styles = []
        if gml_feature_styles is not None:
            self.gml_feature_styles = gml_feature_styles
        else:
            self.gml_feature_styles = []


        super(GmlFeatureType, self).__init__(**kw_args)
    # >>> gml_feature_type

    # <<< gml_feature_styles
    # @generated
    def get_gml_feature_styles(self):
        """ 
        """
        return self._gml_feature_styles

    def set_gml_feature_styles(self, value):
        for p in self._gml_feature_styles:
            filtered = [q for q in p.gml_feature_types if q != self]
            self._gml_feature_styles._gml_feature_types = filtered
        for r in value:
            if self not in r._gml_feature_types:
                r._gml_feature_types.append(self)
        self._gml_feature_styles = value

    gml_feature_styles = property(get_gml_feature_styles, set_gml_feature_styles)

    def add_gml_feature_styles(self, *gml_feature_styles):
        for obj in gml_feature_styles:
            if self not in obj._gml_feature_types:
                obj._gml_feature_types.append(self)
            self._gml_feature_styles.append(obj)

    def remove_gml_feature_styles(self, *gml_feature_styles):
        for obj in gml_feature_styles:
            if self in obj._gml_feature_types:
                obj._gml_feature_types.remove(self)
            self._gml_feature_styles.remove(obj)
    # >>> gml_feature_styles


    def __str__(self):
        """ Returns a string representation of the GmlFeatureType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_feature_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlFeatureType.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlFeatureType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlFeatureType.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlFeatureType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_feature_type.serialize


class GmlHalo(IdentifiedObject):
    """ A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.
    """
    # <<< gml_halo
    # @generated
    def __init__(self, radius='', opacity=0.0, gml_text_symbols=None, **kw_args):
        """ Initialises a new 'GmlHalo' instance.
        """
        # The Radius element gives the absolute size of a halo radius in pixels encoded as a floating-point number. The radius is taken from the outside edge of a font glyph to extend the area of coverage of the glyph (and the inside edge of ?holes? in the glyphs). The default radius is one pixel. Negative values are not allowed. 
        self.radius = radius

        # Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        self.opacity = opacity


        self._gml_text_symbols = []
        if gml_text_symbols is not None:
            self.gml_text_symbols = gml_text_symbols
        else:
            self.gml_text_symbols = []


        super(GmlHalo, self).__init__(**kw_args)
    # >>> gml_halo

    # <<< gml_text_symbols
    # @generated
    def get_gml_text_symbols(self):
        """ 
        """
        return self._gml_text_symbols

    def set_gml_text_symbols(self, value):
        for x in self._gml_text_symbols:
            x._gml_halo = None
        for y in value:
            y._gml_halo = self
        self._gml_text_symbols = value

    gml_text_symbols = property(get_gml_text_symbols, set_gml_text_symbols)

    def add_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_halo = self
            self._gml_text_symbols.append(obj)

    def remove_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_halo = None
            self._gml_text_symbols.remove(obj)
    # >>> gml_text_symbols


    def __str__(self):
        """ Returns a string representation of the GmlHalo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_halo.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlHalo.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlHalo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlHalo.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlHalo.radius>%s</%s:GmlHalo.radius>' % \
            (indent, ns_prefix, self.radius, ns_prefix)
        s += '%s<%s:GmlHalo.opacity>%s</%s:GmlHalo.opacity>' % \
            (indent, ns_prefix, self.opacity, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlHalo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_halo.serialize


class GmlObservation(Element):
    """ A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.
    """
    # <<< gml_observation
    # @generated
    def __init__(self, target='', using='', date_time='', result_of='', change_items=None, gml_values=None, locations=None, **kw_args):
        """ Initialises a new 'GmlObservation' instance.
        """
        # Contains or points to the specimen, region or station which is the object of the observation 
        self.target = target

        # Contains or points to a description of a sensor, instrument or procedure used for the observation. 
        self.using = using

 
        self.date_time = date_time

        # Indicates the result of the observation. 
        self.result_of = result_of


        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._gml_values = []
        if gml_values is not None:
            self.gml_values = gml_values
        else:
            self.gml_values = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []


        super(GmlObservation, self).__init__(**kw_args)
    # >>> gml_observation

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._gml_observation = None
        for y in value:
            y._gml_observation = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._gml_observation = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._gml_observation = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< gml_values
    # @generated
    def get_gml_values(self):
        """ 
        """
        return self._gml_values

    def set_gml_values(self, value):
        for x in self._gml_values:
            x._gml_observation = None
        for y in value:
            y._gml_observation = self
        self._gml_values = value

    gml_values = property(get_gml_values, set_gml_values)

    def add_gml_values(self, *gml_values):
        for obj in gml_values:
            obj._gml_observation = self
            self._gml_values.append(obj)

    def remove_gml_values(self, *gml_values):
        for obj in gml_values:
            obj._gml_observation = None
            self._gml_values.remove(obj)
    # >>> gml_values

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.gml_observatins if q != self]
            self._locations._gml_observatins = filtered
        for r in value:
            if self not in r._gml_observatins:
                r._gml_observatins.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._gml_observatins:
                obj._gml_observatins.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._gml_observatins:
                obj._gml_observatins.remove(self)
            self._locations.remove(obj)
    # >>> locations


    def __str__(self):
        """ Returns a string representation of the GmlObservation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_observation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlObservation.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlObservation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.change_items:
            s += '%s<%s:GmlObservation.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_values:
            s += '%s<%s:GmlObservation.gml_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:GmlObservation.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlObservation.target>%s</%s:GmlObservation.target>' % \
            (indent, ns_prefix, self.target, ns_prefix)
        s += '%s<%s:GmlObservation.using>%s</%s:GmlObservation.using>' % \
            (indent, ns_prefix, self.using, ns_prefix)
        s += '%s<%s:GmlObservation.date_time>%s</%s:GmlObservation.date_time>' % \
            (indent, ns_prefix, self.date_time, ns_prefix)
        s += '%s<%s:GmlObservation.result_of>%s</%s:GmlObservation.result_of>' % \
            (indent, ns_prefix, self.result_of, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlObservation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_observation.serialize


class GmlBaseSymbol(IdentifiedObject):
    """ Allows referencing and extension of external symbols, which may be stored in a symbol repository. The graphical properties from a referenced external symbol override the ones read in from the base symbol.
    """
    # <<< gml_base_symbol
    # @generated
    def __init__(self, gml_symbols=None, **kw_args):
        """ Initialises a new 'GmlBaseSymbol' instance.
        """

        self._gml_symbols = []
        if gml_symbols is not None:
            self.gml_symbols = gml_symbols
        else:
            self.gml_symbols = []


        super(GmlBaseSymbol, self).__init__(**kw_args)
    # >>> gml_base_symbol

    # <<< gml_symbols
    # @generated
    def get_gml_symbols(self):
        """ 
        """
        return self._gml_symbols

    def set_gml_symbols(self, value):
        for x in self._gml_symbols:
            x._gml_base_symbol = None
        for y in value:
            y._gml_base_symbol = self
        self._gml_symbols = value

    gml_symbols = property(get_gml_symbols, set_gml_symbols)

    def add_gml_symbols(self, *gml_symbols):
        for obj in gml_symbols:
            obj._gml_base_symbol = self
            self._gml_symbols.append(obj)

    def remove_gml_symbols(self, *gml_symbols):
        for obj in gml_symbols:
            obj._gml_base_symbol = None
            self._gml_symbols.remove(obj)
    # >>> gml_symbols


    def __str__(self):
        """ Returns a string representation of the GmlBaseSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_base_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlBaseSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlBaseSymbol", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_symbols:
            s += '%s<%s:GmlBaseSymbol.gml_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlBaseSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_base_symbol.serialize


class GmlValue(IdentifiedObject):
    """ Used for direct representation of values.
    """
    # <<< gml_value
    # @generated
    def __init__(self, value=0.0, time_period='', date_time='', measurement_value=None, gml_observation=None, **kw_args):
        """ Initialises a new 'GmlValue' instance.
        """
 
        self.value = value

 
        self.time_period = time_period

 
        self.date_time = date_time


        self._measurement_value = None
        self.measurement_value = measurement_value

        self._gml_observation = None
        self.gml_observation = gml_observation


        super(GmlValue, self).__init__(**kw_args)
    # >>> gml_value

    # <<< measurement_value
    # @generated
    def get_measurement_value(self):
        """ 
        """
        return self._measurement_value

    def set_measurement_value(self, value):
        if self._measurement_value is not None:
            filtered = [x for x in self.measurement_value.gml_values if x != self]
            self._measurement_value._gml_values = filtered

        self._measurement_value = value
        if self._measurement_value is not None:
            self._measurement_value._gml_values.append(self)

    measurement_value = property(get_measurement_value, set_measurement_value)
    # >>> measurement_value

    # <<< gml_observation
    # @generated
    def get_gml_observation(self):
        """ 
        """
        return self._gml_observation

    def set_gml_observation(self, value):
        if self._gml_observation is not None:
            filtered = [x for x in self.gml_observation.gml_values if x != self]
            self._gml_observation._gml_values = filtered

        self._gml_observation = value
        if self._gml_observation is not None:
            self._gml_observation._gml_values.append(self)

    gml_observation = property(get_gml_observation, set_gml_observation)
    # >>> gml_observation


    def __str__(self):
        """ Returns a string representation of the GmlValue.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_value.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlValue.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlValue", self.uri)
        if format:
            indent += ' ' * depth

        if self.measurement_value is not None:
            s += '%s<%s:GmlValue.measurement_value rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement_value.uri)
        if self.gml_observation is not None:
            s += '%s<%s:GmlValue.gml_observation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_observation.uri)
        s += '%s<%s:GmlValue.value>%s</%s:GmlValue.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:GmlValue.time_period>%s</%s:GmlValue.time_period>' % \
            (indent, ns_prefix, self.time_period, ns_prefix)
        s += '%s<%s:GmlValue.date_time>%s</%s:GmlValue.date_time>' % \
            (indent, ns_prefix, self.date_time, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlValue")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_value.serialize


class GmlFill(IdentifiedObject):
    """ Specifies how the area of the geometry will be filled.
    """
    # <<< gml_fill
    # @generated
    def __init__(self, opacity=0.0, gml_colour=None, gml_polygon_symbols=None, gml_svg_parameters=None, gml_marks=None, gml_text_symbols=None, **kw_args):
        """ Initialises a new 'GmlFill' instance.
        """
        # Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        self.opacity = opacity


        self._gml_colour = None
        self.gml_colour = gml_colour

        self._gml_polygon_symbols = []
        if gml_polygon_symbols is not None:
            self.gml_polygon_symbols = gml_polygon_symbols
        else:
            self.gml_polygon_symbols = []

        self._gml_svg_parameters = []
        if gml_svg_parameters is not None:
            self.gml_svg_parameters = gml_svg_parameters
        else:
            self.gml_svg_parameters = []

        self._gml_marks = []
        if gml_marks is not None:
            self.gml_marks = gml_marks
        else:
            self.gml_marks = []

        self._gml_text_symbols = []
        if gml_text_symbols is not None:
            self.gml_text_symbols = gml_text_symbols
        else:
            self.gml_text_symbols = []


        super(GmlFill, self).__init__(**kw_args)
    # >>> gml_fill

    # <<< gml_colour
    # @generated
    def get_gml_colour(self):
        """ 
        """
        return self._gml_colour

    def set_gml_colour(self, value):
        if self._gml_colour is not None:
            filtered = [x for x in self.gml_colour.gml_fills if x != self]
            self._gml_colour._gml_fills = filtered

        self._gml_colour = value
        if self._gml_colour is not None:
            self._gml_colour._gml_fills.append(self)

    gml_colour = property(get_gml_colour, set_gml_colour)
    # >>> gml_colour

    # <<< gml_polygon_symbols
    # @generated
    def get_gml_polygon_symbols(self):
        """ 
        """
        return self._gml_polygon_symbols

    def set_gml_polygon_symbols(self, value):
        for x in self._gml_polygon_symbols:
            x._gml_fill = None
        for y in value:
            y._gml_fill = self
        self._gml_polygon_symbols = value

    gml_polygon_symbols = property(get_gml_polygon_symbols, set_gml_polygon_symbols)

    def add_gml_polygon_symbols(self, *gml_polygon_symbols):
        for obj in gml_polygon_symbols:
            obj._gml_fill = self
            self._gml_polygon_symbols.append(obj)

    def remove_gml_polygon_symbols(self, *gml_polygon_symbols):
        for obj in gml_polygon_symbols:
            obj._gml_fill = None
            self._gml_polygon_symbols.remove(obj)
    # >>> gml_polygon_symbols

    # <<< gml_svg_parameters
    # @generated
    def get_gml_svg_parameters(self):
        """ 
        """
        return self._gml_svg_parameters

    def set_gml_svg_parameters(self, value):
        for p in self._gml_svg_parameters:
            filtered = [q for q in p.gml_fills if q != self]
            self._gml_svg_parameters._gml_fills = filtered
        for r in value:
            if self not in r._gml_fills:
                r._gml_fills.append(self)
        self._gml_svg_parameters = value

    gml_svg_parameters = property(get_gml_svg_parameters, set_gml_svg_parameters)

    def add_gml_svg_parameters(self, *gml_svg_parameters):
        for obj in gml_svg_parameters:
            if self not in obj._gml_fills:
                obj._gml_fills.append(self)
            self._gml_svg_parameters.append(obj)

    def remove_gml_svg_parameters(self, *gml_svg_parameters):
        for obj in gml_svg_parameters:
            if self in obj._gml_fills:
                obj._gml_fills.remove(self)
            self._gml_svg_parameters.remove(obj)
    # >>> gml_svg_parameters

    # <<< gml_marks
    # @generated
    def get_gml_marks(self):
        """ 
        """
        return self._gml_marks

    def set_gml_marks(self, value):
        for p in self._gml_marks:
            filtered = [q for q in p.gml_fills if q != self]
            self._gml_marks._gml_fills = filtered
        for r in value:
            if self not in r._gml_fills:
                r._gml_fills.append(self)
        self._gml_marks = value

    gml_marks = property(get_gml_marks, set_gml_marks)

    def add_gml_marks(self, *gml_marks):
        for obj in gml_marks:
            if self not in obj._gml_fills:
                obj._gml_fills.append(self)
            self._gml_marks.append(obj)

    def remove_gml_marks(self, *gml_marks):
        for obj in gml_marks:
            if self in obj._gml_fills:
                obj._gml_fills.remove(self)
            self._gml_marks.remove(obj)
    # >>> gml_marks

    # <<< gml_text_symbols
    # @generated
    def get_gml_text_symbols(self):
        """ 
        """
        return self._gml_text_symbols

    def set_gml_text_symbols(self, value):
        for x in self._gml_text_symbols:
            x._gml_fill = None
        for y in value:
            y._gml_fill = self
        self._gml_text_symbols = value

    gml_text_symbols = property(get_gml_text_symbols, set_gml_text_symbols)

    def add_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_fill = self
            self._gml_text_symbols.append(obj)

    def remove_gml_text_symbols(self, *gml_text_symbols):
        for obj in gml_text_symbols:
            obj._gml_fill = None
            self._gml_text_symbols.remove(obj)
    # >>> gml_text_symbols


    def __str__(self):
        """ Returns a string representation of the GmlFill.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_fill.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlFill.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlFill", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_colour is not None:
            s += '%s<%s:GmlFill.gml_colour rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_colour.uri)
        for obj in self.gml_polygon_symbols:
            s += '%s<%s:GmlFill.gml_polygon_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_svg_parameters:
            s += '%s<%s:GmlFill.gml_svg_parameters rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_marks:
            s += '%s<%s:GmlFill.gml_marks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlFill.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlFill.opacity>%s</%s:GmlFill.opacity>' % \
            (indent, ns_prefix, self.opacity, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlFill")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_fill.serialize


class GmlColour(IdentifiedObject):
    """ The solid color that will be used. The color value is RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign. The hexadecimal digits between A and F may be in either uppercase or lowercase. For example, full red is encoded as '#ff0000' (with no quotation marks). If the Stroke cssParameter element is absent, the default color is defined to be black ('#000000').
    """
    # <<< gml_colour
    # @generated
    def __init__(self, blue='', green='', red='', gml_fills=None, gml_fonts=None, gml_strokes=None, **kw_args):
        """ Initialises a new 'GmlColour' instance.
        """
        # The color value for BLUE (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.). 
        self.blue = blue

        # The color value for GREEN (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        self.green = green

        # The color value for RED (RGB-encoded using two hexadecimal digits per primary-color component, in the order Red, Green, Blue, prefixed with a hash (#) sign.) 
        self.red = red


        self._gml_fills = []
        if gml_fills is not None:
            self.gml_fills = gml_fills
        else:
            self.gml_fills = []

        self._gml_fonts = []
        if gml_fonts is not None:
            self.gml_fonts = gml_fonts
        else:
            self.gml_fonts = []

        self._gml_strokes = []
        if gml_strokes is not None:
            self.gml_strokes = gml_strokes
        else:
            self.gml_strokes = []


        super(GmlColour, self).__init__(**kw_args)
    # >>> gml_colour

    # <<< gml_fills
    # @generated
    def get_gml_fills(self):
        """ 
        """
        return self._gml_fills

    def set_gml_fills(self, value):
        for x in self._gml_fills:
            x._gml_colour = None
        for y in value:
            y._gml_colour = self
        self._gml_fills = value

    gml_fills = property(get_gml_fills, set_gml_fills)

    def add_gml_fills(self, *gml_fills):
        for obj in gml_fills:
            obj._gml_colour = self
            self._gml_fills.append(obj)

    def remove_gml_fills(self, *gml_fills):
        for obj in gml_fills:
            obj._gml_colour = None
            self._gml_fills.remove(obj)
    # >>> gml_fills

    # <<< gml_fonts
    # @generated
    def get_gml_fonts(self):
        """ 
        """
        return self._gml_fonts

    def set_gml_fonts(self, value):
        for x in self._gml_fonts:
            x._gml_colour = None
        for y in value:
            y._gml_colour = self
        self._gml_fonts = value

    gml_fonts = property(get_gml_fonts, set_gml_fonts)

    def add_gml_fonts(self, *gml_fonts):
        for obj in gml_fonts:
            obj._gml_colour = self
            self._gml_fonts.append(obj)

    def remove_gml_fonts(self, *gml_fonts):
        for obj in gml_fonts:
            obj._gml_colour = None
            self._gml_fonts.remove(obj)
    # >>> gml_fonts

    # <<< gml_strokes
    # @generated
    def get_gml_strokes(self):
        """ 
        """
        return self._gml_strokes

    def set_gml_strokes(self, value):
        for x in self._gml_strokes:
            x._gml_colour = None
        for y in value:
            y._gml_colour = self
        self._gml_strokes = value

    gml_strokes = property(get_gml_strokes, set_gml_strokes)

    def add_gml_strokes(self, *gml_strokes):
        for obj in gml_strokes:
            obj._gml_colour = self
            self._gml_strokes.append(obj)

    def remove_gml_strokes(self, *gml_strokes):
        for obj in gml_strokes:
            obj._gml_colour = None
            self._gml_strokes.remove(obj)
    # >>> gml_strokes


    def __str__(self):
        """ Returns a string representation of the GmlColour.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_colour.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlColour.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlColour", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_fills:
            s += '%s<%s:GmlColour.gml_fills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_fonts:
            s += '%s<%s:GmlColour.gml_fonts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_strokes:
            s += '%s<%s:GmlColour.gml_strokes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlColour.blue>%s</%s:GmlColour.blue>' % \
            (indent, ns_prefix, self.blue, ns_prefix)
        s += '%s<%s:GmlColour.green>%s</%s:GmlColour.green>' % \
            (indent, ns_prefix, self.green, ns_prefix)
        s += '%s<%s:GmlColour.red>%s</%s:GmlColour.red>' % \
            (indent, ns_prefix, self.red, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlColour")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_colour.serialize


class GmlLabelStyle(IdentifiedObject):
    """ The style for the text that is to be displayed along with the graphical representation of a feature. The content of the label is not necessarily defined in the GML data set. More precisely, the content can be static text specified in the style itself and the text from the GML data set. Label style has two elements: gml:style that specifies the style and gml:label that is used to compose the label content.
    """
    # <<< gml_label_style
    # @generated
    def __init__(self, transform='', style='', label_expression='', gml_geometry_styles=None, gml_feature_style=None, gml_topology_styles=None, **kw_args):
        """ Initialises a new 'GmlLabelStyle' instance.
        """
        # Allows us to specify a transformation expression that will be applied to the symbol in the rendering phase. Its type is xsd:string and the value is specified in the SVG specification (transform attribute). 
        self.transform = transform

        # Used to specify the style of the rendered text. The CSS2 styling expressions grammar should be used to express graphic properties. 
        self.style = style

        # Allows both text content and unbounded number of gml:LabelExpression elements. The value of gml:LabelExpression element is an XPath expression that selects the value of some property of the feature. 
        self.label_expression = label_expression


        self._gml_geometry_styles = []
        if gml_geometry_styles is not None:
            self.gml_geometry_styles = gml_geometry_styles
        else:
            self.gml_geometry_styles = []

        self._gml_feature_style = None
        self.gml_feature_style = gml_feature_style

        self._gml_topology_styles = []
        if gml_topology_styles is not None:
            self.gml_topology_styles = gml_topology_styles
        else:
            self.gml_topology_styles = []


        super(GmlLabelStyle, self).__init__(**kw_args)
    # >>> gml_label_style

    # <<< gml_geometry_styles
    # @generated
    def get_gml_geometry_styles(self):
        """ 
        """
        return self._gml_geometry_styles

    def set_gml_geometry_styles(self, value):
        for x in self._gml_geometry_styles:
            x._gml_label_style = None
        for y in value:
            y._gml_label_style = self
        self._gml_geometry_styles = value

    gml_geometry_styles = property(get_gml_geometry_styles, set_gml_geometry_styles)

    def add_gml_geometry_styles(self, *gml_geometry_styles):
        for obj in gml_geometry_styles:
            obj._gml_label_style = self
            self._gml_geometry_styles.append(obj)

    def remove_gml_geometry_styles(self, *gml_geometry_styles):
        for obj in gml_geometry_styles:
            obj._gml_label_style = None
            self._gml_geometry_styles.remove(obj)
    # >>> gml_geometry_styles

    # <<< gml_feature_style
    # @generated
    def get_gml_feature_style(self):
        """ 
        """
        return self._gml_feature_style

    def set_gml_feature_style(self, value):
        if self._gml_feature_style is not None:
            filtered = [x for x in self.gml_feature_style.gml_label_styles if x != self]
            self._gml_feature_style._gml_label_styles = filtered

        self._gml_feature_style = value
        if self._gml_feature_style is not None:
            self._gml_feature_style._gml_label_styles.append(self)

    gml_feature_style = property(get_gml_feature_style, set_gml_feature_style)
    # >>> gml_feature_style

    # <<< gml_topology_styles
    # @generated
    def get_gml_topology_styles(self):
        """ 
        """
        return self._gml_topology_styles

    def set_gml_topology_styles(self, value):
        for x in self._gml_topology_styles:
            x._gml_lable_style = None
        for y in value:
            y._gml_lable_style = self
        self._gml_topology_styles = value

    gml_topology_styles = property(get_gml_topology_styles, set_gml_topology_styles)

    def add_gml_topology_styles(self, *gml_topology_styles):
        for obj in gml_topology_styles:
            obj._gml_lable_style = self
            self._gml_topology_styles.append(obj)

    def remove_gml_topology_styles(self, *gml_topology_styles):
        for obj in gml_topology_styles:
            obj._gml_lable_style = None
            self._gml_topology_styles.remove(obj)
    # >>> gml_topology_styles


    def __str__(self):
        """ Returns a string representation of the GmlLabelStyle.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_label_style.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlLabelStyle.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlLabelStyle", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_geometry_styles:
            s += '%s<%s:GmlLabelStyle.gml_geometry_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_feature_style is not None:
            s += '%s<%s:GmlLabelStyle.gml_feature_style rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_feature_style.uri)
        for obj in self.gml_topology_styles:
            s += '%s<%s:GmlLabelStyle.gml_topology_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlLabelStyle.transform>%s</%s:GmlLabelStyle.transform>' % \
            (indent, ns_prefix, self.transform, ns_prefix)
        s += '%s<%s:GmlLabelStyle.style>%s</%s:GmlLabelStyle.style>' % \
            (indent, ns_prefix, self.style, ns_prefix)
        s += '%s<%s:GmlLabelStyle.label_expression>%s</%s:GmlLabelStyle.label_expression>' % \
            (indent, ns_prefix, self.label_expression, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlLabelStyle")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_label_style.serialize


class GmlGraphic(IdentifiedObject):
    """ A 'graphic symbol' with an inherent shape, color(s), and possibly size. A 'graphic' can be very informally defined as 'a little picture' and can be of either a raster or vector-graphic source type.
    """
    # <<< gml_graphic
    # @generated
    def __init__(self, x_scale=0.0, size=0, y_scale=0.0, opacity=0.0, symbol_id='', rotation=0.0, min_size=0, gml_marks=None, gml_point_symbols=None, **kw_args):
        """ Initialises a new 'GmlGraphic' instance.
        """
        # Horizontal scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbar). 
        self.x_scale = x_scale

        # Gives the absolute size of the graphic in pixels encoded as a floatingpoint number. The default size for an object is context-dependent. Negative values are not allowed. 
        self.size = size

        # Vertical scaling factor of normal symbol - particularly applicable to busbars if not described through a sequence of gmlPositions (e.g., Busbars). 
        self.y_scale = y_scale

        # Specifies the level of translucency to use when rendering the Graphic.The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        self.opacity = opacity

        # The identifier of the symbol, if not derived from the type of CIM object (PSR, Asset, Organisation, Document, etc.) gmlSymbolPlacement is associated with. 
        self.symbol_id = symbol_id

        # Gives the rotation of a graphic in the clockwise direction about its center point in decimal degrees, encoded as a floating-point number. Negative values mean counter-clockwise rotation. The default value is 0.0 (no rotation). Note that there is no connection between source geometry types and rotations; the point used for plotting has no inherent direction. Also, the point within the graphic about which it is rotated is format dependent. If a format does not include an inherent rotation point, then the point of rotation should be the centroid. 
        self.rotation = rotation

        # The minimum symbol size allowed. 
        self.min_size = min_size


        self._gml_marks = []
        if gml_marks is not None:
            self.gml_marks = gml_marks
        else:
            self.gml_marks = []

        self._gml_point_symbols = []
        if gml_point_symbols is not None:
            self.gml_point_symbols = gml_point_symbols
        else:
            self.gml_point_symbols = []


        super(GmlGraphic, self).__init__(**kw_args)
    # >>> gml_graphic

    # <<< gml_marks
    # @generated
    def get_gml_marks(self):
        """ 
        """
        return self._gml_marks

    def set_gml_marks(self, value):
        for p in self._gml_marks:
            filtered = [q for q in p.gml_graphics if q != self]
            self._gml_marks._gml_graphics = filtered
        for r in value:
            if self not in r._gml_graphics:
                r._gml_graphics.append(self)
        self._gml_marks = value

    gml_marks = property(get_gml_marks, set_gml_marks)

    def add_gml_marks(self, *gml_marks):
        for obj in gml_marks:
            if self not in obj._gml_graphics:
                obj._gml_graphics.append(self)
            self._gml_marks.append(obj)

    def remove_gml_marks(self, *gml_marks):
        for obj in gml_marks:
            if self in obj._gml_graphics:
                obj._gml_graphics.remove(self)
            self._gml_marks.remove(obj)
    # >>> gml_marks

    # <<< gml_point_symbols
    # @generated
    def get_gml_point_symbols(self):
        """ 
        """
        return self._gml_point_symbols

    def set_gml_point_symbols(self, value):
        for x in self._gml_point_symbols:
            x._gml_graphic = None
        for y in value:
            y._gml_graphic = self
        self._gml_point_symbols = value

    gml_point_symbols = property(get_gml_point_symbols, set_gml_point_symbols)

    def add_gml_point_symbols(self, *gml_point_symbols):
        for obj in gml_point_symbols:
            obj._gml_graphic = self
            self._gml_point_symbols.append(obj)

    def remove_gml_point_symbols(self, *gml_point_symbols):
        for obj in gml_point_symbols:
            obj._gml_graphic = None
            self._gml_point_symbols.remove(obj)
    # >>> gml_point_symbols


    def __str__(self):
        """ Returns a string representation of the GmlGraphic.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_graphic.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlGraphic.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlGraphic", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_marks:
            s += '%s<%s:GmlGraphic.gml_marks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_point_symbols:
            s += '%s<%s:GmlGraphic.gml_point_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlGraphic.x_scale>%s</%s:GmlGraphic.x_scale>' % \
            (indent, ns_prefix, self.x_scale, ns_prefix)
        s += '%s<%s:GmlGraphic.size>%s</%s:GmlGraphic.size>' % \
            (indent, ns_prefix, self.size, ns_prefix)
        s += '%s<%s:GmlGraphic.y_scale>%s</%s:GmlGraphic.y_scale>' % \
            (indent, ns_prefix, self.y_scale, ns_prefix)
        s += '%s<%s:GmlGraphic.opacity>%s</%s:GmlGraphic.opacity>' % \
            (indent, ns_prefix, self.opacity, ns_prefix)
        s += '%s<%s:GmlGraphic.symbol_id>%s</%s:GmlGraphic.symbol_id>' % \
            (indent, ns_prefix, self.symbol_id, ns_prefix)
        s += '%s<%s:GmlGraphic.rotation>%s</%s:GmlGraphic.rotation>' % \
            (indent, ns_prefix, self.rotation, ns_prefix)
        s += '%s<%s:GmlGraphic.min_size>%s</%s:GmlGraphic.min_size>' % \
            (indent, ns_prefix, self.min_size, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlGraphic")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_graphic.serialize


class GmlStroke(IdentifiedObject):
    """ The element encapsulating the graphical symbolization parameters for linear geometries.
    """
    # <<< gml_stroke
    # @generated
    def __init__(self, opacity=0.0, linejoin='', dash_offset='', dash_array='', width=0.0, line_cap='', line_style='', gml_svg_parameters=None, gml_line_symbols=None, gml_marks=None, gml_colour=None, gml_polygon_symbols=None, **kw_args):
        """ Initialises a new 'GmlStroke' instance.
        """
        # Specifies the level of translucency to use when rendering the stroke. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        self.opacity = opacity

        # Enumerated values telling how line strings should be joined (between line segments). The values are represented as content strings.  The allowed values for line join are 'mitre', 'round', and 'bevel'. The default values are system-dependent. 
        self.linejoin = linejoin

        # Specifies the distance as a float into the 'stroke-dasharray' pattern at which to start drawing. 
        self.dash_offset = dash_offset

        # Encodes a dash pattern as a series of space separated floats. The first number gives the length in pixels of dash to draw, the second gives the amount of space to leave, and this pattern repeats. If an odd number of values is given, then the pattern is expanded by repeating it twice to give an even number of values. Decimal values have a system-dependent interpretation (usually depending on whether antialiasing is being used). The default is to draw an unbroken line. 
        self.dash_array = dash_array

        # The absolute width (thickness) of a stroke in pixels encoded as a float. The default is 1.0. Fractional numbers are allowed (with a system-dependent interpretation) but negative numbers are not. 
        self.width = width

        # Enumerated values telling how line strings should be capped (at the two ends of the line string). The values are represented as content strings.  The allowed values for line cap are 'butt', 'round', and 'square'. The default values are system-dependent. 
        self.line_cap = line_cap

        # The name of a defined line style. Usually will be an enumerated value and will be system-specific. 
        self.line_style = line_style


        self._gml_svg_parameters = []
        if gml_svg_parameters is not None:
            self.gml_svg_parameters = gml_svg_parameters
        else:
            self.gml_svg_parameters = []

        self._gml_line_symbols = []
        if gml_line_symbols is not None:
            self.gml_line_symbols = gml_line_symbols
        else:
            self.gml_line_symbols = []

        self._gml_marks = []
        if gml_marks is not None:
            self.gml_marks = gml_marks
        else:
            self.gml_marks = []

        self._gml_colour = None
        self.gml_colour = gml_colour

        self._gml_polygon_symbols = []
        if gml_polygon_symbols is not None:
            self.gml_polygon_symbols = gml_polygon_symbols
        else:
            self.gml_polygon_symbols = []


        super(GmlStroke, self).__init__(**kw_args)
    # >>> gml_stroke

    # <<< gml_svg_parameters
    # @generated
    def get_gml_svg_parameters(self):
        """ 
        """
        return self._gml_svg_parameters

    def set_gml_svg_parameters(self, value):
        for p in self._gml_svg_parameters:
            filtered = [q for q in p.gml_stokes if q != self]
            self._gml_svg_parameters._gml_stokes = filtered
        for r in value:
            if self not in r._gml_stokes:
                r._gml_stokes.append(self)
        self._gml_svg_parameters = value

    gml_svg_parameters = property(get_gml_svg_parameters, set_gml_svg_parameters)

    def add_gml_svg_parameters(self, *gml_svg_parameters):
        for obj in gml_svg_parameters:
            if self not in obj._gml_stokes:
                obj._gml_stokes.append(self)
            self._gml_svg_parameters.append(obj)

    def remove_gml_svg_parameters(self, *gml_svg_parameters):
        for obj in gml_svg_parameters:
            if self in obj._gml_stokes:
                obj._gml_stokes.remove(self)
            self._gml_svg_parameters.remove(obj)
    # >>> gml_svg_parameters

    # <<< gml_line_symbols
    # @generated
    def get_gml_line_symbols(self):
        """ 
        """
        return self._gml_line_symbols

    def set_gml_line_symbols(self, value):
        for x in self._gml_line_symbols:
            x._gml_stroke = None
        for y in value:
            y._gml_stroke = self
        self._gml_line_symbols = value

    gml_line_symbols = property(get_gml_line_symbols, set_gml_line_symbols)

    def add_gml_line_symbols(self, *gml_line_symbols):
        for obj in gml_line_symbols:
            obj._gml_stroke = self
            self._gml_line_symbols.append(obj)

    def remove_gml_line_symbols(self, *gml_line_symbols):
        for obj in gml_line_symbols:
            obj._gml_stroke = None
            self._gml_line_symbols.remove(obj)
    # >>> gml_line_symbols

    # <<< gml_marks
    # @generated
    def get_gml_marks(self):
        """ 
        """
        return self._gml_marks

    def set_gml_marks(self, value):
        for p in self._gml_marks:
            filtered = [q for q in p.gml_strokes if q != self]
            self._gml_marks._gml_strokes = filtered
        for r in value:
            if self not in r._gml_strokes:
                r._gml_strokes.append(self)
        self._gml_marks = value

    gml_marks = property(get_gml_marks, set_gml_marks)

    def add_gml_marks(self, *gml_marks):
        for obj in gml_marks:
            if self not in obj._gml_strokes:
                obj._gml_strokes.append(self)
            self._gml_marks.append(obj)

    def remove_gml_marks(self, *gml_marks):
        for obj in gml_marks:
            if self in obj._gml_strokes:
                obj._gml_strokes.remove(self)
            self._gml_marks.remove(obj)
    # >>> gml_marks

    # <<< gml_colour
    # @generated
    def get_gml_colour(self):
        """ 
        """
        return self._gml_colour

    def set_gml_colour(self, value):
        if self._gml_colour is not None:
            filtered = [x for x in self.gml_colour.gml_strokes if x != self]
            self._gml_colour._gml_strokes = filtered

        self._gml_colour = value
        if self._gml_colour is not None:
            self._gml_colour._gml_strokes.append(self)

    gml_colour = property(get_gml_colour, set_gml_colour)
    # >>> gml_colour

    # <<< gml_polygon_symbols
    # @generated
    def get_gml_polygon_symbols(self):
        """ 
        """
        return self._gml_polygon_symbols

    def set_gml_polygon_symbols(self, value):
        for x in self._gml_polygon_symbols:
            x._gml_stroke = None
        for y in value:
            y._gml_stroke = self
        self._gml_polygon_symbols = value

    gml_polygon_symbols = property(get_gml_polygon_symbols, set_gml_polygon_symbols)

    def add_gml_polygon_symbols(self, *gml_polygon_symbols):
        for obj in gml_polygon_symbols:
            obj._gml_stroke = self
            self._gml_polygon_symbols.append(obj)

    def remove_gml_polygon_symbols(self, *gml_polygon_symbols):
        for obj in gml_polygon_symbols:
            obj._gml_stroke = None
            self._gml_polygon_symbols.remove(obj)
    # >>> gml_polygon_symbols


    def __str__(self):
        """ Returns a string representation of the GmlStroke.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_stroke.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlStroke.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlStroke", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_svg_parameters:
            s += '%s<%s:GmlStroke.gml_svg_parameters rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_line_symbols:
            s += '%s<%s:GmlStroke.gml_line_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_marks:
            s += '%s<%s:GmlStroke.gml_marks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_colour is not None:
            s += '%s<%s:GmlStroke.gml_colour rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_colour.uri)
        for obj in self.gml_polygon_symbols:
            s += '%s<%s:GmlStroke.gml_polygon_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlStroke.opacity>%s</%s:GmlStroke.opacity>' % \
            (indent, ns_prefix, self.opacity, ns_prefix)
        s += '%s<%s:GmlStroke.linejoin>%s</%s:GmlStroke.linejoin>' % \
            (indent, ns_prefix, self.linejoin, ns_prefix)
        s += '%s<%s:GmlStroke.dash_offset>%s</%s:GmlStroke.dash_offset>' % \
            (indent, ns_prefix, self.dash_offset, ns_prefix)
        s += '%s<%s:GmlStroke.dash_array>%s</%s:GmlStroke.dash_array>' % \
            (indent, ns_prefix, self.dash_array, ns_prefix)
        s += '%s<%s:GmlStroke.width>%s</%s:GmlStroke.width>' % \
            (indent, ns_prefix, self.width, ns_prefix)
        s += '%s<%s:GmlStroke.line_cap>%s</%s:GmlStroke.line_cap>' % \
            (indent, ns_prefix, self.line_cap, ns_prefix)
        s += '%s<%s:GmlStroke.line_style>%s</%s:GmlStroke.line_style>' % \
            (indent, ns_prefix, self.line_style, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlStroke")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_stroke.serialize


class GmlCoordinateSystem(IdentifiedObject):
    """ A coordinate reference system consists of a set of coordinate system axes that is related to the earth through a datum that defines the size and shape of the earth or some abstract reference system such as those used for rendering schemantic diagrams, internal views of items such as cabinets, vaults, etc. Geometries in GML indicate the coordinate reference system in which their measurements have been made.
    """
    # <<< gml_coordinate_system
    # @generated
    def __init__(self, position_unit_name='', z_max='', y_max='', z_min='', y_min='', x_min='', scale='', x_max='', gml_positions=None, gml_diagram_objects=None, diagrams=None, **kw_args):
        """ Initialises a new 'GmlCoordinateSystem' instance.
        """
 
        self.position_unit_name = position_unit_name

        # If applicable, the maximum position allowed along the Z axis of the coordinate reference system. 
        self.z_max = z_max

        # The maximum position allowed along the Y axis of the coordinate reference system. 
        self.y_max = y_max

        # If applicable, the minimum position allowed along the Z axis of the coordinate reference system. 
        self.z_min = z_min

        # The minimum position allowed along the Y axis of the coordinate reference system. 
        self.y_min = y_min

        # The minimum position allowed along the X axis of the coordinate reference system. 
        self.x_min = x_min

 
        self.scale = scale

        # The maximum position allowed along the X axis of the coordinate reference system. 
        self.x_max = x_max


        self._gml_positions = []
        if gml_positions is not None:
            self.gml_positions = gml_positions
        else:
            self.gml_positions = []

        self._gml_diagram_objects = []
        if gml_diagram_objects is not None:
            self.gml_diagram_objects = gml_diagram_objects
        else:
            self.gml_diagram_objects = []

        self._diagrams = []
        if diagrams is not None:
            self.diagrams = diagrams
        else:
            self.diagrams = []


        super(GmlCoordinateSystem, self).__init__(**kw_args)
    # >>> gml_coordinate_system

    # <<< gml_positions
    # @generated
    def get_gml_positions(self):
        """ 
        """
        return self._gml_positions

    def set_gml_positions(self, value):
        for x in self._gml_positions:
            x._gml_coordinate_system = None
        for y in value:
            y._gml_coordinate_system = self
        self._gml_positions = value

    gml_positions = property(get_gml_positions, set_gml_positions)

    def add_gml_positions(self, *gml_positions):
        for obj in gml_positions:
            obj._gml_coordinate_system = self
            self._gml_positions.append(obj)

    def remove_gml_positions(self, *gml_positions):
        for obj in gml_positions:
            obj._gml_coordinate_system = None
            self._gml_positions.remove(obj)
    # >>> gml_positions

    # <<< gml_diagram_objects
    # @generated
    def get_gml_diagram_objects(self):
        """ 
        """
        return self._gml_diagram_objects

    def set_gml_diagram_objects(self, value):
        for p in self._gml_diagram_objects:
            filtered = [q for q in p.gml_coordinate_systems if q != self]
            self._gml_diagram_objects._gml_coordinate_systems = filtered
        for r in value:
            if self not in r._gml_coordinate_systems:
                r._gml_coordinate_systems.append(self)
        self._gml_diagram_objects = value

    gml_diagram_objects = property(get_gml_diagram_objects, set_gml_diagram_objects)

    def add_gml_diagram_objects(self, *gml_diagram_objects):
        for obj in gml_diagram_objects:
            if self not in obj._gml_coordinate_systems:
                obj._gml_coordinate_systems.append(self)
            self._gml_diagram_objects.append(obj)

    def remove_gml_diagram_objects(self, *gml_diagram_objects):
        for obj in gml_diagram_objects:
            if self in obj._gml_coordinate_systems:
                obj._gml_coordinate_systems.remove(self)
            self._gml_diagram_objects.remove(obj)
    # >>> gml_diagram_objects

    # <<< diagrams
    # @generated
    def get_diagrams(self):
        """ 
        """
        return self._diagrams

    def set_diagrams(self, value):
        for x in self._diagrams:
            x._gml_coordinate_system = None
        for y in value:
            y._gml_coordinate_system = self
        self._diagrams = value

    diagrams = property(get_diagrams, set_diagrams)

    def add_diagrams(self, *diagrams):
        for obj in diagrams:
            obj._gml_coordinate_system = self
            self._diagrams.append(obj)

    def remove_diagrams(self, *diagrams):
        for obj in diagrams:
            obj._gml_coordinate_system = None
            self._diagrams.remove(obj)
    # >>> diagrams


    def __str__(self):
        """ Returns a string representation of the GmlCoordinateSystem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_coordinate_system.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlCoordinateSystem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlCoordinateSystem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_positions:
            s += '%s<%s:GmlCoordinateSystem.gml_positions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_diagram_objects:
            s += '%s<%s:GmlCoordinateSystem.gml_diagram_objects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.diagrams:
            s += '%s<%s:GmlCoordinateSystem.diagrams rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlCoordinateSystem.position_unit_name>%s</%s:GmlCoordinateSystem.position_unit_name>' % \
            (indent, ns_prefix, self.position_unit_name, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.z_max>%s</%s:GmlCoordinateSystem.z_max>' % \
            (indent, ns_prefix, self.z_max, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.y_max>%s</%s:GmlCoordinateSystem.y_max>' % \
            (indent, ns_prefix, self.y_max, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.z_min>%s</%s:GmlCoordinateSystem.z_min>' % \
            (indent, ns_prefix, self.z_min, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.y_min>%s</%s:GmlCoordinateSystem.y_min>' % \
            (indent, ns_prefix, self.y_min, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.x_min>%s</%s:GmlCoordinateSystem.x_min>' % \
            (indent, ns_prefix, self.x_min, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.scale>%s</%s:GmlCoordinateSystem.scale>' % \
            (indent, ns_prefix, self.scale, ns_prefix)
        s += '%s<%s:GmlCoordinateSystem.x_max>%s</%s:GmlCoordinateSystem.x_max>' % \
            (indent, ns_prefix, self.x_max, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlCoordinateSystem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_coordinate_system.serialize


class GmlFeatureStyle(IdentifiedObject):
    """ Used for styling a particular aspect or aspects of a feature, such as geometry, topology or arbitrary text string.
    """
    # <<< gml_feature_style
    # @generated
    def __init__(self, query_grammar='xpath', version='', feature_type_name='', base_type='', feature_type='', semantic_type_identifier='', feature_constraint='', gml_geometry_styles=None, gml_feature_types=None, gml_label_styles=None, gml_symbols=None, gml_tobology_styles=None, **kw_args):
        """ Initialises a new 'GmlFeatureStyle' instance.
        """
        # Grammar used in the content of the gml:featureConstraint element. Values are: "xpath", "other", "xquery"
        self.query_grammar = 'xpath'

        # Allows version numbers to be identified when the SLD pieces are used independently. 
        self.version = version

        # Identifies the specific feature type that the feature-type style is for. 
        self.feature_type_name = feature_type_name

        # Another way of selecting the feature instances to which the style applies is to specify, as the value of this attribute, the name of the base type from which feature or features derive. 
        self.base_type = base_type

        # The simplest and most common way of relating features and styles is by using this attribute. Its value will be the declared name of a feature, instances of which we want to style. For example, if the featureType = Switch, this FeatureStyle object will simply apply to all Switch features. 
        self.feature_type = feature_type

        # The SemanticTypeIdentifier is experimental in GML and is intended to be used to identify what the feature style is suitable to be used for using community-controlled name(s). For example, a single style may be suitable to use with many different feature types. 
        self.semantic_type_identifier = semantic_type_identifier

        # This property is used to further constrain the feature instance set to which the style applies. It is optional and its value is an XPath expression. If the property does not exist, the style applies to all feature instances selected by 'featureType' or 'baseType'. 
        self.feature_constraint = feature_constraint


        self._gml_geometry_styles = []
        if gml_geometry_styles is not None:
            self.gml_geometry_styles = gml_geometry_styles
        else:
            self.gml_geometry_styles = []

        self._gml_feature_types = []
        if gml_feature_types is not None:
            self.gml_feature_types = gml_feature_types
        else:
            self.gml_feature_types = []

        self._gml_label_styles = []
        if gml_label_styles is not None:
            self.gml_label_styles = gml_label_styles
        else:
            self.gml_label_styles = []

        self._gml_symbols = []
        if gml_symbols is not None:
            self.gml_symbols = gml_symbols
        else:
            self.gml_symbols = []

        self._gml_tobology_styles = []
        if gml_tobology_styles is not None:
            self.gml_tobology_styles = gml_tobology_styles
        else:
            self.gml_tobology_styles = []


        super(GmlFeatureStyle, self).__init__(**kw_args)
    # >>> gml_feature_style

    # <<< gml_geometry_styles
    # @generated
    def get_gml_geometry_styles(self):
        """ 
        """
        return self._gml_geometry_styles

    def set_gml_geometry_styles(self, value):
        for x in self._gml_geometry_styles:
            x._gml_feature_style = None
        for y in value:
            y._gml_feature_style = self
        self._gml_geometry_styles = value

    gml_geometry_styles = property(get_gml_geometry_styles, set_gml_geometry_styles)

    def add_gml_geometry_styles(self, *gml_geometry_styles):
        for obj in gml_geometry_styles:
            obj._gml_feature_style = self
            self._gml_geometry_styles.append(obj)

    def remove_gml_geometry_styles(self, *gml_geometry_styles):
        for obj in gml_geometry_styles:
            obj._gml_feature_style = None
            self._gml_geometry_styles.remove(obj)
    # >>> gml_geometry_styles

    # <<< gml_feature_types
    # @generated
    def get_gml_feature_types(self):
        """ 
        """
        return self._gml_feature_types

    def set_gml_feature_types(self, value):
        for p in self._gml_feature_types:
            filtered = [q for q in p.gml_feature_styles if q != self]
            self._gml_feature_types._gml_feature_styles = filtered
        for r in value:
            if self not in r._gml_feature_styles:
                r._gml_feature_styles.append(self)
        self._gml_feature_types = value

    gml_feature_types = property(get_gml_feature_types, set_gml_feature_types)

    def add_gml_feature_types(self, *gml_feature_types):
        for obj in gml_feature_types:
            if self not in obj._gml_feature_styles:
                obj._gml_feature_styles.append(self)
            self._gml_feature_types.append(obj)

    def remove_gml_feature_types(self, *gml_feature_types):
        for obj in gml_feature_types:
            if self in obj._gml_feature_styles:
                obj._gml_feature_styles.remove(self)
            self._gml_feature_types.remove(obj)
    # >>> gml_feature_types

    # <<< gml_label_styles
    # @generated
    def get_gml_label_styles(self):
        """ 
        """
        return self._gml_label_styles

    def set_gml_label_styles(self, value):
        for x in self._gml_label_styles:
            x._gml_feature_style = None
        for y in value:
            y._gml_feature_style = self
        self._gml_label_styles = value

    gml_label_styles = property(get_gml_label_styles, set_gml_label_styles)

    def add_gml_label_styles(self, *gml_label_styles):
        for obj in gml_label_styles:
            obj._gml_feature_style = self
            self._gml_label_styles.append(obj)

    def remove_gml_label_styles(self, *gml_label_styles):
        for obj in gml_label_styles:
            obj._gml_feature_style = None
            self._gml_label_styles.remove(obj)
    # >>> gml_label_styles

    # <<< gml_symbols
    # @generated
    def get_gml_symbols(self):
        """ 
        """
        return self._gml_symbols

    def set_gml_symbols(self, value):
        for p in self._gml_symbols:
            filtered = [q for q in p.gml_feature_styles if q != self]
            self._gml_symbols._gml_feature_styles = filtered
        for r in value:
            if self not in r._gml_feature_styles:
                r._gml_feature_styles.append(self)
        self._gml_symbols = value

    gml_symbols = property(get_gml_symbols, set_gml_symbols)

    def add_gml_symbols(self, *gml_symbols):
        for obj in gml_symbols:
            if self not in obj._gml_feature_styles:
                obj._gml_feature_styles.append(self)
            self._gml_symbols.append(obj)

    def remove_gml_symbols(self, *gml_symbols):
        for obj in gml_symbols:
            if self in obj._gml_feature_styles:
                obj._gml_feature_styles.remove(self)
            self._gml_symbols.remove(obj)
    # >>> gml_symbols

    # <<< gml_tobology_styles
    # @generated
    def get_gml_tobology_styles(self):
        """ 
        """
        return self._gml_tobology_styles

    def set_gml_tobology_styles(self, value):
        for x in self._gml_tobology_styles:
            x._gml_feature_style = None
        for y in value:
            y._gml_feature_style = self
        self._gml_tobology_styles = value

    gml_tobology_styles = property(get_gml_tobology_styles, set_gml_tobology_styles)

    def add_gml_tobology_styles(self, *gml_tobology_styles):
        for obj in gml_tobology_styles:
            obj._gml_feature_style = self
            self._gml_tobology_styles.append(obj)

    def remove_gml_tobology_styles(self, *gml_tobology_styles):
        for obj in gml_tobology_styles:
            obj._gml_feature_style = None
            self._gml_tobology_styles.remove(obj)
    # >>> gml_tobology_styles


    def __str__(self):
        """ Returns a string representation of the GmlFeatureStyle.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_feature_style.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlFeatureStyle.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlFeatureStyle", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_geometry_styles:
            s += '%s<%s:GmlFeatureStyle.gml_geometry_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_feature_types:
            s += '%s<%s:GmlFeatureStyle.gml_feature_types rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_label_styles:
            s += '%s<%s:GmlFeatureStyle.gml_label_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_symbols:
            s += '%s<%s:GmlFeatureStyle.gml_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_tobology_styles:
            s += '%s<%s:GmlFeatureStyle.gml_tobology_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GmlFeatureStyle.query_grammar>%s</%s:GmlFeatureStyle.query_grammar>' % \
            (indent, ns_prefix, self.query_grammar, ns_prefix)
        s += '%s<%s:GmlFeatureStyle.version>%s</%s:GmlFeatureStyle.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)
        s += '%s<%s:GmlFeatureStyle.feature_type_name>%s</%s:GmlFeatureStyle.feature_type_name>' % \
            (indent, ns_prefix, self.feature_type_name, ns_prefix)
        s += '%s<%s:GmlFeatureStyle.base_type>%s</%s:GmlFeatureStyle.base_type>' % \
            (indent, ns_prefix, self.base_type, ns_prefix)
        s += '%s<%s:GmlFeatureStyle.feature_type>%s</%s:GmlFeatureStyle.feature_type>' % \
            (indent, ns_prefix, self.feature_type, ns_prefix)
        s += '%s<%s:GmlFeatureStyle.semantic_type_identifier>%s</%s:GmlFeatureStyle.semantic_type_identifier>' % \
            (indent, ns_prefix, self.semantic_type_identifier, ns_prefix)
        s += '%s<%s:GmlFeatureStyle.feature_constraint>%s</%s:GmlFeatureStyle.feature_constraint>' % \
            (indent, ns_prefix, self.feature_constraint, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlFeatureStyle")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_feature_style.serialize


class GmlPointSymbol(GmlSymbol):
    """ Used to draw a 'graphic' at a point.
    """
    # <<< gml_point_symbol
    # @generated
    def __init__(self, gml_graphic=None, gml_diagram_object=None, **kw_args):
        """ Initialises a new 'GmlPointSymbol' instance.
        """

        self._gml_graphic = None
        self.gml_graphic = gml_graphic

        self._gml_diagram_object = None
        self.gml_diagram_object = gml_diagram_object


        super(GmlPointSymbol, self).__init__(**kw_args)
    # >>> gml_point_symbol

    # <<< gml_graphic
    # @generated
    def get_gml_graphic(self):
        """ 
        """
        return self._gml_graphic

    def set_gml_graphic(self, value):
        if self._gml_graphic is not None:
            filtered = [x for x in self.gml_graphic.gml_point_symbols if x != self]
            self._gml_graphic._gml_point_symbols = filtered

        self._gml_graphic = value
        if self._gml_graphic is not None:
            self._gml_graphic._gml_point_symbols.append(self)

    gml_graphic = property(get_gml_graphic, set_gml_graphic)
    # >>> gml_graphic

    # <<< gml_diagram_object
    # @generated
    def get_gml_diagram_object(self):
        """ 
        """
        return self._gml_diagram_object

    def set_gml_diagram_object(self, value):
        if self._gml_diagram_object is not None:
            filtered = [x for x in self.gml_diagram_object.gml_point_symbols if x != self]
            self._gml_diagram_object._gml_point_symbols = filtered

        self._gml_diagram_object = value
        if self._gml_diagram_object is not None:
            self._gml_diagram_object._gml_point_symbols.append(self)

    gml_diagram_object = property(get_gml_diagram_object, set_gml_diagram_object)
    # >>> gml_diagram_object


    def __str__(self):
        """ Returns a string representation of the GmlPointSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_point_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlPointSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlPointSymbol", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_graphic is not None:
            s += '%s<%s:GmlPointSymbol.gml_graphic rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_graphic.uri)
        if self.gml_diagram_object is not None:
            s += '%s<%s:GmlPointSymbol.gml_diagram_object rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_diagram_object.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlSymbol.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_base_symbol is not None:
            s += '%s<%s:GmlSymbol.gml_base_symbol rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_base_symbol.uri)
        s += '%s<%s:GmlSymbol.level>%s</%s:GmlSymbol.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:GmlSymbol.type>%s</%s:GmlSymbol.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlSymbol.version>%s</%s:GmlSymbol.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlPointSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_point_symbol.serialize


class GmlPolygonGeometry(GmlDiagramObject):
    """ Used to show the footprint of substations, sites, service territories, tax districts, school districts, etc.
    """
    pass
    # <<< gml_polygon_geometry
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GmlPolygonGeometry' instance.
        """


        super(GmlPolygonGeometry, self).__init__(**kw_args)
    # >>> gml_polygon_geometry


    def __str__(self):
        """ Returns a string representation of the GmlPolygonGeometry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_polygon_geometry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlPolygonGeometry.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlPolygonGeometry", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)
        for obj in self.diagrams:
            s += '%s<%s:GmlDiagramObject.diagrams rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_line_symbols:
            s += '%s<%s:GmlDiagramObject.gml_line_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_coordinate_systems:
            s += '%s<%s:GmlDiagramObject.gml_coordinate_systems rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_raster_symbols:
            s += '%s<%s:GmlDiagramObject.gml_raster_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_polygon_symbols:
            s += '%s<%s:GmlDiagramObject.gml_polygon_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_point_symbols:
            s += '%s<%s:GmlDiagramObject.gml_point_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlDiagramObject.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlPolygonGeometry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_polygon_geometry.serialize


class GmlPolygonSymbol(GmlSymbol):
    """ Used to draw a polygon (or other area-type geometries), including filling its interior and stroking its border (outline).
    """
    # <<< gml_polygon_symbol
    # @generated
    def __init__(self, gml_fill=None, gml_diagram_object=None, gml_stroke=None, **kw_args):
        """ Initialises a new 'GmlPolygonSymbol' instance.
        """

        self._gml_fill = None
        self.gml_fill = gml_fill

        self._gml_diagram_object = None
        self.gml_diagram_object = gml_diagram_object

        self._gml_stroke = None
        self.gml_stroke = gml_stroke


        super(GmlPolygonSymbol, self).__init__(**kw_args)
    # >>> gml_polygon_symbol

    # <<< gml_fill
    # @generated
    def get_gml_fill(self):
        """ 
        """
        return self._gml_fill

    def set_gml_fill(self, value):
        if self._gml_fill is not None:
            filtered = [x for x in self.gml_fill.gml_polygon_symbols if x != self]
            self._gml_fill._gml_polygon_symbols = filtered

        self._gml_fill = value
        if self._gml_fill is not None:
            self._gml_fill._gml_polygon_symbols.append(self)

    gml_fill = property(get_gml_fill, set_gml_fill)
    # >>> gml_fill

    # <<< gml_diagram_object
    # @generated
    def get_gml_diagram_object(self):
        """ 
        """
        return self._gml_diagram_object

    def set_gml_diagram_object(self, value):
        if self._gml_diagram_object is not None:
            filtered = [x for x in self.gml_diagram_object.gml_polygon_symbols if x != self]
            self._gml_diagram_object._gml_polygon_symbols = filtered

        self._gml_diagram_object = value
        if self._gml_diagram_object is not None:
            self._gml_diagram_object._gml_polygon_symbols.append(self)

    gml_diagram_object = property(get_gml_diagram_object, set_gml_diagram_object)
    # >>> gml_diagram_object

    # <<< gml_stroke
    # @generated
    def get_gml_stroke(self):
        """ 
        """
        return self._gml_stroke

    def set_gml_stroke(self, value):
        if self._gml_stroke is not None:
            filtered = [x for x in self.gml_stroke.gml_polygon_symbols if x != self]
            self._gml_stroke._gml_polygon_symbols = filtered

        self._gml_stroke = value
        if self._gml_stroke is not None:
            self._gml_stroke._gml_polygon_symbols.append(self)

    gml_stroke = property(get_gml_stroke, set_gml_stroke)
    # >>> gml_stroke


    def __str__(self):
        """ Returns a string representation of the GmlPolygonSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_polygon_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlPolygonSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlPolygonSymbol", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_fill is not None:
            s += '%s<%s:GmlPolygonSymbol.gml_fill rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_fill.uri)
        if self.gml_diagram_object is not None:
            s += '%s<%s:GmlPolygonSymbol.gml_diagram_object rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_diagram_object.uri)
        if self.gml_stroke is not None:
            s += '%s<%s:GmlPolygonSymbol.gml_stroke rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_stroke.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlSymbol.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_base_symbol is not None:
            s += '%s<%s:GmlSymbol.gml_base_symbol rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_base_symbol.uri)
        s += '%s<%s:GmlSymbol.level>%s</%s:GmlSymbol.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:GmlSymbol.type>%s</%s:GmlSymbol.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlSymbol.version>%s</%s:GmlSymbol.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlPolygonSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_polygon_symbol.serialize


class GmlLineSymbol(GmlSymbol):
    """ Used to style a 'stroke' along a linear geometry type, such as a string of line segments.
    """
    # <<< gml_line_symbol
    # @generated
    def __init__(self, source_side='', gml_diagram_object=None, gml_stroke=None, **kw_args):
        """ Initialises a new 'GmlLineSymbol' instance.
        """
        # For dynamic network update (i.e. colouring) purposes 
        self.source_side = source_side


        self._gml_diagram_object = None
        self.gml_diagram_object = gml_diagram_object

        self._gml_stroke = None
        self.gml_stroke = gml_stroke


        super(GmlLineSymbol, self).__init__(**kw_args)
    # >>> gml_line_symbol

    # <<< gml_diagram_object
    # @generated
    def get_gml_diagram_object(self):
        """ 
        """
        return self._gml_diagram_object

    def set_gml_diagram_object(self, value):
        if self._gml_diagram_object is not None:
            filtered = [x for x in self.gml_diagram_object.gml_line_symbols if x != self]
            self._gml_diagram_object._gml_line_symbols = filtered

        self._gml_diagram_object = value
        if self._gml_diagram_object is not None:
            self._gml_diagram_object._gml_line_symbols.append(self)

    gml_diagram_object = property(get_gml_diagram_object, set_gml_diagram_object)
    # >>> gml_diagram_object

    # <<< gml_stroke
    # @generated
    def get_gml_stroke(self):
        """ 
        """
        return self._gml_stroke

    def set_gml_stroke(self, value):
        if self._gml_stroke is not None:
            filtered = [x for x in self.gml_stroke.gml_line_symbols if x != self]
            self._gml_stroke._gml_line_symbols = filtered

        self._gml_stroke = value
        if self._gml_stroke is not None:
            self._gml_stroke._gml_line_symbols.append(self)

    gml_stroke = property(get_gml_stroke, set_gml_stroke)
    # >>> gml_stroke


    def __str__(self):
        """ Returns a string representation of the GmlLineSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_line_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlLineSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlLineSymbol", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_diagram_object is not None:
            s += '%s<%s:GmlLineSymbol.gml_diagram_object rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_diagram_object.uri)
        if self.gml_stroke is not None:
            s += '%s<%s:GmlLineSymbol.gml_stroke rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_stroke.uri)
        s += '%s<%s:GmlLineSymbol.source_side>%s</%s:GmlLineSymbol.source_side>' % \
            (indent, ns_prefix, self.source_side, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlSymbol.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_base_symbol is not None:
            s += '%s<%s:GmlSymbol.gml_base_symbol rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_base_symbol.uri)
        s += '%s<%s:GmlSymbol.level>%s</%s:GmlSymbol.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:GmlSymbol.type>%s</%s:GmlSymbol.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlSymbol.version>%s</%s:GmlSymbol.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlLineSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_line_symbol.serialize


class GmlPointGeometry(GmlDiagramObject):
    """ Typically used for rendering power system resources and/or point assets.
    """
    pass
    # <<< gml_point_geometry
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'GmlPointGeometry' instance.
        """


        super(GmlPointGeometry, self).__init__(**kw_args)
    # >>> gml_point_geometry


    def __str__(self):
        """ Returns a string representation of the GmlPointGeometry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_point_geometry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlPointGeometry.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlPointGeometry", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)
        for obj in self.diagrams:
            s += '%s<%s:GmlDiagramObject.diagrams rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_line_symbols:
            s += '%s<%s:GmlDiagramObject.gml_line_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_coordinate_systems:
            s += '%s<%s:GmlDiagramObject.gml_coordinate_systems rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_raster_symbols:
            s += '%s<%s:GmlDiagramObject.gml_raster_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_polygon_symbols:
            s += '%s<%s:GmlDiagramObject.gml_polygon_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_point_symbols:
            s += '%s<%s:GmlDiagramObject.gml_point_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlDiagramObject.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlPointGeometry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_point_geometry.serialize


class GmlRasterSymbol(GmlSymbol):
    """ Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).
    """
    # <<< gml_raster_symbol
    # @generated
    def __init__(self, green_source_name='', brighness_only=False, relief_factor='', overlapbehaviour='', gray_sourcename='', opacity=0.0, red_sourcename='', blue_sourcename='', gml_diagram_object=None, **kw_args):
        """ Initialises a new 'GmlRasterSymbol' instance.
        """
        # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        self.green_source_name = green_source_name

        # If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers. 
        self.brighness_only = brighness_only

        # The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent. 
        self.relief_factor = relief_factor

        # Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes. 
        self.overlapbehaviour = overlapbehaviour

        # A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        self.gray_sourcename = gray_sourcename

        # Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0. 
        self.opacity = opacity

        # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        self.red_sourcename = red_sourcename

        # Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        self.blue_sourcename = blue_sourcename


        self._gml_diagram_object = None
        self.gml_diagram_object = gml_diagram_object


        super(GmlRasterSymbol, self).__init__(**kw_args)
    # >>> gml_raster_symbol

    # <<< gml_diagram_object
    # @generated
    def get_gml_diagram_object(self):
        """ 
        """
        return self._gml_diagram_object

    def set_gml_diagram_object(self, value):
        if self._gml_diagram_object is not None:
            filtered = [x for x in self.gml_diagram_object.gml_raster_symbols if x != self]
            self._gml_diagram_object._gml_raster_symbols = filtered

        self._gml_diagram_object = value
        if self._gml_diagram_object is not None:
            self._gml_diagram_object._gml_raster_symbols.append(self)

    gml_diagram_object = property(get_gml_diagram_object, set_gml_diagram_object)
    # >>> gml_diagram_object


    def __str__(self):
        """ Returns a string representation of the GmlRasterSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_raster_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlRasterSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlRasterSymbol", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_diagram_object is not None:
            s += '%s<%s:GmlRasterSymbol.gml_diagram_object rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_diagram_object.uri)
        s += '%s<%s:GmlRasterSymbol.green_source_name>%s</%s:GmlRasterSymbol.green_source_name>' % \
            (indent, ns_prefix, self.green_source_name, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.brighness_only>%s</%s:GmlRasterSymbol.brighness_only>' % \
            (indent, ns_prefix, self.brighness_only, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.relief_factor>%s</%s:GmlRasterSymbol.relief_factor>' % \
            (indent, ns_prefix, self.relief_factor, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.overlapbehaviour>%s</%s:GmlRasterSymbol.overlapbehaviour>' % \
            (indent, ns_prefix, self.overlapbehaviour, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.gray_sourcename>%s</%s:GmlRasterSymbol.gray_sourcename>' % \
            (indent, ns_prefix, self.gray_sourcename, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.opacity>%s</%s:GmlRasterSymbol.opacity>' % \
            (indent, ns_prefix, self.opacity, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.red_sourcename>%s</%s:GmlRasterSymbol.red_sourcename>' % \
            (indent, ns_prefix, self.red_sourcename, ns_prefix)
        s += '%s<%s:GmlRasterSymbol.blue_sourcename>%s</%s:GmlRasterSymbol.blue_sourcename>' % \
            (indent, ns_prefix, self.blue_sourcename, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlSymbol.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_base_symbol is not None:
            s += '%s<%s:GmlSymbol.gml_base_symbol rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_base_symbol.uri)
        s += '%s<%s:GmlSymbol.level>%s</%s:GmlSymbol.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:GmlSymbol.type>%s</%s:GmlSymbol.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlSymbol.version>%s</%s:GmlSymbol.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlRasterSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_raster_symbol.serialize


class GmlLineGeometry(GmlDiagramObject):
    """ Typically used for rendering linear assets and/or power system resources.
    """
    # <<< gml_line_geometry
    # @generated
    def __init__(self, source_side='', **kw_args):
        """ Initialises a new 'GmlLineGeometry' instance.
        """
        # For dynamic network update (i.e. colouring) purposes 
        self.source_side = source_side



        super(GmlLineGeometry, self).__init__(**kw_args)
    # >>> gml_line_geometry


    def __str__(self):
        """ Returns a string representation of the GmlLineGeometry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_line_geometry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlLineGeometry.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlLineGeometry", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:GmlLineGeometry.source_side>%s</%s:GmlLineGeometry.source_side>' % \
            (indent, ns_prefix, self.source_side, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)
        for obj in self.diagrams:
            s += '%s<%s:GmlDiagramObject.diagrams rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_line_symbols:
            s += '%s<%s:GmlDiagramObject.gml_line_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_coordinate_systems:
            s += '%s<%s:GmlDiagramObject.gml_coordinate_systems rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_raster_symbols:
            s += '%s<%s:GmlDiagramObject.gml_raster_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_polygon_symbols:
            s += '%s<%s:GmlDiagramObject.gml_polygon_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_point_symbols:
            s += '%s<%s:GmlDiagramObject.gml_point_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_text_symbols:
            s += '%s<%s:GmlDiagramObject.gml_text_symbols rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlLineGeometry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_line_geometry.serialize


class GmlTextSymbol(GmlSymbol):
    """ Used for styling text labels, i.e., for rendering them according to various graphical parameters.
    """
    # <<< gml_text_symbol
    # @generated
    def __init__(self, min_font_size=0, property='', field_id='', label='', label_type='', gml_font=None, gml_label_placement=None, gml_fill=None, gml_halo=None, gml_diagram_object=None, **kw_args):
        """ Initialises a new 'GmlTextSymbol' instance.
        """
        # The minimum font size allowed. 
        self.min_font_size = min_font_size

        # Generic method for capturing all unspecified information pertaining to the TextSymbol. 
        self.property = property

        # The name of the field of the class being annotated. Most objects will include name, description, and aliasName. Many objects may contain other fields such as comment, status, etc. 
        self.field_id = field_id

        # Text-label content. If the value is not provided, then no text will be rendered. 
        self.label = label

        # The type-classification of a label. 
        self.label_type = label_type


        self._gml_font = None
        self.gml_font = gml_font

        self._gml_label_placement = None
        self.gml_label_placement = gml_label_placement

        self._gml_fill = None
        self.gml_fill = gml_fill

        self._gml_halo = None
        self.gml_halo = gml_halo

        self._gml_diagram_object = None
        self.gml_diagram_object = gml_diagram_object


        super(GmlTextSymbol, self).__init__(**kw_args)
    # >>> gml_text_symbol

    # <<< gml_font
    # @generated
    def get_gml_font(self):
        """ 
        """
        return self._gml_font

    def set_gml_font(self, value):
        if self._gml_font is not None:
            filtered = [x for x in self.gml_font.gml_text_symbols if x != self]
            self._gml_font._gml_text_symbols = filtered

        self._gml_font = value
        if self._gml_font is not None:
            self._gml_font._gml_text_symbols.append(self)

    gml_font = property(get_gml_font, set_gml_font)
    # >>> gml_font

    # <<< gml_label_placement
    # @generated
    def get_gml_label_placement(self):
        """ 
        """
        return self._gml_label_placement

    def set_gml_label_placement(self, value):
        if self._gml_label_placement is not None:
            filtered = [x for x in self.gml_label_placement.gml_text_symbols if x != self]
            self._gml_label_placement._gml_text_symbols = filtered

        self._gml_label_placement = value
        if self._gml_label_placement is not None:
            self._gml_label_placement._gml_text_symbols.append(self)

    gml_label_placement = property(get_gml_label_placement, set_gml_label_placement)
    # >>> gml_label_placement

    # <<< gml_fill
    # @generated
    def get_gml_fill(self):
        """ 
        """
        return self._gml_fill

    def set_gml_fill(self, value):
        if self._gml_fill is not None:
            filtered = [x for x in self.gml_fill.gml_text_symbols if x != self]
            self._gml_fill._gml_text_symbols = filtered

        self._gml_fill = value
        if self._gml_fill is not None:
            self._gml_fill._gml_text_symbols.append(self)

    gml_fill = property(get_gml_fill, set_gml_fill)
    # >>> gml_fill

    # <<< gml_halo
    # @generated
    def get_gml_halo(self):
        """ 
        """
        return self._gml_halo

    def set_gml_halo(self, value):
        if self._gml_halo is not None:
            filtered = [x for x in self.gml_halo.gml_text_symbols if x != self]
            self._gml_halo._gml_text_symbols = filtered

        self._gml_halo = value
        if self._gml_halo is not None:
            self._gml_halo._gml_text_symbols.append(self)

    gml_halo = property(get_gml_halo, set_gml_halo)
    # >>> gml_halo

    # <<< gml_diagram_object
    # @generated
    def get_gml_diagram_object(self):
        """ 
        """
        return self._gml_diagram_object

    def set_gml_diagram_object(self, value):
        if self._gml_diagram_object is not None:
            filtered = [x for x in self.gml_diagram_object.gml_text_symbols if x != self]
            self._gml_diagram_object._gml_text_symbols = filtered

        self._gml_diagram_object = value
        if self._gml_diagram_object is not None:
            self._gml_diagram_object._gml_text_symbols.append(self)

    gml_diagram_object = property(get_gml_diagram_object, set_gml_diagram_object)
    # >>> gml_diagram_object


    def __str__(self):
        """ Returns a string representation of the GmlTextSymbol.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gml_text_symbol.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GmlTextSymbol.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GmlTextSymbol", self.uri)
        if format:
            indent += ' ' * depth

        if self.gml_font is not None:
            s += '%s<%s:GmlTextSymbol.gml_font rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_font.uri)
        if self.gml_label_placement is not None:
            s += '%s<%s:GmlTextSymbol.gml_label_placement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_label_placement.uri)
        if self.gml_fill is not None:
            s += '%s<%s:GmlTextSymbol.gml_fill rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_fill.uri)
        if self.gml_halo is not None:
            s += '%s<%s:GmlTextSymbol.gml_halo rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_halo.uri)
        if self.gml_diagram_object is not None:
            s += '%s<%s:GmlTextSymbol.gml_diagram_object rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_diagram_object.uri)
        s += '%s<%s:GmlTextSymbol.min_font_size>%s</%s:GmlTextSymbol.min_font_size>' % \
            (indent, ns_prefix, self.min_font_size, ns_prefix)
        s += '%s<%s:GmlTextSymbol.property>%s</%s:GmlTextSymbol.property>' % \
            (indent, ns_prefix, self.property, ns_prefix)
        s += '%s<%s:GmlTextSymbol.field_id>%s</%s:GmlTextSymbol.field_id>' % \
            (indent, ns_prefix, self.field_id, ns_prefix)
        s += '%s<%s:GmlTextSymbol.label>%s</%s:GmlTextSymbol.label>' % \
            (indent, ns_prefix, self.label, ns_prefix)
        s += '%s<%s:GmlTextSymbol.label_type>%s</%s:GmlTextSymbol.label_type>' % \
            (indent, ns_prefix, self.label_type, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.gml_feature_styles:
            s += '%s<%s:GmlSymbol.gml_feature_styles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_base_symbol is not None:
            s += '%s<%s:GmlSymbol.gml_base_symbol rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_base_symbol.uri)
        s += '%s<%s:GmlSymbol.level>%s</%s:GmlSymbol.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:GmlSymbol.type>%s</%s:GmlSymbol.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:GmlSymbol.version>%s</%s:GmlSymbol.version>' % \
            (indent, ns_prefix, self.version, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GmlTextSymbol")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gml_text_symbol.serialize


# <<< inf_gmlsupport
# @generated
# >>> inf_gmlsupport

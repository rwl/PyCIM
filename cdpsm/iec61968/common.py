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

""" This package contains the information classes that support distribution management in general.This package contains the information classes that support distribution management in general.
"""

from cdpsm.iec61970.core import IdentifiedObject
from cdpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Common"

class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """
    # <<< location
    # @generated
    def __init__(self, position_points=None, **kw_args):
        """ Initialises a new 'Location' instance.
        """

        self._position_points = []
        if position_points is not None:
            self.position_points = position_points
        else:
            self.position_points = []


        super(Location, self).__init__(**kw_args)
    # >>> location

    # <<< position_points
    # @generated
    def get_position_points(self):
        """ Sequence of position points describing this location.Sequence of position points describing this location.
        """
        return self._position_points

    def set_position_points(self, value):
        for x in self._position_points:
            x._location = None
        for y in value:
            y._location = self
        self._position_points = value

    position_points = property(get_position_points, set_position_points)

    def add_position_points(self, *position_points):
        for obj in position_points:
            obj._location = self
            self._position_points.append(obj)

    def remove_position_points(self, *position_points):
        for obj in position_points:
            obj._location = None
            self._position_points.remove(obj)
    # >>> position_points


    def __str__(self):
        """ Returns a string representation of the Location.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Location.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Location", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Location")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> location.serialize


class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """
    # <<< position_point
    # @generated
    def __init__(self, sequence_number=0, x_position='', y_position='', location=None, **kw_args):
        """ Initialises a new 'PositionPoint' instance.
        """
        # Zero-relative sequence number of this point within a series of points.Zero-relative sequence number of this point within a series of points. 
        self.sequence_number = sequence_number

        # X axis position.X axis position. 
        self.x_position = x_position

        # Y axis position.Y axis position. 
        self.y_position = y_position


        self._location = None
        self.location = location


        super(PositionPoint, self).__init__(**kw_args)
    # >>> position_point

    # <<< location
    # @generated
    def get_location(self):
        """ Location that this position point describes.Location that this position point describes.
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.position_points if x != self]
            self._location._position_points = filtered

        self._location = value
        if self._location is not None:
            self._location._position_points.append(self)

    location = property(get_location, set_location)
    # >>> location


    def __str__(self):
        """ Returns a string representation of the PositionPoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< position_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PositionPoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PositionPoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.location is not None:
            s += '%s<%s:PositionPoint.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        s += '%s<%s:PositionPoint.sequence_number>%s</%s:PositionPoint.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:PositionPoint.x_position>%s</%s:PositionPoint.x_position>' % \
            (indent, ns_prefix, self.x_position, ns_prefix)
        s += '%s<%s:PositionPoint.y_position>%s</%s:PositionPoint.y_position>' % \
            (indent, ns_prefix, self.y_position, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PositionPoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> position_point.serialize


class GeoLocation(Location):
    """ Geographical location.Geographical location.
    """
    # <<< geo_location
    # @generated
    def __init__(self, power_system_resources=None, **kw_args):
        """ Initialises a new 'GeoLocation' instance.
        """

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(GeoLocation, self).__init__(**kw_args)
    # >>> geo_location

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ All power system resources at this geographical location.All power system resources at this geographical location.
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for x in self._power_system_resources:
            x._geo_location = None
        for y in value:
            y._geo_location = self
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._geo_location = self
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._geo_location = None
            self._power_system_resources.remove(obj)
    # >>> power_system_resources


    def __str__(self):
        """ Returns a string representation of the GeoLocation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< geo_location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeoLocation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeoLocation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.power_system_resources:
            s += '%s<%s:GeoLocation.power_system_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeoLocation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> geo_location.serialize


# <<< common
# @generated
# >>> common

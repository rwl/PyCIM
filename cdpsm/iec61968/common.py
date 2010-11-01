# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" This package contains the information classes that support distribution management in general.
"""

from cdpsm.iec61970.core import IdentifiedObject
from cdpsm import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Common"

class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """
    # <<< location
    # @generated
    def __init__(self, position_points=None, *args, **kw_args):
        """ Initialises a new 'Location' instance.

        @param position_points: Sequence of position points describing this location.
        """

        self._position_points = []
        if position_points is not None:
            self.position_points = position_points
        else:
            self.position_points = []


        super(Location, self).__init__(*args, **kw_args)
    # >>> location

    # <<< position_points
    # @generated
    def get_position_points(self):
        """ Sequence of position points describing this location.
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



class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """
    # <<< position_point
    # @generated
    def __init__(self, sequence_number=0, x_position='', y_position='', location=None, *args, **kw_args):
        """ Initialises a new 'PositionPoint' instance.

        @param sequence_number: Zero-relative sequence number of this point within a series of points. 
        @param x_position: X axis position. 
        @param y_position: Y axis position. 
        @param location: Location that this position point describes.
        """
        # Zero-relative sequence number of this point within a series of points. 
        self.sequence_number = sequence_number

        # X axis position. 
        self.x_position = x_position

        # Y axis position. 
        self.y_position = y_position


        self._location = None
        self.location = location


        super(PositionPoint, self).__init__(*args, **kw_args)
    # >>> position_point

    # <<< location
    # @generated
    def get_location(self):
        """ Location that this position point describes.
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



class GeoLocation(Location):
    """ Geographical location.
    """
    # <<< geo_location
    # @generated
    def __init__(self, power_system_resources=None, *args, **kw_args):
        """ Initialises a new 'GeoLocation' instance.

        @param power_system_resources: All power system resources at this geographical location.
        """

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(GeoLocation, self).__init__(*args, **kw_args)
    # >>> geo_location

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ All power system resources at this geographical location.
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



# <<< common
# @generated
# >>> common

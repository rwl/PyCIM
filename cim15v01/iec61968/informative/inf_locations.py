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


from cim15v01.iec61968.common import Agreement
from cim15v01.iec61968.informative.inf_common import Role
from cim15v01.iec61968.common import Location
from cim15v01.iec61970.core import IdentifiedObject
from cim15v01.iec61968.common import GeoLocation
from cim15v01 import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfLocations"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfLocations"

class RightOfWay(Agreement):
    """ A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """
    # <<< right_of_way
    # @generated
    def __init__(self, property_data='', land_properties=None, *args, **kw_args):
        """ Initialises a new 'RightOfWay' instance.

        @param property_data: Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        @param land_properties: All land properties this right of way applies to.
        """
        # Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        self.property_data = property_data


        self._land_properties = []
        if land_properties is not None:
            self.land_properties = land_properties
        else:
            self.land_properties = []


        super(RightOfWay, self).__init__(*args, **kw_args)
    # >>> right_of_way

    # <<< land_properties
    # @generated
    def get_land_properties(self):
        """ All land properties this right of way applies to.
        """
        return self._land_properties

    def set_land_properties(self, value):
        for p in self._land_properties:
            filtered = [q for q in p.right_of_ways if q != self]
            self._land_properties._right_of_ways = filtered
        for r in value:
            if self not in r._right_of_ways:
                r._right_of_ways.append(self)
        self._land_properties = value

    land_properties = property(get_land_properties, set_land_properties)

    def add_land_properties(self, *land_properties):
        for obj in land_properties:
            if self not in obj._right_of_ways:
                obj._right_of_ways.append(self)
            self._land_properties.append(obj)

    def remove_land_properties(self, *land_properties):
        for obj in land_properties:
            if self in obj._right_of_ways:
                obj._right_of_ways.remove(self)
            self._land_properties.remove(obj)
    # >>> land_properties



class OrgPropertyRole(Role):
    """ Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.
    """
    # <<< org_property_role
    # @generated
    def __init__(self, erp_organisation=None, land_property=None, *args, **kw_args):
        """ Initialises a new 'OrgPropertyRole' instance.

        @param erp_organisation:
        @param land_property:
        """

        self._erp_organisation = None
        self.erp_organisation = erp_organisation

        self._land_property = []
        if land_property is not None:
            self.land_property = land_property
        else:
            self.land_property = []


        super(OrgPropertyRole, self).__init__(*args, **kw_args)
    # >>> org_property_role

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.land_property_roles if x != self]
            self._erp_organisation._land_property_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._land_property_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ 
        """
        return self._land_property

    def set_land_property(self, value):
        for p in self._land_property:
            filtered = [q for q in p.erp_organisation_roles if q != self]
            self._land_property._erp_organisation_roles = filtered
        for r in value:
            if self not in r._erp_organisation_roles:
                r._erp_organisation_roles.append(self)
        self._land_property = value

    land_property = property(get_land_property, set_land_property)

    def add_land_property(self, *land_property):
        for obj in land_property:
            if self not in obj._erp_organisation_roles:
                obj._erp_organisation_roles.append(self)
            self._land_property.append(obj)

    def remove_land_property(self, *land_property):
        for obj in land_property:
            if self in obj._erp_organisation_roles:
                obj._erp_organisation_roles.remove(self)
            self._land_property.remove(obj)
    # >>> land_property



class SchematicLocation(Location):
    """ Schematic location. Intended to be used in the context of diagrams (worked out by WG13 in 2008 and 2009).
    """
    pass
    # <<< schematic_location
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'SchematicLocation' instance.

        """


        super(SchematicLocation, self).__init__(*args, **kw_args)
    # >>> schematic_location



class Route(IdentifiedObject):
    """ Route that is followed, for example by service crews.
    """
    # <<< route
    # @generated
    def __init__(self, category='', locations=None, crews=None, status=None, *args, **kw_args):
        """ Initialises a new 'Route' instance.

        @param category: Category by utility's work management standards and practices. 
        @param locations:
        @param crews:
        @param status:
        """
        # Category by utility's work management standards and practices. 
        self.category = category


        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.status = status


        super(Route, self).__init__(*args, **kw_args)
    # >>> route

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.routes if q != self]
            self._locations._routes = filtered
        for r in value:
            if self not in r._routes:
                r._routes.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._routes:
                obj._routes.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._routes:
                obj._routes.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for x in self._crews:
            x._route = None
        for y in value:
            y._route = self
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            obj._route = self
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            obj._route = None
            self._crews.remove(obj)
    # >>> crews

    # <<< status
    # @generated
    status = None
    # >>> status



class Zone(GeoLocation):
    """ Area divided off from other areas. It may be part of the electrical network, a land area where special restrictions apply, weather areas, etc. For weather, it is an area where a set of relatively homogenous weather measurements apply.
    """
    # <<< zone
    # @generated
    def __init__(self, kind='special_restriction_land', *args, **kw_args):
        """ Initialises a new 'Zone' instance.

        @param kind: Kind of this zone. Values are: "special_restriction_land", "electrical_network", "weather_zone", "other"
        """
        # Kind of this zone. Values are: "special_restriction_land", "electrical_network", "weather_zone", "other"
        self.kind = kind



        super(Zone, self).__init__(*args, **kw_args)
    # >>> zone



class Direction(Element):
    """ Used for navigating from one location to another location.
    """
    # <<< direction
    # @generated
    def __init__(self, direction_info='', location=None, *args, **kw_args):
        """ Initialises a new 'Direction' instance.

        @param direction_info: Detailed directional information. 
        @param location:
        """
        # Detailed directional information. 
        self.direction_info = direction_info


        self._location = None
        self.location = location


        super(Direction, self).__init__(*args, **kw_args)
    # >>> direction

    # <<< location
    # @generated
    def get_location(self):
        """ 
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.directions if x != self]
            self._location._directions = filtered

        self._location = value
        if self._location is not None:
            self._location._directions.append(self)

    location = property(get_location, set_location)
    # >>> location



class RedLine(IdentifiedObject):
    """ This class is used for handling the accompanying annotations, time stamp, author, etc. of designs, drawings and maps. A red line can be associated with any Location object.
    """
    # <<< red_line
    # @generated
    def __init__(self, status=None, locations=None, *args, **kw_args):
        """ Initialises a new 'RedLine' instance.

        @param status:
        @param locations:
        """

        self.status = status

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []


        super(RedLine, self).__init__(*args, **kw_args)
    # >>> red_line

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.red_lines if q != self]
            self._locations._red_lines = filtered
        for r in value:
            if self not in r._red_lines:
                r._red_lines.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._red_lines:
                obj._red_lines.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._red_lines:
                obj._red_lines.remove(self)
            self._locations.remove(obj)
    # >>> locations



class LocationGrant(Agreement):
    """ A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """
    # <<< location_grant
    # @generated
    def __init__(self, property_data='', land_property=None, *args, **kw_args):
        """ Initialises a new 'LocationGrant' instance.

        @param property_data: Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        @param land_property: Land property this location grant applies to.
        """
        # Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number. 
        self.property_data = property_data


        self._land_property = None
        self.land_property = land_property


        super(LocationGrant, self).__init__(*args, **kw_args)
    # >>> location_grant

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ Land property this location grant applies to.
        """
        return self._land_property

    def set_land_property(self, value):
        if self._land_property is not None:
            filtered = [x for x in self.land_property.location_grants if x != self]
            self._land_property._location_grants = filtered

        self._land_property = value
        if self._land_property is not None:
            self._land_property._location_grants.append(self)

    land_property = property(get_land_property, set_land_property)
    # >>> land_property



class LandProperty(IdentifiedObject):
    """ Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.
    """
    # <<< land_property
    # @generated
    def __init__(self, kind='store', demographic_kind='other', external_record_reference='', location_grants=None, asset_containers=None, erp_site_level_datas=None, erp_person_roles=None, right_of_ways=None, erp_organisation_roles=None, locations=None, status=None, *args, **kw_args):
        """ Initialises a new 'LandProperty' instance.

        @param kind: Kind of (land) property, categorised according to its main functional use from the utility's perspective. Values are: "store", "depot", "customer_premise", "external", "grid_supply_point", "substation", "building"
        @param demographic_kind: Demographics around the site. Values are: "other", "urban", "rural"
        @param external_record_reference: Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation. 
        @param location_grants: All location grants this land property has.
        @param asset_containers:
        @param erp_site_level_datas:
        @param erp_person_roles:
        @param right_of_ways: All rights of way this land property has.
        @param erp_organisation_roles:
        @param locations: The spatail description of a piece of property.
        @param status:
        """
        # Kind of (land) property, categorised according to its main functional use from the utility's perspective. Values are: "store", "depot", "customer_premise", "external", "grid_supply_point", "substation", "building"
        self.kind = kind

        # Demographics around the site. Values are: "other", "urban", "rural"
        self.demographic_kind = demographic_kind

        # Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation. 
        self.external_record_reference = external_record_reference


        self._location_grants = []
        if location_grants is not None:
            self.location_grants = location_grants
        else:
            self.location_grants = []

        self._asset_containers = []
        if asset_containers is not None:
            self.asset_containers = asset_containers
        else:
            self.asset_containers = []

        self._erp_site_level_datas = []
        if erp_site_level_datas is not None:
            self.erp_site_level_datas = erp_site_level_datas
        else:
            self.erp_site_level_datas = []

        self._erp_person_roles = []
        if erp_person_roles is not None:
            self.erp_person_roles = erp_person_roles
        else:
            self.erp_person_roles = []

        self._right_of_ways = []
        if right_of_ways is not None:
            self.right_of_ways = right_of_ways
        else:
            self.right_of_ways = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self.status = status


        super(LandProperty, self).__init__(*args, **kw_args)
    # >>> land_property

    # <<< location_grants
    # @generated
    def get_location_grants(self):
        """ All location grants this land property has.
        """
        return self._location_grants

    def set_location_grants(self, value):
        for x in self._location_grants:
            x._land_property = None
        for y in value:
            y._land_property = self
        self._location_grants = value

    location_grants = property(get_location_grants, set_location_grants)

    def add_location_grants(self, *location_grants):
        for obj in location_grants:
            obj._land_property = self
            self._location_grants.append(obj)

    def remove_location_grants(self, *location_grants):
        for obj in location_grants:
            obj._land_property = None
            self._location_grants.remove(obj)
    # >>> location_grants

    # <<< asset_containers
    # @generated
    def get_asset_containers(self):
        """ 
        """
        return self._asset_containers

    def set_asset_containers(self, value):
        for p in self._asset_containers:
            filtered = [q for q in p.land_properties if q != self]
            self._asset_containers._land_properties = filtered
        for r in value:
            if self not in r._land_properties:
                r._land_properties.append(self)
        self._asset_containers = value

    asset_containers = property(get_asset_containers, set_asset_containers)

    def add_asset_containers(self, *asset_containers):
        for obj in asset_containers:
            if self not in obj._land_properties:
                obj._land_properties.append(self)
            self._asset_containers.append(obj)

    def remove_asset_containers(self, *asset_containers):
        for obj in asset_containers:
            if self in obj._land_properties:
                obj._land_properties.remove(self)
            self._asset_containers.remove(obj)
    # >>> asset_containers

    # <<< erp_site_level_datas
    # @generated
    def get_erp_site_level_datas(self):
        """ 
        """
        return self._erp_site_level_datas

    def set_erp_site_level_datas(self, value):
        for x in self._erp_site_level_datas:
            x._land_property = None
        for y in value:
            y._land_property = self
        self._erp_site_level_datas = value

    erp_site_level_datas = property(get_erp_site_level_datas, set_erp_site_level_datas)

    def add_erp_site_level_datas(self, *erp_site_level_datas):
        for obj in erp_site_level_datas:
            obj._land_property = self
            self._erp_site_level_datas.append(obj)

    def remove_erp_site_level_datas(self, *erp_site_level_datas):
        for obj in erp_site_level_datas:
            obj._land_property = None
            self._erp_site_level_datas.remove(obj)
    # >>> erp_site_level_datas

    # <<< erp_person_roles
    # @generated
    def get_erp_person_roles(self):
        """ 
        """
        return self._erp_person_roles

    def set_erp_person_roles(self, value):
        for x in self._erp_person_roles:
            x._land_property = None
        for y in value:
            y._land_property = self
        self._erp_person_roles = value

    erp_person_roles = property(get_erp_person_roles, set_erp_person_roles)

    def add_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._land_property = self
            self._erp_person_roles.append(obj)

    def remove_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._land_property = None
            self._erp_person_roles.remove(obj)
    # >>> erp_person_roles

    # <<< right_of_ways
    # @generated
    def get_right_of_ways(self):
        """ All rights of way this land property has.
        """
        return self._right_of_ways

    def set_right_of_ways(self, value):
        for p in self._right_of_ways:
            filtered = [q for q in p.land_properties if q != self]
            self._right_of_ways._land_properties = filtered
        for r in value:
            if self not in r._land_properties:
                r._land_properties.append(self)
        self._right_of_ways = value

    right_of_ways = property(get_right_of_ways, set_right_of_ways)

    def add_right_of_ways(self, *right_of_ways):
        for obj in right_of_ways:
            if self not in obj._land_properties:
                obj._land_properties.append(self)
            self._right_of_ways.append(obj)

    def remove_right_of_ways(self, *right_of_ways):
        for obj in right_of_ways:
            if self in obj._land_properties:
                obj._land_properties.remove(self)
            self._right_of_ways.remove(obj)
    # >>> right_of_ways

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for p in self._erp_organisation_roles:
            filtered = [q for q in p.land_property if q != self]
            self._erp_organisation_roles._land_property = filtered
        for r in value:
            if self not in r._land_property:
                r._land_property.append(self)
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            if self not in obj._land_property:
                obj._land_property.append(self)
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            if self in obj._land_property:
                obj._land_property.remove(self)
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< locations
    # @generated
    def get_locations(self):
        """ The spatail description of a piece of property.
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.land_properties if q != self]
            self._locations._land_properties = filtered
        for r in value:
            if self not in r._land_properties:
                r._land_properties.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._land_properties:
                obj._land_properties.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._land_properties:
                obj._land_properties.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< status
    # @generated
    status = None
    # >>> status



class Hazard(IdentifiedObject):
    """ A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.
    """
    # <<< hazard
    # @generated
    def __init__(self, category='', locations=None, status=None, *args, **kw_args):
        """ Initialises a new 'Hazard' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param locations: The point or polygon location of a given hazard.
        @param status:
        """
        # Category by utility's corporate standards and practices. 
        self.category = category


        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self.status = status


        super(Hazard, self).__init__(*args, **kw_args)
    # >>> hazard

    # <<< locations
    # @generated
    def get_locations(self):
        """ The point or polygon location of a given hazard.
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.hazards if q != self]
            self._locations._hazards = filtered
        for r in value:
            if self not in r._hazards:
                r._hazards.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._hazards:
                obj._hazards.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._hazards:
                obj._hazards.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< status
    # @generated
    status = None
    # >>> status



class PersonPropertyRole(Role):
    """ The role of a person relative to a given piece of property. Examples of roles include: owner, renter, contractor, etc.
    """
    # <<< person_property_role
    # @generated
    def __init__(self, land_property=None, erp_person=None, *args, **kw_args):
        """ Initialises a new 'PersonPropertyRole' instance.

        @param land_property:
        @param erp_person:
        """

        self._land_property = None
        self.land_property = land_property

        self._erp_person = None
        self.erp_person = erp_person


        super(PersonPropertyRole, self).__init__(*args, **kw_args)
    # >>> person_property_role

    # <<< land_property
    # @generated
    def get_land_property(self):
        """ 
        """
        return self._land_property

    def set_land_property(self, value):
        if self._land_property is not None:
            filtered = [x for x in self.land_property.erp_person_roles if x != self]
            self._land_property._erp_person_roles = filtered

        self._land_property = value
        if self._land_property is not None:
            self._land_property._erp_person_roles.append(self)

    land_property = property(get_land_property, set_land_property)
    # >>> land_property

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.land_property_roles if x != self]
            self._erp_person._land_property_roles = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._land_property_roles.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person



# <<< inf_locations
# @generated
# >>> inf_locations

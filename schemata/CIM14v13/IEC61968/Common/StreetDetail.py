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

from CIM14v13.Element import Element

class StreetDetail(Element):
    """Street details, in the context of address.
    """

    def __init__(self, buildingName='', type='', name='', withinTownLimits=False, number='', suffix='', prefix='', code='', addressGeneral='', suiteNumber='', *args, **kw_args):
        """Initializes a new 'StreetDetail' instance.

        @param buildingName: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. 
        @param type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. 
        @param name: Name of the street. 
        @param withinTownLimits: True if this street is within the legal geographical boundaries of the specified town (default). 
        @param number: Designator of the specific location on the street. 
        @param suffix: Suffix to the street name. For example: North, South, East, West. 
        @param prefix: Prefix to the street name. For example: North, South, East, West. 
        @param code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. 
        @param addressGeneral: Additional address information, for example a mailstop. 
        @param suiteNumber: Number of the apartment or suite. 
        """
        #: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. 
        self.buildingName = buildingName

        #: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. 
        self.type = type

        #: Name of the street. 
        self.name = name

        #: True if this street is within the legal geographical boundaries of the specified town (default). 
        self.withinTownLimits = withinTownLimits

        #: Designator of the specific location on the street. 
        self.number = number

        #: Suffix to the street name. For example: North, South, East, West. 
        self.suffix = suffix

        #: Prefix to the street name. For example: North, South, East, West. 
        self.prefix = prefix

        #: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. 
        self.code = code

        #: Additional address information, for example a mailstop. 
        self.addressGeneral = addressGeneral

        #: Number of the apartment or suite. 
        self.suiteNumber = suiteNumber

        super(StreetDetail, self).__init__(*args, **kw_args)


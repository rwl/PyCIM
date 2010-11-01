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

from CIM14v13.IEC61968.Common.Location import Location

class Zone(Location):
    """Area divided off from other areas. It may be part of the electrical network, a land area where special restrictions apply, weather areas, etc. For weather, it is an area where a set of relatively homogenous weather measurements apply.
    """

    def __init__(self, kind='specialRestrictionLand', *args, **kw_args):
        """Initializes a new 'Zone' instance.

        @param kind: Kind of this zone. Values are: "specialRestrictionLand", "electricalNetwork", "weatherZone", "other"
        """
        #: Kind of this zone. Values are: "specialRestrictionLand", "electricalNetwork", "weatherZone", "other"
        self.kind = kind

        super(Zone, self).__init__(*args, **kw_args)


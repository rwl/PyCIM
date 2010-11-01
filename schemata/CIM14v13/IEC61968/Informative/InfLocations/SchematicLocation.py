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

class SchematicLocation(Location):
    """Schematic location. Intended to be used in the context of diagrams (worked out by WG13 in 2008 and 2009).
    """

    def __init__(self, *args, **kw_args):
        """Initializes a new 'SchematicLocation' instance.

        """
        super(SchematicLocation, self).__init__(*args, **kw_args)


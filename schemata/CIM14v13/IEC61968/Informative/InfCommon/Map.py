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

from CIM14v13.IEC61968.Informative.InfCommon.Diagram import Diagram

class Map(Diagram):
    """A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.
    """

    def __init__(self, mapLocGrid='', pageNumber=0, **kw_args):
        """Initializes a new 'Map' instance.

        @param mapLocGrid: Map grid number. 
        @param pageNumber: Page number for particular set of maps specified by 'category'. 
        """
        #: Map grid number.
        self.mapLocGrid = mapLocGrid

        #: Page number for particular set of maps specified by 'category'.
        self.pageNumber = pageNumber

        super(Map, self).__init__(**kw_args)


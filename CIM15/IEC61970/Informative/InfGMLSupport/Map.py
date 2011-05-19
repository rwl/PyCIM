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

from CIM15.IEC61970.Informative.InfGMLSupport.Diagram import Diagram

class Map(Diagram):
    """A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.
    """

    def __init__(self, pageNumber=0, mapLocGrid='', *args, **kw_args):
        """Initialises a new 'Map' instance.

        @param pageNumber: Page number for particular set of maps specified by 'category'. 
        @param mapLocGrid: Map grid number. 
        """
        #: Page number for particular set of maps specified by 'category'.
        self.pageNumber = pageNumber

        #: Map grid number.
        self.mapLocGrid = mapLocGrid

        super(Map, self).__init__(*args, **kw_args)

    _attrs = ["pageNumber", "mapLocGrid"]
    _attr_types = {"pageNumber": int, "mapLocGrid": str}
    _defaults = {"pageNumber": 0, "mapLocGrid": ''}
    _enums = {}
    _refs = []
    _many_refs = []


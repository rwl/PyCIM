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

from CIM14.Element import Element

class StreetDetail(Element):
    """Street details, in the context of address.
    """

    def __init__(self, number='', type='', suiteNumber='', addressGeneral='', buildingName='', name='', withinTownLimits=False, suffix='', code='', prefix='', *args, **kw_args):
        """Initialises a new 'StreetDetail' instance.

        @param number: Designator of the specific location on the street. 
        @param type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. 
        @param suiteNumber: Number of the apartment or suite. 
        @param addressGeneral: Additional address information, for example a mailstop. 
        @param buildingName: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. 
        @param name: Name of the street. 
        @param withinTownLimits: True if this street is within the legal geographical boundaries of the specified town (default). 
        @param suffix: Suffix to the street name. For example: North, South, East, West. 
        @param code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. 
        @param prefix: Prefix to the street name. For example: North, South, East, West. 
        """
        #: Designator of the specific location on the street.
        self.number = number

        #: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.
        self.type = type

        #: Number of the apartment or suite.
        self.suiteNumber = suiteNumber

        #: Additional address information, for example a mailstop.
        self.addressGeneral = addressGeneral

        #: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc.
        self.buildingName = buildingName

        #: Name of the street.
        self.name = name

        #: True if this street is within the legal geographical boundaries of the specified town (default).
        self.withinTownLimits = withinTownLimits

        #: Suffix to the street name. For example: North, South, East, West.
        self.suffix = suffix

        #: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets.
        self.code = code

        #: Prefix to the street name. For example: North, South, East, West.
        self.prefix = prefix

        super(StreetDetail, self).__init__(*args, **kw_args)

    _attrs = ["number", "type", "suiteNumber", "addressGeneral", "buildingName", "name", "withinTownLimits", "suffix", "code", "prefix"]
    _attr_types = {"number": str, "type": str, "suiteNumber": str, "addressGeneral": str, "buildingName": str, "name": str, "withinTownLimits": bool, "suffix": str, "code": str, "prefix": str}
    _defaults = {"number": '', "type": '', "suiteNumber": '', "addressGeneral": '', "buildingName": '', "name": '', "withinTownLimits": False, "suffix": '', "code": '', "prefix": ''}
    _enums = {}
    _refs = []
    _many_refs = []


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


class StreetDetail(object):
    """Street details, in the context of address.Street details, in the context of address.
    """

    def __init__(self, withinTownLimits=False, name='', type='', prefix='', buildingName='', suiteNumber='', suffix='', addressGeneral='', code='', number=''):
        """Initialises a new 'StreetDetail' instance.

        @param withinTownLimits: True if this street is within the legal geographical boundaries of the specified town (default). 
        @param name: Name of the street. 
        @param type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. 
        @param prefix: Prefix to the street name. For example: North, South, East, West. 
        @param buildingName: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. 
        @param suiteNumber: Number of the apartment or suite. 
        @param suffix: Suffix to the street name. For example: North, South, East, West. 
        @param addressGeneral: Additional address information, for example a mailstop. 
        @param code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. 
        @param number: Designator of the specific location on the street. 
        """
        #: True if this street is within the legal geographical boundaries of the specified town (default).
        self.withinTownLimits = withinTownLimits

        #: Name of the street.
        self.name = name

        #: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.
        self.type = type

        #: Prefix to the street name. For example: North, South, East, West.
        self.prefix = prefix

        #: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc.
        self.buildingName = buildingName

        #: Number of the apartment or suite.
        self.suiteNumber = suiteNumber

        #: Suffix to the street name. For example: North, South, East, West.
        self.suffix = suffix

        #: Additional address information, for example a mailstop.
        self.addressGeneral = addressGeneral

        #: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets.
        self.code = code

        #: Designator of the specific location on the street.
        self.number = number


    _attrs = ["withinTownLimits", "name", "type", "prefix", "buildingName", "suiteNumber", "suffix", "addressGeneral", "code", "number"]
    _attr_types = {"withinTownLimits": bool, "name": str, "type": str, "prefix": str, "buildingName": str, "suiteNumber": str, "suffix": str, "addressGeneral": str, "code": str, "number": str}
    _defaults = {"withinTownLimits": False, "name": '', "type": '', "prefix": '', "buildingName": '', "suiteNumber": '', "suffix": '', "addressGeneral": '', "code": '', "number": ''}
    _enums = {}
    _refs = []
    _many_refs = []


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


class TelephoneNumber(object):
    """Telephone number.Telephone number.
    """

    def __init__(self, cityCode='', localNumber='', extension='', areaCode='', countryCode=''):
        """Initialises a new 'TelephoneNumber' instance.

        @param cityCode: (if applicable) City code. 
        @param localNumber: Main (local) part of this telephone number. 
        @param extension: (if applicable) Extension for this telephone number. 
        @param areaCode: Area or region code. 
        @param countryCode: Country code. 
        """
        #: (if applicable) City code.
        self.cityCode = cityCode

        #: Main (local) part of this telephone number.
        self.localNumber = localNumber

        #: (if applicable) Extension for this telephone number.
        self.extension = extension

        #: Area or region code.
        self.areaCode = areaCode

        #: Country code.
        self.countryCode = countryCode


    _attrs = ["cityCode", "localNumber", "extension", "areaCode", "countryCode"]
    _attr_types = {"cityCode": str, "localNumber": str, "extension": str, "areaCode": str, "countryCode": str}
    _defaults = {"cityCode": '', "localNumber": '', "extension": '', "areaCode": '', "countryCode": ''}
    _enums = {}
    _refs = []
    _many_refs = []


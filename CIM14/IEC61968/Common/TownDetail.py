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

class TownDetail(Element):
    """Town details, in the context of address.
    """

    def __init__(self, code='', country='', stateOrProvince='', name='', section='', *args, **kw_args):
        """Initialises a new 'TownDetail' instance.

        @param code: Town code. 
        @param country: Name of the country. 
        @param stateOrProvince: Name of the state or province. 
        @param name: Town name. 
        @param section: Town section. For example, it is common for there to be 36 sections per township. 
        """
        #: Town code.
        self.code = code

        #: Name of the country.
        self.country = country

        #: Name of the state or province.
        self.stateOrProvince = stateOrProvince

        #: Town name.
        self.name = name

        #: Town section. For example, it is common for there to be 36 sections per township.
        self.section = section

        super(TownDetail, self).__init__(*args, **kw_args)

    _attrs = ["code", "country", "stateOrProvince", "name", "section"]
    _attr_types = {"code": str, "country": str, "stateOrProvince": str, "name": str, "section": str}
    _defaults = {"code": '', "country": '', "stateOrProvince": '', "name": '', "section": ''}
    _enums = {}
    _refs = []
    _many_refs = []


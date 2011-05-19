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

from CIM15.Element import Element

class IEC61970CIMVersion(Element):
    """This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.
    """

    def __init__(self, date='', version='', *args, **kw_args):
        """Initialises a new 'IEC61970CIMVersion' instance.

        @param date: Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        @param version: Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version. For ecample IEC61970CIM13v18. 
        """
        #: Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05.
        self.date = date

        #: Form is IEC61970CIMXXvYY where XX is the major CIM package version and the YY is the minor version. For ecample IEC61970CIM13v18.
        self.version = version

        super(IEC61970CIMVersion, self).__init__(*args, **kw_args)

    _attrs = ["date", "version"]
    _attr_types = {"date": str, "version": str}
    _defaults = {"date": '', "version": ''}
    _enums = {}
    _refs = []
    _many_refs = []


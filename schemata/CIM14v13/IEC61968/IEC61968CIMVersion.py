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

class IEC61968CIMVersion(Element):
    """IEC 61968 version number assigned to this UML model.
    """

    def __init__(self, version='', date='', *args, **kw_args):
        """Initializes a new 'IEC61968CIMVersion' instance.

        @param version: Form is IEC61968CIMXXvYY where XX is the major CIM package version and the YY is the minor version.  For example IEC61968CIM10v17. 
        @param date: Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        """
        #: Form is IEC61968CIMXXvYY where XX is the major CIM package version and the YY is the minor version.  For example IEC61968CIM10v17. 
        self.version = version

        #: Form is YYYY-MM-DD for example for January 5, 2009 it is 2009-01-05. 
        self.date = date

        super(IEC61968CIMVersion, self).__init__(*args, **kw_args)


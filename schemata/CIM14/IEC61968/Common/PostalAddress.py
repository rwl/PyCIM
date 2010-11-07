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

from CIM14.Element import Element

class PostalAddress(Element):
    """General purpose postal address information.
    """

    def __init__(self, poBox='', postalCode='', streetDetail=None, townDetail=None, **kw_args):
        """Initializes a new 'PostalAddress' instance.

        @param poBox: Post office box. 
        @param postalCode: Postal code for the address. 
        @param streetDetail: Street detail.
        @param townDetail: Town detail.
        """
        #: Post office box.
        self.poBox = poBox

        #: Postal code for the address.
        self.postalCode = postalCode

        self.streetDetail = streetDetail

        self.townDetail = townDetail

        super(PostalAddress, self).__init__(**kw_args)

    # Street detail.
    streetDetail = None

    # Town detail.
    townDetail = None


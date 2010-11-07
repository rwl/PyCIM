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

class ElectronicAddress(Element):
    """Electronic address information.
    """

    def __init__(self, password='', email='', radio='', userID='', lan='', web='', status=None, **kw_args):
        """Initializes a new 'ElectronicAddress' instance.

        @param password: Password needed to log in. 
        @param email: Email address. 
        @param radio: Radio address. 
        @param userID: User ID needed to log in, which can be for an individual person, an organisation, a location, etc. 
        @param lan: Address on local area network. 
        @param web: World Wide Web address. 
        @param status: Status of this electronic address.
        """
        #: Password needed to log in.
        self.password = password

        #: Email address.
        self.email = email

        #: Radio address.
        self.radio = radio

        #: User ID needed to log in, which can be for an individual person, an organisation, a location, etc.
        self.userID = userID

        #: Address on local area network.
        self.lan = lan

        #: World Wide Web address.
        self.web = web

        self.status = status

        super(ElectronicAddress, self).__init__(**kw_args)

    # Status of this electronic address.
    status = None


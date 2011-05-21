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

class ElectronicAddress(Element):
    """Electronic address information.
    """

    def __init__(self, password='', email='', radio='', userID='', lan='', web='', status=None, *args, **kw_args):
        """Initialises a new 'ElectronicAddress' instance.

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

        super(ElectronicAddress, self).__init__(*args, **kw_args)

    _attrs = ["password", "email", "radio", "userID", "lan", "web"]
    _attr_types = {"password": str, "email": str, "radio": str, "userID": str, "lan": str, "web": str}
    _defaults = {"password": '', "email": '', "radio": '', "userID": '', "lan": '', "web": ''}
    _enums = {}
    _refs = ["status"]
    _many_refs = []

    # Status of this electronic address.
    status = None


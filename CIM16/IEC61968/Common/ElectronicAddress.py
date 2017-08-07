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


class ElectronicAddress(object):
    """Electronic address information.Electronic address information.
    """

    def __init__(self, radio='', password='', lan='', userID='', email='', web='', status=None):
        """Initialises a new 'ElectronicAddress' instance.

        @param radio: Radio address. 
        @param password: Password needed to log in. 
        @param lan: Address on local area network. 
        @param userID: User ID needed to log in, which can be for an individual person, an organisation, a location, etc. 
        @param email: Email address. 
        @param web: World wide web address. 
        @param status: Status of this electronic address.
        """
        #: Radio address.
        self.radio = radio

        #: Password needed to log in.
        self.password = password

        #: Address on local area network.
        self.lan = lan

        #: User ID needed to log in, which can be for an individual person, an organisation, a location, etc.
        self.userID = userID

        #: Email address.
        self.email = email

        #: World wide web address.
        self.web = web

        self.status = status


    _attrs = ["radio", "password", "lan", "userID", "email", "web"]
    _attr_types = {"radio": str, "password": str, "lan": str, "userID": str, "email": str, "web": str}
    _defaults = {"radio": '', "password": '', "lan": '', "userID": '', "email": '', "web": ''}
    _enums = {}
    _refs = ["status"]
    _many_refs = []

    # Status of this electronic address.
    status = None


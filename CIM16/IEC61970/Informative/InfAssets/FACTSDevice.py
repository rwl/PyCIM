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

from CIM16.IEC61968.Assets.Asset import Asset

class FACTSDevice(Asset):
    """FACTS device asset.FACTS device asset.
    """

    def __init__(self, kind="tcpar", *args, **kw_args):
        """Initialises a new 'FACTSDevice' instance.

        @param kind: Kind of FACTS device. Values are: "tcpar", "tssc", "tsbr", "svc", "tcsc", "tcvl", "statcom", "upfc"
        """
        #: Kind of FACTS device. Values are: "tcpar", "tssc", "tsbr", "svc", "tcsc", "tcvl", "statcom", "upfc"
        self.kind = kind

        super(FACTSDevice, self).__init__(*args, **kw_args)

    _attrs = ["kind"]
    _attr_types = {"kind": str}
    _defaults = {"kind": "tcpar"}
    _enums = {"kind": "FACTSDeviceKind"}
    _refs = []
    _many_refs = []


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

from CIM15.IEC61970.AuxiliaryEquipment.AuxiliaryEquipment import AuxiliaryEquipment

class SurgeProtector(AuxiliaryEquipment):
    """Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.
    """

    def __init__(self, SurgeProtectorInfo=None, *args, **kw_args):
        """Initialises a new 'SurgeProtector' instance.

        @param SurgeProtectorInfo: Surge protector data.
        """
        self._SurgeProtectorInfo = None
        self.SurgeProtectorInfo = SurgeProtectorInfo

        super(SurgeProtector, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SurgeProtectorInfo"]
    _many_refs = []

    def getSurgeProtectorInfo(self):
        """Surge protector data.
        """
        return self._SurgeProtectorInfo

    def setSurgeProtectorInfo(self, value):
        if self._SurgeProtectorInfo is not None:
            filtered = [x for x in self.SurgeProtectorInfo.SurgeProtectors if x != self]
            self._SurgeProtectorInfo._SurgeProtectors = filtered

        self._SurgeProtectorInfo = value
        if self._SurgeProtectorInfo is not None:
            if self not in self._SurgeProtectorInfo._SurgeProtectors:
                self._SurgeProtectorInfo._SurgeProtectors.append(self)

    SurgeProtectorInfo = property(getSurgeProtectorInfo, setSurgeProtectorInfo)


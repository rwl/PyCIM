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

from CIM15.IEC61970.Informative.InfAssets.Structure import Structure

class Tower(Structure):
    """Tower asset. Dimensions of the Tower are specified in associated DimensionsInfo class. When used for planning purposes, a transmission tower carrying two 3-phase circuits will have 2 instances of Connection, each of which will have 3 MountingPoint instances, one for each phase all with coordinates relative to a common origin on the tower. (It may also have a 3rd Connection with a single MountingPoint for the Neutral line).Tower asset. Dimensions of the Tower are specified in associated DimensionsInfo class. When used for planning purposes, a transmission tower carrying two 3-phase circuits will have 2 instances of Connection, each of which will have 3 MountingPoint instances, one for each phase all with coordinates relative to a common origin on the tower. (It may also have a 3rd Connection with a single MountingPoint for the Neutral line).
    """

    def __init__(self, constructionKind="suspension", *args, **kw_args):
        """Initialises a new 'Tower' instance.

        @param constructionKind: Construction structure on the tower. Values are: "suspension", "tension"
        """
        #: Construction structure on the tower. Values are: "suspension", "tension"
        self.constructionKind = constructionKind

        super(Tower, self).__init__(*args, **kw_args)

    _attrs = ["constructionKind"]
    _attr_types = {"constructionKind": str}
    _defaults = {"constructionKind": "suspension"}
    _enums = {"constructionKind": "TowerConstructionKind"}
    _refs = []
    _many_refs = []


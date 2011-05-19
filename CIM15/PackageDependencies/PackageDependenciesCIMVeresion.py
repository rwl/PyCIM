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

class PackageDependenciesCIMVeresion(Element):
    """The version of dependencies description among top level subpackages of the combined CIM model.  This is not the same as the combined packages version.The version of dependencies description among top level subpackages of the combined CIM model.  This is not the same as the combined packages version.
    """

    def __init__(self, vesion='', date='', *args, **kw_args):
        """Initialises a new 'PackageDependenciesCIMVeresion' instance.

        @param vesion: The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package. 
        @param date: Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated. 
        """
        #: The version of the main subpackages of the combined CIM model.  The format is simply an integer.  The version (and date) initial values should be updated any time the dependencies in the model change and require an actual change to the diagrams within this package.
        self.vesion = vesion

        #: Date of last change to the main package dependencies in format YYYY-MM-DD.   This is updated when the version attribute is updated.
        self.date = date

        super(PackageDependenciesCIMVeresion, self).__init__(*args, **kw_args)

    _attrs = ["vesion", "date"]
    _attr_types = {"vesion": str, "date": str}
    _defaults = {"vesion": '', "date": ''}
    _enums = {}
    _refs = []
    _many_refs = []


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

from CIM15.IEC61968.Common.Document import Document

class OneCallRequest(Document):
    """A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.
    """

    def __init__(self, markedIndicator=False, explosivesUsed=False, markingInstruction='', WorkLocations=None, *args, **kw_args):
        """Initialises a new 'OneCallRequest' instance.

        @param markedIndicator: True if work location has been marked, for example for a dig area. 
        @param explosivesUsed: True if explosives have been or are planned to be used. 
        @param markingInstruction: Instructions for marking a dig area, if applicable. 
        @param WorkLocations:
        """
        #: True if work location has been marked, for example for a dig area.
        self.markedIndicator = markedIndicator

        #: True if explosives have been or are planned to be used.
        self.explosivesUsed = explosivesUsed

        #: Instructions for marking a dig area, if applicable.
        self.markingInstruction = markingInstruction

        self._WorkLocations = []
        self.WorkLocations = [] if WorkLocations is None else WorkLocations

        super(OneCallRequest, self).__init__(*args, **kw_args)

    _attrs = ["markedIndicator", "explosivesUsed", "markingInstruction"]
    _attr_types = {"markedIndicator": bool, "explosivesUsed": bool, "markingInstruction": str}
    _defaults = {"markedIndicator": False, "explosivesUsed": False, "markingInstruction": ''}
    _enums = {}
    _refs = ["WorkLocations"]
    _many_refs = ["WorkLocations"]

    def getWorkLocations(self):
        
        return self._WorkLocations

    def setWorkLocations(self, value):
        for x in self._WorkLocations:
            x.OneCallRequest = None
        for y in value:
            y._OneCallRequest = self
        self._WorkLocations = value

    WorkLocations = property(getWorkLocations, setWorkLocations)

    def addWorkLocations(self, *WorkLocations):
        for obj in WorkLocations:
            obj.OneCallRequest = self

    def removeWorkLocations(self, *WorkLocations):
        for obj in WorkLocations:
            obj.OneCallRequest = None


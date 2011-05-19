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

from CIM15.IEC61970.Informative.InfAssets.ProcedureDataSet import ProcedureDataSet

class InspectionDataSet(ProcedureDataSet):
    """Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.
    """

    def __init__(self, locationCondition='', AccordingToSchedules=None, *args, **kw_args):
        """Initialises a new 'InspectionDataSet' instance.

        @param locationCondition: Description of the conditions of the location where the asset resides. 
        @param AccordingToSchedules:
        """
        #: Description of the conditions of the location where the asset resides.
        self.locationCondition = locationCondition

        self._AccordingToSchedules = []
        self.AccordingToSchedules = [] if AccordingToSchedules is None else AccordingToSchedules

        super(InspectionDataSet, self).__init__(*args, **kw_args)

    _attrs = ["locationCondition"]
    _attr_types = {"locationCondition": str}
    _defaults = {"locationCondition": ''}
    _enums = {}
    _refs = ["AccordingToSchedules"]
    _many_refs = ["AccordingToSchedules"]

    def getAccordingToSchedules(self):
        
        return self._AccordingToSchedules

    def setAccordingToSchedules(self, value):
        for x in self._AccordingToSchedules:
            x.ForInspectionDataSet = None
        for y in value:
            y._ForInspectionDataSet = self
        self._AccordingToSchedules = value

    AccordingToSchedules = property(getAccordingToSchedules, setAccordingToSchedules)

    def addAccordingToSchedules(self, *AccordingToSchedules):
        for obj in AccordingToSchedules:
            obj.ForInspectionDataSet = self

    def removeAccordingToSchedules(self, *AccordingToSchedules):
        for obj in AccordingToSchedules:
            obj.ForInspectionDataSet = None


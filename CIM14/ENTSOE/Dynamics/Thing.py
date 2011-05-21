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

from CIM14.ENTSOE.Dynamics.Element import Element

class Thing(Element):

    def __init__(self, ScheduleSteps=None, synchronousGeneratorType=None, tpqo=None, ElectricalAssets=None, SafetyDocuments=None, ratedS=None, tppdo=None, tpdo=None, ChangeItems=None, ErpOrganisationRoles=None, CircuitSections=None, tppqo=None, DocumentRoles=None, PSREvent=None, OutageStepRoles=None, NetworkDataSets=None, *args, **kw_args):
        """Initialises a new 'Thing' instance.

        @param ScheduleSteps:
        @param synchronousGeneratorType:
        @param tpqo:
        @param ElectricalAssets:
        @param EAID_4B45E775_795A_4030_865F_0AB320000DDD-B:
        @param SafetyDocuments:
        @param ratedS:
        @param tppdo:
        @param tpdo:
        @param ChangeItems:
        @param ErpOrganisationRoles:
        @param CircuitSections:
        @param tppqo:
        @param DocumentRoles:
        @param PSREvent:
        @param OutageStepRoles:
        @param NetworkDataSets:
        """
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self.synchronousGeneratorType = [] if synchronousGeneratorType is None else synchronousGeneratorType

        self.tpqo = [] if tpqo is None else tpqo

        self.ElectricalAssets = [] if ElectricalAssets is None else ElectricalAssets

        self.SafetyDocuments = [] if SafetyDocuments is None else SafetyDocuments

        self.ratedS = [] if ratedS is None else ratedS

        self.tppdo = [] if tppdo is None else tppdo

        self.tpdo = [] if tpdo is None else tpdo

        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self.CircuitSections = [] if CircuitSections is None else CircuitSections

        self.tppqo = [] if tppqo is None else tppqo

        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self.PSREvent = [] if PSREvent is None else PSREvent

        self.OutageStepRoles = [] if OutageStepRoles is None else OutageStepRoles

        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        super(Thing, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ScheduleSteps", "synchronousGeneratorType", "tpqo", "ElectricalAssets", "EAID_4B45E775_795A_4030_865F_0AB320000DDD-B", "SafetyDocuments", "ratedS", "tppdo", "tpdo", "ChangeItems", "ErpOrganisationRoles", "CircuitSections", "tppqo", "DocumentRoles", "PSREvent", "OutageStepRoles", "NetworkDataSets"]
    _many_refs = ["ScheduleSteps", "synchronousGeneratorType", "tpqo", "ElectricalAssets", "EAID_4B45E775_795A_4030_865F_0AB320000DDD-B", "SafetyDocuments", "ratedS", "tppdo", "tpdo", "ChangeItems", "ErpOrganisationRoles", "CircuitSections", "tppqo", "DocumentRoles", "PSREvent", "OutageStepRoles", "NetworkDataSets"]

    def add_ScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            self.ScheduleSteps.append(obj)

    def remove_ScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            self.ScheduleSteps.remove(obj)

    def add_synchronousGeneratorType(self, *synchronousGeneratorType):
        for obj in synchronousGeneratorType:
            self.synchronousGeneratorType.append(obj)

    def remove_synchronousGeneratorType(self, *synchronousGeneratorType):
        for obj in synchronousGeneratorType:
            self.synchronousGeneratorType.remove(obj)

    def add_tpqo(self, *tpqo):
        for obj in tpqo:
            self.tpqo.append(obj)

    def remove_tpqo(self, *tpqo):
        for obj in tpqo:
            self.tpqo.remove(obj)

    def add_ElectricalAssets(self, *ElectricalAssets):
        for obj in ElectricalAssets:
            self.ElectricalAssets.append(obj)

    def remove_ElectricalAssets(self, *ElectricalAssets):
        for obj in ElectricalAssets:
            self.ElectricalAssets.remove(obj)

    def add_SafetyDocuments(self, *SafetyDocuments):
        for obj in SafetyDocuments:
            self.SafetyDocuments.append(obj)

    def remove_SafetyDocuments(self, *SafetyDocuments):
        for obj in SafetyDocuments:
            self.SafetyDocuments.remove(obj)

    def add_ratedS(self, *ratedS):
        for obj in ratedS:
            self.ratedS.append(obj)

    def remove_ratedS(self, *ratedS):
        for obj in ratedS:
            self.ratedS.remove(obj)

    def add_tppdo(self, *tppdo):
        for obj in tppdo:
            self.tppdo.append(obj)

    def remove_tppdo(self, *tppdo):
        for obj in tppdo:
            self.tppdo.remove(obj)

    def add_tpdo(self, *tpdo):
        for obj in tpdo:
            self.tpdo.append(obj)

    def remove_tpdo(self, *tpdo):
        for obj in tpdo:
            self.tpdo.remove(obj)

    def add_ChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            self.ChangeItems.append(obj)

    def remove_ChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            self.ChangeItems.remove(obj)

    def add_ErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            self.ErpOrganisationRoles.append(obj)

    def remove_ErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            self.ErpOrganisationRoles.remove(obj)

    def add_CircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            self.CircuitSections.append(obj)

    def remove_CircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            self.CircuitSections.remove(obj)

    def add_tppqo(self, *tppqo):
        for obj in tppqo:
            self.tppqo.append(obj)

    def remove_tppqo(self, *tppqo):
        for obj in tppqo:
            self.tppqo.remove(obj)

    def add_DocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            self.DocumentRoles.append(obj)

    def remove_DocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            self.DocumentRoles.remove(obj)

    def add_PSREvent(self, *PSREvent):
        for obj in PSREvent:
            self.PSREvent.append(obj)

    def remove_PSREvent(self, *PSREvent):
        for obj in PSREvent:
            self.PSREvent.remove(obj)

    def add_OutageStepRoles(self, *OutageStepRoles):
        for obj in OutageStepRoles:
            self.OutageStepRoles.append(obj)

    def remove_OutageStepRoles(self, *OutageStepRoles):
        for obj in OutageStepRoles:
            self.OutageStepRoles.remove(obj)

    def add_NetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            self.NetworkDataSets.append(obj)

    def remove_NetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            self.NetworkDataSets.remove(obj)


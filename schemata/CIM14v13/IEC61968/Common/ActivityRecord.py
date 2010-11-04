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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ActivityRecord(IdentifiedObject):
    """Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """

    def __init__(self, reason='', category='', severity='', createdDateTime='', MarketFactors=None, Documents=None, Organisations=None, ScheduledEvent=None, Assets=None, ErpPersons=None, Locations=None, status=None, **kw_args):
        """Initializes a new 'ActivityRecord' instance.

        @param reason: Reason for event resulting in this activity record, typically supplied when user initiated. 
        @param category: Category of event resulting in this activity record. 
        @param severity: Severity level of event resulting in this activity record. 
        @param createdDateTime: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable). 
        @param MarketFactors:
        @param Documents: All documents for which this activity record has been created.
        @param Organisations:
        @param ScheduledEvent:
        @param Assets: All assets for which this activity record has been created.
        @param ErpPersons:
        @param Locations:
        @param status: Information on consequence of event resulting in this activity record.
        """
        #: Reason for event resulting in this activity record, typically supplied when user initiated.
        self.reason = reason

        #: Category of event resulting in this activity record.
        self.category = category

        #: Severity level of event resulting in this activity record.
        self.severity = severity

        #: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable).
        self.createdDateTime = createdDateTime

        self.MarketFactors = [] if MarketFactors is None else MarketFactors

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        self._ScheduledEvent = None
        self.ScheduledEvent = ScheduledEvent

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self.status = status

        super(ActivityRecord, self).__init__(**kw_args)

    def add_MarketFactors(self, *MarketFactors):
        for obj in MarketFactors:
            self.MarketFactors.append(obj)

    def remove_MarketFactors(self, *MarketFactors):
        for obj in MarketFactors:
            self.MarketFactors.remove(obj)

    def getDocuments(self):
        """All documents for which this activity record has been created.
        """
        return self._Documents

    def setDocuments(self, value):
        for p in self._Documents:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Documents._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Documents = value

    Documents = property(getDocuments, setDocuments)

    def addDocuments(self, *Documents):
        for obj in Documents:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Documents.append(obj)

    def removeDocuments(self, *Documents):
        for obj in Documents:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Documents.remove(obj)

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Organisations._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Organisations.remove(obj)

    def getScheduledEvent(self):
        
        return self._ScheduledEvent

    def setScheduledEvent(self, value):
        if self._ScheduledEvent is not None:
            self._ScheduledEvent._ActivityRecord = None

        self._ScheduledEvent = value
        if self._ScheduledEvent is not None:
            self._ScheduledEvent._ActivityRecord = self

    ScheduledEvent = property(getScheduledEvent, setScheduledEvent)

    def getAssets(self):
        """All assets for which this activity record has been created.
        """
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Assets._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Assets.remove(obj)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._ErpPersons._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._ErpPersons.remove(obj)

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Locations._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Locations.remove(obj)

    # Information on consequence of event resulting in this activity record.
    status = None


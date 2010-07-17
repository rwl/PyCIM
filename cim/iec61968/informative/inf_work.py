# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" The package covers all types of work, including inspection, maintenance, repair, restoration, and construction. It covers the full life cycle including request, initiate, track and record work. Standardized designs (compatible units) are used where possible.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Work package is used to define classes related to work. There are several different aspects of work. The Work Initiation (Work, Project, Request). The Work Design package is used for managing designs (CompatibleUnit, Design, DesignLocation, WorkTask). The Work Schedule package is used for the scheduling and coordination of work (AccessPermit, MaterialItem, OneCallRequest, Regulation). The Work Closing package is used for tracking costs of work (CostType, LaborItem, WorkCostDetail, VehicleItem). The Work Standards package is used for the definition of compatible units (CULaborItem, CUVehicleItem, CUGroup). This package is used for inspection and maintenance (InspectionDataSet, Procedure). The WorkService package defines Appointment class.'
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Document
from cim.iec61968.informative.inf_common import ScheduledEvent
from cim.iec61968.informative.inf_assets import ProcedureDataSet
from cim.iec61968.common import ActivityRecord
from cim.iec61968.common import Location

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infwork"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfWork"

class DesignLocation(IdentifiedObject):
    """ A logical part of the design (e.g., pole and all equipment on a pole). This includes points and spans.
    """
    # <<< design_location
    # @generated
    def __init__(self, span_length=0.0, material_items=None, design_location_cus=None, designs=None, status=None, misc_cost_items=None, condition_factors=None, diagrams=None, erp_bom_item_datas=None, work_locations=None, **kw_args):
        """ Initialises a new 'DesignLocation' instance.
        """
        # The legth of the span from the previous pole to this pole. 
        self.span_length = span_length


        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []

        self.status = status

        self._misc_cost_items = []
        if misc_cost_items is not None:
            self.misc_cost_items = misc_cost_items
        else:
            self.misc_cost_items = []

        self._condition_factors = []
        if condition_factors is not None:
            self.condition_factors = condition_factors
        else:
            self.condition_factors = []

        self._diagrams = []
        if diagrams is not None:
            self.diagrams = diagrams
        else:
            self.diagrams = []

        self._erp_bom_item_datas = []
        if erp_bom_item_datas is not None:
            self.erp_bom_item_datas = erp_bom_item_datas
        else:
            self.erp_bom_item_datas = []

        self._work_locations = []
        if work_locations is not None:
            self.work_locations = work_locations
        else:
            self.work_locations = []


        super(DesignLocation, self).__init__(**kw_args)
    # >>> design_location

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._design_location = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._design_location = None
            self._material_items.remove(obj)
    # >>> material_items

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for x in self._design_location_cus:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            obj._design_location = self
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            obj._design_location = None
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for p in self._designs:
            filtered = [q for q in p.design_locations if q != self]
            self._designs._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._designs.remove(obj)
    # >>> designs

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< misc_cost_items
    # @generated
    def get_misc_cost_items(self):
        """ 
        """
        return self._misc_cost_items

    def set_misc_cost_items(self, value):
        for x in self._misc_cost_items:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._misc_cost_items = value

    misc_cost_items = property(get_misc_cost_items, set_misc_cost_items)

    def add_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._design_location = self
            self._misc_cost_items.append(obj)

    def remove_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._design_location = None
            self._misc_cost_items.remove(obj)
    # >>> misc_cost_items

    # <<< condition_factors
    # @generated
    def get_condition_factors(self):
        """ 
        """
        return self._condition_factors

    def set_condition_factors(self, value):
        for p in self._condition_factors:
            filtered = [q for q in p.design_locations if q != self]
            self._condition_factors._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._condition_factors = value

    condition_factors = property(get_condition_factors, set_condition_factors)

    def add_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._condition_factors.append(obj)

    def remove_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._condition_factors.remove(obj)
    # >>> condition_factors

    # <<< diagrams
    # @generated
    def get_diagrams(self):
        """ 
        """
        return self._diagrams

    def set_diagrams(self, value):
        for p in self._diagrams:
            filtered = [q for q in p.design_locations if q != self]
            self._diagrams._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._diagrams = value

    diagrams = property(get_diagrams, set_diagrams)

    def add_diagrams(self, *diagrams):
        for obj in diagrams:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._diagrams.append(obj)

    def remove_diagrams(self, *diagrams):
        for obj in diagrams:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._diagrams.remove(obj)
    # >>> diagrams

    # <<< erp_bom_item_datas
    # @generated
    def get_erp_bom_item_datas(self):
        """ 
        """
        return self._erp_bom_item_datas

    def set_erp_bom_item_datas(self, value):
        for x in self._erp_bom_item_datas:
            x._design_location = None
        for y in value:
            y._design_location = self
        self._erp_bom_item_datas = value

    erp_bom_item_datas = property(get_erp_bom_item_datas, set_erp_bom_item_datas)

    def add_erp_bom_item_datas(self, *erp_bom_item_datas):
        for obj in erp_bom_item_datas:
            obj._design_location = self
            self._erp_bom_item_datas.append(obj)

    def remove_erp_bom_item_datas(self, *erp_bom_item_datas):
        for obj in erp_bom_item_datas:
            obj._design_location = None
            self._erp_bom_item_datas.remove(obj)
    # >>> erp_bom_item_datas

    # <<< work_locations
    # @generated
    def get_work_locations(self):
        """ 
        """
        return self._work_locations

    def set_work_locations(self, value):
        for p in self._work_locations:
            filtered = [q for q in p.design_locations if q != self]
            self._work_locations._design_locations = filtered
        for r in value:
            if self not in r._design_locations:
                r._design_locations.append(self)
        self._work_locations = value

    work_locations = property(get_work_locations, set_work_locations)

    def add_work_locations(self, *work_locations):
        for obj in work_locations:
            if self not in obj._design_locations:
                obj._design_locations.append(self)
            self._work_locations.append(obj)

    def remove_work_locations(self, *work_locations):
        for obj in work_locations:
            if self in obj._design_locations:
                obj._design_locations.remove(self)
            self._work_locations.remove(obj)
    # >>> work_locations


    def __str__(self):
        """ Returns a string representation of the DesignLocation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< design_location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DesignLocation.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DesignLocation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.material_items:
            s += '%s<%s:DesignLocation.material_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_location_cus:
            s += '%s<%s:DesignLocation.design_location_cus rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.designs:
            s += '%s<%s:DesignLocation.designs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:DesignLocation.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.misc_cost_items:
            s += '%s<%s:DesignLocation.misc_cost_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.condition_factors:
            s += '%s<%s:DesignLocation.condition_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.diagrams:
            s += '%s<%s:DesignLocation.diagrams rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_bom_item_datas:
            s += '%s<%s:DesignLocation.erp_bom_item_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_locations:
            s += '%s<%s:DesignLocation.work_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:DesignLocation.span_length>%s</%s:DesignLocation.span_length>' % \
            (indent, ns_prefix, self.span_length, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DesignLocation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> design_location.serialize


class Capability(IdentifiedObject):
    """ Capabilities of a crew.
    """
    # <<< capability
    # @generated
    def __init__(self, performance_factor='', category='', crew=None, status=None, work_tasks=None, validity_interval=None, crafts=None, **kw_args):
        """ Initialises a new 'Capability' instance.
        """
        # Capability performance factor. 
        self.performance_factor = performance_factor

        # Category by utility's work management standards and practices. 
        self.category = category


        self._crew = None
        self.crew = crew

        self.status = status

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self.validity_interval = validity_interval

        self._crafts = []
        if crafts is not None:
            self.crafts = crafts
        else:
            self.crafts = []


        super(Capability, self).__init__(**kw_args)
    # >>> capability

    # <<< crew
    # @generated
    def get_crew(self):
        """ 
        """
        return self._crew

    def set_crew(self, value):
        if self._crew is not None:
            filtered = [x for x in self.crew.capabilities if x != self]
            self._crew._capabilities = filtered

        self._crew = value
        if self._crew is not None:
            self._crew._capabilities.append(self)

    crew = property(get_crew, set_crew)
    # >>> crew

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.capabilities if q != self]
            self._work_tasks._capabilities = filtered
        for r in value:
            if self not in r._capabilities:
                r._capabilities.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._capabilities:
                obj._capabilities.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._capabilities:
                obj._capabilities.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< validity_interval
    # @generated
    # Date and time interval for which this capability is valid (when it became effective and when it expires).
    validity_interval = None
    # >>> validity_interval

    # <<< crafts
    # @generated
    def get_crafts(self):
        """ 
        """
        return self._crafts

    def set_crafts(self, value):
        for p in self._crafts:
            filtered = [q for q in p.capabilities if q != self]
            self._crafts._capabilities = filtered
        for r in value:
            if self not in r._capabilities:
                r._capabilities.append(self)
        self._crafts = value

    crafts = property(get_crafts, set_crafts)

    def add_crafts(self, *crafts):
        for obj in crafts:
            if self not in obj._capabilities:
                obj._capabilities.append(self)
            self._crafts.append(obj)

    def remove_crafts(self, *crafts):
        for obj in crafts:
            if self in obj._capabilities:
                obj._capabilities.remove(self)
            self._crafts.remove(obj)
    # >>> crafts


    def __str__(self):
        """ Returns a string representation of the Capability.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< capability.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Capability.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Capability", self.uri)
        if format:
            indent += ' ' * depth

        if self.crew is not None:
            s += '%s<%s:Capability.crew rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.crew.uri)
        if self.status is not None:
            s += '%s<%s:Capability.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.work_tasks:
            s += '%s<%s:Capability.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.validity_interval is not None:
            s += '%s<%s:Capability.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        for obj in self.crafts:
            s += '%s<%s:Capability.crafts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Capability.performance_factor>%s</%s:Capability.performance_factor>' % \
            (indent, ns_prefix, self.performance_factor, ns_prefix)
        s += '%s<%s:Capability.category>%s</%s:Capability.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Capability")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> capability.serialize


class Design(Document):
    """ A design for consideration by customers, potential customers, or internal work. Note that the Version of design is the revision attribute that is inherited from Document.
    """
    # <<< design
    # @generated
    def __init__(self, kind='estimated', price=0.0, cost_estimate=0.0, design_locations_cus=None, work_cost_details=None, erp_quote_line_item=None, design_locations=None, work=None, erp_boms=None, condition_factors=None, work_tasks=None, **kw_args):
        """ Initialises a new 'Design' instance.
        """
        # Kind of this design. Values are: "estimated", "as_built", "other"
        self.kind = 'estimated'

        # Price to customer for implementing design. 
        self.price = price

        # Estimated cost (not price) of design. 
        self.cost_estimate = cost_estimate


        self._design_locations_cus = []
        if design_locations_cus is not None:
            self.design_locations_cus = design_locations_cus
        else:
            self.design_locations_cus = []

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._erp_quote_line_item = None
        self.erp_quote_line_item = erp_quote_line_item

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []

        self._work = None
        self.work = work

        self._erp_boms = []
        if erp_boms is not None:
            self.erp_boms = erp_boms
        else:
            self.erp_boms = []

        self._condition_factors = []
        if condition_factors is not None:
            self.condition_factors = condition_factors
        else:
            self.condition_factors = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []


        super(Design, self).__init__(**kw_args)
    # >>> design

    # <<< design_locations_cus
    # @generated
    def get_design_locations_cus(self):
        """ 
        """
        return self._design_locations_cus

    def set_design_locations_cus(self, value):
        for p in self._design_locations_cus:
            filtered = [q for q in p.designs if q != self]
            self._design_locations_cus._designs = filtered
        for r in value:
            if self not in r._designs:
                r._designs.append(self)
        self._design_locations_cus = value

    design_locations_cus = property(get_design_locations_cus, set_design_locations_cus)

    def add_design_locations_cus(self, *design_locations_cus):
        for obj in design_locations_cus:
            if self not in obj._designs:
                obj._designs.append(self)
            self._design_locations_cus.append(obj)

    def remove_design_locations_cus(self, *design_locations_cus):
        for obj in design_locations_cus:
            if self in obj._designs:
                obj._designs.remove(self)
            self._design_locations_cus.remove(obj)
    # >>> design_locations_cus

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._design = None
        for y in value:
            y._design = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._design = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._design = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< erp_quote_line_item
    # @generated
    def get_erp_quote_line_item(self):
        """ 
        """
        return self._erp_quote_line_item

    def set_erp_quote_line_item(self, value):
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._design = None

        self._erp_quote_line_item = value
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._design = self

    erp_quote_line_item = property(get_erp_quote_line_item, set_erp_quote_line_item)
    # >>> erp_quote_line_item

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.designs if q != self]
            self._design_locations._designs = filtered
        for r in value:
            if self not in r._designs:
                r._designs.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._designs:
                obj._designs.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._designs:
                obj._designs.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations

    # <<< work
    # @generated
    def get_work(self):
        """ 
        """
        return self._work

    def set_work(self, value):
        if self._work is not None:
            filtered = [x for x in self.work.designs if x != self]
            self._work._designs = filtered

        self._work = value
        if self._work is not None:
            self._work._designs.append(self)

    work = property(get_work, set_work)
    # >>> work

    # <<< erp_boms
    # @generated
    def get_erp_boms(self):
        """ 
        """
        return self._erp_boms

    def set_erp_boms(self, value):
        for x in self._erp_boms:
            x._design = None
        for y in value:
            y._design = self
        self._erp_boms = value

    erp_boms = property(get_erp_boms, set_erp_boms)

    def add_erp_boms(self, *erp_boms):
        for obj in erp_boms:
            obj._design = self
            self._erp_boms.append(obj)

    def remove_erp_boms(self, *erp_boms):
        for obj in erp_boms:
            obj._design = None
            self._erp_boms.remove(obj)
    # >>> erp_boms

    # <<< condition_factors
    # @generated
    def get_condition_factors(self):
        """ 
        """
        return self._condition_factors

    def set_condition_factors(self, value):
        for p in self._condition_factors:
            filtered = [q for q in p.designs if q != self]
            self._condition_factors._designs = filtered
        for r in value:
            if self not in r._designs:
                r._designs.append(self)
        self._condition_factors = value

    condition_factors = property(get_condition_factors, set_condition_factors)

    def add_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self not in obj._designs:
                obj._designs.append(self)
            self._condition_factors.append(obj)

    def remove_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self in obj._designs:
                obj._designs.remove(self)
            self._condition_factors.remove(obj)
    # >>> condition_factors

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._design = None
        for y in value:
            y._design = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._design = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._design = None
            self._work_tasks.remove(obj)
    # >>> work_tasks


    def __str__(self):
        """ Returns a string representation of the Design.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< design.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Design.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Design", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.design_locations_cus:
            s += '%s<%s:Design.design_locations_cus rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_cost_details:
            s += '%s<%s:Design.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_quote_line_item is not None:
            s += '%s<%s:Design.erp_quote_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_quote_line_item.uri)
        for obj in self.design_locations:
            s += '%s<%s:Design.design_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work is not None:
            s += '%s<%s:Design.work rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work.uri)
        for obj in self.erp_boms:
            s += '%s<%s:Design.erp_boms rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.condition_factors:
            s += '%s<%s:Design.condition_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_tasks:
            s += '%s<%s:Design.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Design.kind>%s</%s:Design.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:Design.price>%s</%s:Design.price>' % \
            (indent, ns_prefix, self.price, ns_prefix)
        s += '%s<%s:Design.cost_estimate>%s</%s:Design.cost_estimate>' % \
            (indent, ns_prefix, self.cost_estimate, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Design")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> design.serialize


class LaborItem(IdentifiedObject):
    """ Labor used for work order.
    """
    # <<< labor_item
    # @generated
    def __init__(self, labor_rate=0.0, cost=0.0, activity_code='', labor_duration=0.0, work_cost_detail=None, erp_persons=None, status=None, work_task=None, **kw_args):
        """ Initialises a new 'LaborItem' instance.
        """
        # The labor rate applied for work. 
        self.labor_rate = labor_rate

        # Total cost for labor. Note that this may not be able to be derived from labor rate and time charged. 
        self.cost = cost

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code

        # Time required to perform work. 
        self.labor_duration = labor_duration


        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self.status = status

        self._work_task = None
        self.work_task = work_task


        super(LaborItem, self).__init__(**kw_args)
    # >>> labor_item

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.labor_items if x != self]
            self._work_cost_detail._labor_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._labor_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.labor_items if q != self]
            self._erp_persons._labor_items = filtered
        for r in value:
            if self not in r._labor_items:
                r._labor_items.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._labor_items:
                obj._labor_items.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._labor_items:
                obj._labor_items.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.labor_items if x != self]
            self._work_task._labor_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._labor_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task


    def __str__(self):
        """ Returns a string representation of the LaborItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< labor_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LaborItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LaborItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.work_cost_detail is not None:
            s += '%s<%s:LaborItem.work_cost_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_detail.uri)
        for obj in self.erp_persons:
            s += '%s<%s:LaborItem.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:LaborItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.work_task is not None:
            s += '%s<%s:LaborItem.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        s += '%s<%s:LaborItem.labor_rate>%s</%s:LaborItem.labor_rate>' % \
            (indent, ns_prefix, self.labor_rate, ns_prefix)
        s += '%s<%s:LaborItem.cost>%s</%s:LaborItem.cost>' % \
            (indent, ns_prefix, self.cost, ns_prefix)
        s += '%s<%s:LaborItem.activity_code>%s</%s:LaborItem.activity_code>' % \
            (indent, ns_prefix, self.activity_code, ns_prefix)
        s += '%s<%s:LaborItem.labor_duration>%s</%s:LaborItem.labor_duration>' % \
            (indent, ns_prefix, self.labor_duration, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LaborItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> labor_item.serialize


class CUMaterialItem(IdentifiedObject):
    """ Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.
    """
    # <<< cumaterial_item
    # @generated
    def __init__(self, corporate_code='', quantity=0, status=None, type_material=None, compatible_units=None, property_units=None, **kw_args):
        """ Initialises a new 'CUMaterialItem' instance.
        """
        # Code for material. 
        self.corporate_code = corporate_code

        # Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial. 
        self.quantity = quantity


        self.status = status

        self._type_material = None
        self.type_material = type_material

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._property_units = []
        if property_units is not None:
            self.property_units = property_units
        else:
            self.property_units = []


        super(CUMaterialItem, self).__init__(**kw_args)
    # >>> cumaterial_item

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< type_material
    # @generated
    def get_type_material(self):
        """ 
        """
        return self._type_material

    def set_type_material(self, value):
        if self._type_material is not None:
            filtered = [x for x in self.type_material.cumaterial_items if x != self]
            self._type_material._cumaterial_items = filtered

        self._type_material = value
        if self._type_material is not None:
            self._type_material._cumaterial_items.append(self)

    type_material = property(get_type_material, set_type_material)
    # >>> type_material

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cumaterial_items if q != self]
            self._compatible_units._cumaterial_items = filtered
        for r in value:
            if self not in r._cumaterial_items:
                r._cumaterial_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cumaterial_items:
                obj._cumaterial_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cumaterial_items:
                obj._cumaterial_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< property_units
    # @generated
    def get_property_units(self):
        """ 
        """
        return self._property_units

    def set_property_units(self, value):
        for p in self._property_units:
            filtered = [q for q in p.cumaterial_items if q != self]
            self._property_units._cumaterial_items = filtered
        for r in value:
            if self not in r._cumaterial_items:
                r._cumaterial_items.append(self)
        self._property_units = value

    property_units = property(get_property_units, set_property_units)

    def add_property_units(self, *property_units):
        for obj in property_units:
            if self not in obj._cumaterial_items:
                obj._cumaterial_items.append(self)
            self._property_units.append(obj)

    def remove_property_units(self, *property_units):
        for obj in property_units:
            if self in obj._cumaterial_items:
                obj._cumaterial_items.remove(self)
            self._property_units.remove(obj)
    # >>> property_units


    def __str__(self):
        """ Returns a string representation of the CUMaterialItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cumaterial_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CUMaterialItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CUMaterialItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:CUMaterialItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.type_material is not None:
            s += '%s<%s:CUMaterialItem.type_material rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_material.uri)
        for obj in self.compatible_units:
            s += '%s<%s:CUMaterialItem.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.property_units:
            s += '%s<%s:CUMaterialItem.property_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:CUMaterialItem.corporate_code>%s</%s:CUMaterialItem.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:CUMaterialItem.quantity>%s</%s:CUMaterialItem.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CUMaterialItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cumaterial_item.serialize


class NonStandardItem(Document):
    """ This document provides information for non-standard items like customer contributions (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids.
    """
    # <<< non_standard_item
    # @generated
    def __init__(self, amount=0.0, code='', **kw_args):
        """ Initialises a new 'NonStandardItem' instance.
        """
        # The projected cost for this item. 
        self.amount = amount

        # The category of non-standard work. 
        self.code = code



        super(NonStandardItem, self).__init__(**kw_args)
    # >>> non_standard_item


    def __str__(self):
        """ Returns a string representation of the NonStandardItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< non_standard_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NonStandardItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NonStandardItem", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:NonStandardItem.amount>%s</%s:NonStandardItem.amount>' % \
            (indent, ns_prefix, self.amount, ns_prefix)
        s += '%s<%s:NonStandardItem.code>%s</%s:NonStandardItem.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "NonStandardItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> non_standard_item.serialize


class TypeMaterial(Document):
    """ Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.
    """
    # <<< type_material
    # @generated
    def __init__(self, stock_item=False, quantity='', cost_type='', est_unit_cost=0.0, erp_req_line_items=None, erp_issue_inventories=None, cumaterial_items=None, material_items=None, **kw_args):
        """ Initialises a new 'TypeMaterial' instance.
        """
        # True if item is a stock item (default). 
        self.stock_item = stock_item

        # The value, unit of measure, and multiplier for the quantity. 
        self.quantity = quantity

        # The category of cost to which this Material Item belongs. 
        self.cost_type = cost_type

        # The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        self.est_unit_cost = est_unit_cost


        self._erp_req_line_items = []
        if erp_req_line_items is not None:
            self.erp_req_line_items = erp_req_line_items
        else:
            self.erp_req_line_items = []

        self._erp_issue_inventories = []
        if erp_issue_inventories is not None:
            self.erp_issue_inventories = erp_issue_inventories
        else:
            self.erp_issue_inventories = []

        self._cumaterial_items = []
        if cumaterial_items is not None:
            self.cumaterial_items = cumaterial_items
        else:
            self.cumaterial_items = []

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []


        super(TypeMaterial, self).__init__(**kw_args)
    # >>> type_material

    # <<< erp_req_line_items
    # @generated
    def get_erp_req_line_items(self):
        """ 
        """
        return self._erp_req_line_items

    def set_erp_req_line_items(self, value):
        for x in self._erp_req_line_items:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._erp_req_line_items = value

    erp_req_line_items = property(get_erp_req_line_items, set_erp_req_line_items)

    def add_erp_req_line_items(self, *erp_req_line_items):
        for obj in erp_req_line_items:
            obj._type_material = self
            self._erp_req_line_items.append(obj)

    def remove_erp_req_line_items(self, *erp_req_line_items):
        for obj in erp_req_line_items:
            obj._type_material = None
            self._erp_req_line_items.remove(obj)
    # >>> erp_req_line_items

    # <<< erp_issue_inventories
    # @generated
    def get_erp_issue_inventories(self):
        """ 
        """
        return self._erp_issue_inventories

    def set_erp_issue_inventories(self, value):
        for x in self._erp_issue_inventories:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._erp_issue_inventories = value

    erp_issue_inventories = property(get_erp_issue_inventories, set_erp_issue_inventories)

    def add_erp_issue_inventories(self, *erp_issue_inventories):
        for obj in erp_issue_inventories:
            obj._type_material = self
            self._erp_issue_inventories.append(obj)

    def remove_erp_issue_inventories(self, *erp_issue_inventories):
        for obj in erp_issue_inventories:
            obj._type_material = None
            self._erp_issue_inventories.remove(obj)
    # >>> erp_issue_inventories

    # <<< cumaterial_items
    # @generated
    def get_cumaterial_items(self):
        """ 
        """
        return self._cumaterial_items

    def set_cumaterial_items(self, value):
        for x in self._cumaterial_items:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._cumaterial_items = value

    cumaterial_items = property(get_cumaterial_items, set_cumaterial_items)

    def add_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            obj._type_material = self
            self._cumaterial_items.append(obj)

    def remove_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            obj._type_material = None
            self._cumaterial_items.remove(obj)
    # >>> cumaterial_items

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._type_material = None
        for y in value:
            y._type_material = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._type_material = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._type_material = None
            self._material_items.remove(obj)
    # >>> material_items


    def __str__(self):
        """ Returns a string representation of the TypeMaterial.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< type_material.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TypeMaterial.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TypeMaterial", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_req_line_items:
            s += '%s<%s:TypeMaterial.erp_req_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_issue_inventories:
            s += '%s<%s:TypeMaterial.erp_issue_inventories rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.cumaterial_items:
            s += '%s<%s:TypeMaterial.cumaterial_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.material_items:
            s += '%s<%s:TypeMaterial.material_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:TypeMaterial.stock_item>%s</%s:TypeMaterial.stock_item>' % \
            (indent, ns_prefix, self.stock_item, ns_prefix)
        s += '%s<%s:TypeMaterial.quantity>%s</%s:TypeMaterial.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        s += '%s<%s:TypeMaterial.cost_type>%s</%s:TypeMaterial.cost_type>' % \
            (indent, ns_prefix, self.cost_type, ns_prefix)
        s += '%s<%s:TypeMaterial.est_unit_cost>%s</%s:TypeMaterial.est_unit_cost>' % \
            (indent, ns_prefix, self.est_unit_cost, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TypeMaterial")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> type_material.serialize


class Appointment(ScheduledEvent):
    """ Meeting time and location.
    """
    # <<< appointment
    # @generated
    def __init__(self, remark='', call_ahead=False, erp_persons=None, call_back=None, address=None, meeting_interval=None, **kw_args):
        """ Initialises a new 'Appointment' instance.
        """
        # Information about the appointment. 
        self.remark = remark

        # True if requested to call customer when someone is about to arrive at their premises. 
        self.call_ahead = call_ahead


        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self._call_back = None
        self.call_back = call_back

        self.address = address

        self.meeting_interval = meeting_interval


        super(Appointment, self).__init__(**kw_args)
    # >>> appointment

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.appointments if q != self]
            self._erp_persons._appointments = filtered
        for r in value:
            if self not in r._appointments:
                r._appointments.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._appointments:
                obj._appointments.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._appointments:
                obj._appointments.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< call_back
    # @generated
    def get_call_back(self):
        """ 
        """
        return self._call_back

    def set_call_back(self, value):
        if self._call_back is not None:
            filtered = [x for x in self.call_back.appointments if x != self]
            self._call_back._appointments = filtered

        self._call_back = value
        if self._call_back is not None:
            self._call_back._appointments.append(self)

    call_back = property(get_call_back, set_call_back)
    # >>> call_back

    # <<< address
    # @generated
    # Address for appointment.
    address = None
    # >>> address

    # <<< meeting_interval
    # @generated
    # Date and time reserved for appointment.
    meeting_interval = None
    # >>> meeting_interval


    def __str__(self):
        """ Returns a string representation of the Appointment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< appointment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Appointment.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Appointment", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_persons:
            s += '%s<%s:Appointment.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.call_back is not None:
            s += '%s<%s:Appointment.call_back rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.call_back.uri)
        if self.address is not None:
            s += '%s<%s:Appointment.address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.address.uri)
        if self.meeting_interval is not None:
            s += '%s<%s:Appointment.meeting_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.meeting_interval.uri)
        s += '%s<%s:Appointment.remark>%s</%s:Appointment.remark>' % \
            (indent, ns_prefix, self.remark, ns_prefix)
        s += '%s<%s:Appointment.call_ahead>%s</%s:Appointment.call_ahead>' % \
            (indent, ns_prefix, self.call_ahead, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.document is not None:
            s += '%s<%s:ScheduledEvent.document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.document.uri)
        for obj in self.assets:
            s += '%s<%s:ScheduledEvent.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.activity_record is not None:
            s += '%s<%s:ScheduledEvent.activity_record rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.activity_record.uri)
        if self.schedule_parameter_info is not None:
            s += '%s<%s:ScheduledEvent.schedule_parameter_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.schedule_parameter_info.uri)
        if self.status is not None:
            s += '%s<%s:ScheduledEvent.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.time_point is not None:
            s += '%s<%s:ScheduledEvent.time_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.time_point.uri)
        s += '%s<%s:ScheduledEvent.duration>%s</%s:ScheduledEvent.duration>' % \
            (indent, ns_prefix, self.duration, ns_prefix)
        s += '%s<%s:ScheduledEvent.category>%s</%s:ScheduledEvent.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Appointment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> appointment.serialize


class MaterialItem(IdentifiedObject):
    """ The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.
    """
    # <<< material_item
    # @generated
    def __init__(self, actual_cost=0.0, material_code='', quantity=0, cost_type='', cost_description='', external_ref_id='', account='', usages=None, design_location=None, status=None, work_task=None, erp_inventory_counts=None, erp_rec_delv_line_items=None, erp_poline_items=None, work_cost_detail=None, type_material=None, **kw_args):
        """ Initialises a new 'MaterialItem' instance.
        """
        # The actual cost of this particular material in this particular quantity. 
        self.actual_cost = actual_cost

        # Code for material. 
        self.material_code = material_code

        # The quantity of material used. 
        self.quantity = quantity

        # The category of cost to which this Material Item belongs. 
        self.cost_type = cost_type

        # Description of the cost. 
        self.cost_description = cost_description

        # External reference identifier for this actual material item such as a purchase order number, a serial number, etc. 
        self.external_ref_id = external_ref_id

        # The account to which this actual material item is charged. 
        self.account = account


        self._usages = []
        if usages is not None:
            self.usages = usages
        else:
            self.usages = []

        self._design_location = None
        self.design_location = design_location

        self.status = status

        self._work_task = None
        self.work_task = work_task

        self._erp_inventory_counts = []
        if erp_inventory_counts is not None:
            self.erp_inventory_counts = erp_inventory_counts
        else:
            self.erp_inventory_counts = []

        self._erp_rec_delv_line_items = []
        if erp_rec_delv_line_items is not None:
            self.erp_rec_delv_line_items = erp_rec_delv_line_items
        else:
            self.erp_rec_delv_line_items = []

        self._erp_poline_items = []
        if erp_poline_items is not None:
            self.erp_poline_items = erp_poline_items
        else:
            self.erp_poline_items = []

        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._type_material = None
        self.type_material = type_material


        super(MaterialItem, self).__init__(**kw_args)
    # >>> material_item

    # <<< usages
    # @generated
    def get_usages(self):
        """ 
        """
        return self._usages

    def set_usages(self, value):
        for x in self._usages:
            x._material_item = None
        for y in value:
            y._material_item = self
        self._usages = value

    usages = property(get_usages, set_usages)

    def add_usages(self, *usages):
        for obj in usages:
            obj._material_item = self
            self._usages.append(obj)

    def remove_usages(self, *usages):
        for obj in usages:
            obj._material_item = None
            self._usages.remove(obj)
    # >>> usages

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.material_items if x != self]
            self._design_location._material_items = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._material_items.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.material_items if x != self]
            self._work_task._material_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._material_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< erp_inventory_counts
    # @generated
    def get_erp_inventory_counts(self):
        """ 
        """
        return self._erp_inventory_counts

    def set_erp_inventory_counts(self, value):
        for x in self._erp_inventory_counts:
            x._material_item = None
        for y in value:
            y._material_item = self
        self._erp_inventory_counts = value

    erp_inventory_counts = property(get_erp_inventory_counts, set_erp_inventory_counts)

    def add_erp_inventory_counts(self, *erp_inventory_counts):
        for obj in erp_inventory_counts:
            obj._material_item = self
            self._erp_inventory_counts.append(obj)

    def remove_erp_inventory_counts(self, *erp_inventory_counts):
        for obj in erp_inventory_counts:
            obj._material_item = None
            self._erp_inventory_counts.remove(obj)
    # >>> erp_inventory_counts

    # <<< erp_rec_delv_line_items
    # @generated
    def get_erp_rec_delv_line_items(self):
        """ 
        """
        return self._erp_rec_delv_line_items

    def set_erp_rec_delv_line_items(self, value):
        for p in self._erp_rec_delv_line_items:
            filtered = [q for q in p.material_items if q != self]
            self._erp_rec_delv_line_items._material_items = filtered
        for r in value:
            if self not in r._material_items:
                r._material_items.append(self)
        self._erp_rec_delv_line_items = value

    erp_rec_delv_line_items = property(get_erp_rec_delv_line_items, set_erp_rec_delv_line_items)

    def add_erp_rec_delv_line_items(self, *erp_rec_delv_line_items):
        for obj in erp_rec_delv_line_items:
            if self not in obj._material_items:
                obj._material_items.append(self)
            self._erp_rec_delv_line_items.append(obj)

    def remove_erp_rec_delv_line_items(self, *erp_rec_delv_line_items):
        for obj in erp_rec_delv_line_items:
            if self in obj._material_items:
                obj._material_items.remove(self)
            self._erp_rec_delv_line_items.remove(obj)
    # >>> erp_rec_delv_line_items

    # <<< erp_poline_items
    # @generated
    def get_erp_poline_items(self):
        """ 
        """
        return self._erp_poline_items

    def set_erp_poline_items(self, value):
        for x in self._erp_poline_items:
            x._material_item = None
        for y in value:
            y._material_item = self
        self._erp_poline_items = value

    erp_poline_items = property(get_erp_poline_items, set_erp_poline_items)

    def add_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._material_item = self
            self._erp_poline_items.append(obj)

    def remove_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._material_item = None
            self._erp_poline_items.remove(obj)
    # >>> erp_poline_items

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.material_items if x != self]
            self._work_cost_detail._material_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._material_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< type_material
    # @generated
    def get_type_material(self):
        """ 
        """
        return self._type_material

    def set_type_material(self, value):
        if self._type_material is not None:
            filtered = [x for x in self.type_material.material_items if x != self]
            self._type_material._material_items = filtered

        self._type_material = value
        if self._type_material is not None:
            self._type_material._material_items.append(self)

    type_material = property(get_type_material, set_type_material)
    # >>> type_material


    def __str__(self):
        """ Returns a string representation of the MaterialItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< material_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MaterialItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MaterialItem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.usages:
            s += '%s<%s:MaterialItem.usages rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.design_location is not None:
            s += '%s<%s:MaterialItem.design_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design_location.uri)
        if self.status is not None:
            s += '%s<%s:MaterialItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.work_task is not None:
            s += '%s<%s:MaterialItem.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.erp_inventory_counts:
            s += '%s<%s:MaterialItem.erp_inventory_counts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_rec_delv_line_items:
            s += '%s<%s:MaterialItem.erp_rec_delv_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_poline_items:
            s += '%s<%s:MaterialItem.erp_poline_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_cost_detail is not None:
            s += '%s<%s:MaterialItem.work_cost_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_detail.uri)
        if self.type_material is not None:
            s += '%s<%s:MaterialItem.type_material rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_material.uri)
        s += '%s<%s:MaterialItem.actual_cost>%s</%s:MaterialItem.actual_cost>' % \
            (indent, ns_prefix, self.actual_cost, ns_prefix)
        s += '%s<%s:MaterialItem.material_code>%s</%s:MaterialItem.material_code>' % \
            (indent, ns_prefix, self.material_code, ns_prefix)
        s += '%s<%s:MaterialItem.quantity>%s</%s:MaterialItem.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        s += '%s<%s:MaterialItem.cost_type>%s</%s:MaterialItem.cost_type>' % \
            (indent, ns_prefix, self.cost_type, ns_prefix)
        s += '%s<%s:MaterialItem.cost_description>%s</%s:MaterialItem.cost_description>' % \
            (indent, ns_prefix, self.cost_description, ns_prefix)
        s += '%s<%s:MaterialItem.external_ref_id>%s</%s:MaterialItem.external_ref_id>' % \
            (indent, ns_prefix, self.external_ref_id, ns_prefix)
        s += '%s<%s:MaterialItem.account>%s</%s:MaterialItem.account>' % \
            (indent, ns_prefix, self.account, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MaterialItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> material_item.serialize


class CUContractorItem(IdentifiedObject):
    """ Compatible unit contractor item.
    """
    # <<< cucontractor_item
    # @generated
    def __init__(self, bid_amount=0.0, activity_code='', compatible_units=None, status=None, **kw_args):
        """ Initialises a new 'CUContractorItem' instance.
        """
        # The amount that a given contractor will charge for performing this unit of work. 
        self.bid_amount = bid_amount

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status


        super(CUContractorItem, self).__init__(**kw_args)
    # >>> cucontractor_item

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cucontractor_items if q != self]
            self._compatible_units._cucontractor_items = filtered
        for r in value:
            if self not in r._cucontractor_items:
                r._cucontractor_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cucontractor_items:
                obj._cucontractor_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cucontractor_items:
                obj._cucontractor_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the CUContractorItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cucontractor_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CUContractorItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CUContractorItem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.compatible_units:
            s += '%s<%s:CUContractorItem.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:CUContractorItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:CUContractorItem.bid_amount>%s</%s:CUContractorItem.bid_amount>' % \
            (indent, ns_prefix, self.bid_amount, ns_prefix)
        s += '%s<%s:CUContractorItem.activity_code>%s</%s:CUContractorItem.activity_code>' % \
            (indent, ns_prefix, self.activity_code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CUContractorItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cucontractor_item.serialize


class CompatibleUnit(Document):
    """ A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.
    """
    # <<< compatible_unit
    # @generated
    def __init__(self, est_cost=0.0, quantity='', cuwork_equipment_items=None, cucontractor_items=None, procedures=None, cuassets=None, cumaterial_items=None, property_unit=None, culabor_items=None, design_location_cus=None, cuallowable_action=None, cugroup=None, cost_type=None, **kw_args):
        """ Initialises a new 'CompatibleUnit' instance.
        """
        # Estimated total cost for perfoming CU. 
        self.est_cost = est_cost

        # The quantity, unit of measure, and multiplier at the CU level that applies to the materials. 
        self.quantity = quantity


        self._cuwork_equipment_items = []
        if cuwork_equipment_items is not None:
            self.cuwork_equipment_items = cuwork_equipment_items
        else:
            self.cuwork_equipment_items = []

        self._cucontractor_items = []
        if cucontractor_items is not None:
            self.cucontractor_items = cucontractor_items
        else:
            self.cucontractor_items = []

        self._procedures = []
        if procedures is not None:
            self.procedures = procedures
        else:
            self.procedures = []

        self._cuassets = []
        if cuassets is not None:
            self.cuassets = cuassets
        else:
            self.cuassets = []

        self._cumaterial_items = []
        if cumaterial_items is not None:
            self.cumaterial_items = cumaterial_items
        else:
            self.cumaterial_items = []

        self._property_unit = None
        self.property_unit = property_unit

        self._culabor_items = []
        if culabor_items is not None:
            self.culabor_items = culabor_items
        else:
            self.culabor_items = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._cuallowable_action = None
        self.cuallowable_action = cuallowable_action

        self._cugroup = None
        self.cugroup = cugroup

        self._cost_type = None
        self.cost_type = cost_type


        super(CompatibleUnit, self).__init__(**kw_args)
    # >>> compatible_unit

    # <<< cuwork_equipment_items
    # @generated
    def get_cuwork_equipment_items(self):
        """ 
        """
        return self._cuwork_equipment_items

    def set_cuwork_equipment_items(self, value):
        for p in self._cuwork_equipment_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._cuwork_equipment_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cuwork_equipment_items = value

    cuwork_equipment_items = property(get_cuwork_equipment_items, set_cuwork_equipment_items)

    def add_cuwork_equipment_items(self, *cuwork_equipment_items):
        for obj in cuwork_equipment_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cuwork_equipment_items.append(obj)

    def remove_cuwork_equipment_items(self, *cuwork_equipment_items):
        for obj in cuwork_equipment_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cuwork_equipment_items.remove(obj)
    # >>> cuwork_equipment_items

    # <<< cucontractor_items
    # @generated
    def get_cucontractor_items(self):
        """ 
        """
        return self._cucontractor_items

    def set_cucontractor_items(self, value):
        for p in self._cucontractor_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._cucontractor_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cucontractor_items = value

    cucontractor_items = property(get_cucontractor_items, set_cucontractor_items)

    def add_cucontractor_items(self, *cucontractor_items):
        for obj in cucontractor_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cucontractor_items.append(obj)

    def remove_cucontractor_items(self, *cucontractor_items):
        for obj in cucontractor_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cucontractor_items.remove(obj)
    # >>> cucontractor_items

    # <<< procedures
    # @generated
    def get_procedures(self):
        """ 
        """
        return self._procedures

    def set_procedures(self, value):
        for p in self._procedures:
            filtered = [q for q in p.compatible_units if q != self]
            self._procedures._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._procedures = value

    procedures = property(get_procedures, set_procedures)

    def add_procedures(self, *procedures):
        for obj in procedures:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._procedures.append(obj)

    def remove_procedures(self, *procedures):
        for obj in procedures:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._procedures.remove(obj)
    # >>> procedures

    # <<< cuassets
    # @generated
    def get_cuassets(self):
        """ 
        """
        return self._cuassets

    def set_cuassets(self, value):
        for p in self._cuassets:
            filtered = [q for q in p.compatible_units if q != self]
            self._cuassets._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cuassets = value

    cuassets = property(get_cuassets, set_cuassets)

    def add_cuassets(self, *cuassets):
        for obj in cuassets:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cuassets.append(obj)

    def remove_cuassets(self, *cuassets):
        for obj in cuassets:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cuassets.remove(obj)
    # >>> cuassets

    # <<< cumaterial_items
    # @generated
    def get_cumaterial_items(self):
        """ 
        """
        return self._cumaterial_items

    def set_cumaterial_items(self, value):
        for p in self._cumaterial_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._cumaterial_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._cumaterial_items = value

    cumaterial_items = property(get_cumaterial_items, set_cumaterial_items)

    def add_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._cumaterial_items.append(obj)

    def remove_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._cumaterial_items.remove(obj)
    # >>> cumaterial_items

    # <<< property_unit
    # @generated
    def get_property_unit(self):
        """ 
        """
        return self._property_unit

    def set_property_unit(self, value):
        if self._property_unit is not None:
            filtered = [x for x in self.property_unit.compatible_units if x != self]
            self._property_unit._compatible_units = filtered

        self._property_unit = value
        if self._property_unit is not None:
            self._property_unit._compatible_units.append(self)

    property_unit = property(get_property_unit, set_property_unit)
    # >>> property_unit

    # <<< culabor_items
    # @generated
    def get_culabor_items(self):
        """ 
        """
        return self._culabor_items

    def set_culabor_items(self, value):
        for p in self._culabor_items:
            filtered = [q for q in p.compatible_units if q != self]
            self._culabor_items._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._culabor_items = value

    culabor_items = property(get_culabor_items, set_culabor_items)

    def add_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._culabor_items.append(obj)

    def remove_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._culabor_items.remove(obj)
    # >>> culabor_items

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.compatible_units if q != self]
            self._design_location_cus._compatible_units = filtered
        for r in value:
            if self not in r._compatible_units:
                r._compatible_units.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._compatible_units:
                obj._compatible_units.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._compatible_units:
                obj._compatible_units.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< cuallowable_action
    # @generated
    def get_cuallowable_action(self):
        """ 
        """
        return self._cuallowable_action

    def set_cuallowable_action(self, value):
        if self._cuallowable_action is not None:
            filtered = [x for x in self.cuallowable_action.compatible_units if x != self]
            self._cuallowable_action._compatible_units = filtered

        self._cuallowable_action = value
        if self._cuallowable_action is not None:
            self._cuallowable_action._compatible_units.append(self)

    cuallowable_action = property(get_cuallowable_action, set_cuallowable_action)
    # >>> cuallowable_action

    # <<< cugroup
    # @generated
    def get_cugroup(self):
        """ 
        """
        return self._cugroup

    def set_cugroup(self, value):
        if self._cugroup is not None:
            filtered = [x for x in self.cugroup.compatible_units if x != self]
            self._cugroup._compatible_units = filtered

        self._cugroup = value
        if self._cugroup is not None:
            self._cugroup._compatible_units.append(self)

    cugroup = property(get_cugroup, set_cugroup)
    # >>> cugroup

    # <<< cost_type
    # @generated
    def get_cost_type(self):
        """ 
        """
        return self._cost_type

    def set_cost_type(self, value):
        if self._cost_type is not None:
            filtered = [x for x in self.cost_type.compatible_units if x != self]
            self._cost_type._compatible_units = filtered

        self._cost_type = value
        if self._cost_type is not None:
            self._cost_type._compatible_units.append(self)

    cost_type = property(get_cost_type, set_cost_type)
    # >>> cost_type


    def __str__(self):
        """ Returns a string representation of the CompatibleUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< compatible_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CompatibleUnit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CompatibleUnit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.cuwork_equipment_items:
            s += '%s<%s:CompatibleUnit.cuwork_equipment_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.cucontractor_items:
            s += '%s<%s:CompatibleUnit.cucontractor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.procedures:
            s += '%s<%s:CompatibleUnit.procedures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.cuassets:
            s += '%s<%s:CompatibleUnit.cuassets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.cumaterial_items:
            s += '%s<%s:CompatibleUnit.cumaterial_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.property_unit is not None:
            s += '%s<%s:CompatibleUnit.property_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.property_unit.uri)
        for obj in self.culabor_items:
            s += '%s<%s:CompatibleUnit.culabor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_location_cus:
            s += '%s<%s:CompatibleUnit.design_location_cus rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.cuallowable_action is not None:
            s += '%s<%s:CompatibleUnit.cuallowable_action rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cuallowable_action.uri)
        if self.cugroup is not None:
            s += '%s<%s:CompatibleUnit.cugroup rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cugroup.uri)
        if self.cost_type is not None:
            s += '%s<%s:CompatibleUnit.cost_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cost_type.uri)
        s += '%s<%s:CompatibleUnit.est_cost>%s</%s:CompatibleUnit.est_cost>' % \
            (indent, ns_prefix, self.est_cost, ns_prefix)
        s += '%s<%s:CompatibleUnit.quantity>%s</%s:CompatibleUnit.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CompatibleUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> compatible_unit.serialize


class InfoQuestion(Document):
    """ Questions and answers associated with a type of document for purposes of clarification. Questions may be predefined or ad hoc.
    """
    # <<< info_question
    # @generated
    def __init__(self, question_remark='', answer='', question_category='', question_code='', answer_date_time='', question_text='', answer_remark='', **kw_args):
        """ Initialises a new 'InfoQuestion' instance.
        """
        # Remarks to qualify the question in this situation. 
        self.question_remark = question_remark

        # Answer to question. 
        self.answer = answer

        # The category of the question. 
        self.question_category = question_category

        # The question code. If blank, refer to questionText. 
        self.question_code = question_code

        # The date and time the quesiton was answered. 
        self.answer_date_time = answer_date_time

        # For non-coded questions, the question is provided here. 
        self.question_text = question_text

        # Remarks to qualify the answer. 
        self.answer_remark = answer_remark



        super(InfoQuestion, self).__init__(**kw_args)
    # >>> info_question


    def __str__(self):
        """ Returns a string representation of the InfoQuestion.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< info_question.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the InfoQuestion.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "InfoQuestion", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:InfoQuestion.question_remark>%s</%s:InfoQuestion.question_remark>' % \
            (indent, ns_prefix, self.question_remark, ns_prefix)
        s += '%s<%s:InfoQuestion.answer>%s</%s:InfoQuestion.answer>' % \
            (indent, ns_prefix, self.answer, ns_prefix)
        s += '%s<%s:InfoQuestion.question_category>%s</%s:InfoQuestion.question_category>' % \
            (indent, ns_prefix, self.question_category, ns_prefix)
        s += '%s<%s:InfoQuestion.question_code>%s</%s:InfoQuestion.question_code>' % \
            (indent, ns_prefix, self.question_code, ns_prefix)
        s += '%s<%s:InfoQuestion.answer_date_time>%s</%s:InfoQuestion.answer_date_time>' % \
            (indent, ns_prefix, self.answer_date_time, ns_prefix)
        s += '%s<%s:InfoQuestion.question_text>%s</%s:InfoQuestion.question_text>' % \
            (indent, ns_prefix, self.question_text, ns_prefix)
        s += '%s<%s:InfoQuestion.answer_remark>%s</%s:InfoQuestion.answer_remark>' % \
            (indent, ns_prefix, self.answer_remark, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "InfoQuestion")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> info_question.serialize


class MaintenanceDataSet(ProcedureDataSet):
    """ The result of a maintenance activity, a type of Procedure, for a given attribute of an asset is documentated in an MaintenanceDataSet.
    """
    # <<< maintenance_data_set
    # @generated
    def __init__(self, condition_before='', maint_code='', condition_after='', **kw_args):
        """ Initialises a new 'MaintenanceDataSet' instance.
        """
        # Description of the condition of the asset just prior to maintenance being performed. 
        self.condition_before = condition_before

        # Code for the type of maintenance performed. 
        self.maint_code = maint_code

        # Condition of asset just following maintenance procedure. 
        self.condition_after = condition_after



        super(MaintenanceDataSet, self).__init__(**kw_args)
    # >>> maintenance_data_set


    def __str__(self):
        """ Returns a string representation of the MaintenanceDataSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< maintenance_data_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MaintenanceDataSet.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MaintenanceDataSet", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:MaintenanceDataSet.condition_before>%s</%s:MaintenanceDataSet.condition_before>' % \
            (indent, ns_prefix, self.condition_before, ns_prefix)
        s += '%s<%s:MaintenanceDataSet.maint_code>%s</%s:MaintenanceDataSet.maint_code>' % \
            (indent, ns_prefix, self.maint_code, ns_prefix)
        s += '%s<%s:MaintenanceDataSet.condition_after>%s</%s:MaintenanceDataSet.condition_after>' % \
            (indent, ns_prefix, self.condition_after, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
        if self.procedure is not None:
            s += '%s<%s:ProcedureDataSet.procedure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.procedure.uri)
        for obj in self.properties:
            s += '%s<%s:ProcedureDataSet.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurement_values:
            s += '%s<%s:ProcedureDataSet.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transformer_observations:
            s += '%s<%s:ProcedureDataSet.transformer_observations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProcedureDataSet.completed_date_time>%s</%s:ProcedureDataSet.completed_date_time>' % \
            (indent, ns_prefix, self.completed_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MaintenanceDataSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> maintenance_data_set.serialize


class Regulation(Document):
    """ Special requirements and/or regulations may pertain to certain types of assets or work. For example, fire protection and scaffolding.
    """
    # <<< regulation
    # @generated
    def __init__(self, reference_number='', **kw_args):
        """ Initialises a new 'Regulation' instance.
        """
        # External reference to regulation, if applicable. 
        self.reference_number = reference_number



        super(Regulation, self).__init__(**kw_args)
    # >>> regulation


    def __str__(self):
        """ Returns a string representation of the Regulation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regulation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Regulation.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Regulation", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Regulation.reference_number>%s</%s:Regulation.reference_number>' % \
            (indent, ns_prefix, self.reference_number, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Regulation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regulation.serialize


class Usage(IdentifiedObject):
    """ The way material and assets are used to perform a certain type of work task. The way is described in text in the inheritied description attribute.
    """
    # <<< usage
    # @generated
    def __init__(self, material_item=None, work_task=None, status=None, work_equipment_asset=None, **kw_args):
        """ Initialises a new 'Usage' instance.
        """

        self._material_item = None
        self.material_item = material_item

        self._work_task = None
        self.work_task = work_task

        self.status = status

        self._work_equipment_asset = None
        self.work_equipment_asset = work_equipment_asset


        super(Usage, self).__init__(**kw_args)
    # >>> usage

    # <<< material_item
    # @generated
    def get_material_item(self):
        """ 
        """
        return self._material_item

    def set_material_item(self, value):
        if self._material_item is not None:
            filtered = [x for x in self.material_item.usages if x != self]
            self._material_item._usages = filtered

        self._material_item = value
        if self._material_item is not None:
            self._material_item._usages.append(self)

    material_item = property(get_material_item, set_material_item)
    # >>> material_item

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.usages if x != self]
            self._work_task._usages = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._usages.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_equipment_asset
    # @generated
    def get_work_equipment_asset(self):
        """ 
        """
        return self._work_equipment_asset

    def set_work_equipment_asset(self, value):
        if self._work_equipment_asset is not None:
            filtered = [x for x in self.work_equipment_asset.usages if x != self]
            self._work_equipment_asset._usages = filtered

        self._work_equipment_asset = value
        if self._work_equipment_asset is not None:
            self._work_equipment_asset._usages.append(self)

    work_equipment_asset = property(get_work_equipment_asset, set_work_equipment_asset)
    # >>> work_equipment_asset


    def __str__(self):
        """ Returns a string representation of the Usage.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< usage.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Usage.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Usage", self.uri)
        if format:
            indent += ' ' * depth

        if self.material_item is not None:
            s += '%s<%s:Usage.material_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.material_item.uri)
        if self.work_task is not None:
            s += '%s<%s:Usage.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        if self.status is not None:
            s += '%s<%s:Usage.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.work_equipment_asset is not None:
            s += '%s<%s:Usage.work_equipment_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_equipment_asset.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Usage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> usage.serialize


class AccessPermit(Document):
    """ A permit is sometimes needed to provide legal access to land or equipment. For example, local authority permission for road works.
    """
    # <<< access_permit
    # @generated
    def __init__(self, payment=0.0, application_number='', expiration_date='', effective_date='', permit_id='', **kw_args):
        """ Initialises a new 'AccessPermit' instance.
        """
        # Total cost of permit. 
        self.payment = payment

        # Permit application number that is used by municipality, state, province, etc. 
        self.application_number = application_number

        # Permit expiration date. 
        self.expiration_date = expiration_date

        # Date that permit became official. 
        self.effective_date = effective_date

        # Permit identifier. 
        self.permit_id = permit_id



        super(AccessPermit, self).__init__(**kw_args)
    # >>> access_permit


    def __str__(self):
        """ Returns a string representation of the AccessPermit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< access_permit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the AccessPermit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "AccessPermit", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:AccessPermit.payment>%s</%s:AccessPermit.payment>' % \
            (indent, ns_prefix, self.payment, ns_prefix)
        s += '%s<%s:AccessPermit.application_number>%s</%s:AccessPermit.application_number>' % \
            (indent, ns_prefix, self.application_number, ns_prefix)
        s += '%s<%s:AccessPermit.expiration_date>%s</%s:AccessPermit.expiration_date>' % \
            (indent, ns_prefix, self.expiration_date, ns_prefix)
        s += '%s<%s:AccessPermit.effective_date>%s</%s:AccessPermit.effective_date>' % \
            (indent, ns_prefix, self.effective_date, ns_prefix)
        s += '%s<%s:AccessPermit.permit_id>%s</%s:AccessPermit.permit_id>' % \
            (indent, ns_prefix, self.permit_id, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "AccessPermit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> access_permit.serialize


class WorkStatusEntry(ActivityRecord):
    """ A type of ActivityRecord that records information about the status of an item, such as a Work or WorkTask, at a point in time.
    """
    # <<< work_status_entry
    # @generated
    def __init__(self, percent_complete=0.0, **kw_args):
        """ Initialises a new 'WorkStatusEntry' instance.
        """
        # Estimated percentage of completion of this individual work task or overall work order. 
        self.percent_complete = percent_complete



        super(WorkStatusEntry, self).__init__(**kw_args)
    # >>> work_status_entry


    def __str__(self):
        """ Returns a string representation of the WorkStatusEntry.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_status_entry.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkStatusEntry.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkStatusEntry", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:WorkStatusEntry.percent_complete>%s</%s:WorkStatusEntry.percent_complete>' % \
            (indent, ns_prefix, self.percent_complete, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.market_factors:
            s += '%s<%s:ActivityRecord.market_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.documents:
            s += '%s<%s:ActivityRecord.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.organisations:
            s += '%s<%s:ActivityRecord.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.scheduled_event is not None:
            s += '%s<%s:ActivityRecord.scheduled_event rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.scheduled_event.uri)
        for obj in self.assets:
            s += '%s<%s:ActivityRecord.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_persons:
            s += '%s<%s:ActivityRecord.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:ActivityRecord.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ActivityRecord.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ActivityRecord.reason>%s</%s:ActivityRecord.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:ActivityRecord.category>%s</%s:ActivityRecord.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:ActivityRecord.severity>%s</%s:ActivityRecord.severity>' % \
            (indent, ns_prefix, self.severity, ns_prefix)
        s += '%s<%s:ActivityRecord.created_date_time>%s</%s:ActivityRecord.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkStatusEntry")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_status_entry.serialize


class WorkTask(Document):
    """ A set of tasks is required to implement a design.
    """
    # <<< work_task
    # @generated
    def __init__(self, sched_override='', priority='', contractor_items=None, crews=None, work_cost_details=None, usages=None, qualification_requirements=None, work=None, work_flow_step=None, labor_items=None, material_items=None, equipment_items=None, design_location_cus=None, overhead_cost=None, assets=None, capabilities=None, misc_cost_items=None, switching_schedules=None, design=None, **kw_args):
        """ Initialises a new 'WorkTask' instance.
        """
        # If specified, override schedule and perform this task in accordance with instructions specified here. 
        self.sched_override = sched_override

        # The priority of this work task. 
        self.priority = priority


        self._contractor_items = []
        if contractor_items is not None:
            self.contractor_items = contractor_items
        else:
            self.contractor_items = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._usages = []
        if usages is not None:
            self.usages = usages
        else:
            self.usages = []

        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._work = None
        self.work = work

        self._work_flow_step = None
        self.work_flow_step = work_flow_step

        self._labor_items = []
        if labor_items is not None:
            self.labor_items = labor_items
        else:
            self.labor_items = []

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._equipment_items = []
        if equipment_items is not None:
            self.equipment_items = equipment_items
        else:
            self.equipment_items = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._overhead_cost = None
        self.overhead_cost = overhead_cost

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._capabilities = []
        if capabilities is not None:
            self.capabilities = capabilities
        else:
            self.capabilities = []

        self._misc_cost_items = []
        if misc_cost_items is not None:
            self.misc_cost_items = misc_cost_items
        else:
            self.misc_cost_items = []

        self._switching_schedules = []
        if switching_schedules is not None:
            self.switching_schedules = switching_schedules
        else:
            self.switching_schedules = []

        self._design = None
        self.design = design


        super(WorkTask, self).__init__(**kw_args)
    # >>> work_task

    # <<< contractor_items
    # @generated
    def get_contractor_items(self):
        """ 
        """
        return self._contractor_items

    def set_contractor_items(self, value):
        for x in self._contractor_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._contractor_items = value

    contractor_items = property(get_contractor_items, set_contractor_items)

    def add_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_task = self
            self._contractor_items.append(obj)

    def remove_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_task = None
            self._contractor_items.remove(obj)
    # >>> contractor_items

    # <<< crews
    # @generated
    def get_crews(self):
        """ All Crews participating in this WorkTask.
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.work_tasks if q != self]
            self._crews._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._work_task = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._work_task = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< usages
    # @generated
    def get_usages(self):
        """ 
        """
        return self._usages

    def set_usages(self, value):
        for x in self._usages:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._usages = value

    usages = property(get_usages, set_usages)

    def add_usages(self, *usages):
        for obj in usages:
            obj._work_task = self
            self._usages.append(obj)

    def remove_usages(self, *usages):
        for obj in usages:
            obj._work_task = None
            self._usages.remove(obj)
    # >>> usages

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.work_tasks if q != self]
            self._qualification_requirements._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< work
    # @generated
    def get_work(self):
        """ 
        """
        return self._work

    def set_work(self, value):
        if self._work is not None:
            filtered = [x for x in self.work.work_tasks if x != self]
            self._work._work_tasks = filtered

        self._work = value
        if self._work is not None:
            self._work._work_tasks.append(self)

    work = property(get_work, set_work)
    # >>> work

    # <<< work_flow_step
    # @generated
    def get_work_flow_step(self):
        """ 
        """
        return self._work_flow_step

    def set_work_flow_step(self, value):
        if self._work_flow_step is not None:
            filtered = [x for x in self.work_flow_step.work_tasks if x != self]
            self._work_flow_step._work_tasks = filtered

        self._work_flow_step = value
        if self._work_flow_step is not None:
            self._work_flow_step._work_tasks.append(self)

    work_flow_step = property(get_work_flow_step, set_work_flow_step)
    # >>> work_flow_step

    # <<< labor_items
    # @generated
    def get_labor_items(self):
        """ 
        """
        return self._labor_items

    def set_labor_items(self, value):
        for x in self._labor_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._labor_items = value

    labor_items = property(get_labor_items, set_labor_items)

    def add_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_task = self
            self._labor_items.append(obj)

    def remove_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_task = None
            self._labor_items.remove(obj)
    # >>> labor_items

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._work_task = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._work_task = None
            self._material_items.remove(obj)
    # >>> material_items

    # <<< equipment_items
    # @generated
    def get_equipment_items(self):
        """ 
        """
        return self._equipment_items

    def set_equipment_items(self, value):
        for x in self._equipment_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._equipment_items = value

    equipment_items = property(get_equipment_items, set_equipment_items)

    def add_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_task = self
            self._equipment_items.append(obj)

    def remove_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_task = None
            self._equipment_items.remove(obj)
    # >>> equipment_items

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.work_tasks if q != self]
            self._design_location_cus._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< overhead_cost
    # @generated
    def get_overhead_cost(self):
        """ 
        """
        return self._overhead_cost

    def set_overhead_cost(self, value):
        if self._overhead_cost is not None:
            filtered = [x for x in self.overhead_cost.work_tasks if x != self]
            self._overhead_cost._work_tasks = filtered

        self._overhead_cost = value
        if self._overhead_cost is not None:
            self._overhead_cost._work_tasks.append(self)

    overhead_cost = property(get_overhead_cost, set_overhead_cost)
    # >>> overhead_cost

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for x in self._assets:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            obj._work_task = self
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            obj._work_task = None
            self._assets.remove(obj)
    # >>> assets

    # <<< capabilities
    # @generated
    def get_capabilities(self):
        """ 
        """
        return self._capabilities

    def set_capabilities(self, value):
        for p in self._capabilities:
            filtered = [q for q in p.work_tasks if q != self]
            self._capabilities._work_tasks = filtered
        for r in value:
            if self not in r._work_tasks:
                r._work_tasks.append(self)
        self._capabilities = value

    capabilities = property(get_capabilities, set_capabilities)

    def add_capabilities(self, *capabilities):
        for obj in capabilities:
            if self not in obj._work_tasks:
                obj._work_tasks.append(self)
            self._capabilities.append(obj)

    def remove_capabilities(self, *capabilities):
        for obj in capabilities:
            if self in obj._work_tasks:
                obj._work_tasks.remove(self)
            self._capabilities.remove(obj)
    # >>> capabilities

    # <<< misc_cost_items
    # @generated
    def get_misc_cost_items(self):
        """ 
        """
        return self._misc_cost_items

    def set_misc_cost_items(self, value):
        for x in self._misc_cost_items:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._misc_cost_items = value

    misc_cost_items = property(get_misc_cost_items, set_misc_cost_items)

    def add_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_task = self
            self._misc_cost_items.append(obj)

    def remove_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_task = None
            self._misc_cost_items.remove(obj)
    # >>> misc_cost_items

    # <<< switching_schedules
    # @generated
    def get_switching_schedules(self):
        """ 
        """
        return self._switching_schedules

    def set_switching_schedules(self, value):
        for x in self._switching_schedules:
            x._work_task = None
        for y in value:
            y._work_task = self
        self._switching_schedules = value

    switching_schedules = property(get_switching_schedules, set_switching_schedules)

    def add_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            obj._work_task = self
            self._switching_schedules.append(obj)

    def remove_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            obj._work_task = None
            self._switching_schedules.remove(obj)
    # >>> switching_schedules

    # <<< design
    # @generated
    def get_design(self):
        """ 
        """
        return self._design

    def set_design(self, value):
        if self._design is not None:
            filtered = [x for x in self.design.work_tasks if x != self]
            self._design._work_tasks = filtered

        self._design = value
        if self._design is not None:
            self._design._work_tasks.append(self)

    design = property(get_design, set_design)
    # >>> design


    def __str__(self):
        """ Returns a string representation of the WorkTask.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_task.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkTask.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkTask", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contractor_items:
            s += '%s<%s:WorkTask.contractor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:WorkTask.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_cost_details:
            s += '%s<%s:WorkTask.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.usages:
            s += '%s<%s:WorkTask.usages rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.qualification_requirements:
            s += '%s<%s:WorkTask.qualification_requirements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work is not None:
            s += '%s<%s:WorkTask.work rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work.uri)
        if self.work_flow_step is not None:
            s += '%s<%s:WorkTask.work_flow_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_flow_step.uri)
        for obj in self.labor_items:
            s += '%s<%s:WorkTask.labor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.material_items:
            s += '%s<%s:WorkTask.material_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipment_items:
            s += '%s<%s:WorkTask.equipment_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_location_cus:
            s += '%s<%s:WorkTask.design_location_cus rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.overhead_cost is not None:
            s += '%s<%s:WorkTask.overhead_cost rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.overhead_cost.uri)
        for obj in self.assets:
            s += '%s<%s:WorkTask.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.capabilities:
            s += '%s<%s:WorkTask.capabilities rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.misc_cost_items:
            s += '%s<%s:WorkTask.misc_cost_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.switching_schedules:
            s += '%s<%s:WorkTask.switching_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.design is not None:
            s += '%s<%s:WorkTask.design rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design.uri)
        s += '%s<%s:WorkTask.sched_override>%s</%s:WorkTask.sched_override>' % \
            (indent, ns_prefix, self.sched_override, ns_prefix)
        s += '%s<%s:WorkTask.priority>%s</%s:WorkTask.priority>' % \
            (indent, ns_prefix, self.priority, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkTask")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_task.serialize


class Request(Document):
    """ A request for work, service or project.
    """
    # <<< request
    # @generated
    def __init__(self, corporate_code='', priority='', action_needed='', organisation=None, projects=None, erp_quote_line_item=None, works=None, **kw_args):
        """ Initialises a new 'Request' instance.
        """
        # The corporate code for this request. 
        self.corporate_code = corporate_code

        # The priority of this request. 
        self.priority = priority

        # Based on the current 'Status.status', the action that is needed before this Request can transition to the desired state, such as initiating the requested Work. For example, missing or additionally needed information may be required from the requesting organisation before a work Design may be created. 
        self.action_needed = action_needed


        self._organisation = None
        self.organisation = organisation

        self._projects = []
        if projects is not None:
            self.projects = projects
        else:
            self.projects = []

        self._erp_quote_line_item = None
        self.erp_quote_line_item = erp_quote_line_item

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []


        super(Request, self).__init__(**kw_args)
    # >>> request

    # <<< organisation
    # @generated
    def get_organisation(self):
        """ 
        """
        return self._organisation

    def set_organisation(self, value):
        if self._organisation is not None:
            filtered = [x for x in self.organisation.requests if x != self]
            self._organisation._requests = filtered

        self._organisation = value
        if self._organisation is not None:
            self._organisation._requests.append(self)

    organisation = property(get_organisation, set_organisation)
    # >>> organisation

    # <<< projects
    # @generated
    def get_projects(self):
        """ 
        """
        return self._projects

    def set_projects(self, value):
        for p in self._projects:
            filtered = [q for q in p.requests if q != self]
            self._projects._requests = filtered
        for r in value:
            if self not in r._requests:
                r._requests.append(self)
        self._projects = value

    projects = property(get_projects, set_projects)

    def add_projects(self, *projects):
        for obj in projects:
            if self not in obj._requests:
                obj._requests.append(self)
            self._projects.append(obj)

    def remove_projects(self, *projects):
        for obj in projects:
            if self in obj._requests:
                obj._requests.remove(self)
            self._projects.remove(obj)
    # >>> projects

    # <<< erp_quote_line_item
    # @generated
    def get_erp_quote_line_item(self):
        """ 
        """
        return self._erp_quote_line_item

    def set_erp_quote_line_item(self, value):
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._request = None

        self._erp_quote_line_item = value
        if self._erp_quote_line_item is not None:
            self._erp_quote_line_item._request = self

    erp_quote_line_item = property(get_erp_quote_line_item, set_erp_quote_line_item)
    # >>> erp_quote_line_item

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._request = None
        for y in value:
            y._request = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._request = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._request = None
            self._works.remove(obj)
    # >>> works


    def __str__(self):
        """ Returns a string representation of the Request.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< request.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Request.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Request", self.uri)
        if format:
            indent += ' ' * depth

        if self.organisation is not None:
            s += '%s<%s:Request.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        for obj in self.projects:
            s += '%s<%s:Request.projects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_quote_line_item is not None:
            s += '%s<%s:Request.erp_quote_line_item rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_quote_line_item.uri)
        for obj in self.works:
            s += '%s<%s:Request.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Request.corporate_code>%s</%s:Request.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Request.priority>%s</%s:Request.priority>' % \
            (indent, ns_prefix, self.priority, ns_prefix)
        s += '%s<%s:Request.action_needed>%s</%s:Request.action_needed>' % \
            (indent, ns_prefix, self.action_needed, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Request")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> request.serialize


class CUAllowableAction(IdentifiedObject):
    """ Allowed actions: Install, Remove, Transfer, Abandon, etc.
    """
    # <<< cuallowable_action
    # @generated
    def __init__(self, compatible_units=None, status=None, **kw_args):
        """ Initialises a new 'CUAllowableAction' instance.
        """

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status


        super(CUAllowableAction, self).__init__(**kw_args)
    # >>> cuallowable_action

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._cuallowable_action = None
        for y in value:
            y._cuallowable_action = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cuallowable_action = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cuallowable_action = None
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the CUAllowableAction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cuallowable_action.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CUAllowableAction.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CUAllowableAction", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.compatible_units:
            s += '%s<%s:CUAllowableAction.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:CUAllowableAction.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CUAllowableAction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cuallowable_action.serialize


class Project(Document):
    """ A collection of related work. For construction projects and maintenance projects, multiple phases may be performed.
    """
    # <<< project
    # @generated
    def __init__(self, budget=0.0, erp_project_accounting=None, works=None, business_case=None, requests=None, parent_project=None, sub_projects=None, **kw_args):
        """ Initialises a new 'Project' instance.
        """
        # Overall project budget. 
        self.budget = budget


        self._erp_project_accounting = None
        self.erp_project_accounting = erp_project_accounting

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._business_case = None
        self.business_case = business_case

        self._requests = []
        if requests is not None:
            self.requests = requests
        else:
            self.requests = []

        self._parent_project = None
        self.parent_project = parent_project

        self._sub_projects = []
        if sub_projects is not None:
            self.sub_projects = sub_projects
        else:
            self.sub_projects = []


        super(Project, self).__init__(**kw_args)
    # >>> project

    # <<< erp_project_accounting
    # @generated
    def get_erp_project_accounting(self):
        """ 
        """
        return self._erp_project_accounting

    def set_erp_project_accounting(self, value):
        if self._erp_project_accounting is not None:
            filtered = [x for x in self.erp_project_accounting.projects if x != self]
            self._erp_project_accounting._projects = filtered

        self._erp_project_accounting = value
        if self._erp_project_accounting is not None:
            self._erp_project_accounting._projects.append(self)

    erp_project_accounting = property(get_erp_project_accounting, set_erp_project_accounting)
    # >>> erp_project_accounting

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._project = None
        for y in value:
            y._project = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._project = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._project = None
            self._works.remove(obj)
    # >>> works

    # <<< business_case
    # @generated
    def get_business_case(self):
        """ 
        """
        return self._business_case

    def set_business_case(self, value):
        if self._business_case is not None:
            filtered = [x for x in self.business_case.projects if x != self]
            self._business_case._projects = filtered

        self._business_case = value
        if self._business_case is not None:
            self._business_case._projects.append(self)

    business_case = property(get_business_case, set_business_case)
    # >>> business_case

    # <<< requests
    # @generated
    def get_requests(self):
        """ 
        """
        return self._requests

    def set_requests(self, value):
        for p in self._requests:
            filtered = [q for q in p.projects if q != self]
            self._requests._projects = filtered
        for r in value:
            if self not in r._projects:
                r._projects.append(self)
        self._requests = value

    requests = property(get_requests, set_requests)

    def add_requests(self, *requests):
        for obj in requests:
            if self not in obj._projects:
                obj._projects.append(self)
            self._requests.append(obj)

    def remove_requests(self, *requests):
        for obj in requests:
            if self in obj._projects:
                obj._projects.remove(self)
            self._requests.remove(obj)
    # >>> requests

    # <<< parent_project
    # @generated
    def get_parent_project(self):
        """ 
        """
        return self._parent_project

    def set_parent_project(self, value):
        if self._parent_project is not None:
            filtered = [x for x in self.parent_project.sub_projects if x != self]
            self._parent_project._sub_projects = filtered

        self._parent_project = value
        if self._parent_project is not None:
            self._parent_project._sub_projects.append(self)

    parent_project = property(get_parent_project, set_parent_project)
    # >>> parent_project

    # <<< sub_projects
    # @generated
    def get_sub_projects(self):
        """ 
        """
        return self._sub_projects

    def set_sub_projects(self, value):
        for x in self._sub_projects:
            x._parent_project = None
        for y in value:
            y._parent_project = self
        self._sub_projects = value

    sub_projects = property(get_sub_projects, set_sub_projects)

    def add_sub_projects(self, *sub_projects):
        for obj in sub_projects:
            obj._parent_project = self
            self._sub_projects.append(obj)

    def remove_sub_projects(self, *sub_projects):
        for obj in sub_projects:
            obj._parent_project = None
            self._sub_projects.remove(obj)
    # >>> sub_projects


    def __str__(self):
        """ Returns a string representation of the Project.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< project.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Project.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Project", self.uri)
        if format:
            indent += ' ' * depth

        if self.erp_project_accounting is not None:
            s += '%s<%s:Project.erp_project_accounting rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_project_accounting.uri)
        for obj in self.works:
            s += '%s<%s:Project.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.business_case is not None:
            s += '%s<%s:Project.business_case rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.business_case.uri)
        for obj in self.requests:
            s += '%s<%s:Project.requests rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent_project is not None:
            s += '%s<%s:Project.parent_project rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent_project.uri)
        for obj in self.sub_projects:
            s += '%s<%s:Project.sub_projects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Project.budget>%s</%s:Project.budget>' % \
            (indent, ns_prefix, self.budget, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Project")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> project.serialize


class CUAsset(IdentifiedObject):
    """ Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..
    """
    # <<< cuasset
    # @generated
    def __init__(self, quantity=0, type_asset_code='', compatible_units=None, type_asset=None, status=None, **kw_args):
        """ Initialises a new 'CUAsset' instance.
        """
        # Quantity of the type asset within the CU. 
        self.quantity = quantity

        # The code for this type of asset. 
        self.type_asset_code = type_asset_code


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._type_asset = None
        self.type_asset = type_asset

        self.status = status


        super(CUAsset, self).__init__(**kw_args)
    # >>> cuasset

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cuassets if q != self]
            self._compatible_units._cuassets = filtered
        for r in value:
            if self not in r._cuassets:
                r._cuassets.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cuassets:
                obj._cuassets.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cuassets:
                obj._cuassets.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            self._type_asset._cuasset = None

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._cuasset = self

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the CUAsset.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cuasset.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CUAsset.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CUAsset", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.compatible_units:
            s += '%s<%s:CUAsset.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.type_asset is not None:
            s += '%s<%s:CUAsset.type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_asset.uri)
        if self.status is not None:
            s += '%s<%s:CUAsset.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:CUAsset.quantity>%s</%s:CUAsset.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        s += '%s<%s:CUAsset.type_asset_code>%s</%s:CUAsset.type_asset_code>' % \
            (indent, ns_prefix, self.type_asset_code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CUAsset")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cuasset.serialize


class PropertyUnit(IdentifiedObject):
    """ Unit of property for reporting purposes.
    """
    # <<< property_unit
    # @generated
    def __init__(self, activity_code='install', accounting_usage='', property_account='', cumaterial_items=None, compatible_units=None, status=None, work_cost_details=None, **kw_args):
        """ Initialises a new 'PropertyUnit' instance.
        """
        # Activity code identifies a specific and distinguishable work action. Values are: "install", "remove", "transfer", "abandon"
        self.activity_code = 'install'

        # A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications. 
        self.accounting_usage = accounting_usage

        # Used for property record accounting. For example, in the USA, this would be a FERC account. 
        self.property_account = property_account


        self._cumaterial_items = []
        if cumaterial_items is not None:
            self.cumaterial_items = cumaterial_items
        else:
            self.cumaterial_items = []

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status

        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []


        super(PropertyUnit, self).__init__(**kw_args)
    # >>> property_unit

    # <<< cumaterial_items
    # @generated
    def get_cumaterial_items(self):
        """ 
        """
        return self._cumaterial_items

    def set_cumaterial_items(self, value):
        for p in self._cumaterial_items:
            filtered = [q for q in p.property_units if q != self]
            self._cumaterial_items._property_units = filtered
        for r in value:
            if self not in r._property_units:
                r._property_units.append(self)
        self._cumaterial_items = value

    cumaterial_items = property(get_cumaterial_items, set_cumaterial_items)

    def add_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self not in obj._property_units:
                obj._property_units.append(self)
            self._cumaterial_items.append(obj)

    def remove_cumaterial_items(self, *cumaterial_items):
        for obj in cumaterial_items:
            if self in obj._property_units:
                obj._property_units.remove(self)
            self._cumaterial_items.remove(obj)
    # >>> cumaterial_items

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._property_unit = None
        for y in value:
            y._property_unit = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._property_unit = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._property_unit = None
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for p in self._work_cost_details:
            filtered = [q for q in p.property_units if q != self]
            self._work_cost_details._property_units = filtered
        for r in value:
            if self not in r._property_units:
                r._property_units.append(self)
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            if self not in obj._property_units:
                obj._property_units.append(self)
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            if self in obj._property_units:
                obj._property_units.remove(self)
            self._work_cost_details.remove(obj)
    # >>> work_cost_details


    def __str__(self):
        """ Returns a string representation of the PropertyUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< property_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PropertyUnit.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PropertyUnit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.cumaterial_items:
            s += '%s<%s:PropertyUnit.cumaterial_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.compatible_units:
            s += '%s<%s:PropertyUnit.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:PropertyUnit.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.work_cost_details:
            s += '%s<%s:PropertyUnit.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PropertyUnit.activity_code>%s</%s:PropertyUnit.activity_code>' % \
            (indent, ns_prefix, self.activity_code, ns_prefix)
        s += '%s<%s:PropertyUnit.accounting_usage>%s</%s:PropertyUnit.accounting_usage>' % \
            (indent, ns_prefix, self.accounting_usage, ns_prefix)
        s += '%s<%s:PropertyUnit.property_account>%s</%s:PropertyUnit.property_account>' % \
            (indent, ns_prefix, self.property_account, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PropertyUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> property_unit.serialize


class InspectionDataSet(ProcedureDataSet):
    """ Documents the result of one inspection, a type of Procedure, for a given attribute of an asset.
    """
    # <<< inspection_data_set
    # @generated
    def __init__(self, location_condition='', according_to_schedules=None, **kw_args):
        """ Initialises a new 'InspectionDataSet' instance.
        """
        # Description of the conditions of the location where the asset resides. 
        self.location_condition = location_condition


        self._according_to_schedules = []
        if according_to_schedules is not None:
            self.according_to_schedules = according_to_schedules
        else:
            self.according_to_schedules = []


        super(InspectionDataSet, self).__init__(**kw_args)
    # >>> inspection_data_set

    # <<< according_to_schedules
    # @generated
    def get_according_to_schedules(self):
        """ 
        """
        return self._according_to_schedules

    def set_according_to_schedules(self, value):
        for x in self._according_to_schedules:
            x._for_inspection_data_set = None
        for y in value:
            y._for_inspection_data_set = self
        self._according_to_schedules = value

    according_to_schedules = property(get_according_to_schedules, set_according_to_schedules)

    def add_according_to_schedules(self, *according_to_schedules):
        for obj in according_to_schedules:
            obj._for_inspection_data_set = self
            self._according_to_schedules.append(obj)

    def remove_according_to_schedules(self, *according_to_schedules):
        for obj in according_to_schedules:
            obj._for_inspection_data_set = None
            self._according_to_schedules.remove(obj)
    # >>> according_to_schedules


    def __str__(self):
        """ Returns a string representation of the InspectionDataSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< inspection_data_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the InspectionDataSet.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "InspectionDataSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.according_to_schedules:
            s += '%s<%s:InspectionDataSet.according_to_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:InspectionDataSet.location_condition>%s</%s:InspectionDataSet.location_condition>' % \
            (indent, ns_prefix, self.location_condition, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
        if self.procedure is not None:
            s += '%s<%s:ProcedureDataSet.procedure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.procedure.uri)
        for obj in self.properties:
            s += '%s<%s:ProcedureDataSet.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurement_values:
            s += '%s<%s:ProcedureDataSet.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transformer_observations:
            s += '%s<%s:ProcedureDataSet.transformer_observations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProcedureDataSet.completed_date_time>%s</%s:ProcedureDataSet.completed_date_time>' % \
            (indent, ns_prefix, self.completed_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "InspectionDataSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> inspection_data_set.serialize


class CostType(IdentifiedObject):
    """ A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.
    """
    # <<< cost_type
    # @generated
    def __init__(self, code='', amount_assignment_flag=False, level='', stage='', work_cost_details=None, erp_journal_entries=None, child_cost_types=None, parent_cost_type=None, status=None, compatible_units=None, **kw_args):
        """ Initialises a new 'CostType' instance.
        """
        # A codified representation of the resource element. 
        self.code = code

        # True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components). 
        self.amount_assignment_flag = amount_assignment_flag

        # The level of the resource element in the hierarchy of resource elements (recursive relationship). 
        self.level = level

        # The stage for which this costType applies: estimated design, estimated actual or actual actual. 
        self.stage = stage


        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._erp_journal_entries = []
        if erp_journal_entries is not None:
            self.erp_journal_entries = erp_journal_entries
        else:
            self.erp_journal_entries = []

        self._child_cost_types = []
        if child_cost_types is not None:
            self.child_cost_types = child_cost_types
        else:
            self.child_cost_types = []

        self._parent_cost_type = None
        self.parent_cost_type = parent_cost_type

        self.status = status

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []


        super(CostType, self).__init__(**kw_args)
    # >>> cost_type

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._cost_type = None
        for y in value:
            y._cost_type = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._cost_type = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._cost_type = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< erp_journal_entries
    # @generated
    def get_erp_journal_entries(self):
        """ 
        """
        return self._erp_journal_entries

    def set_erp_journal_entries(self, value):
        for p in self._erp_journal_entries:
            filtered = [q for q in p.cost_types if q != self]
            self._erp_journal_entries._cost_types = filtered
        for r in value:
            if self not in r._cost_types:
                r._cost_types.append(self)
        self._erp_journal_entries = value

    erp_journal_entries = property(get_erp_journal_entries, set_erp_journal_entries)

    def add_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self not in obj._cost_types:
                obj._cost_types.append(self)
            self._erp_journal_entries.append(obj)

    def remove_erp_journal_entries(self, *erp_journal_entries):
        for obj in erp_journal_entries:
            if self in obj._cost_types:
                obj._cost_types.remove(self)
            self._erp_journal_entries.remove(obj)
    # >>> erp_journal_entries

    # <<< child_cost_types
    # @generated
    def get_child_cost_types(self):
        """ 
        """
        return self._child_cost_types

    def set_child_cost_types(self, value):
        for x in self._child_cost_types:
            x._parent_cost_type = None
        for y in value:
            y._parent_cost_type = self
        self._child_cost_types = value

    child_cost_types = property(get_child_cost_types, set_child_cost_types)

    def add_child_cost_types(self, *child_cost_types):
        for obj in child_cost_types:
            obj._parent_cost_type = self
            self._child_cost_types.append(obj)

    def remove_child_cost_types(self, *child_cost_types):
        for obj in child_cost_types:
            obj._parent_cost_type = None
            self._child_cost_types.remove(obj)
    # >>> child_cost_types

    # <<< parent_cost_type
    # @generated
    def get_parent_cost_type(self):
        """ 
        """
        return self._parent_cost_type

    def set_parent_cost_type(self, value):
        if self._parent_cost_type is not None:
            filtered = [x for x in self.parent_cost_type.child_cost_types if x != self]
            self._parent_cost_type._child_cost_types = filtered

        self._parent_cost_type = value
        if self._parent_cost_type is not None:
            self._parent_cost_type._child_cost_types.append(self)

    parent_cost_type = property(get_parent_cost_type, set_parent_cost_type)
    # >>> parent_cost_type

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._cost_type = None
        for y in value:
            y._cost_type = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cost_type = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cost_type = None
            self._compatible_units.remove(obj)
    # >>> compatible_units


    def __str__(self):
        """ Returns a string representation of the CostType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cost_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CostType.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CostType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.work_cost_details:
            s += '%s<%s:CostType.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_journal_entries:
            s += '%s<%s:CostType.erp_journal_entries rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.child_cost_types:
            s += '%s<%s:CostType.child_cost_types rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent_cost_type is not None:
            s += '%s<%s:CostType.parent_cost_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent_cost_type.uri)
        if self.status is not None:
            s += '%s<%s:CostType.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.compatible_units:
            s += '%s<%s:CostType.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:CostType.code>%s</%s:CostType.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:CostType.amount_assignment_flag>%s</%s:CostType.amount_assignment_flag>' % \
            (indent, ns_prefix, self.amount_assignment_flag, ns_prefix)
        s += '%s<%s:CostType.level>%s</%s:CostType.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:CostType.stage>%s</%s:CostType.stage>' % \
            (indent, ns_prefix, self.stage, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CostType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cost_type.serialize


class WorkCostSummary(Document):
    """ A roll up by cost category for the entire cost of a work order. For example, total labor.
    """
    # <<< work_cost_summary
    # @generated
    def __init__(self, work_cost_detail=None, **kw_args):
        """ Initialises a new 'WorkCostSummary' instance.
        """

        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail


        super(WorkCostSummary, self).__init__(**kw_args)
    # >>> work_cost_summary

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            self._work_cost_detail._work_cost_summary = None

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._work_cost_summary = self

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail


    def __str__(self):
        """ Returns a string representation of the WorkCostSummary.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_cost_summary.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkCostSummary.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkCostSummary", self.uri)
        if format:
            indent += ' ' * depth

        if self.work_cost_detail is not None:
            s += '%s<%s:WorkCostSummary.work_cost_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_detail.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkCostSummary")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_cost_summary.serialize


class MiscCostItem(IdentifiedObject):
    """ Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.
    """
    # <<< misc_cost_item
    # @generated
    def __init__(self, cost_per_unit=0.0, external_ref_id='', cost_type='', quantity=0, account='', work_cost_detail=None, design_location=None, work_task=None, status=None, **kw_args):
        """ Initialises a new 'MiscCostItem' instance.
        """
        # The cost per unit for this misc. item. 
        self.cost_per_unit = cost_per_unit

        # External Reference ID (e.g. PO#, Serial #) 
        self.external_ref_id = external_ref_id

        # The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead. 
        self.cost_type = cost_type

        # The quantity of the misc. item being assigned to this location. 
        self.quantity = quantity

        # This drives the accounting treatment for this misc. item. 
        self.account = account


        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._design_location = None
        self.design_location = design_location

        self._work_task = None
        self.work_task = work_task

        self.status = status


        super(MiscCostItem, self).__init__(**kw_args)
    # >>> misc_cost_item

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.misc_cost_items if x != self]
            self._work_cost_detail._misc_cost_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._misc_cost_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.misc_cost_items if x != self]
            self._design_location._misc_cost_items = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._misc_cost_items.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.misc_cost_items if x != self]
            self._work_task._misc_cost_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._misc_cost_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the MiscCostItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< misc_cost_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MiscCostItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MiscCostItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.work_cost_detail is not None:
            s += '%s<%s:MiscCostItem.work_cost_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_detail.uri)
        if self.design_location is not None:
            s += '%s<%s:MiscCostItem.design_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design_location.uri)
        if self.work_task is not None:
            s += '%s<%s:MiscCostItem.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        if self.status is not None:
            s += '%s<%s:MiscCostItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:MiscCostItem.cost_per_unit>%s</%s:MiscCostItem.cost_per_unit>' % \
            (indent, ns_prefix, self.cost_per_unit, ns_prefix)
        s += '%s<%s:MiscCostItem.external_ref_id>%s</%s:MiscCostItem.external_ref_id>' % \
            (indent, ns_prefix, self.external_ref_id, ns_prefix)
        s += '%s<%s:MiscCostItem.cost_type>%s</%s:MiscCostItem.cost_type>' % \
            (indent, ns_prefix, self.cost_type, ns_prefix)
        s += '%s<%s:MiscCostItem.quantity>%s</%s:MiscCostItem.quantity>' % \
            (indent, ns_prefix, self.quantity, ns_prefix)
        s += '%s<%s:MiscCostItem.account>%s</%s:MiscCostItem.account>' % \
            (indent, ns_prefix, self.account, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MiscCostItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> misc_cost_item.serialize


class CULaborItem(IdentifiedObject):
    """ Compatible unit labor item.
    """
    # <<< culabor_item
    # @generated
    def __init__(self, labor_rate=0.0, activity_code='', labor_duration=0.0, qualification_requirements=None, culabor_code=None, status=None, compatible_units=None, **kw_args):
        """ Initialises a new 'CULaborItem' instance.
        """
        # The labor rate applied for work. 
        self.labor_rate = labor_rate

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code

        # Estimated time to perform work. 
        self.labor_duration = labor_duration


        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._culabor_code = None
        self.culabor_code = culabor_code

        self.status = status

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []


        super(CULaborItem, self).__init__(**kw_args)
    # >>> culabor_item

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.culabor_items if q != self]
            self._qualification_requirements._culabor_items = filtered
        for r in value:
            if self not in r._culabor_items:
                r._culabor_items.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._culabor_items:
                obj._culabor_items.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._culabor_items:
                obj._culabor_items.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< culabor_code
    # @generated
    def get_culabor_code(self):
        """ 
        """
        return self._culabor_code

    def set_culabor_code(self, value):
        if self._culabor_code is not None:
            filtered = [x for x in self.culabor_code.culabor_items if x != self]
            self._culabor_code._culabor_items = filtered

        self._culabor_code = value
        if self._culabor_code is not None:
            self._culabor_code._culabor_items.append(self)

    culabor_code = property(get_culabor_code, set_culabor_code)
    # >>> culabor_code

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.culabor_items if q != self]
            self._compatible_units._culabor_items = filtered
        for r in value:
            if self not in r._culabor_items:
                r._culabor_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._culabor_items:
                obj._culabor_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._culabor_items:
                obj._culabor_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units


    def __str__(self):
        """ Returns a string representation of the CULaborItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< culabor_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CULaborItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CULaborItem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.qualification_requirements:
            s += '%s<%s:CULaborItem.qualification_requirements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.culabor_code is not None:
            s += '%s<%s:CULaborItem.culabor_code rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.culabor_code.uri)
        if self.status is not None:
            s += '%s<%s:CULaborItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.compatible_units:
            s += '%s<%s:CULaborItem.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:CULaborItem.labor_rate>%s</%s:CULaborItem.labor_rate>' % \
            (indent, ns_prefix, self.labor_rate, ns_prefix)
        s += '%s<%s:CULaborItem.activity_code>%s</%s:CULaborItem.activity_code>' % \
            (indent, ns_prefix, self.activity_code, ns_prefix)
        s += '%s<%s:CULaborItem.labor_duration>%s</%s:CULaborItem.labor_duration>' % \
            (indent, ns_prefix, self.labor_duration, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CULaborItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> culabor_item.serialize


class CULaborCode(IdentifiedObject):
    """ Labor code associated with various compatible unit labor items.
    """
    # <<< culabor_code
    # @generated
    def __init__(self, code='', culabor_items=None, status=None, **kw_args):
        """ Initialises a new 'CULaborCode' instance.
        """
        # Labor code. 
        self.code = code


        self._culabor_items = []
        if culabor_items is not None:
            self.culabor_items = culabor_items
        else:
            self.culabor_items = []

        self.status = status


        super(CULaborCode, self).__init__(**kw_args)
    # >>> culabor_code

    # <<< culabor_items
    # @generated
    def get_culabor_items(self):
        """ 
        """
        return self._culabor_items

    def set_culabor_items(self, value):
        for x in self._culabor_items:
            x._culabor_code = None
        for y in value:
            y._culabor_code = self
        self._culabor_items = value

    culabor_items = property(get_culabor_items, set_culabor_items)

    def add_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            obj._culabor_code = self
            self._culabor_items.append(obj)

    def remove_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            obj._culabor_code = None
            self._culabor_items.remove(obj)
    # >>> culabor_items

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the CULaborCode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< culabor_code.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CULaborCode.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CULaborCode", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.culabor_items:
            s += '%s<%s:CULaborCode.culabor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:CULaborCode.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:CULaborCode.code>%s</%s:CULaborCode.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CULaborCode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> culabor_code.serialize


class ShiftPattern(IdentifiedObject):
    """ The patterns of shifts worked by people or crews.
    """
    # <<< shift_pattern
    # @generated
    def __init__(self, cycle_count=0, assignment_type='', validity_interval=None, crews=None, status=None, **kw_args):
        """ Initialises a new 'ShiftPattern' instance.
        """
        # Number of cycles for a temporary shift. 
        self.cycle_count = cycle_count

        # Type of assignement intended to be worked on this shift, for example, temporary, standard, etc. 
        self.assignment_type = assignment_type


        self.validity_interval = validity_interval

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.status = status


        super(ShiftPattern, self).__init__(**kw_args)
    # >>> shift_pattern

    # <<< validity_interval
    # @generated
    # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
    validity_interval = None
    # >>> validity_interval

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.shift_patterns if q != self]
            self._crews._shift_patterns = filtered
        for r in value:
            if self not in r._shift_patterns:
                r._shift_patterns.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._shift_patterns:
                obj._shift_patterns.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._shift_patterns:
                obj._shift_patterns.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ShiftPattern.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< shift_pattern.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ShiftPattern.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ShiftPattern", self.uri)
        if format:
            indent += ' ' * depth

        if self.validity_interval is not None:
            s += '%s<%s:ShiftPattern.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        for obj in self.crews:
            s += '%s<%s:ShiftPattern.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ShiftPattern.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ShiftPattern.cycle_count>%s</%s:ShiftPattern.cycle_count>' % \
            (indent, ns_prefix, self.cycle_count, ns_prefix)
        s += '%s<%s:ShiftPattern.assignment_type>%s</%s:ShiftPattern.assignment_type>' % \
            (indent, ns_prefix, self.assignment_type, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShiftPattern")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> shift_pattern.serialize


class OverheadCost(IdentifiedObject):
    """ Overhead cost applied to work order.
    """
    # <<< overhead_cost
    # @generated
    def __init__(self, cost=0.0, code='', work_cost_details=None, work_tasks=None, status=None, **kw_args):
        """ Initialises a new 'OverheadCost' instance.
        """
        # The overhead cost to be applied. 
        self.cost = cost

        # Overhead code. 
        self.code = code


        self._work_cost_details = []
        if work_cost_details is not None:
            self.work_cost_details = work_cost_details
        else:
            self.work_cost_details = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self.status = status


        super(OverheadCost, self).__init__(**kw_args)
    # >>> overhead_cost

    # <<< work_cost_details
    # @generated
    def get_work_cost_details(self):
        """ 
        """
        return self._work_cost_details

    def set_work_cost_details(self, value):
        for x in self._work_cost_details:
            x._overhead_cost = None
        for y in value:
            y._overhead_cost = self
        self._work_cost_details = value

    work_cost_details = property(get_work_cost_details, set_work_cost_details)

    def add_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._overhead_cost = self
            self._work_cost_details.append(obj)

    def remove_work_cost_details(self, *work_cost_details):
        for obj in work_cost_details:
            obj._overhead_cost = None
            self._work_cost_details.remove(obj)
    # >>> work_cost_details

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._overhead_cost = None
        for y in value:
            y._overhead_cost = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._overhead_cost = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._overhead_cost = None
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the OverheadCost.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< overhead_cost.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OverheadCost.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OverheadCost", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.work_cost_details:
            s += '%s<%s:OverheadCost.work_cost_details rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_tasks:
            s += '%s<%s:OverheadCost.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:OverheadCost.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:OverheadCost.cost>%s</%s:OverheadCost.cost>' % \
            (indent, ns_prefix, self.cost, ns_prefix)
        s += '%s<%s:OverheadCost.code>%s</%s:OverheadCost.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OverheadCost")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> overhead_cost.serialize


class DesignLocationCU(IdentifiedObject):
    """ Compatible unit at a given design location.
    """
    # <<< design_location_cu
    # @generated
    def __init__(self, cu_action='install', removal_year='', cu_usage='', cu_account='', cu_quantity=0, energization_flag=False, designs=None, design_location=None, cugroups=None, condition_factors=None, work_tasks=None, compatible_units=None, status=None, **kw_args):
        """ Initialises a new 'DesignLocationCU' instance.
        """
        # A code that instructs the crew what action to perform. Values are: "install", "remove", "transfer", "abandon"
        self.cu_action = 'install'

        # Year when a CU that represents an asset is removed. 
        self.removal_year = removal_year

        # As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation. 
        self.cu_usage = cu_usage

        # A code that helps direct accounting (capital, expense, or accounting treatment). 
        self.cu_account = cu_account

        # The quantity of the CU being assigned to this location. 
        self.cu_quantity = cu_quantity

        # True if associated electrical equipment is intended to be energized while work is being performed. 
        self.energization_flag = energization_flag


        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []

        self._design_location = None
        self.design_location = design_location

        self._cugroups = []
        if cugroups is not None:
            self.cugroups = cugroups
        else:
            self.cugroups = []

        self._condition_factors = []
        if condition_factors is not None:
            self.condition_factors = condition_factors
        else:
            self.condition_factors = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self.status = status


        super(DesignLocationCU, self).__init__(**kw_args)
    # >>> design_location_cu

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for p in self._designs:
            filtered = [q for q in p.design_locations_cus if q != self]
            self._designs._design_locations_cus = filtered
        for r in value:
            if self not in r._design_locations_cus:
                r._design_locations_cus.append(self)
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            if self not in obj._design_locations_cus:
                obj._design_locations_cus.append(self)
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            if self in obj._design_locations_cus:
                obj._design_locations_cus.remove(self)
            self._designs.remove(obj)
    # >>> designs

    # <<< design_location
    # @generated
    def get_design_location(self):
        """ 
        """
        return self._design_location

    def set_design_location(self, value):
        if self._design_location is not None:
            filtered = [x for x in self.design_location.design_location_cus if x != self]
            self._design_location._design_location_cus = filtered

        self._design_location = value
        if self._design_location is not None:
            self._design_location._design_location_cus.append(self)

    design_location = property(get_design_location, set_design_location)
    # >>> design_location

    # <<< cugroups
    # @generated
    def get_cugroups(self):
        """ 
        """
        return self._cugroups

    def set_cugroups(self, value):
        for p in self._cugroups:
            filtered = [q for q in p.design_location_cus if q != self]
            self._cugroups._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._cugroups = value

    cugroups = property(get_cugroups, set_cugroups)

    def add_cugroups(self, *cugroups):
        for obj in cugroups:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._cugroups.append(obj)

    def remove_cugroups(self, *cugroups):
        for obj in cugroups:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._cugroups.remove(obj)
    # >>> cugroups

    # <<< condition_factors
    # @generated
    def get_condition_factors(self):
        """ 
        """
        return self._condition_factors

    def set_condition_factors(self, value):
        for p in self._condition_factors:
            filtered = [q for q in p.design_location_cus if q != self]
            self._condition_factors._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._condition_factors = value

    condition_factors = property(get_condition_factors, set_condition_factors)

    def add_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._condition_factors.append(obj)

    def remove_condition_factors(self, *condition_factors):
        for obj in condition_factors:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._condition_factors.remove(obj)
    # >>> condition_factors

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.design_location_cus if q != self]
            self._work_tasks._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.design_location_cus if q != self]
            self._compatible_units._design_location_cus = filtered
        for r in value:
            if self not in r._design_location_cus:
                r._design_location_cus.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._design_location_cus:
                obj._design_location_cus.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._design_location_cus:
                obj._design_location_cus.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the DesignLocationCU.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< design_location_cu.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DesignLocationCU.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DesignLocationCU", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.designs:
            s += '%s<%s:DesignLocationCU.designs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.design_location is not None:
            s += '%s<%s:DesignLocationCU.design_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design_location.uri)
        for obj in self.cugroups:
            s += '%s<%s:DesignLocationCU.cugroups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.condition_factors:
            s += '%s<%s:DesignLocationCU.condition_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_tasks:
            s += '%s<%s:DesignLocationCU.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.compatible_units:
            s += '%s<%s:DesignLocationCU.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:DesignLocationCU.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:DesignLocationCU.cu_action>%s</%s:DesignLocationCU.cu_action>' % \
            (indent, ns_prefix, self.cu_action, ns_prefix)
        s += '%s<%s:DesignLocationCU.removal_year>%s</%s:DesignLocationCU.removal_year>' % \
            (indent, ns_prefix, self.removal_year, ns_prefix)
        s += '%s<%s:DesignLocationCU.cu_usage>%s</%s:DesignLocationCU.cu_usage>' % \
            (indent, ns_prefix, self.cu_usage, ns_prefix)
        s += '%s<%s:DesignLocationCU.cu_account>%s</%s:DesignLocationCU.cu_account>' % \
            (indent, ns_prefix, self.cu_account, ns_prefix)
        s += '%s<%s:DesignLocationCU.cu_quantity>%s</%s:DesignLocationCU.cu_quantity>' % \
            (indent, ns_prefix, self.cu_quantity, ns_prefix)
        s += '%s<%s:DesignLocationCU.energization_flag>%s</%s:DesignLocationCU.energization_flag>' % \
            (indent, ns_prefix, self.energization_flag, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DesignLocationCU")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> design_location_cu.serialize


class WorkFlowStep(IdentifiedObject):
    """ A pre-defined set of work steps for a given type of work.
    """
    # <<< work_flow_step
    # @generated
    def __init__(self, sequence_number=0, work=None, work_tasks=None, status=None, **kw_args):
        """ Initialises a new 'WorkFlowStep' instance.
        """
        # Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow. 
        self.sequence_number = sequence_number


        self._work = None
        self.work = work

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self.status = status


        super(WorkFlowStep, self).__init__(**kw_args)
    # >>> work_flow_step

    # <<< work
    # @generated
    def get_work(self):
        """ 
        """
        return self._work

    def set_work(self, value):
        if self._work is not None:
            filtered = [x for x in self.work.work_flow_steps if x != self]
            self._work._work_flow_steps = filtered

        self._work = value
        if self._work is not None:
            self._work._work_flow_steps.append(self)

    work = property(get_work, set_work)
    # >>> work

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for x in self._work_tasks:
            x._work_flow_step = None
        for y in value:
            y._work_flow_step = self
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._work_flow_step = self
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            obj._work_flow_step = None
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the WorkFlowStep.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_flow_step.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkFlowStep.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkFlowStep", self.uri)
        if format:
            indent += ' ' * depth

        if self.work is not None:
            s += '%s<%s:WorkFlowStep.work rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work.uri)
        for obj in self.work_tasks:
            s += '%s<%s:WorkFlowStep.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:WorkFlowStep.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:WorkFlowStep.sequence_number>%s</%s:WorkFlowStep.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkFlowStep")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_flow_step.serialize


class ConditionFactor(IdentifiedObject):
    """ This is to specify the various condition factors for a design that may alter the cost estimate or the allocation.
    """
    # <<< condition_factor
    # @generated
    def __init__(self, kind='labor', cf_value='', status=None, design_location_cus=None, design_locations=None, designs=None, **kw_args):
        """ Initialises a new 'ConditionFactor' instance.
        """
        # Kind of this condition factor. Values are: "labor", "account_allocation", "travel", "other", "material"
        self.kind = 'labor'

        # The actual value of the condition factor, such as labor flat fee or percentage. 
        self.cf_value = cf_value


        self.status = status

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []

        self._designs = []
        if designs is not None:
            self.designs = designs
        else:
            self.designs = []


        super(ConditionFactor, self).__init__(**kw_args)
    # >>> condition_factor

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.condition_factors if q != self]
            self._design_location_cus._condition_factors = filtered
        for r in value:
            if self not in r._condition_factors:
                r._condition_factors.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._condition_factors:
                obj._condition_factors.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._condition_factors:
                obj._condition_factors.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.condition_factors if q != self]
            self._design_locations._condition_factors = filtered
        for r in value:
            if self not in r._condition_factors:
                r._condition_factors.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._condition_factors:
                obj._condition_factors.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._condition_factors:
                obj._condition_factors.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations

    # <<< designs
    # @generated
    def get_designs(self):
        """ 
        """
        return self._designs

    def set_designs(self, value):
        for p in self._designs:
            filtered = [q for q in p.condition_factors if q != self]
            self._designs._condition_factors = filtered
        for r in value:
            if self not in r._condition_factors:
                r._condition_factors.append(self)
        self._designs = value

    designs = property(get_designs, set_designs)

    def add_designs(self, *designs):
        for obj in designs:
            if self not in obj._condition_factors:
                obj._condition_factors.append(self)
            self._designs.append(obj)

    def remove_designs(self, *designs):
        for obj in designs:
            if self in obj._condition_factors:
                obj._condition_factors.remove(self)
            self._designs.remove(obj)
    # >>> designs


    def __str__(self):
        """ Returns a string representation of the ConditionFactor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< condition_factor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConditionFactor.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConditionFactor", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:ConditionFactor.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.design_location_cus:
            s += '%s<%s:ConditionFactor.design_location_cus rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_locations:
            s += '%s<%s:ConditionFactor.design_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.designs:
            s += '%s<%s:ConditionFactor.designs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ConditionFactor.kind>%s</%s:ConditionFactor.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:ConditionFactor.cf_value>%s</%s:ConditionFactor.cf_value>' % \
            (indent, ns_prefix, self.cf_value, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConditionFactor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> condition_factor.serialize


class OneCallRequest(Document):
    """ A request for other utilities to mark their underground facilities prior to commencement of construction and/or maintenance.
    """
    # <<< one_call_request
    # @generated
    def __init__(self, marking_instruction='', marked_indicator=False, explosives_used=False, work_locations=None, **kw_args):
        """ Initialises a new 'OneCallRequest' instance.
        """
        # Instructions for marking a dig area, if applicable. 
        self.marking_instruction = marking_instruction

        # True if work location has been marked, for example for a dig area. 
        self.marked_indicator = marked_indicator

        # True if explosives have been or are planned to be used. 
        self.explosives_used = explosives_used


        self._work_locations = []
        if work_locations is not None:
            self.work_locations = work_locations
        else:
            self.work_locations = []


        super(OneCallRequest, self).__init__(**kw_args)
    # >>> one_call_request

    # <<< work_locations
    # @generated
    def get_work_locations(self):
        """ 
        """
        return self._work_locations

    def set_work_locations(self, value):
        for x in self._work_locations:
            x._one_call_request = None
        for y in value:
            y._one_call_request = self
        self._work_locations = value

    work_locations = property(get_work_locations, set_work_locations)

    def add_work_locations(self, *work_locations):
        for obj in work_locations:
            obj._one_call_request = self
            self._work_locations.append(obj)

    def remove_work_locations(self, *work_locations):
        for obj in work_locations:
            obj._one_call_request = None
            self._work_locations.remove(obj)
    # >>> work_locations


    def __str__(self):
        """ Returns a string representation of the OneCallRequest.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< one_call_request.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OneCallRequest.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OneCallRequest", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.work_locations:
            s += '%s<%s:OneCallRequest.work_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OneCallRequest.marking_instruction>%s</%s:OneCallRequest.marking_instruction>' % \
            (indent, ns_prefix, self.marking_instruction, ns_prefix)
        s += '%s<%s:OneCallRequest.marked_indicator>%s</%s:OneCallRequest.marked_indicator>' % \
            (indent, ns_prefix, self.marked_indicator, ns_prefix)
        s += '%s<%s:OneCallRequest.explosives_used>%s</%s:OneCallRequest.explosives_used>' % \
            (indent, ns_prefix, self.explosives_used, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OneCallRequest")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> one_call_request.serialize


class Assignment(Document):
    """ An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item, Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc. TimeSchedules may be set up directly for Assignments or indirectly via the associated WorkTask. Note that these associations are all inherited through the recursive relationship on Document.
    """
    # <<< assignment
    # @generated
    def __init__(self, crews=None, effective_period=None, **kw_args):
        """ Initialises a new 'Assignment' instance.
        """

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.effective_period = effective_period


        super(Assignment, self).__init__(**kw_args)
    # >>> assignment

    # <<< crews
    # @generated
    def get_crews(self):
        """ All Crews having this Assignment.
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.assignments if q != self]
            self._crews._assignments = filtered
        for r in value:
            if self not in r._assignments:
                r._assignments.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._assignments:
                obj._assignments.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._assignments:
                obj._assignments.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< effective_period
    # @generated
    # Period between the assignment becoming effective and its expiration.
    effective_period = None
    # >>> effective_period


    def __str__(self):
        """ Returns a string representation of the Assignment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< assignment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Assignment.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Assignment", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.crews:
            s += '%s<%s:Assignment.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.effective_period is not None:
            s += '%s<%s:Assignment.effective_period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.effective_period.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Assignment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> assignment.serialize


class QualificationRequirement(IdentifiedObject):
    """ Certain skills are required and must be certified in order for a person (typically a member of a crew) to be qualified to work on types of equipment.
    """
    # <<< qualification_requirement
    # @generated
    def __init__(self, qualification_id='', specifications=None, work_tasks=None, culabor_items=None, skills=None, **kw_args):
        """ Initialises a new 'QualificationRequirement' instance.
        """
        # Qualification identifier. 
        self.qualification_id = qualification_id


        self._specifications = []
        if specifications is not None:
            self.specifications = specifications
        else:
            self.specifications = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._culabor_items = []
        if culabor_items is not None:
            self.culabor_items = culabor_items
        else:
            self.culabor_items = []

        self._skills = []
        if skills is not None:
            self.skills = skills
        else:
            self.skills = []


        super(QualificationRequirement, self).__init__(**kw_args)
    # >>> qualification_requirement

    # <<< specifications
    # @generated
    def get_specifications(self):
        """ 
        """
        return self._specifications

    def set_specifications(self, value):
        for p in self._specifications:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._specifications._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._specifications = value

    specifications = property(get_specifications, set_specifications)

    def add_specifications(self, *specifications):
        for obj in specifications:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._specifications.append(obj)

    def remove_specifications(self, *specifications):
        for obj in specifications:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._specifications.remove(obj)
    # >>> specifications

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ 
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._work_tasks._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< culabor_items
    # @generated
    def get_culabor_items(self):
        """ 
        """
        return self._culabor_items

    def set_culabor_items(self, value):
        for p in self._culabor_items:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._culabor_items._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._culabor_items = value

    culabor_items = property(get_culabor_items, set_culabor_items)

    def add_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._culabor_items.append(obj)

    def remove_culabor_items(self, *culabor_items):
        for obj in culabor_items:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._culabor_items.remove(obj)
    # >>> culabor_items

    # <<< skills
    # @generated
    def get_skills(self):
        """ 
        """
        return self._skills

    def set_skills(self, value):
        for p in self._skills:
            filtered = [q for q in p.qualification_requirements if q != self]
            self._skills._qualification_requirements = filtered
        for r in value:
            if self not in r._qualification_requirements:
                r._qualification_requirements.append(self)
        self._skills = value

    skills = property(get_skills, set_skills)

    def add_skills(self, *skills):
        for obj in skills:
            if self not in obj._qualification_requirements:
                obj._qualification_requirements.append(self)
            self._skills.append(obj)

    def remove_skills(self, *skills):
        for obj in skills:
            if self in obj._qualification_requirements:
                obj._qualification_requirements.remove(self)
            self._skills.remove(obj)
    # >>> skills


    def __str__(self):
        """ Returns a string representation of the QualificationRequirement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< qualification_requirement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the QualificationRequirement.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "QualificationRequirement", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.specifications:
            s += '%s<%s:QualificationRequirement.specifications rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_tasks:
            s += '%s<%s:QualificationRequirement.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.culabor_items:
            s += '%s<%s:QualificationRequirement.culabor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.skills:
            s += '%s<%s:QualificationRequirement.skills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:QualificationRequirement.qualification_id>%s</%s:QualificationRequirement.qualification_id>' % \
            (indent, ns_prefix, self.qualification_id, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "QualificationRequirement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> qualification_requirement.serialize


class Crew(IdentifiedObject):
    """ A crew is a group of people (ErpPersons) with specific skills, tools, and vehicles.
    """
    # <<< crew
    # @generated
    def __init__(self, category='', capabilities=None, work_tasks=None, vehicles=None, crew_members=None, assignments=None, tools=None, route=None, outage_steps=None, work_equipment_assets=None, locations=None, shift_patterns=None, switching_schedules=None, organisations=None, **kw_args):
        """ Initialises a new 'Crew' instance.
        """
        # Category by utility's work management standards and practices. 
        self.category = category


        self._capabilities = []
        if capabilities is not None:
            self.capabilities = capabilities
        else:
            self.capabilities = []

        self._work_tasks = []
        if work_tasks is not None:
            self.work_tasks = work_tasks
        else:
            self.work_tasks = []

        self._vehicles = []
        if vehicles is not None:
            self.vehicles = vehicles
        else:
            self.vehicles = []

        self._crew_members = []
        if crew_members is not None:
            self.crew_members = crew_members
        else:
            self.crew_members = []

        self._assignments = []
        if assignments is not None:
            self.assignments = assignments
        else:
            self.assignments = []

        self._tools = []
        if tools is not None:
            self.tools = tools
        else:
            self.tools = []

        self._route = None
        self.route = route

        self._outage_steps = []
        if outage_steps is not None:
            self.outage_steps = outage_steps
        else:
            self.outage_steps = []

        self._work_equipment_assets = []
        if work_equipment_assets is not None:
            self.work_equipment_assets = work_equipment_assets
        else:
            self.work_equipment_assets = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._shift_patterns = []
        if shift_patterns is not None:
            self.shift_patterns = shift_patterns
        else:
            self.shift_patterns = []

        self._switching_schedules = []
        if switching_schedules is not None:
            self.switching_schedules = switching_schedules
        else:
            self.switching_schedules = []

        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []


        super(Crew, self).__init__(**kw_args)
    # >>> crew

    # <<< capabilities
    # @generated
    def get_capabilities(self):
        """ 
        """
        return self._capabilities

    def set_capabilities(self, value):
        for x in self._capabilities:
            x._crew = None
        for y in value:
            y._crew = self
        self._capabilities = value

    capabilities = property(get_capabilities, set_capabilities)

    def add_capabilities(self, *capabilities):
        for obj in capabilities:
            obj._crew = self
            self._capabilities.append(obj)

    def remove_capabilities(self, *capabilities):
        for obj in capabilities:
            obj._crew = None
            self._capabilities.remove(obj)
    # >>> capabilities

    # <<< work_tasks
    # @generated
    def get_work_tasks(self):
        """ All WorkTasks this Crew participates in.
        """
        return self._work_tasks

    def set_work_tasks(self, value):
        for p in self._work_tasks:
            filtered = [q for q in p.crews if q != self]
            self._work_tasks._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._work_tasks = value

    work_tasks = property(get_work_tasks, set_work_tasks)

    def add_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self not in obj._crews:
                obj._crews.append(self)
            self._work_tasks.append(obj)

    def remove_work_tasks(self, *work_tasks):
        for obj in work_tasks:
            if self in obj._crews:
                obj._crews.remove(self)
            self._work_tasks.remove(obj)
    # >>> work_tasks

    # <<< vehicles
    # @generated
    def get_vehicles(self):
        """ 
        """
        return self._vehicles

    def set_vehicles(self, value):
        for x in self._vehicles:
            x._crew = None
        for y in value:
            y._crew = self
        self._vehicles = value

    vehicles = property(get_vehicles, set_vehicles)

    def add_vehicles(self, *vehicles):
        for obj in vehicles:
            obj._crew = self
            self._vehicles.append(obj)

    def remove_vehicles(self, *vehicles):
        for obj in vehicles:
            obj._crew = None
            self._vehicles.remove(obj)
    # >>> vehicles

    # <<< crew_members
    # @generated
    def get_crew_members(self):
        """ All ErpPersons that are members of this Crew.
        """
        return self._crew_members

    def set_crew_members(self, value):
        for p in self._crew_members:
            filtered = [q for q in p.crews if q != self]
            self._crew_members._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._crew_members = value

    crew_members = property(get_crew_members, set_crew_members)

    def add_crew_members(self, *crew_members):
        for obj in crew_members:
            if self not in obj._crews:
                obj._crews.append(self)
            self._crew_members.append(obj)

    def remove_crew_members(self, *crew_members):
        for obj in crew_members:
            if self in obj._crews:
                obj._crews.remove(self)
            self._crew_members.remove(obj)
    # >>> crew_members

    # <<< assignments
    # @generated
    def get_assignments(self):
        """ All Assignments for this Crew.
        """
        return self._assignments

    def set_assignments(self, value):
        for p in self._assignments:
            filtered = [q for q in p.crews if q != self]
            self._assignments._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._assignments = value

    assignments = property(get_assignments, set_assignments)

    def add_assignments(self, *assignments):
        for obj in assignments:
            if self not in obj._crews:
                obj._crews.append(self)
            self._assignments.append(obj)

    def remove_assignments(self, *assignments):
        for obj in assignments:
            if self in obj._crews:
                obj._crews.remove(self)
            self._assignments.remove(obj)
    # >>> assignments

    # <<< tools
    # @generated
    def get_tools(self):
        """ 
        """
        return self._tools

    def set_tools(self, value):
        for x in self._tools:
            x._crew = None
        for y in value:
            y._crew = self
        self._tools = value

    tools = property(get_tools, set_tools)

    def add_tools(self, *tools):
        for obj in tools:
            obj._crew = self
            self._tools.append(obj)

    def remove_tools(self, *tools):
        for obj in tools:
            obj._crew = None
            self._tools.remove(obj)
    # >>> tools

    # <<< route
    # @generated
    def get_route(self):
        """ 
        """
        return self._route

    def set_route(self, value):
        if self._route is not None:
            filtered = [x for x in self.route.crews if x != self]
            self._route._crews = filtered

        self._route = value
        if self._route is not None:
            self._route._crews.append(self)

    route = property(get_route, set_route)
    # >>> route

    # <<< outage_steps
    # @generated
    def get_outage_steps(self):
        """ 
        """
        return self._outage_steps

    def set_outage_steps(self, value):
        for p in self._outage_steps:
            filtered = [q for q in p.crews if q != self]
            self._outage_steps._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._outage_steps = value

    outage_steps = property(get_outage_steps, set_outage_steps)

    def add_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            if self not in obj._crews:
                obj._crews.append(self)
            self._outage_steps.append(obj)

    def remove_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            if self in obj._crews:
                obj._crews.remove(self)
            self._outage_steps.remove(obj)
    # >>> outage_steps

    # <<< work_equipment_assets
    # @generated
    def get_work_equipment_assets(self):
        """ 
        """
        return self._work_equipment_assets

    def set_work_equipment_assets(self, value):
        for x in self._work_equipment_assets:
            x._crew = None
        for y in value:
            y._crew = self
        self._work_equipment_assets = value

    work_equipment_assets = property(get_work_equipment_assets, set_work_equipment_assets)

    def add_work_equipment_assets(self, *work_equipment_assets):
        for obj in work_equipment_assets:
            obj._crew = self
            self._work_equipment_assets.append(obj)

    def remove_work_equipment_assets(self, *work_equipment_assets):
        for obj in work_equipment_assets:
            obj._crew = None
            self._work_equipment_assets.remove(obj)
    # >>> work_equipment_assets

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.crews if q != self]
            self._locations._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._crews:
                obj._crews.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._crews:
                obj._crews.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< shift_patterns
    # @generated
    def get_shift_patterns(self):
        """ 
        """
        return self._shift_patterns

    def set_shift_patterns(self, value):
        for p in self._shift_patterns:
            filtered = [q for q in p.crews if q != self]
            self._shift_patterns._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._shift_patterns = value

    shift_patterns = property(get_shift_patterns, set_shift_patterns)

    def add_shift_patterns(self, *shift_patterns):
        for obj in shift_patterns:
            if self not in obj._crews:
                obj._crews.append(self)
            self._shift_patterns.append(obj)

    def remove_shift_patterns(self, *shift_patterns):
        for obj in shift_patterns:
            if self in obj._crews:
                obj._crews.remove(self)
            self._shift_patterns.remove(obj)
    # >>> shift_patterns

    # <<< switching_schedules
    # @generated
    def get_switching_schedules(self):
        """ All SwitchingSchedules executed by this Crew.
        """
        return self._switching_schedules

    def set_switching_schedules(self, value):
        for p in self._switching_schedules:
            filtered = [q for q in p.crews if q != self]
            self._switching_schedules._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._switching_schedules = value

    switching_schedules = property(get_switching_schedules, set_switching_schedules)

    def add_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            if self not in obj._crews:
                obj._crews.append(self)
            self._switching_schedules.append(obj)

    def remove_switching_schedules(self, *switching_schedules):
        for obj in switching_schedules:
            if self in obj._crews:
                obj._crews.remove(self)
            self._switching_schedules.remove(obj)
    # >>> switching_schedules

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.crews if q != self]
            self._organisations._crews = filtered
        for r in value:
            if self not in r._crews:
                r._crews.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._crews:
                obj._crews.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._crews:
                obj._crews.remove(self)
            self._organisations.remove(obj)
    # >>> organisations


    def __str__(self):
        """ Returns a string representation of the Crew.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< crew.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Crew.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Crew", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.capabilities:
            s += '%s<%s:Crew.capabilities rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_tasks:
            s += '%s<%s:Crew.work_tasks rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.vehicles:
            s += '%s<%s:Crew.vehicles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crew_members:
            s += '%s<%s:Crew.crew_members rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.assignments:
            s += '%s<%s:Crew.assignments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.tools:
            s += '%s<%s:Crew.tools rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.route is not None:
            s += '%s<%s:Crew.route rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.route.uri)
        for obj in self.outage_steps:
            s += '%s<%s:Crew.outage_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.work_equipment_assets:
            s += '%s<%s:Crew.work_equipment_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:Crew.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.shift_patterns:
            s += '%s<%s:Crew.shift_patterns rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.switching_schedules:
            s += '%s<%s:Crew.switching_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.organisations:
            s += '%s<%s:Crew.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Crew.category>%s</%s:Crew.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Crew")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> crew.serialize


class DiagnosisDataSet(ProcedureDataSet):
    """ The result of a problem (typically an asset failure) diagnosis.
    """
    # <<< diagnosis_data_set
    # @generated
    def __init__(self, phase_code='abc', failure_mode='', root_remark='', root_cause='', final_origin='', final_cause='', preliminary_code='', effect='', preliminary_remark='', root_origin='', final_code='', final_remark='', preliminary_date_time='', **kw_args):
        """ Initialises a new 'DiagnosisDataSet' instance.
        """
        # Phase(s) diagnosed. Values are: "abc", "ab", "b", "bc", "ac", "split_secondary1_n", "abn", "abcn", "cn", "an", "split_secondary12_n", "bcn", "split_secondary2_n", "acn", "a", "c", "n", "bn"
        self.phase_code = 'abc'

        # Failuer mode, for example: Failure to Insulate; Failure to conduct; Failure to contain oil; Failure to provide ground plane; Other. 
        self.failure_mode = failure_mode

        # Remarks pertaining to root cause findings during problem diagnosis. 
        self.root_remark = root_remark

        # Root cause of problem determined during diagnosis. 
        self.root_cause = root_cause

        # Origin of problem determined during diagnosis. 
        self.final_origin = final_origin

        # Cause of problem determined during diagnosis. 
        self.final_cause = final_cause

        # Code for problem category determined during preliminary assessment. 
        self.preliminary_code = preliminary_code

        # Effect of problem. 
        self.effect = effect

        # Remarks pertaining to preliminary assessment of problem. 
        self.preliminary_remark = preliminary_remark

        # Root origin of problem determined during diagnosis. 
        self.root_origin = root_origin

        # Code for diagnosed probem category. 
        self.final_code = final_code

        # Remarks pertaining to findings during problem diagnosis. 
        self.final_remark = final_remark

        # Date and time preliminary assessment of problem was performed. 
        self.preliminary_date_time = preliminary_date_time



        super(DiagnosisDataSet, self).__init__(**kw_args)
    # >>> diagnosis_data_set


    def __str__(self):
        """ Returns a string representation of the DiagnosisDataSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< diagnosis_data_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DiagnosisDataSet.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DiagnosisDataSet", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:DiagnosisDataSet.phase_code>%s</%s:DiagnosisDataSet.phase_code>' % \
            (indent, ns_prefix, self.phase_code, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.failure_mode>%s</%s:DiagnosisDataSet.failure_mode>' % \
            (indent, ns_prefix, self.failure_mode, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.root_remark>%s</%s:DiagnosisDataSet.root_remark>' % \
            (indent, ns_prefix, self.root_remark, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.root_cause>%s</%s:DiagnosisDataSet.root_cause>' % \
            (indent, ns_prefix, self.root_cause, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.final_origin>%s</%s:DiagnosisDataSet.final_origin>' % \
            (indent, ns_prefix, self.final_origin, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.final_cause>%s</%s:DiagnosisDataSet.final_cause>' % \
            (indent, ns_prefix, self.final_cause, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.preliminary_code>%s</%s:DiagnosisDataSet.preliminary_code>' % \
            (indent, ns_prefix, self.preliminary_code, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.effect>%s</%s:DiagnosisDataSet.effect>' % \
            (indent, ns_prefix, self.effect, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.preliminary_remark>%s</%s:DiagnosisDataSet.preliminary_remark>' % \
            (indent, ns_prefix, self.preliminary_remark, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.root_origin>%s</%s:DiagnosisDataSet.root_origin>' % \
            (indent, ns_prefix, self.root_origin, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.final_code>%s</%s:DiagnosisDataSet.final_code>' % \
            (indent, ns_prefix, self.final_code, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.final_remark>%s</%s:DiagnosisDataSet.final_remark>' % \
            (indent, ns_prefix, self.final_remark, ns_prefix)
        s += '%s<%s:DiagnosisDataSet.preliminary_date_time>%s</%s:DiagnosisDataSet.preliminary_date_time>' % \
            (indent, ns_prefix, self.preliminary_date_time, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
        if self.procedure is not None:
            s += '%s<%s:ProcedureDataSet.procedure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.procedure.uri)
        for obj in self.properties:
            s += '%s<%s:ProcedureDataSet.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurement_values:
            s += '%s<%s:ProcedureDataSet.measurement_values rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transformer_observations:
            s += '%s<%s:ProcedureDataSet.transformer_observations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProcedureDataSet.completed_date_time>%s</%s:ProcedureDataSet.completed_date_time>' % \
            (indent, ns_prefix, self.completed_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DiagnosisDataSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> diagnosis_data_set.serialize


class ContractorItem(IdentifiedObject):
    """ Contractor information for work task.
    """
    # <<< contractor_item
    # @generated
    def __init__(self, cost=0.0, bid_amount=0.0, activity_code='', work_task=None, work_cost_detail=None, erp_payables=None, status=None, **kw_args):
        """ Initialises a new 'ContractorItem' instance.
        """
        # The total amount charged. 
        self.cost = cost

        # The amount that a given contractor will charge for performing this unit of work. 
        self.bid_amount = bid_amount

        # Activity code identifies a specific and distinguishable unit of work. 
        self.activity_code = activity_code


        self._work_task = None
        self.work_task = work_task

        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._erp_payables = []
        if erp_payables is not None:
            self.erp_payables = erp_payables
        else:
            self.erp_payables = []

        self.status = status


        super(ContractorItem, self).__init__(**kw_args)
    # >>> contractor_item

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.contractor_items if x != self]
            self._work_task._contractor_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._contractor_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.contractor_items if x != self]
            self._work_cost_detail._contractor_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._contractor_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< erp_payables
    # @generated
    def get_erp_payables(self):
        """ 
        """
        return self._erp_payables

    def set_erp_payables(self, value):
        for p in self._erp_payables:
            filtered = [q for q in p.contractor_items if q != self]
            self._erp_payables._contractor_items = filtered
        for r in value:
            if self not in r._contractor_items:
                r._contractor_items.append(self)
        self._erp_payables = value

    erp_payables = property(get_erp_payables, set_erp_payables)

    def add_erp_payables(self, *erp_payables):
        for obj in erp_payables:
            if self not in obj._contractor_items:
                obj._contractor_items.append(self)
            self._erp_payables.append(obj)

    def remove_erp_payables(self, *erp_payables):
        for obj in erp_payables:
            if self in obj._contractor_items:
                obj._contractor_items.remove(self)
            self._erp_payables.remove(obj)
    # >>> erp_payables

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ContractorItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< contractor_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ContractorItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ContractorItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.work_task is not None:
            s += '%s<%s:ContractorItem.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        if self.work_cost_detail is not None:
            s += '%s<%s:ContractorItem.work_cost_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_detail.uri)
        for obj in self.erp_payables:
            s += '%s<%s:ContractorItem.erp_payables rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ContractorItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ContractorItem.cost>%s</%s:ContractorItem.cost>' % \
            (indent, ns_prefix, self.cost, ns_prefix)
        s += '%s<%s:ContractorItem.bid_amount>%s</%s:ContractorItem.bid_amount>' % \
            (indent, ns_prefix, self.bid_amount, ns_prefix)
        s += '%s<%s:ContractorItem.activity_code>%s</%s:ContractorItem.activity_code>' % \
            (indent, ns_prefix, self.activity_code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ContractorItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> contractor_item.serialize


class CUGroup(IdentifiedObject):
    """ A Compatible Unit Group identifies a set of compatible units which may be jointly utilized for estimating and designating jobs.
    """
    # <<< cugroup
    # @generated
    def __init__(self, parent_cugroups=None, child_cugroups=None, design_location_cus=None, status=None, compatible_units=None, **kw_args):
        """ Initialises a new 'CUGroup' instance.
        """

        self._parent_cugroups = []
        if parent_cugroups is not None:
            self.parent_cugroups = parent_cugroups
        else:
            self.parent_cugroups = []

        self._child_cugroups = []
        if child_cugroups is not None:
            self.child_cugroups = child_cugroups
        else:
            self.child_cugroups = []

        self._design_location_cus = []
        if design_location_cus is not None:
            self.design_location_cus = design_location_cus
        else:
            self.design_location_cus = []

        self.status = status

        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []


        super(CUGroup, self).__init__(**kw_args)
    # >>> cugroup

    # <<< parent_cugroups
    # @generated
    def get_parent_cugroups(self):
        """ 
        """
        return self._parent_cugroups

    def set_parent_cugroups(self, value):
        for p in self._parent_cugroups:
            filtered = [q for q in p.child_cugroups if q != self]
            self._parent_cugroups._child_cugroups = filtered
        for r in value:
            if self not in r._child_cugroups:
                r._child_cugroups.append(self)
        self._parent_cugroups = value

    parent_cugroups = property(get_parent_cugroups, set_parent_cugroups)

    def add_parent_cugroups(self, *parent_cugroups):
        for obj in parent_cugroups:
            if self not in obj._child_cugroups:
                obj._child_cugroups.append(self)
            self._parent_cugroups.append(obj)

    def remove_parent_cugroups(self, *parent_cugroups):
        for obj in parent_cugroups:
            if self in obj._child_cugroups:
                obj._child_cugroups.remove(self)
            self._parent_cugroups.remove(obj)
    # >>> parent_cugroups

    # <<< child_cugroups
    # @generated
    def get_child_cugroups(self):
        """ 
        """
        return self._child_cugroups

    def set_child_cugroups(self, value):
        for p in self._child_cugroups:
            filtered = [q for q in p.parent_cugroups if q != self]
            self._child_cugroups._parent_cugroups = filtered
        for r in value:
            if self not in r._parent_cugroups:
                r._parent_cugroups.append(self)
        self._child_cugroups = value

    child_cugroups = property(get_child_cugroups, set_child_cugroups)

    def add_child_cugroups(self, *child_cugroups):
        for obj in child_cugroups:
            if self not in obj._parent_cugroups:
                obj._parent_cugroups.append(self)
            self._child_cugroups.append(obj)

    def remove_child_cugroups(self, *child_cugroups):
        for obj in child_cugroups:
            if self in obj._parent_cugroups:
                obj._parent_cugroups.remove(self)
            self._child_cugroups.remove(obj)
    # >>> child_cugroups

    # <<< design_location_cus
    # @generated
    def get_design_location_cus(self):
        """ 
        """
        return self._design_location_cus

    def set_design_location_cus(self, value):
        for p in self._design_location_cus:
            filtered = [q for q in p.cugroups if q != self]
            self._design_location_cus._cugroups = filtered
        for r in value:
            if self not in r._cugroups:
                r._cugroups.append(self)
        self._design_location_cus = value

    design_location_cus = property(get_design_location_cus, set_design_location_cus)

    def add_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self not in obj._cugroups:
                obj._cugroups.append(self)
            self._design_location_cus.append(obj)

    def remove_design_location_cus(self, *design_location_cus):
        for obj in design_location_cus:
            if self in obj._cugroups:
                obj._cugroups.remove(self)
            self._design_location_cus.remove(obj)
    # >>> design_location_cus

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for x in self._compatible_units:
            x._cugroup = None
        for y in value:
            y._cugroup = self
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cugroup = self
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            obj._cugroup = None
            self._compatible_units.remove(obj)
    # >>> compatible_units


    def __str__(self):
        """ Returns a string representation of the CUGroup.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cugroup.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CUGroup.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CUGroup", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.parent_cugroups:
            s += '%s<%s:CUGroup.parent_cugroups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.child_cugroups:
            s += '%s<%s:CUGroup.child_cugroups rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_location_cus:
            s += '%s<%s:CUGroup.design_location_cus rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:CUGroup.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.compatible_units:
            s += '%s<%s:CUGroup.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CUGroup")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cugroup.serialize


class CUWorkEquipmentItem(IdentifiedObject):
    """ Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    """
    # <<< cuwork_equipment_item
    # @generated
    def __init__(self, equip_code='', rate=0.0, compatible_units=None, type_asset=None, status=None, **kw_args):
        """ Initialises a new 'CUWorkEquipmentItem' instance.
        """
        # The equipment type code. 
        self.equip_code = equip_code

        # Standard usage rate for the type of vehicle. 
        self.rate = rate


        self._compatible_units = []
        if compatible_units is not None:
            self.compatible_units = compatible_units
        else:
            self.compatible_units = []

        self._type_asset = None
        self.type_asset = type_asset

        self.status = status


        super(CUWorkEquipmentItem, self).__init__(**kw_args)
    # >>> cuwork_equipment_item

    # <<< compatible_units
    # @generated
    def get_compatible_units(self):
        """ 
        """
        return self._compatible_units

    def set_compatible_units(self, value):
        for p in self._compatible_units:
            filtered = [q for q in p.cuwork_equipment_items if q != self]
            self._compatible_units._cuwork_equipment_items = filtered
        for r in value:
            if self not in r._cuwork_equipment_items:
                r._cuwork_equipment_items.append(self)
        self._compatible_units = value

    compatible_units = property(get_compatible_units, set_compatible_units)

    def add_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self not in obj._cuwork_equipment_items:
                obj._cuwork_equipment_items.append(self)
            self._compatible_units.append(obj)

    def remove_compatible_units(self, *compatible_units):
        for obj in compatible_units:
            if self in obj._cuwork_equipment_items:
                obj._cuwork_equipment_items.remove(self)
            self._compatible_units.remove(obj)
    # >>> compatible_units

    # <<< type_asset
    # @generated
    def get_type_asset(self):
        """ 
        """
        return self._type_asset

    def set_type_asset(self, value):
        if self._type_asset is not None:
            self._type_asset._cuwork_equipment_asset = None

        self._type_asset = value
        if self._type_asset is not None:
            self._type_asset._cuwork_equipment_asset = self

    type_asset = property(get_type_asset, set_type_asset)
    # >>> type_asset

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the CUWorkEquipmentItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cuwork_equipment_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CUWorkEquipmentItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CUWorkEquipmentItem", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.compatible_units:
            s += '%s<%s:CUWorkEquipmentItem.compatible_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.type_asset is not None:
            s += '%s<%s:CUWorkEquipmentItem.type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.type_asset.uri)
        if self.status is not None:
            s += '%s<%s:CUWorkEquipmentItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:CUWorkEquipmentItem.equip_code>%s</%s:CUWorkEquipmentItem.equip_code>' % \
            (indent, ns_prefix, self.equip_code, ns_prefix)
        s += '%s<%s:CUWorkEquipmentItem.rate>%s</%s:CUWorkEquipmentItem.rate>' % \
            (indent, ns_prefix, self.rate, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CUWorkEquipmentItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cuwork_equipment_item.serialize


class WorkLocation(Location):
    """ Information about a particular location for various forms of work such as a one call request.
    """
    # <<< work_location
    # @generated
    def __init__(self, block='', nearest_intersection='', subdivision='', lot='', one_call_request=None, design_locations=None, **kw_args):
        """ Initialises a new 'WorkLocation' instance.
        """
        # Name, identifier, or description of the block, if applicable, in which work is to occur. 
        self.block = block

        # The names of streets at the nearest intersection to work area. 
        self.nearest_intersection = nearest_intersection

        # Name, identifier, or description of the subdivision, if applicable, in which work is to occur. 
        self.subdivision = subdivision

        # Name, identifier, or description of the lot, if applicable, in which work is to occur. 
        self.lot = lot


        self._one_call_request = None
        self.one_call_request = one_call_request

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []


        super(WorkLocation, self).__init__(**kw_args)
    # >>> work_location

    # <<< one_call_request
    # @generated
    def get_one_call_request(self):
        """ 
        """
        return self._one_call_request

    def set_one_call_request(self, value):
        if self._one_call_request is not None:
            filtered = [x for x in self.one_call_request.work_locations if x != self]
            self._one_call_request._work_locations = filtered

        self._one_call_request = value
        if self._one_call_request is not None:
            self._one_call_request._work_locations.append(self)

    one_call_request = property(get_one_call_request, set_one_call_request)
    # >>> one_call_request

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.work_locations if q != self]
            self._design_locations._work_locations = filtered
        for r in value:
            if self not in r._work_locations:
                r._work_locations.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._work_locations:
                obj._work_locations.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._work_locations:
                obj._work_locations.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations


    def __str__(self):
        """ Returns a string representation of the WorkLocation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkLocation.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkLocation", self.uri)
        if format:
            indent += ' ' * depth

        if self.one_call_request is not None:
            s += '%s<%s:WorkLocation.one_call_request rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.one_call_request.uri)
        for obj in self.design_locations:
            s += '%s<%s:WorkLocation.design_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:WorkLocation.block>%s</%s:WorkLocation.block>' % \
            (indent, ns_prefix, self.block, ns_prefix)
        s += '%s<%s:WorkLocation.nearest_intersection>%s</%s:WorkLocation.nearest_intersection>' % \
            (indent, ns_prefix, self.nearest_intersection, ns_prefix)
        s += '%s<%s:WorkLocation.subdivision>%s</%s:WorkLocation.subdivision>' % \
            (indent, ns_prefix, self.subdivision, ns_prefix)
        s += '%s<%s:WorkLocation.lot>%s</%s:WorkLocation.lot>' % \
            (indent, ns_prefix, self.lot, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkLocation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_location.serialize


class WorkCostDetail(Document):
    """ A collection of all of the individual cost items collected from multiple sources.
    """
    # <<< work_cost_detail
    # @generated
    def __init__(self, amount=0.0, is_debit=False, transaction_date_time='', type='', overhead_cost=None, work_task=None, labor_items=None, erp_project_accounting=None, equipment_items=None, work_cost_summary=None, design=None, misc_cost_items=None, cost_type=None, works=None, contractor_items=None, material_items=None, property_units=None, **kw_args):
        """ Initialises a new 'WorkCostDetail' instance.
        """
        # Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other. 
        self.amount = amount

        # True if 'amount' is a debit, false if it is a credit. 
        self.is_debit = is_debit

        # Date and time that 'amount' is posted to the work. 
        self.transaction_date_time = transaction_date_time

        # Type of work cost. 
        self.type = type


        self._overhead_cost = None
        self.overhead_cost = overhead_cost

        self._work_task = None
        self.work_task = work_task

        self._labor_items = []
        if labor_items is not None:
            self.labor_items = labor_items
        else:
            self.labor_items = []

        self._erp_project_accounting = None
        self.erp_project_accounting = erp_project_accounting

        self._equipment_items = []
        if equipment_items is not None:
            self.equipment_items = equipment_items
        else:
            self.equipment_items = []

        self._work_cost_summary = None
        self.work_cost_summary = work_cost_summary

        self._design = None
        self.design = design

        self._misc_cost_items = []
        if misc_cost_items is not None:
            self.misc_cost_items = misc_cost_items
        else:
            self.misc_cost_items = []

        self._cost_type = None
        self.cost_type = cost_type

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._contractor_items = []
        if contractor_items is not None:
            self.contractor_items = contractor_items
        else:
            self.contractor_items = []

        self._material_items = []
        if material_items is not None:
            self.material_items = material_items
        else:
            self.material_items = []

        self._property_units = []
        if property_units is not None:
            self.property_units = property_units
        else:
            self.property_units = []


        super(WorkCostDetail, self).__init__(**kw_args)
    # >>> work_cost_detail

    # <<< overhead_cost
    # @generated
    def get_overhead_cost(self):
        """ 
        """
        return self._overhead_cost

    def set_overhead_cost(self, value):
        if self._overhead_cost is not None:
            filtered = [x for x in self.overhead_cost.work_cost_details if x != self]
            self._overhead_cost._work_cost_details = filtered

        self._overhead_cost = value
        if self._overhead_cost is not None:
            self._overhead_cost._work_cost_details.append(self)

    overhead_cost = property(get_overhead_cost, set_overhead_cost)
    # >>> overhead_cost

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.work_cost_details if x != self]
            self._work_task._work_cost_details = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._work_cost_details.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< labor_items
    # @generated
    def get_labor_items(self):
        """ 
        """
        return self._labor_items

    def set_labor_items(self, value):
        for x in self._labor_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._labor_items = value

    labor_items = property(get_labor_items, set_labor_items)

    def add_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_cost_detail = self
            self._labor_items.append(obj)

    def remove_labor_items(self, *labor_items):
        for obj in labor_items:
            obj._work_cost_detail = None
            self._labor_items.remove(obj)
    # >>> labor_items

    # <<< erp_project_accounting
    # @generated
    def get_erp_project_accounting(self):
        """ 
        """
        return self._erp_project_accounting

    def set_erp_project_accounting(self, value):
        if self._erp_project_accounting is not None:
            filtered = [x for x in self.erp_project_accounting.work_cost_details if x != self]
            self._erp_project_accounting._work_cost_details = filtered

        self._erp_project_accounting = value
        if self._erp_project_accounting is not None:
            self._erp_project_accounting._work_cost_details.append(self)

    erp_project_accounting = property(get_erp_project_accounting, set_erp_project_accounting)
    # >>> erp_project_accounting

    # <<< equipment_items
    # @generated
    def get_equipment_items(self):
        """ 
        """
        return self._equipment_items

    def set_equipment_items(self, value):
        for x in self._equipment_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._equipment_items = value

    equipment_items = property(get_equipment_items, set_equipment_items)

    def add_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_cost_detail = self
            self._equipment_items.append(obj)

    def remove_equipment_items(self, *equipment_items):
        for obj in equipment_items:
            obj._work_cost_detail = None
            self._equipment_items.remove(obj)
    # >>> equipment_items

    # <<< work_cost_summary
    # @generated
    def get_work_cost_summary(self):
        """ 
        """
        return self._work_cost_summary

    def set_work_cost_summary(self, value):
        if self._work_cost_summary is not None:
            self._work_cost_summary._work_cost_detail = None

        self._work_cost_summary = value
        if self._work_cost_summary is not None:
            self._work_cost_summary._work_cost_detail = self

    work_cost_summary = property(get_work_cost_summary, set_work_cost_summary)
    # >>> work_cost_summary

    # <<< design
    # @generated
    def get_design(self):
        """ 
        """
        return self._design

    def set_design(self, value):
        if self._design is not None:
            filtered = [x for x in self.design.work_cost_details if x != self]
            self._design._work_cost_details = filtered

        self._design = value
        if self._design is not None:
            self._design._work_cost_details.append(self)

    design = property(get_design, set_design)
    # >>> design

    # <<< misc_cost_items
    # @generated
    def get_misc_cost_items(self):
        """ 
        """
        return self._misc_cost_items

    def set_misc_cost_items(self, value):
        for x in self._misc_cost_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._misc_cost_items = value

    misc_cost_items = property(get_misc_cost_items, set_misc_cost_items)

    def add_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_cost_detail = self
            self._misc_cost_items.append(obj)

    def remove_misc_cost_items(self, *misc_cost_items):
        for obj in misc_cost_items:
            obj._work_cost_detail = None
            self._misc_cost_items.remove(obj)
    # >>> misc_cost_items

    # <<< cost_type
    # @generated
    def get_cost_type(self):
        """ 
        """
        return self._cost_type

    def set_cost_type(self, value):
        if self._cost_type is not None:
            filtered = [x for x in self.cost_type.work_cost_details if x != self]
            self._cost_type._work_cost_details = filtered

        self._cost_type = value
        if self._cost_type is not None:
            self._cost_type._work_cost_details.append(self)

    cost_type = property(get_cost_type, set_cost_type)
    # >>> cost_type

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for p in self._works:
            filtered = [q for q in p.work_cost_details if q != self]
            self._works._work_cost_details = filtered
        for r in value:
            if self not in r._work_cost_details:
                r._work_cost_details.append(self)
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            if self not in obj._work_cost_details:
                obj._work_cost_details.append(self)
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            if self in obj._work_cost_details:
                obj._work_cost_details.remove(self)
            self._works.remove(obj)
    # >>> works

    # <<< contractor_items
    # @generated
    def get_contractor_items(self):
        """ 
        """
        return self._contractor_items

    def set_contractor_items(self, value):
        for x in self._contractor_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._contractor_items = value

    contractor_items = property(get_contractor_items, set_contractor_items)

    def add_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_cost_detail = self
            self._contractor_items.append(obj)

    def remove_contractor_items(self, *contractor_items):
        for obj in contractor_items:
            obj._work_cost_detail = None
            self._contractor_items.remove(obj)
    # >>> contractor_items

    # <<< material_items
    # @generated
    def get_material_items(self):
        """ 
        """
        return self._material_items

    def set_material_items(self, value):
        for x in self._material_items:
            x._work_cost_detail = None
        for y in value:
            y._work_cost_detail = self
        self._material_items = value

    material_items = property(get_material_items, set_material_items)

    def add_material_items(self, *material_items):
        for obj in material_items:
            obj._work_cost_detail = self
            self._material_items.append(obj)

    def remove_material_items(self, *material_items):
        for obj in material_items:
            obj._work_cost_detail = None
            self._material_items.remove(obj)
    # >>> material_items

    # <<< property_units
    # @generated
    def get_property_units(self):
        """ 
        """
        return self._property_units

    def set_property_units(self, value):
        for p in self._property_units:
            filtered = [q for q in p.work_cost_details if q != self]
            self._property_units._work_cost_details = filtered
        for r in value:
            if self not in r._work_cost_details:
                r._work_cost_details.append(self)
        self._property_units = value

    property_units = property(get_property_units, set_property_units)

    def add_property_units(self, *property_units):
        for obj in property_units:
            if self not in obj._work_cost_details:
                obj._work_cost_details.append(self)
            self._property_units.append(obj)

    def remove_property_units(self, *property_units):
        for obj in property_units:
            if self in obj._work_cost_details:
                obj._work_cost_details.remove(self)
            self._property_units.remove(obj)
    # >>> property_units


    def __str__(self):
        """ Returns a string representation of the WorkCostDetail.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_cost_detail.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkCostDetail.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkCostDetail", self.uri)
        if format:
            indent += ' ' * depth

        if self.overhead_cost is not None:
            s += '%s<%s:WorkCostDetail.overhead_cost rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.overhead_cost.uri)
        if self.work_task is not None:
            s += '%s<%s:WorkCostDetail.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.labor_items:
            s += '%s<%s:WorkCostDetail.labor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_project_accounting is not None:
            s += '%s<%s:WorkCostDetail.erp_project_accounting rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_project_accounting.uri)
        for obj in self.equipment_items:
            s += '%s<%s:WorkCostDetail.equipment_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_cost_summary is not None:
            s += '%s<%s:WorkCostDetail.work_cost_summary rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_summary.uri)
        if self.design is not None:
            s += '%s<%s:WorkCostDetail.design rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.design.uri)
        for obj in self.misc_cost_items:
            s += '%s<%s:WorkCostDetail.misc_cost_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.cost_type is not None:
            s += '%s<%s:WorkCostDetail.cost_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cost_type.uri)
        for obj in self.works:
            s += '%s<%s:WorkCostDetail.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contractor_items:
            s += '%s<%s:WorkCostDetail.contractor_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.material_items:
            s += '%s<%s:WorkCostDetail.material_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.property_units:
            s += '%s<%s:WorkCostDetail.property_units rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:WorkCostDetail.amount>%s</%s:WorkCostDetail.amount>' % \
            (indent, ns_prefix, self.amount, ns_prefix)
        s += '%s<%s:WorkCostDetail.is_debit>%s</%s:WorkCostDetail.is_debit>' % \
            (indent, ns_prefix, self.is_debit, ns_prefix)
        s += '%s<%s:WorkCostDetail.transaction_date_time>%s</%s:WorkCostDetail.transaction_date_time>' % \
            (indent, ns_prefix, self.transaction_date_time, ns_prefix)
        s += '%s<%s:WorkCostDetail.type>%s</%s:WorkCostDetail.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkCostDetail")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_cost_detail.serialize


class EquipmentItem(IdentifiedObject):
    """ An equipment item, such as a vehicle, used for a work order.
    """
    # <<< equipment_item
    # @generated
    def __init__(self, cost=0.0, code='', work_cost_detail=None, work_task=None, status=None, **kw_args):
        """ Initialises a new 'EquipmentItem' instance.
        """
        # The cost for vehicle usage. 
        self.cost = cost

        # Code for type of vehicle. 
        self.code = code


        self._work_cost_detail = None
        self.work_cost_detail = work_cost_detail

        self._work_task = None
        self.work_task = work_task

        self.status = status


        super(EquipmentItem, self).__init__(**kw_args)
    # >>> equipment_item

    # <<< work_cost_detail
    # @generated
    def get_work_cost_detail(self):
        """ 
        """
        return self._work_cost_detail

    def set_work_cost_detail(self, value):
        if self._work_cost_detail is not None:
            filtered = [x for x in self.work_cost_detail.equipment_items if x != self]
            self._work_cost_detail._equipment_items = filtered

        self._work_cost_detail = value
        if self._work_cost_detail is not None:
            self._work_cost_detail._equipment_items.append(self)

    work_cost_detail = property(get_work_cost_detail, set_work_cost_detail)
    # >>> work_cost_detail

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.equipment_items if x != self]
            self._work_task._equipment_items = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._equipment_items.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the EquipmentItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< equipment_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EquipmentItem.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EquipmentItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.work_cost_detail is not None:
            s += '%s<%s:EquipmentItem.work_cost_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_cost_detail.uri)
        if self.work_task is not None:
            s += '%s<%s:EquipmentItem.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        if self.status is not None:
            s += '%s<%s:EquipmentItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:EquipmentItem.cost>%s</%s:EquipmentItem.cost>' % \
            (indent, ns_prefix, self.cost, ns_prefix)
        s += '%s<%s:EquipmentItem.code>%s</%s:EquipmentItem.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EquipmentItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> equipment_item.serialize


class BusinessCase(Document):
    """ Business justification for capital expenditures, usually addressing operations and maintenance costs as well.
    """
    # <<< business_case
    # @generated
    def __init__(self, corporate_code='', works=None, projects=None, **kw_args):
        """ Initialises a new 'BusinessCase' instance.
        """
        # A codified representation of the business case (i.e., codes for highway relocation, replace substation transformers, etc.). 
        self.corporate_code = corporate_code


        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._projects = []
        if projects is not None:
            self.projects = projects
        else:
            self.projects = []


        super(BusinessCase, self).__init__(**kw_args)
    # >>> business_case

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._business_case = None
        for y in value:
            y._business_case = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._business_case = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._business_case = None
            self._works.remove(obj)
    # >>> works

    # <<< projects
    # @generated
    def get_projects(self):
        """ 
        """
        return self._projects

    def set_projects(self, value):
        for x in self._projects:
            x._business_case = None
        for y in value:
            y._business_case = self
        self._projects = value

    projects = property(get_projects, set_projects)

    def add_projects(self, *projects):
        for obj in projects:
            obj._business_case = self
            self._projects.append(obj)

    def remove_projects(self, *projects):
        for obj in projects:
            obj._business_case = None
            self._projects.remove(obj)
    # >>> projects


    def __str__(self):
        """ Returns a string representation of the BusinessCase.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< business_case.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusinessCase.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusinessCase", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.works:
            s += '%s<%s:BusinessCase.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.projects:
            s += '%s<%s:BusinessCase.projects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:BusinessCase.corporate_code>%s</%s:BusinessCase.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusinessCase")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> business_case.serialize


# <<< inf_work
# @generated
# >>> inf_work

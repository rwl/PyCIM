#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Run Envisage with the CIM plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import logging

from enthought.envisage.core_plugin import CorePlugin

from puddle.workbench.workbench_plugin import WorkbenchPlugin
from puddle.workbench.workbench_application import WorkbenchApplication

from enthought.plugins.ipython_shell.ipython_shell_plugin \
    import IPythonShellPlugin as PythonShellPlugin

from enthought.logger.plugin.logger_plugin import LoggerPlugin

from puddle.plugin import PuddlePlugin
from puddle.resource.resource_plugin import ResourcePlugin
from puddle.python_editor.python_editor_plugin import PythonEditorPlugin
from puddle.property_view.property_view_plugin import PropertyViewPlugin

from CIMPlugin import CIMPlugin

from UCTE.Plugin.UCTEPlugin import UCTEPlugin

#------------------------------------------------------------------------------
#  Logging:
#------------------------------------------------------------------------------

logger = logging.getLogger()
handler = logging.StreamHandler()
#handler = logging.StreamHandler(file("/tmp/cim.log", "w"))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

#------------------------------------------------------------------------------
#  "main" function:
#------------------------------------------------------------------------------

def main():
    """ Runs the application.
    """
    # Create an Envisage application.
    application = WorkbenchApplication(
        id = "cim",
        plugins = [
            CorePlugin(),
            PuddlePlugin(),
            WorkbenchPlugin(),
            ResourcePlugin(),
            PythonShellPlugin(),
            LoggerPlugin(),
            PythonEditorPlugin(),
            PropertyViewPlugin(),
            CIMPlugin(),
            UCTEPlugin()
        ]
    )

    # Run it!
    application.run()

    return


if __name__ == "__main__":
    main()

# EOF -------------------------------------------------------------------------

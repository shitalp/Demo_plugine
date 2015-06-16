#!/usr/bin/env python3
from cement.core import foundation, controller, handler
from cement.core.controller import CementBaseController, expose
from ee.core.services import EEService

# define application controllers


class Demo_PlugineController(CementBaseController):

    class Meta:
        label = 'monit'
        description = "Demo Plugin for ee"
        stacked_on = 'base'
        stacked_type = 'nested'
        # arguments = [
        #     (['--monit'], dict(help="option under base controller")),
        #     ]

    @expose(help="another base controller command")
    def start(self):
        EEService.start_service(self, "monit")


    @expose(help="another base controller command")
    def status(self):
        EEService.get_service_status(self, "monit")

    @expose(help="another base controller command")
    def reload(self):
        EEService.restart_service(self, "monit")



def load(ee):
    handler.register(Demo_PlugineController)

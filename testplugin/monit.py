#!/usr/bin/env python3
from cement.core import foundation, controller, handler
from cement.core.controller import CementBaseController, expose
from ee.core.services import EEService

# define application controllers


class Start_PlugineController(CementBaseController):

    class Meta:
        label = 'start'
        description = "Demo Plugin for ee"
        stacked_on = 'base'
        stacked_type = 'nested'
        # arguments = [
        #     (['--monit'], dict(help="option under base controller")),
        #     ]

    @expose(help="another base controller command")
    def start(self):
        EEService.start_service(self, "monit")



class Status_PlugineController(CementBaseController):

    class Meta:
        label = 'status'
        description = "Demo Plugin for ee"
        stacked_on = 'base'
        stacked_type = 'nested'
        # arguments = [
        #     (['--monit'], dict(help="option under base controller")),
        #     ]
    @expose(help="another base controller command")
    def monit(self):
        EEService.get_service_status(self, "monit")


class Stop_PlugineController(CementBaseController):

    class Meta:
        label = 'stop'
        description = "Demo Plugin for ee"
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(help="another base controller command")
    def monit(self):
        EEService.stop_service(self, "monit")


def load(ee):
    handler.register(Start_PlugineController)
    handler.register(Stop_PlugineController)
    handler.register(Status_PlugineController)

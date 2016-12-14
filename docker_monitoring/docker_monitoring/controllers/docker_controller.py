import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from docker_monitoring.lib.base import BaseController, render

log = logging.getLogger(__name__)

class DockerControllerController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/docker_controller.mako')
        # or, return a string
        return 'Hello World'

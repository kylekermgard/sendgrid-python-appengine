"""
This is the main application for the SendGrid API.  It is the starting page for the sendgrid api
helper class.
"""
import cgi

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from sendgrid import *

class MainPage(webapp.RequestHandler):
  def get(self):

    # initialize class
    x = SendGridApi('changeme@example.com', 'example')

    # giberish for now
    x.set_username('jose@sendgrid.com')
    x.set_password('password')

    # write out the response for now
    self.response.out.write(x.get_username() + ' ' + x.get_password())
    


application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
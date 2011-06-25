"""
This is the main application.  It is the starting page for the sendgrid api
helper class.
"""
class SendGridApi(object):

  def __init__(self, username, password):
    """Constructor.

    Args:
      username: Username used in making API requests
      password: Password use in making API requests
    """
    
    self.username = username
    self.password = password

  """Mutator methods

  Used to set specific paramters within SendGrid Api
  """

  def set_username(self, username):
    self._username = username

  def set_password(self, password):
    self._password = password
    
  def set_from(self, from_email_address):
    self._from = from_email_address

    

  """Accessor methods

  Used to get specific paramters within SendGrid Api
  """

  def get_username(self):
    return self._username

  def get_password(self):
    return self._password

  def get_from(self):
    return self._from
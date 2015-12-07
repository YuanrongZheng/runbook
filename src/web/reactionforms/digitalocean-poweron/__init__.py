######################################################################
# Cloud Routes Web Application
# -------------------------------------------------------------------
# Reaction - Forms Class
######################################################################

from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, NumberRange
from ..base import BaseReactForm


class ReactForm(BaseReactForm):

    ''' Class that creates a Reaction form for the dashboard '''
    title = "DigitalOcean: Power On Droplet"
    description = """
    <P>
      This reaction provides the ability to Power On a DigitalOcean Droplet. This reaction is useful when combined with other DigitalOcean reactions. For example, the Power On Reaction could be used to Power on a secondary database while the Power Off reaction can be used to power off the primary.
    </P>
    """
    placeholders = BaseReactForm.placeholders
    placeholders.update({
        'dropletid' : '12345',
        'name_prefix' : 'WebServer',
        'api_key' : placeholders['apikey'],
        'region' : 'nyc3',
        'size' : '512mb',
        'image' : 'ubuntu-14-04-x64',
        'ssh_keys' : 'key01',
    })


    apikey = TextField(
        "API Key",
        description=BaseReactForm.descriptions['apikey'],
        validators=[DataRequired(message='API Key is a required field')])
    dropletid = TextField(
        "Droplet ID#",
        description=BaseReactForm.descriptions['digitalocean']['dropletid'],
        validators=[DataRequired(message='Droplet ID# is a required field'), NumberRange(min=1, max=None, message="Droplet ID should be a numeric ID number")])
    call_on = SelectField(
        "Call On",
        description=BaseReactForm.descriptions['callon'],
        choices=[('false', 'False Monitors'), ('true', 'True Monitors')],
        validators=[DataRequired(message='Call On is a required field')])


if __name__ == '__main__':
    pass

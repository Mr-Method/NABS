from nabs import db
from datetime import datetime

# Generating timestamp for BD
now = datetime.now()
# Formatting date time
timestamp = now.strftime("%Y-%m-%d %H:%M")


class Devices(db.Model):
    """
    Class DB for devices profiles
    """

    # Add id in DB
    id = db.Column(db.Integer, primary_key=True)
    # Add device ip DB
    device_ip = db.Column(db.Integer, index=True, nullable=False)
    # Add device hostname ip DB
    device_hostname = db.Column(db.String(50), index=True, nullable=True)
    # device_env = db.Column(db.String(100), index=True, nullable=True)
    # Add timestamp in DB
    timestamp = db.Column(db.DateTime, default=datetime.now())

    # Return format massages from DB
    def __repr__(self):
        return "<Devices %r>" % self.device_ip


class Configs(db.Model):
    """
    Class DB for configs file
    """

    # Add id in DB
    id = db.Column(db.Integer, primary_key=True)
    # Add timestamp in DB
    timestamp = db.Column(db.DateTime, default=datetime.now())
    # Add device config file in DB
    device_config = db.Column(db.Text, nullable=False)
    # Add device ip DB
    device_ip = db.Column(db.Integer, db.ForeignKey("devices.device_ip"))

    # Return format massages from DB
    def __repr__(self):
        return "<Configs %r>" % self.device_ip
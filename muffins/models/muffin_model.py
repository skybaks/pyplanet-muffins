from peewee import *
from pyplanet.core.db import TimedModel


class PlayerMuffin(TimedModel):
	login = CharField(null=False, max_length=150)
	"""
	Player login that the muffin belongs to
	"""

	muffin_name = CharField(null=False, max_length=150)
	"""
	The name of the muffin
	"""

	muffin_tier = IntegerField(null=False)
	"""
	The tier level of the muffin
	"""

	class Meta:
		db_table = 'muffins_playermuffin'

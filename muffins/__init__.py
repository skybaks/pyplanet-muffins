import logging

from pyplanet.apps.config import AppConfig
from pyplanet.contrib.command import Command

from .bakery import roll_muffin

logger = logging.getLogger(__name__)

class MuffinsApp(AppConfig):
	game_dependencies = []
	app_dependencies = ['core.maniaplanet', 'core.trackmania', 'core.shootmania']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


	async def on_start(self):
		await self.instance.permission_manager.register('baking', 'Allowed to bake muffins in the bakery', app=self, min_level=2, namespace='muffin')
		await self.instance.command_manager.register(
			Command(command='muffin', aliases=[], target=self.bake_muffin, admin=True, perms='muffin:baking', description='Bake a muffin for a player')
				.add_param(name='player', nargs=1, type=str, required=True)
				.add_param(name='message', nargs='*', type=str, default='', required=False),
		)


	async def bake_muffin(self, player, data, **kwargs) -> None:
		muffin = roll_muffin()
		muffin_text = f'$<$n$fff{muffin.fmt_tier()}$> ' if muffin.fmt_tier() else ''
		muffin_text += f'$<$fff{muffin.name}$>'
		await self.instance.chat(f'$ff0$<$fff{player.nickname}$> » {muffin_text} for data.player')

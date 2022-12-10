import logging

from pyplanet.apps.config import AppConfig
from pyplanet.contrib.command import Command
from pyplanet.utils.style import style_strip

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
				.add_param(name='player', nargs='*', type=str, required=True),
		)


	async def bake_muffin(self, player, data, **kwargs) -> None:
		data_player = ' '.join(data.player)
		target_player = None
		for online_player in self.instance.player_manager.online:
			if online_player.login == data_player \
				or style_strip(online_player.nickname.lower()) == data_player.lower():
				target_player = online_player
				logger.debug('Found player ' + data_player)
				break
		if not target_player:
			await self.instance.chat(f'$f00No player player found for $<$fff{data_player}$>', player)
			return

		muffin = roll_muffin()
		muffin_text = f'$<$n$fff{muffin.fmt_tier()}$> ' if muffin.fmt_tier() else ''
		muffin_text += f'$<$fff{muffin.name}$>'
		await self.instance.chat(f'$ff0$<$fff{player.nickname}$> » {muffin_text} for $<$fff{target_player.nickname}$>')

import logging
from random import randrange

from pyplanet.apps.config import AppConfig
from pyplanet.contrib.command import Command
from pyplanet.utils.style import style_strip
from pyplanet.apps.core.maniaplanet.models import Player

from .bakery import Muffin, roll_muffin
from .models import PlayerMuffin

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
			Command(command='muffin', aliases=[], target=self.give_muffin, description='Give one of your muffins to a player')
				.add_param(name='player', nargs='*', type=str, required=True),
			Command(command='eat', aliases=[], target=self.eat_muffin, description='Eat one of your muffins. Yummy!'),
		)


	async def bake_muffin(self, player: Player, data, **kwargs) -> None:
		data_player = ' '.join(data.player)
		target_player = await self._lookup_player(data_player)
		if not target_player:
			await self.instance.chat(f'$f00No player found for $<$fff{data_player}$>', player)
			return
		muffin = roll_muffin()
		muffin_text = await self._get_muffin_text(muffin)
		await self.instance.chat(f'$ff0$<$fff{player.nickname}$> » {muffin_text} for $<$fff{target_player.nickname}$>')
		await self.instance.chat(f'$0cfYou received a muffin! Use $<$fff/eat$> to eat it or $<$fff/muffin$> to give it to another player', target_player.login)

		logger.debug('Create new entry for muffin')
		try:
			await PlayerMuffin.execute(PlayerMuffin.insert(login=target_player.login, muffin_name=muffin.name, muffin_tier=int(muffin.tier)))
		except Exception as e:
			logger.error(e)


	async def give_muffin(self, player: Player, data, **kwargs) -> None:
		data_player = ' '.join(data.player)
		target_player = await self._lookup_player(data_player)
		if not target_player:
			await self.instance.chat(f'$f00No player found for $<$fff{data_player}$>', player)
			return

		players_muffins = await self._get_muffins(player.login)
		if len(players_muffins) > 0:
			player_muffin = players_muffins[randrange(0, len(players_muffins))]
			muffin = Muffin.from_playermuffin(player_muffin)
			muffin_text = await self._get_muffin_text(muffin)
			await self.instance.chat(f'$ff0$<$fff{player.nickname}$> gives their $<$fff{muffin_text}$> to $<$fff{target_player.nickname}$>')
			await self.instance.chat(f'$0cfYou received a muffin! Use $<$fff/eat$> to eat it or $<$fff/muffin$> to give it to another player', target_player.login)

			logger.debug('Updating the login of muffin with id ' + str(player_muffin.id))
			try:
				await PlayerMuffin.execute(PlayerMuffin.update(login=target_player.login).where(PlayerMuffin.id == player_muffin.id))
			except Exception as e:
				logger.error(e)
		else:
			await self.instance.chat(f'$f00You don\'t have any muffins to give', player)


	async def eat_muffin(self, player: Player, data, **kwargs) -> None:
		players_muffins = await self._get_muffins(player.login)
		if len(players_muffins) > 0:
			player_muffin = players_muffins[randrange(0, len(players_muffins))]
			muffin = Muffin.from_playermuffin(player_muffin)
			muffin_text = await self._get_muffin_text(muffin)
			await self.instance.chat(f'$ff0$<$fff{player.nickname}$> eats their $<$fff{muffin_text}$>. It tastes {muffin.get_taste()}')

			logger.debug('Deleting muffin with id ' + str(player_muffin.id))
			try:
				await PlayerMuffin.execute(PlayerMuffin.delete().where(PlayerMuffin.id == player_muffin.id))
			except Exception as e:
				logger.error(e)
		else:
			await self.instance.chat('$f00You don\'t have any muffins to eat', player)


	async def _get_muffins(self, login) -> 'list[PlayerMuffin]':
		login_muffins = await PlayerMuffin.execute(PlayerMuffin.select().where(PlayerMuffin.login == login))
		return list(login_muffins) if len(login_muffins) > 0 else []


	async def _lookup_player(self, search_text) -> Player:
		for online_player in self.instance.player_manager.online:
			if online_player.login == search_text \
				or style_strip(online_player.nickname.lower()) == search_text.lower():
				logger.debug('Found player ' + search_text)
				return online_player
		else:
			return None


	async def _get_muffin_text(self, muffin) -> str:
		muffin_text = f'$<$n$fff{muffin.fmt_tier()}$> ' if muffin.fmt_tier() else ''
		muffin_text += f'$<$fff{muffin.name}$>'
		return muffin_text

import logging
import random
from enum import IntEnum

logger = logging.getLogger(__name__)


class MuffinTier(IntEnum):
	NORMAL = 100
	UNCOMMON = 200
	RARE = 300
	LEGENDARY = 400

	@staticmethod
	def fmt_string(value: 'MuffinTier') -> str:
		if value == MuffinTier.NORMAL:
			return ''
		elif value == MuffinTier.UNCOMMON:
			return '$3bb[Uncommon]'
		elif value == MuffinTier.RARE:
			return '$73e[Rare]'
		elif value == MuffinTier.LEGENDARY:
			return '$ff9[L$fe9e$ee9g$ed9en$ec9d$dc9a$db9ry]'
		else:
			return str(value)


class Muffin:
	def __init__(self, name: str, tier: MuffinTier) -> None:
		self.name = name
		self.tier = tier

	def fmt_tier(self) -> str:
		return MuffinTier.fmt_string(self.tier)

	def get_taste(self) -> str:
		tastes = []
		if self.tier == MuffinTier.LEGENDARY:
			tastes += [
				'heavenly!',
				'scrumdiddlyumptious!',
				'sublime!',
				'amazing!',
				'incredible!',
				'awesome!',
				'fabulous!',
				'perfect!',
				'outstanding!',
				'stupendous!',
				'wonderful!',
				'fantastic!',
				'divine!',
			]
		elif self.tier == MuffinTier.RARE:
			tastes += [
				'flavorful.',
				'zesty.',
				'unique.',
				'quite yummy.',
				'quite good.',
				'savory.',
				'excellent.',
				'remarkable.',
				'delectable.',
				'delightful.',
				'succulent.',
				'rich.',
				'scrumptious.',
				'piquant.',
			]
		elif self.tier == MuffinTier.UNCOMMON:
			tastes += [
				'good.',
				'pretty good.',
				'nice.',
				'yummy.',
				'pleasant.',
			]
		else:
			tastes += [
				'okay.',
				'alright.',
				'interesting.',
				'palatable.',
			]
		return random.choice(tastes)

	@staticmethod
	def from_playermuffin(player_muffin) -> 'Muffin':
		return Muffin(player_muffin.muffin_name, MuffinTier(player_muffin.muffin_tier))


def _create_muffin_list() -> 'list[Muffin]':
	return [
		Muffin('Muffin', MuffinTier.NORMAL),

		Muffin('Blueberry Muffin', MuffinTier.UNCOMMON),
		Muffin('Chocolate Muffin', MuffinTier.UNCOMMON),
		Muffin('Pancake Muffin', MuffinTier.UNCOMMON),
		Muffin('Cream Cheese Muffin', MuffinTier.UNCOMMON),
		Muffin('Pumpkin Muffin', MuffinTier.UNCOMMON),
		Muffin('Banana Muffin', MuffinTier.UNCOMMON),
		Muffin('Chocolate Chip Muffin', MuffinTier.UNCOMMON),
		Muffin('Cinnamon Muffin', MuffinTier.UNCOMMON),
		Muffin('Mini Cherry Muffin', MuffinTier.UNCOMMON),
		Muffin('Zucchini Muffin', MuffinTier.UNCOMMON),
		Muffin('Strawberry Muffin', MuffinTier.UNCOMMON),
		Muffin('Applesauce Muffin', MuffinTier.UNCOMMON),
		Muffin('Cranberry Muffin', MuffinTier.UNCOMMON),
		Muffin('Poppy Seed Muffin', MuffinTier.UNCOMMON),
		Muffin('English Muffin', MuffinTier.UNCOMMON),
		Muffin('Quiche Muffin', MuffinTier.UNCOMMON),
		Muffin('Honey Muffin', MuffinTier.UNCOMMON),
		Muffin('Monkey Muffin', MuffinTier.UNCOMMON),
		Muffin('Brown Sugar Muffin', MuffinTier.UNCOMMON),
		Muffin('Carrot Muffin', MuffinTier.UNCOMMON),
		Muffin('Cornbread Muffin', MuffinTier.UNCOMMON),
		Muffin('Avocado Muffin', MuffinTier.UNCOMMON),

		Muffin('Banana Blueberry Muffin', MuffinTier.RARE),
		Muffin('Crumb Apple Muffin', MuffinTier.RARE),
		Muffin('Lemon Blueberry Muffin', MuffinTier.RARE),
		Muffin('Lemon Crumb Muffin', MuffinTier.RARE),
		Muffin('Banana Bread Muffin', MuffinTier.RARE),
		Muffin('Skinny Chocolate Muffin', MuffinTier.RARE),
		Muffin('Fruity Pebbles Muffin', MuffinTier.RARE),
		Muffin('Mini Crumb-Cake Muffin', MuffinTier.RARE),
		Muffin('Zucchini Cream Cheese Muffin', MuffinTier.RARE),
		Muffin('Pumpkin Brownie Muffin', MuffinTier.RARE),
		Muffin('Pumpkin Cream Cheese Muffin', MuffinTier.RARE),
		Muffin('Pumpkin Streusel Muffin', MuffinTier.RARE),
		Muffin('Bacon Pepper and Egg Muffin', MuffinTier.RARE),
		Muffin('Blueberry Monkey Bread Muffin', MuffinTier.RARE),
		Muffin('Lemon-Raspberry Streusel Muffin', MuffinTier.RARE),
		Muffin('Maple-Chai Pumpkin Muffin', MuffinTier.RARE),
		Muffin('Avocado Pineapple Muffin', MuffinTier.RARE),
		Muffin('Sweet Potato Muffin', MuffinTier.RARE),
		Muffin('Banana Oat Muffin', MuffinTier.RARE),
		Muffin('Blueberry Cream Muffin', MuffinTier.RARE),
		Muffin('Peanut Butter Banana Muffin', MuffinTier.RARE),
		Muffin('Sweet Corn Muffin', MuffinTier.RARE),
		Muffin('Feta and Chive Muffin', MuffinTier.RARE),
		Muffin('Carmel Apple Muffin', MuffinTier.RARE),
		Muffin('Blueberry Orange Muffin', MuffinTier.RARE),
		Muffin('Coconut Chocolate Muffin', MuffinTier.RARE),
		Muffin('Buttermilk Cranberry Muffin', MuffinTier.RARE),
		Muffin('Pumpkin Surprise Muffin', MuffinTier.RARE),
		Muffin('Brown Sugar Oat Muffin', MuffinTier.RARE),
		Muffin('Morning Maple Muffin', MuffinTier.RARE),
		Muffin('Lemon Meringue Muffin', MuffinTier.RARE),
		Muffin('Breakfast Egg Muffin', MuffinTier.RARE),
		Muffin('Cinnamon Doughnut Muffin', MuffinTier.RARE),
		Muffin('Rhubarb Streusel Muffin', MuffinTier.RARE),
		Muffin('Whole Wheat Blueberry Muffin', MuffinTier.RARE),
		Muffin('Pineapple Upside-Down Muffin', MuffinTier.RARE),
		Muffin('Irish Soda Bread Muffin', MuffinTier.RARE),
		Muffin('Pumpkin Banana Muffin', MuffinTier.RARE),
		Muffin('Wild Blueberry Muffin', MuffinTier.RARE),
		Muffin('Sausage Pancake Muffin', MuffinTier.RARE),
		Muffin('Coconut Carrot Muffin', MuffinTier.RARE),
		Muffin('Frozen Blueberry Muffin', MuffinTier.RARE),
		Muffin('Coffee Cake Muffin', MuffinTier.RARE),
		Muffin('Apple Streusel Muffin', MuffinTier.RARE),
		Muffin('Cranberry Pumpkin Muffin', MuffinTier.RARE),
		Muffin('Sour Cream Chip Muffin', MuffinTier.RARE),
		Muffin('Cranberry Sweet Potato Muffin', MuffinTier.RARE),
		Muffin('Zucchini Chocolate Chip Muffin', MuffinTier.RARE),
		Muffin('Chocolate Chip Oatmeal Muffin', MuffinTier.RARE),
		Muffin('Walnut Zucchini Muffin', MuffinTier.RARE),
		Muffin('Apple Spice Muffin', MuffinTier.RARE),
		Muffin('Pecan Pie Mini Muffin', MuffinTier.RARE),
		Muffin('Sausage Cheese Muffin', MuffinTier.RARE),
		Muffin('Ginger Pear Muffin', MuffinTier.RARE),
		Muffin('Banana Macadamia Muffin', MuffinTier.RARE),
		Muffin('Pumpkin Spice Muffin', MuffinTier.RARE),
		Muffin('Cranberry Nut Muffin', MuffinTier.RARE),
		Muffin('Cheddar Cheese Muffin', MuffinTier.RARE),
		Muffin('Pepperoni Pizza Muffin', MuffinTier.RARE),
		Muffin('Oatmeal Raisin Muffin', MuffinTier.RARE),
		Muffin('Mango Coconut Muffin', MuffinTier.RARE),

		Muffin('Chocolate Zucchini Doughnut Muffin', MuffinTier.LEGENDARY),
		Muffin('Chocolate Chip Baked Oatmeal Muffin', MuffinTier.LEGENDARY),
		Muffin('Peanut Butter Cadbury Mini Egg Muffin', MuffinTier.LEGENDARY),
		Muffin('Blueberry Cream Cheese Muffin', MuffinTier.LEGENDARY),
		Muffin('Cream Cheese Banana Muffin', MuffinTier.LEGENDARY),
		Muffin('Cream Cheese Filled Chocolate Chip Muffin', MuffinTier.LEGENDARY),
		Muffin('Chocolate Chip Pumpkin Doughnut Muffin', MuffinTier.LEGENDARY),
		Muffin('Pumpkin Apple Streusel Muffin', MuffinTier.LEGENDARY),
		Muffin('Double Chocolate Banana Muffin', MuffinTier.LEGENDARY),
		Muffin('Lemon Pound Cake Muffin', MuffinTier.LEGENDARY),
		Muffin('Pomegranate Cream Cheese Surprise Muffin', MuffinTier.LEGENDARY),
		Muffin('Lemon-Filled Gingerbread Muffin', MuffinTier.LEGENDARY),
		Muffin('Bacon-Peanut Butter Cornbread Muffin', MuffinTier.LEGENDARY),
		Muffin('Coastal Carolina Frittatas Muffin', MuffinTier.LEGENDARY),
		Muffin('Smores Monkey Bread Muffin', MuffinTier.LEGENDARY),
		Muffin('Bakery Style Maple Walnut Muffin', MuffinTier.LEGENDARY),
		Muffin('Cinnamon Sugar Mini-Donut Muffin', MuffinTier.LEGENDARY),
		Muffin('Peanut Butter and Jelly Mini Muffin', MuffinTier.LEGENDARY),
	]

MUFFINS = list()
if not MUFFINS:
	MUFFINS = _create_muffin_list()


def roll_muffin() -> Muffin:
	""" Roll for a new muffin.

	Chooses a random muffin from the list of muffins along the following distribution:
	- 50% Normal
	- 30% Uncommon
	- 15% Rare
	- 5% Legendary
	"""
	roll = random.random()
	selected_tier = None
	if roll > 0.95:
		selected_tier = MuffinTier.LEGENDARY
	elif roll > 0.80:
		selected_tier = MuffinTier.RARE
	elif roll > 0.50:
		selected_tier = MuffinTier.UNCOMMON
	else:
		selected_tier = MuffinTier.NORMAL
	logger.debug(f'Rolled a {str(roll)} which is a ' + str(selected_tier))
	return random.choice([muffin for muffin in MUFFINS if muffin.tier == selected_tier])

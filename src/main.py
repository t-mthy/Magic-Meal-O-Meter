import random

# dictonary of meals based on mood
# 🤪
adventurous_mood = {"German Potato Dumplings": "https://www.thespruceeats.com/bavarian-potato-dumplings-1447183",
                    "Portuguese Egg Tarts": "https://www.tastingtable.com/686035/portuguese-egg-tart-recipe-pastry/",
                    "Chicken and Waffles": "https://www.sweetteaandthyme.com/fried-chicken-waffles-spicy-honey-sauce/",
                    "Paella": "https://tastesbetterfromscratch.com/paella/",
                    "Chicken Katsu Curry": "https://japan.recipetineats.com/katsu-curry-japanese-curry-rice-with-chicken-cutlet/",
                    "Sashimi": "https://aubreyskitchen.com/salmon-sashimi/",
                    "Banh Mi": "https://www.tastingtable.com/649760/simple-banh-mi-sandwich-recipe/",
                    "Menudo": "https://www.mexicoinmykitchen.com/menudo-soup/",
                    "Spanakopita": "https://www.themediterraneandish.com/spanakopita-recipe-greek-spinach-pie/",
                    "Cantonese Steamed Fish": "https://thewoksoflife.com/cantonese-steamed-fish/"}

# 😡
angry_mood = {"Hot Chicken Sandwich": "https://littlesunnykitchen.com/nashville-hot-chicken-sandwich/",
              "Ice Cream Sundae": "https://dinnerthendessert.com/ice-cream-sundae/",
              "Spicy Szechuan Noodles": "https://drivemehungry.com/spicy-szechuan-noodles-with-garlic-chili-oil/",
              "Potato Salad": "https://www.foodiecrush.com/how-to-make-the-best-potato-salad/",
              "Pesto Pasta Salad": "https://tastesbetterfromscratch.com/pesto-pasta-salad/",
              "McDonald's McNuggets": "https://www.mcdonalds.com/us/en-us/product/chicken-mcnuggets-4-piece.html",
              "Chow Mein": "https://natashaskitchen.com/chicken-chow-mein/"}

# 😐
bored_mood = {"Chinese Dumplings": "https://thewoksoflife.com/dumpling-recipe-youll-ever-need/",
              "Pho": "https://iamafoodblog.com/authentic-instant-pot-pho-recipe/",
              "Gyro": "https://www.christinascucina.com/homemade-greek-gyros-with-tzatziki/",
              "Sushi Bake": "https://keepingitrelle.com/easy-sushi-bake-recipe/",
              "Lasagna": "https://www.spendwithpennies.com/easy-homemade-lasagna/",
              "Baked Potato": "https://www.gimmesomeoven.com/baked-potato/",
              "Korean Corn Dog": "https://www.honestfoodtalks.com/korean-corn-dog-recipe/"}

# 😌
calm_mood = {"Clam Chowder": "https://damndelicious.net/2015/04/25/easy-clam-chowder/",
             "Poke Bowl": "https://momsdish.com/hawaiian-poke-bowl",
             "Butternut Squash Soup": "https://cookieandkate.com/roasted-butternut-squash-soup/",
             "Vietnamese Spring Rolls": "https://www.hungryhuy.com/how-to-make-goi-cuon-vietnamese-spring-rolls/",
             "Chicken Pot Pie": "https://www.thewholesomedish.com/the-best-classic-chicken-pot-pie/",
             "Beef Stew": "https://www.onceuponachef.com/recipes/beef-stew-with-carrots-potatoes.html",
             "Prosciutto Arugula Flatbread Pizza": "https://www.kyleecooks.com/prosciutto-arugula-flatbread-pizza/",
             "Smoked Salmon Bagel": "https://feelgoodfoodie.net/recipe/smoked-salmon-bagel/",
             "Charcuterie Board": "https://tastesbetterfromscratch.com/charcuterie-board/"}


# 😁
excited_mood = {"Lobster Roll": "https://www.foodiecrush.com/lobster-rolls/",
                "Birria Tacos": "https://houseofyumm.com/beef-birria-and-birria-tacos/",
                "Korean Barbeque": "https://www.maangchi.com/recipe/bulgogi",
                "Hot Pot": "https://thewoksoflife.com/chinese-hot-pot-at-home/",
                "Tacos": "https://thekitchencommunity.org/mexican-tacos/",
                "Butter Chicken": "https://cafedelites.com/butter-chicken/"}

# 😊
happy_mood = {"Spaghetti and Meatballs": "https://natashaskitchen.com/spaghetti-and-meatballs-recipe/",
              "Miso Ramen": "https://www.justonecookbook.com/homemade-chashu-miso-ramen/",
              "Pizza": "https://tasty.co/recipe/pizza-dough",
              "Cheeseburger": "https://www.recipetineats.com/cheeseburger-recipe/",
              "Mac and Cheese": "https://www.thechunkychef.com/family-favorite-baked-mac-and-cheese/",
              "Sushi": "https://www.fifteenspatulas.com/homemade-sushi/",
              "Chicken Tikka Masala": "https://nishkitchen.com/authentic-chicken-tikka-masala-recipe/",
              "Mango Sticky Rice": "https://www.epicurious.com/recipes/food/views/sticky-rice-with-mango-12066",
              "Waffles": "https://www.shugarysweets.com/homemade-waffles/"}

# 🥱
lazy_mood = {"Mini Pizza Bites": "https://myminichefs.com/pull-apart-pizza-bites/",
             "Cereal": "https://www.tasteofhome.com/collection/what-to-put-in-cereal/",
             "Grilled Cheese": "https://natashaskitchen.com/grilled-cheese-sandwich/",
             "Spam, Eggs, and Rice": "https://eatingrichly.com/spam-eggs-and-rice/",
             "Kimchi Fried Rice": "https://mykoreankitchen.com/kimchi-fried-rice/",
             "Fruit and Yogurt Parfait": "https://feelgoodfoodie.net/recipe/fruit-yogurt-parfait/",
             "Pasta Carbonara": "https://www.cookingclassy.com/pasta-carbonara/",
             "Tortilla Pizza": "https://freshaprilflours.com/5-minute-personal-tortilla-pizza/",
             "Crispy Potstickers": "https://kirbiecravings.com/crispy-skirt-potstickers/",
             "In-N-Out Double-Double": "https://www.in-n-out.com/menu"}

# 🥳
proud_mood = {"Peking Duck": "https://redhousespice.com/peking-duck/",
              "Beef Wellington": "https://www.foodnetwork.com/recipes/tyler-florence/the-ultimate-beef-wellington-recipe2-1952280",
              "Barbeque Ribs": "https://www.inspiredtaste.net/7179/sweet-and-spicy-oven-baked-ribs/",
              "Chicago Style Deep Dish Pizza": "https://www.kingarthurbaking.com/recipes/chicago-style-deep-dish-pizza-recipe",
              "Bacon Wrapped Pork Tenderloin": "https://www.recipetineats.com/bacon-wrapped-pork-tenderloin/",
              "Seared Salmon": "https://cafedelites.com/crispy-seared-lemon-garlic-herb-salmon/"}

# 😍
romantic_mood = {"Steak": "https://www.recipetineats.com/how-to-cook-steak/",
                 "Spicy Tuna Crispy Rice": "https://cookingwithayeh.com/spicy-tuna-crispy-rice/",
                 "Garlic Lamb Chops": "https://www.foodandwine.com/recipes/lamb-chops-sizzled-garlic",
                 "Shrimp Scampi": "https://www.bonappetit.com/recipe/shrimp-scampi",
                 "Broiled Lobster Tails": "https://sweetcsdesigns.com/10-minute-perfect-broiled-lobster-tails-recipe/",
                 "Scallops with Risotto": "https://pinchofyum.com/brown-butter-scallops-parmesan-risotto",
                 "Pan Seared Sea Bass": "https://organicallyaddison.com/pan-seared-chilean-sea-bass/",
                 "Chicken Parmesan": "https://cafedelites.com/crispy-chicken-parmesan/",
                 "Chocolate Lava Cake": "https://www.foodandwine.com/recipes/molten-chocolate-cakes"}

# 😞
sad_mood = {"Chicken Nuggets": "https://iwashyoudry.com/chick-fil-a-chicken-nuggets/",
            "Fried Chicken": "https://thestayathomechef.com/fried-chicken/",
            "Carne Asada Burrito": "https://www.mylatinatable.com/best-carne-asada-burritos-recipe/",
            "Chocolate Cake": "https://addapinch.com/the-best-chocolate-cake-recipe-ever/",
            "Braised Pork Belly": "https://thewoksoflife.com/shanghai-style-braised-pork-belly/",
            "Quesadillas": "https://www.recipetineats.com/quesadilla/",
            "Fruit Salad": "https://www.cookingclassy.com/honey-lime-rainbow-fruit-salad/",
            "Garlic Bread": "https://www.ambitiouskitchen.com/the-best-garlic-bread-recipe/"}

# 😬
stressed_mood = {"Upgraded Instant Ramen": "https://www.budgetbytes.com/6-ways-to-upgrade-instant-ramen/",
                 "Baked Ham and Cheese Sliders": "https://www.allrecipes.com/recipe/216756/baked-ham-and-cheese-party-sandwiches/",
                 "Costco Chicken Bake": "https://momsdish.com/recipe/608/chicken-bake-inspired-costco",
                 "Hamburger": "https://tastesbetterfromscratch.com/hamburger-recipe/",
                 "Oatmeal Breakfast Smoothie": "https://kristineskitchenblog.com/oatmeal-breakfast-smoothie-kid-favorite/",
                 "Taco Bell Crunchwrap Supreme": "https://www.tacobell.com/food/specialties/crunchwrap-supreme",
                 "Spam Musubi": "https://www.favfamilyrecipes.com/musubi/"}

# 😴
tired_mood = {"Avocado Toast": "https://cookieandkate.com/avocado-toast-recipe/",
              "Dunkin\' Donuts": "https://www.dunkindonuts.com/en/menu/donuts",
              "Chicken Caesar Salad": "https://www.spendwithpennies.com/chicken-caesar-salad/",
              "Bacon and Scrambled Eggs": "https://brooklynfarmgirl.com/scrambled-eggs-with-bacon/",
              "Chicken Noodle Soup": "https://tastesbetterfromscratch.com/chicken-noodle-soup/",
              "Japanese Egg Sandwich": "https://www.justonecookbook.com/japanese-egg-sandwich-tamago-sando/",
              "BLT Sandwich": "https://thefoodcharlatan.com/b-l-a-t-bacon-lettuce-avocado-tomato-sandwich-with-aioli-sauce-and-feta/",
              "Huevos Rancheros": "https://cookieandkate.com/huevos-rancheros-recipe/",
              "Beef Chili": "https://www.thewholesomedish.com/the-best-classic-chili/"}


# chooses random meal from the mood dict
def adventurous_meal():
    meal, recipe = random.choice(list(adventurous_mood.items()))
    Element('meal').write(meal)
    Element('recipe').write(recipe)
    document.getElementById('value3').href = recipe

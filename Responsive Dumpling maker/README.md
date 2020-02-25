### Responsive Dumpling Maker

a Twitter bot has been created with 22 responsive methods based on the basic dumpling bot and open source code from the GitHub page of PROSECCO. All the responsive rules are shown below.

Question|Yes|No|
|:--:|:--:|:--:|
Have meat?|A random dumpling| Not meat(GF) dumpling
Have veggie?| A random dumpling|Not veggie dumpling
Have beef?| Beef dumpling | Not beef dumpling
HAve chicken?| Chicken dumpling| Not chicken dumpling
Have pork?| Pork dumpling| Not pork dumpling
Have seafood?| Seafood dumpling| Not seafood dumpling
Spicy? | Spicy dumpling| Not spicy dumpling
Salty?| Salty dumpling | Not salty dumpling
Single layer?| Single layer dumpling| Double layers dumpling
Double layers dumpling?| Double layers dumpling| Single layer dumpling
Want dumpling?| A random dumpling| Greeting

In conclusion, this responsive bot can reply to some basic requirements when taking an order. Moreover, it has an input detection function, which can respond to the user’s spelling keywords in both lower case and capital letters. For example, if the bot received an order such as “SeAFoOd”, it will reply to the customer a random seafood dumpling. The responsive rules are created by a simple Python program automatically. Additionally, when the bot received a message irrelevant to the dumpling, it will simply greet to customer. However, this bot has some disadvantages. First, the codes are a little duplicated because different types of dumplings require various kinds of materials. For example, “spicy dumpling” needs certain
categories of meat, veggie, and spicy sauce. For classifying the materials for dumplings, it needs to write duplicated codes. Another limitation is that the bot can basically reply to a random single layer dumpling to almost requirements because the double layers dumpling is still complicated to deal with. For example, The response to the “salty dumpling” is only a random single layer salty dumpling not including double layers dumpling.

#### Usage
Just to simply copy and paste the code on the cheap bot done quick website then run it.



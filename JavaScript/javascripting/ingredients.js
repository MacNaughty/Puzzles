var ingredients = ["eggs", "milk", "flour", "sugar", "baking soda", "baking powder", "chocolate chips", "bananas"];
var size = ingredients.length;
// Write a while loop that prints out the contents of ingredients:
var count = 0;
while (count < size) {
  console.log(ingredients[count]);
  count++;
}

// Write a for loop that prints out the contents of ingredients:
for (i = 0; i < size; i++) {
  console.log(ingredients[i]);
}

// Write any loop (while or for) that prints out the contents of ingredients backwards:
for (i = size - 1; i >= 0; i--) {
  console.log(ingredients[i]);
}
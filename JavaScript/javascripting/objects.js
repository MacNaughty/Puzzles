var pizza = {
       toppings: ['cheese', 'sauce', 'pepperoni'],
       crust: 'deep dish',
       serves: 2
    }

const util = require('util')
console.log(util.inspect(pizza));
const chalk = require('chalk')
const spawn = require('child_process').spawn
console.log(chalk.yellow('requesting...'))
const search = spawn('python',['./callable.py', 'search', 'margarita'])
let buffer = ''
const onData = data => {
  console.log(chalk.yellow('buffering...'))
  buffer += data
}
const onEnd = () => {
  console.log(chalk.yellow('buffer complete !'))
  try {
    console.log(chalk.blue('raw output from Python'), buffer)
    const js = JSON.parse(buffer)
    console.log(chalk.green('raw output as JS object'), js)
    console.log(chalk.green('assert JS object properties can be read'), js.drinks.map(({ strDrink }) => strDrink))
  } catch (e) {
    console.error(chalk.red('there was an error'), buffer)
  }
}
search.stdout.on('data', onData)
search.stdout.on('end', onEnd)

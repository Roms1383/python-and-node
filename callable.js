const args = process.argv.slice(2)
const method = args[0]
const parameter = args.length > 1
? args[1]
: undefined
const rest = require('./rest')
rest[method](parameter)
.then(console.log)
.catch(console.error)

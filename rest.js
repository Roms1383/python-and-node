const request = require('request-promise-native')
/**
 * if request(...) => return raw JSON string (use json.loads in Python)
 * if request(..., { json: true }) => return JS object (use demjson.decode in Python)
 */
const search = async name => request(`https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${name}`)
module.exports = { search }

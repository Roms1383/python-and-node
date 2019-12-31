import sys
import chalk
import json
from Naked.toolshed.shell import muterun_js

response = muterun_js('./callable.js', 'search margarita')
if response.exitcode == 0:
  try:
    output = response.stdout.decode("utf-8")
    print(chalk.blue('raw output from JS'), output)
    dictionary = json.loads(output)
    print(chalk.green('decoded output as Python dictionary'), dictionary)
    print(chalk.green('assert Python dictionary keys can be read'), [drink['strDrink'] for drink in dictionary['drinks']])
  except Exception as e:
    print(chalk.red(e))
else:
  sys.stderr.write(chalk.red(str(response.stderr)))
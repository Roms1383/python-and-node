import sys
import chalk
import json
from Naked.toolshed.shell import muterun_js

def drinks(dictionary):
  output = []
  for drink in dictionary['drinks']:
    output.append(drink['strDrink'])
  return output

response = muterun_js('./callable.js', 'search margarita')
if response.exitcode == 0:
  try:
    output = response.stdout.decode("utf-8")
    print(chalk.blue('raw output from JS'), output)
    dictionary = json.loads(output)
    print(chalk.green('decoded output as Python dictionary'), dictionary)
    print(chalk.green('assert Python dictionary keys can be read'), drinks(dictionary))
  except Exception as e:
    print(chalk.red(e))
else:
  sys.stderr.write(chalk.red(str(response.stderr)))
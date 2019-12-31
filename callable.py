import sys
from rest import Rest

client = Rest()
method = str(sys.argv[1])
parameter = sys.argv[2] if len(sys.argv) > 2 else None
call = getattr(client, method)
try:
  response = call(parameter) if parameter is not None else call()
  print(response)
except Exception as e:
  print(e)

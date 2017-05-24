from domino import Domino
import os

domino = Domino("luik/quick-start",
                api_key=os.environ['DOMINO_USER_API_KEY'],
                host=os.environ['DOMINO_API_HOST'])

domino_run = domino.endpoint_run([{'field1': 'value1', 'field2': 'value2'}, 'parameter2'])
print(domino_run)

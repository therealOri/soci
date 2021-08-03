import socid_extractor as se
import requests
import time
import json
from rich.console import Console
import os

os.system('clear||cls')
BANNER = '''[magenta]
                    _ 
   _________  _____(_)
  / ___/ __ \/ ___/ / 
 (__  ) /_/ / /__/ /  
/____/\____/\___/_/


[green]by https://github.com/therealOri[/green]

[/magenta]
'''

console = Console()
console.print(BANNER)

url = input('Url here: ')
os.system('clear||cls')

r = requests.get(url)
data = se.extract(r.text)


time = time.strftime("%b-%d-%Y_%I:%M:%S",time.localtime())
with open(f'output_{time}.json', 'w') as oj: # Could use some help with better file names. To avoid any confusion about what is in each file.
    json.dump(data, oj)
    oj.close()
    

with open(f"output_{time}.json", "r") as pjp:
    j_data = json.load(pjp)

    PrettyJson = json.dumps(j_data, indent=1, separators=(',', ': '), sort_keys=True)
    print(f"Displaying Pretty Printed JSON Data for {url}\n")
    print(PrettyJson)
    pjp.close()
    
print(f'\n\nResults have also been saved into {oj.name}.')

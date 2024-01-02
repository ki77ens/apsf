import requests
import sys
from colorama import Fore as f

url = sys.argv[1]
lives = []

with open(sys.argv[2], 'r') as arq:
    for line in arq:
        line = line.strip()
        request = f'{url}/{line}'
        http = requests.get(request)
        code = http.status_code
        
        if code not in {301, 404}:
            if b'Page not found... ' not in http.content:
                print(f.GREEN + f'[ + ] PAGE FOUND - {request}')
                lives.append(request)
            else:
                print(f.RED + f'[ - ] PAGE NOT FOUND - {request}')
        else:
            print(f.RED + f'[ - ] PAGE NOT FOUND - {request}')

print('FINISHED')
for live in lives:
    print(live)

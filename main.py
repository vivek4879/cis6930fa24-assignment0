import argparse
import requests
import sys
import json

def get_data_from_url(url, page):
    response = requests.get(url, params={'page': page})
    if response.status_code != 200:
        print("failed")
    else:
        return response.json()

def get_data_from_json(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data

def output_print(response):
    data = response
    for record in data['items']:
        title = record.get('title', ' ')
        subjects = record.get('subjects', [' '])
        if subjects:
            subjects = ','.join(subjects)
        else:
            subjects = ''

        field_offices = record.get('field_offices', [' '])
        if field_offices:
            field_offices = ','.join(field_offices)
        else:
            field_offices=''
        
        print(f'{title}þ{subjects}þ{field_offices}')

def main(page = None, thefile = None):
    url = 'https://api.fbi.gov/wanted/v1/list'
    if page is not None:
        response = get_data_from_url(url,page)
        with open("test.json",'w') as f:
            json.dump(response, f)

    elif thefile is not None:
        response = get_data_from_json(thefile)
    
    output_print(response)
 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type = str, required = False, help = 'Given some api file')
    parser.add_argument("--page", type = int, required = False, help = 'give some page number')

    args = parser.parse_args()

    if args.page:
        main(page=args.page)

    elif args.file:
        main(thefile=args.file)

    else:
        parser.print_help(sys.stderr)

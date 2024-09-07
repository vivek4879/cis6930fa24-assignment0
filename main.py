import argparse
import requests
import sys

def output_print(response):
    if response.status_code == 200:
            data = response.json()
            for record in data['items']:
                title = record.get('title', ' ')
                subjects = record.get('subjects', [' '])
                if subjects:
                    subjects = ','.join(subjects)

                field_offices = record.get('field_offices', [' '])
                if field_offices:
                    field_offices = ','.join(field_offices)
                print(f'{title}þ{subjects}þ{field_offices}')
    else:
        print("failed")


def main(page = None, thefile = None):
    if page is not None:
        response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': page})
        output_print(response)

    elif thefile is not None:
        url = thefile
        response = requests.get(url)
        output_print(response)
 

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type = str, required = False, help = 'Given some api file')
    parser.add_argument("--page", type = int, required = False, help = 'givesome page number')

    args = parser.parse_args()

    if args.page:
        main(page=args.page)

    elif args.thefile:
        main(thefile=args.thefile)

    else:
        parser.print_help(sys.stderr)

import csv


all_data = [{
            "id": 100,
            "email": "george.bluth@reqres.in",
            "first_name": "George",
            "last_name": "Bluth",
            "avatar": "https://reqres.in/img/faces/1-image.jpg"
        }]

def export_to_csv(all_data):
    print(all_data)
    file_path = './all_data.csv'
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=all_data[0].keys())
        writer.writeheader()
        writer.writerows(all_data)

    print(f'Data written to {file_path}')


if __name__ == '__main__':
    print('csv_export.py, this is a main caller')
    export_to_csv(all_data)
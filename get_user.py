"""
1. Make a GET request to https://reqres.in/api/users
2. Fetch    "id",
            "email"
            "first_name"
            "last_name"
            "avatar"
3. Fetch the above data for all the pages
4. Export the data to CSV file
"""
import csv
import requests


URL = "https://reqres.in/api/users"


class Users:

    def get_page_count(self, url):
        try:
            response = requests.get(url)
            page_count = response.json()['total_pages']
            return page_count
        except:
            logger.error('get_page_count() - Failed to make a GET request')

    def get_all_data(self, url):
        page_count = self.get_page_count(url)

        all_data = []
        for i in range(1, page_count + 1):
            logging.info(f'fetching data from page {i}')
            try:
                response = requests.get(f'{url}?page={i}')
                data_from_page = response.json()
                logger.info(f'fetch {len(data_from_page)} records')
                all_data.extend(data_from_page['data'])
            except Exception as e:
                logger.error(f'Fetching data failed  for page {i}')

        logger.info(f'all data has been fetched {len(all_data)}')
        return all_data


if __name__ == '__main__':
    import logging

    # Create a custom logger
    logger = logging.getLogger(__name__)
    logger.info('get_user.py user is the main caller')
    from csv_export import export_to_csv
    user_object = Users()
    result = user_object.get_all_data(URL)
    export_to_csv(result)
    logger.info('DONE')

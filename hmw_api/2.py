import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на Яндекс.Диск"""
        headers = {'Authorization': f'OAuth {self.token}'}
        file_name = file_path.split('\\')[-1]
        res = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={file_name}', headers=headers).json()
        with open(file_path, 'rb') as file:
            try:
                requests.put(res['href'], files={'file': file})
            except KeyError:
                print(res)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь до файла на компьютере: ')
    token =  input('Введите токен Яндекс.Диска: ')

    uploader = YaUploader(token)
    uploader.upload(path_to_file)

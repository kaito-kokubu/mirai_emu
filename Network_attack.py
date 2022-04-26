import subprocess
import datetime


class DownloadError(Exception):
    """Download Error"""
    pass

def main():
    file_id = '1DyKXHA6mv4RVz4rQcsxLb4OEmUjJTjaX'
    file_name = 'dummpyfile'
    print(f"download start time: {datetime.datetime.now()}")
    cp = subprocess.run(f'wget "https://drive.google.com/uc?export=download&id={file_id}" -O ./{file_name}', shell=True)
    print(f"download finish time: {datetime.datetime.now()}")
    if cp == 0:
        raise DownloadError('We could not download dummy file...')
    else:
        return


if __name__ == '__main__':
    main()

#https://drive.google.com/file/d/1DyKXHA6mv4RVz4rQcsxLb4OEmUjJTjaX/view?usp=sharing
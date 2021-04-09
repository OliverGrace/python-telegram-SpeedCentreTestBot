import urllib.parse


def sub_convert(link):
    link = urllib.parse.quote(link, safe='')
    return 'https://转换前端/sub?target=clash&new_name=true&url=' + link + '&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online_Full_NoAuto.ini'
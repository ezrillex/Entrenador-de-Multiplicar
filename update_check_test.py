import urllib.request

url = 'https://ezrillex.club/uploads/multiplication-trainer-updates/latest-version.txt'
with urllib.request.urlopen(url) as response:
    webContent = response.read()

webContent = str(webContent)


write = False
version = ""
for x in range(len(webContent)):
    if webContent[x] == "'":
        write = True
        z = x
    if write is True:
        version += webContent[x]
    if webContent[x] == "'" and z > x:
        write = False
print(version)

urllib.request.urlretrieve(url, 'latest-version.txt')


files_url = 'https://ezrillex.club/uploads/multiplication-trainer-updates/latest-version-files/update.zip'

urllib.request.urlretrieve(files_url, "update_files.zip")


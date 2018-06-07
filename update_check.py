import urllib.request
import zipfile
from trainer import version

print("Checking www.ezrillex.club for new updates...")

url = 'https://ezrillex.club/uploads/multiplication-trainer-updates/latest-version.txt'
with urllib.request.urlopen(url) as response:
    webContent = response.read()

webContent = str(webContent)

write = False
server_version = ""

for x in range(len(webContent)):
    if webContent[x].isdigit() is True or webContent[x] == '.':
        server_version += webContent[x]
    if webContent[x] == ";":
        break

server_version = float(server_version)
print(server_version)

update_now = None
if version() == server_version:
    print("The latest version is already installed")
elif version() < server_version:
    print("There are new updates available. ¿Do you want to update?")
    print("1 - YES, 2 - NO")
    update_now = int(input())
elif version() > server_version:
    print("Warning: Actual version %s is greater than the server latest %s version!" % (version(), server_version))

if update_now == 1:
    # This downloads the file so that if i want later I can add a hash after the latest version number to check the file
    # integrity.

    print("Update in progress...")
    print("Downloading new version info...")
    urllib.request.urlretrieve(url, 'latest-version.txt')

    files_url = 'https://ezrillex.club/uploads/multiplication-trainer-updates/latest-version-files/update_files.zip'

    print("Downloading new version files... This might take a few minutes depending on your internet speed.")
    urllib.request.urlretrieve(files_url, "update_files.zip")

    print("Checking downloaded file integrity...")
    # TODO file check integrity.

    print("Extracting new version files...")
    file = zipfile.ZipFile('update_files.zip')
    file.extractall()
    file.close()

    print("Launching updater module...")
    # TODO launch a updater.exe script to do the proper file updates outside the program

    # In the updater script this will go there.
    print("Converting incompatible old files...")
    print("Updated succesfully to %s!" % server_version)
elif update_now == 2:
    print("No updates will be applied. Remember if you find any bug or glitch, new updates might include a fix.")


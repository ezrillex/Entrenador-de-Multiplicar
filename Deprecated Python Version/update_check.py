def update_check():
    import urllib.request
    import zipfile
    from trainer import version
    import hashlib
    import os
    import ctypes

    class AdminStateUnknownError(Exception):
        """Cannot determine whether the user is an admin."""
        pass

    def is_user_admin():
        # type: () -> bool
        """Return True if user has admin privileges.

        Raises:
            AdminStateUnknownError if user privileges cannot be determined.
        """
        try:
            return os.getuid() == 0
        except AttributeError:
            pass
        try:
            return ctypes.windll.shell32.IsUserAnAdmin() == 1
        except AttributeError:
            raise AdminStateUnknownError

    def check_file_integrity(file_path):
        print("Checking file integrity for errors...")
        with zipfile.ZipFile(file_path) as file:
            test = file.testzip()
            if test is None:
                return True
            elif test is not None:
                return False

    if is_user_admin() is False:
        print("Warning! You don't have administrator rights. Please run the program with administrator rights in "
              "order to properly install any updates! If you are using the portable version of this software, make "
              "sure you have the appropriate permissions to write files to the directory you store the software.")

    print("Checking redacted for new updates...")

    url = 'redacted'
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
        print("This is either a 'Developer' build or a custom GitHub compile.")

    if update_now == 1:
        print("Update in progress...")
        print("Downloading new version info...")
        urllib.request.urlretrieve(url, 'latest-version.txt')

        files_url = 'redacted/uploads/multiplication-trainer-updates/latest-version-files/update_files.zip'

        print("Downloading updated files... This might take a few minutes depending on your internet speed.")
        urllib.request.urlretrieve(files_url, "update_files.zip")

        print("Checking downloaded file integrity...")
        if check_file_integrity('update_files.zip') is False:
            print("ERROR! Downloaded files are corrupted! Update will now abort. Please try again. If the problem "
                  "persists try downloading the update directly from the website <website-url>.")
            os.remove('update_files.zip')
            os.remove('latest-version.txt')
        else:
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


update_check()

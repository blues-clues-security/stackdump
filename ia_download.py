#####################################################################
#   Author: Bloodvault
#   Date:   November 2021
#####################################################################
# @note: Imports
import internetarchive as ia
from getpass import getpass

# @note: Create a config file to store the Archive.org login session
try:
    cfg_file = 'F:\\Coding Projects\\Cheatsh\\archive.org\\ia.ini'
except:
    pass

# @note: Either use the config file if ran recently, or pass new credentials
try:
    ia.get_session(config_file=cfg_file)
except:
    # @note: Prompt for archive.org credentials
    archive_user = input('Enter archive.org email address: ')
    archive_password = getpass('Enter the corresponding password: ')
    ia.configure(username=archive_user,
                password=archive_password, 
                config_file=cfg_file)

# @note: Create networkengineering dump for testing purposes
# ia.download('stackexchange',
#                 # @see: Use this flag to test collecting the correct packages
#                 #dry_run=True,
#                 verbose=True,
#                 ignore_existing=True,
#                 checksum=True,
#                 glob_pattern='networkengineering.stackexchange*.7z',
#                 destdir='F:\\Coding Projects\\Cheatsh\\archive.org\\dump\\networkengineering\\')

# @note: These packages are used to populate Stackdump (https://github.com/sornram9254/stackdump)
# @warning: You'll need to rename the corresponding XML files after unpacking to all lowercase
# @warning: Not going to unzip as the data could be immense
# @see: Download options below commented, if you run every option the command will not download anything
stack_downloads = ['Comments','Posts','Users']
for item in stack_downloads:
    ia.download('stackexchange',
                # @note: Use this flag to test collecting the correct packages
                #dry_run=True,
                verbose=True,
                # @note: Ignore_existing will not download if filename exists, checksum will evaluate the checksum of files
                ignore_existing=True,
                checksum=True,
                glob_pattern=f'stackoverflow*{item}*.7z',
                destdir='F:\\Coding Projects\\Cheatsh\\archive.org\\dump\\')
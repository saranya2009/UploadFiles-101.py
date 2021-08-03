import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A11eOZGeePtxtOjqN3Jer1iFi-G-eysiZ-cTiucLp_7yJIlBBFCPIMvl_rgAI6ggEf5-KSp25zUuT7JBq7i3k2S9CNcuKzyupiSZPU16WawNEM5T1Sjzlp7kNRFFizwXufYJxU9OomYE'
    transferData = TransferData(access_token)
    print('Enter the path of the file like OneDrive/Desktop/Python ')
    print('Note: The above path is an example')
    file_from = input("Enter the folder path to transfer : ")
    print('Type the path of the file like this including the name of the folder you wanted to transfer')
    print('this is for an example /test_dropbox/test.txt')
    file_to = input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved successfully !")

main()
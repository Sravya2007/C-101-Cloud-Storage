import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AvqmHba3WU15kI6niCAqb-cCkuefum6BDBdLHsJVOb8bm09QBaOK-IXH8lmZX6r_jATRQhPFtQrT3qQ3TFAsea8tjeALIA_ySGDsoe8a472CyoWCNOYWS0Q3AAi8-8FapjqnD1w'
    transferData = TransferData(access_token)

    file_from = input('Enter the file name to transfer: ')
    #/folder_name_in_dropbox/filename.ext
    file_to = input("Enter the destination where the file should be transferred: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File uploaded!")

if __name__ == '__main__':
    main()
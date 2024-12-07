from minio import Minio
from io import BytesIO

minio_url = "120.46.1.4:9000"
minio_access_key = "mysterious_name"
minio_secret_key = "88888888"

# with open("try.pdf", "rb") as f:
#     data = f.read()


def get_download_url(file_name, type) -> str:
    return "http://" + minio_url + "/zxb/" + type + "/" + file_name


class MinioClient:
    def __init__(self):
        self.client = Minio(endpoint=minio_url, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

    def upload_file(self, data, file_name, type):
        if type == "jpg" or type == "jpeg":
            file_name = "jpg/" + file_name
            content_type = "image/jpeg"
        elif type == "png":
            file_name = "png/" + file_name
            content_type = "image/png"
        elif type == "txt":
            file_name = "txt/" + file_name
            content_type = "text/plain"
        elif type == "pdf":
            file_name = "pdf/" + file_name
            content_type = "application/pdf"
        elif type == "zip":
            file_name = "zip/" + file_name
            content_type = "application/zip"
        elif type == "word":
            file_name = "word/" + file_name
            content_type = "application/msword"
        elif type == "excel":
            file_name = "excel/" + file_name
            content_type = "application/vnd.ms-excel"
        elif type == "ppt":
            file_name = "ppt/" + file_name
            content_type = "application/vnd.ms-powerpoint"
        elif type == "rar":
            file_name = "rar/" + file_name
            content_type = "application/x-rar-compressed"
        else:
            raise ValueError("Invalid file type")
        self.client.put_object("zxb", file_name, BytesIO(data), len(data), content_type=content_type)


# if __name__ == "__main__":
#     print(get_download_url("try.pdf", "pdf"))

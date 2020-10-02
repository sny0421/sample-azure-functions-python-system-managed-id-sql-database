import os
import requests
import struct
import sys

def get_sql_access_token():
    # 環境変数を読み込み
    resource_uri = os.environ["RESOURCE_URI_SQL"]
    identity_endpoint = os.environ["IDENTITY_ENDPOINT"]
    identity_header = os.environ["IDENTITY_HEADER"]
    # 認証用 URI とヘッダーの作成
    token_auth_uri = f"{identity_endpoint}?resource={resource_uri}&api-version=2017-09-01"
    head_msi = {'secret':identity_header}
    # アクセストークンの取得
    response = requests.get(token_auth_uri, headers=head_msi)
    access_token = bytes(response.json()['access_token'], 'utf-8')
    expire_token = b""
    for i in access_token:
            expire_token += bytes({i})
            expire_token += bytes(1)
    token_struct = struct.pack("=i", len(expire_token)) + expire_token 
    return token_struct

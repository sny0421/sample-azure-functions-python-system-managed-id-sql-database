# Query Azure SQL Database from Azure Function (Python) by Managed ID

## Azure SQL Database の作成
Azure SQL Database リソースを展開します。
SKU は Basic で構いません。

### Active Directory 管理者の有効化
SQL データベースリソースを選択し、[Active Directory 管理者]をクリックします。
[管理者の設定]をクリックします。
Azure AD に登録されているユーザー（ポータルにサインインしているユーザー）を選択し、[選択]をクリックします。
[保存]をクリックします。

### クライアント IP と Azure サービスからのアクセス許可
[ファイアウォールと仮想ネットワーク]をクリックします。
[Azure サービスおよびリソースにこのサーバーへのアクセスを許可する]を[はい]にします。
[クライアント IP アドレス]で接続元デバイスの IP を追加します。
[保存]をクリックします。

## データベース
### テーブル作成
データベースリソースを選択し、[クエリ エディター (プレビュー)]をクリックします。
[Active Directory 認証]で[(現在ログインしているユーザー名) として続行]をクリックします。
クエリ エディターに次のクエリを入力し、テーブルを作成します。

```
CREATE TABLE test(id NCHAR(5) PRIMARY KEY, name NVARCHAR(256))
```

### Azure Function へのアクセス権設定
クエリ エディターに次のクエリを入力し、Azure Function へのアクセス権を付与します。

```
CREATE USER "sample-azfunc-mid" FROM EXTERNAL PROVIDER;
ALTER ROLE db_datareader ADD MEMBER "sample-azfunc-mid";
ALTER ROLE db_datawriter ADD MEMBER "sample-azfunc-mid";
ALTER ROLE db_ddladmin ADD MEMBER "sample-azfunc-mid";
```


https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions

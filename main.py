from apiclient.discovery import build
import json
import time

# APIを使うための情報を設定
DEVELOPER_KEY = "AIzaSyDkIyxC7xNhWvl0SjY5ebxkEGJQQUYEkgo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

item_list = []
search = youtube.search().list(
    part = "snippet",
    # チャンネルIDはYouTubeホーム画面URLから取得、↓の***の部分
    # https://www.youtube.com/channel/***/featured
    channelId = "UCqm3BQLlJfvkTsX_hvm0UmA",
    maxResults = 50 # 一回で取得する動画情報数
)
data = search.execute()

# 一回じゃ取りきれないので何回か実行する
while True:
    item_list = item_list + data["items"]
    print(len(item_list))
    print(data["pageInfo"])
    # 取りきったら終了
    if "nextPageToken" not in data:
        break
    time.sleep(1)
    search = youtube.search().list_next(search, data)
    data = search.execute()

# 取得したデータを保存
with open('movieData.json', 'w',  encoding="utf8") as f:
    json.dump(item_list, f, ensure_ascii=False)

import json
import urllib.request

# さっきのJSONファイル
json_file = open('movieData.json', 'r')
data = json.load(json_file)
json_file.close()

i = 1
for line in data:
    # 画像ファイル名
    image_file = "/Users/genki/watame/" + str(i) + ".jpg"
    i += 1
    # URLの場所を指定して取得
    url = line["snippet"]["thumbnails"]["medium"]["url"]
    print(line["snippet"]["title"])
    # urllibライブライを使って画像を保存
    tgt = urllib.request.urlopen(url).read()
    with open(image_file, mode='wb') as f:
        f.write(tgt)
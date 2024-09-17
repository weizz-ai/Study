import requests
import json

# 歌曲ID
song_id = input(" 请输入歌曲ID：")

# 网易云音乐评论API的URL
url = f"https://music.163.com/api/v1/resource/comments/R_SO_4_{song_id}?limit=20&offset=0"

# 发送请求
response = requests.get()

# 检查请求是否成功
if response.status_code == 200:
    # 解析JSON数据
    comments_data = response.json()
    # print(response.json())
    # 获取评论列表
    comments_list = comments_data['comments']

    # 遍历评论列表并打印
    for comment in :
        print(comment['content'])  # 打印评论内容
else:
    print("请求失败，状态码：", response.status_code)
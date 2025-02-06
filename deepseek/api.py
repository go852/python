import requests

API_KEY = 'sk-b2997eadee2844eb9cc9a31c99665aba'
API_URL = 'https://api.deepseek.com/v1/analyze'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

payload = {
    'text': '这是一个示例文本，用于测试 DeepSeek API。',
    'language': 'zh'
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    print('分析结果:')
    print(data)
else:
    print(f'请求失败，状态码: {response.status_code}')
    print(f'错误信息: {response.text}')
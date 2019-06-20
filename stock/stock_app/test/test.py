import json

js = json.loads('{"\u6728\u6613\u67d0\u95f2\u4eba":"中国"}')
print(js)
print(json.dumps(js))
print(json.dumps(js, ensure_ascii=False))

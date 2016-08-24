'''
python3 crawler_server.py で実行
localhost:8080?query=hogehoge にアクセス
すると, saved_image以下にhogehogeに関する画像が保存される.

ポート番号のプロセスが残っている場合は
lsof -i :8080
でPIDを調べて
kill
する.
'''

from bottle import route, run, request
from get_pages import get_pages_from_google

# curl -X GET "http://127.0.0.1:8080/get_pages?query=react+Redux"
@route('/get_pages')
def get_pages():
    query = request.query.get('query')
    get_pages_from_google(query)
    return 'got page'

run(host='localhost', port=8080, debug=True, reloader=True)

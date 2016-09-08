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

from bottle import route, run, request, response
from get_pages import get_pages_from_google
import subprocess

# curl -X GET "http://127.0.0.1:8080/get_pages?query=react+Redux"
@route('/get_pages')
def get_pages():
    print("get_pagesへアクセスされました. ")
    response.set_header('Access-Control-Allow-Origin','*')
    query = request.query.get('query')
    for i in query:
        cmd = "swipl -q -f ./prolog/main.pl -t main '%s' > query.txt"(i)
        subprocess.call( cmd, shell=True)
        f = open('./query.txt', 'r')
        str_list = f.readlines()
        str_list = map(str.strip,str_list) #改行削除
        str_set = set(str_list)
    get_pages_from_google(query)
    return 'got page'

@route('/test')
def test():
    cmd = "swipl -q -f ./prolog/main.pl -t main 'javascript' > query.txt"
    subprocess.call( cmd, shell=True)
    return "test"

run(host='localhost', port=8080, debug=True, reloader=True)

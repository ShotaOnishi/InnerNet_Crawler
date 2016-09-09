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
from get_pages import get_pages_from_google, get_pages_from_qiita
import subprocess

# curl -X GET "http://127.0.0.1:8080/get_pages?query=react+Redux"
@route('/get_pages')
def get_pages():
    print("[CRAWLER_SERVER]get_pagesへアクセスされました. ")
    response.set_header('Access-Control-Allow-Origin','*')
    query = request.query.get('query')
    query_list=query.split()
    print("[CRAWLER_SERVER]query_list=" + str(query_list))
    for i in query_list:
        cmd = "swipl -q -f ./prolog/main.pl -t main '%s' > query.txt" %(i)
        subprocess.call( cmd, shell=True)
        f = open('./query.txt', 'r')
        str_list = f.readlines()
        str_list = map(str.strip,str_list) #改行削除
        str_set = set(str_list)
    str_list = list(str_set)
    thesaurus = " ".join(str_list)
    print("[CRAWLER_SERVER]str_list="+str(str_list))
    print("[CRAWLER_SERVER]query="+query)
    get_pages_from_qiita(query)
    print("[CRAWLER_SERVER]シソーラスでも検索")
    get_pages_from_qiita(thesaurus)
    get_pages_from_google(query)
    print("[CRAWLER_SERVER]シソーラスでも検索")
    get_pages_from_google(thesaurus)
    return 'got page'

@route('/test')
def test():
    cmd = "swipl -q -f ./prolog/main.pl -t main 'javascript' > query.txt"
    subprocess.call( cmd, shell=True)
    return "test"

run(host='localhost', port=8080, debug=True, reloader=True)

import os

def save_pages(tags=None, image=None, title=None, domain=None, url=None):
    '''
    tags: 配列
    image, title, domain, url: string
    '''
    POST_URL = "http://localhost:3000/api/v1/pages"
    image_f = "-F \'page[image]=@/%s\'" % (image)
    title_f = "-F \'page[title]=%s\'" % (title)
    memo_f = "-F \'page[memo]=%s\'" % ("")
    url_f = "-F \'page[url]=%s\'" % (url)
    list_to_hash(tags)
    tags_attributes = list_to_hash(tags)
    tags_attributes_f = "-F \'page[tags_attributes]=%s\'" % (tags_attributes)
    domain_attributes_f = "-F \'page[domain_attributes]=%s\'" % (domain)
    g = dict(image_f=image_f, title_f=title_f, memo_f=memo_f, url_f=url_f, tags_attributes_f=tags_attributes_f, domain_attributes_f=domain_attributes_f, url=POST_URL)
    command = "curl -X POST %(image_f)s %(title_f)s %(memo_f)s %(url_f)s %(tags_attributes_f)s %(domain_attributes_f)s %(url)s" %g
    os.system(command)
    return "saveしました. "

def list_to_hash(tags):
    tags_attributes = ""
    hashes = ""
    for c, t in enumerate(tags):
        base_str = "{\"name\"=>\"%s\"}"
        hash_str = base_str % (t)
        if hashes == "":
            hashes = hash_str
        else:
            hashes = hashes + "," + hash_str
    tags_attributes = '[%s]' % hashes
    return tags_attributes

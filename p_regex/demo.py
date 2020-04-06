import re


def test_re_img():
    with open('img.html','r',encoding='utf-8') as f:
        html = f.read()
        p = re.compile(r'<img.+?str=\"(?P<src>.+?)\".+?>', re.M| re.I)
        list_img = p.findall(html)
        print(list_img)
        for ls in list_img:
            print(ls.replace('&amp;', '&'))

if __name__ == '__main__':
    test_re_img()
import urllib.request as req
import re
from sys import argv


DOMAIN = 'http://www.matematicas.uady.mx'


def get_url(path, default_domain):
    parser = req.urlparse(path)
    if parser.hostname is None:
        return req.urljoin(default_domain, parser.path)
    else:
        return parser.geturl()


def links_from_site(domain):
    u = req.urlopen(domain)
    html_bytes = u.read()
    html = html_bytes.decode('latin-1') #Bad google!
    try:
        links = [u.split('"')[1] for u in re.findall(r'href=[\S]+', html)]
    except:
        print ('Error: malformed href... skiping whole page')
        return []
    abs_links = [get_url(l, DOMAIN) for l in links]
    return abs_links


def crawl(root, links, depth=3):
    if depth <= 0:
        return links
    
    for l in links_from_site(root):
        print ('working on ', l)
        try:
            links[l] += 1
        except:
            links[l] = 1
        
        d = depth - 1
        crawl(l, links, depth=d)
    


if __name__ == '__main__':
    if len(argv) == 1:
        links = {}
        try:
            print (crawl(DOMAIN, links))
        except:
            print (links)
            print ('owwwww... dying')
        
    else:
        for url in argv[1:]:
            print ('\n'.join(links_from_site(url)))

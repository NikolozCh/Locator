import sys, socket, pygeoip, argparse
 class Locator(object):
    def __init__(self, url=False, ip=False, datfile=False):
        self.url = url
        self.ip = ip
        self.datfile = datfile
        self.target = ''
     def query(self):
        try:
            if not self.datfile:
                # .dat default file path goes here, for me it's
                self.datfile = 'N:\\Tools\\IP Locator\\GeoLiteCity.dat'
            if not not self.url:
                print('[*] Translating %s' % (self.url))
                try:
                    self.target += socket.gethostbyname(self.url)
                    print(self.target)
                except Exception:
                    print('\n[!] Failed to Resolve URL')
                    return
            else:
                self.target += self.ip
            print('[*] Querying for Records of %s...\n' % (self.target))
            query_obj = pygeoip.GeoIP(self.datfile)
            for key, val in query_obj.record_by_addr(self.target).items():
                print('%s: %s' % (key, val))
            print('\n[*] Query Complete!')
        except Exception as e:
            print('\n[*] Error Occured: %s' % (e))
            sys.exit(-1)
 if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IP Locator Software')
    parser.add_argument('-u', '--url', help='Locate an IP on a URL', action='store', default=False, dest='url')
    parser.add_argument('-t', '--target', help='Locate The Specified IP', action='store', default=False, dest='ip')
    parser.add_argument('-d', '--dat', help='Custom database filepath', action='store', default=False, dest='datfile')
    args = parser.parse_args()
    gela = Locator(url=args.url, ip=args.ip, datfile=args.datfile)
    gela.query()

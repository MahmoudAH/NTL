import urllib.request,json
def main():
  gata=urllib.request.urlopen("https://www.google.com/").read()
  jsonr=json.load(gata.decode("utf-8"))
  print(gata,type(gata))
if __name__ == '__main__':main()

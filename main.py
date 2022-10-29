import requests
import os
def main():
 path = input("file path >: ")
 if os.path.exists(path):
  lmao = path
  fr = requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(lmao, 'rb')}).json()["data"]["downloadPage"]
  os.system("cls")
  print(fr)
  main()
 else:
  os.system("cls")
  print("invaild path fr")
  main()
main()

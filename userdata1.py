import codecs


def get_webinfo(path):
    web_info={}
    config = codecs.open(path)
    for line in config:
        result = [ele.strip() for ele in line.split('=')]
        web_info.update([result])

    return web_info


def get_userinfo(path):
    user_info=[]
    config=codecs.open(path)
    for line in config:
        user_dict = {}
        result = [ele.strip() for ele in line.split(' ')]
        for r in result:
            account = [ele.strip() for ele in r.split('=')]
            print(account)
            user_dict.update(dict([account]))
        user_info.append(user_dict)
    return user_info


if __name__ == '__main__':
    webinfo = get_webinfo(r'D:\BaiduNetdiskDownload\webinfo.txt')
    for key in webinfo:
        print(key,webinfo[key])
    userinfo = get_userinfo(r'D:\BaiduNetdiskDownload\userinfo.txt')
    for l in userinfo:
        print(l)

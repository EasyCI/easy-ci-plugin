# -*- coding: UTF-8 -*-

import json
import os
import sys

import requests

# 公有参数列表
commonParameter1_flowId = sys.argv[1]
commonParameter2_repoName = sys.argv[2]
commonParameter3_platform = sys.argv[3]

# 私有参数列表
firApiToken = sys.argv[4]
firChangeLog = sys.argv[5]

# 寻找 Android 项目的 bundle_id
bundleId = ''
userHomePath = os.environ['HOME']
appGradlePath = userHomePath + '/easy-ci-workspace/' + commonParameter1_flowId + '/' + commonParameter2_repoName + '/app/build.gradle'
buildGradleFile = open(appGradlePath, 'r')
for currentLine in buildGradleFile.readlines():
    if currentLine.strip().split('"')[0].strip() == 'applicationId':
        bundleId = currentLine.strip().split('"')[1].strip()
        buildGradleFile.close()
        break

headers = {"Content-Type": "application/json"}
payload = '{\"type\" : \"' + commonParameter3_platform.lower() + '\",\"bundle_id\" : \"' + bundleId + '\",\"api_token\" : \"' + firApiToken + '\"}'
r = requests.post("http://api.fir.im/apps", headers=headers, data=payload)

temp = json.loads(r.text)
preview_url = "https://fir.im/" + temp["short"]
key = temp["cert"]["binary"]["key"]
token = temp["cert"]["binary"]["token"]
payload = (
    ('key', key), ('token', token), ('x:name', commonParameter2_repoName), ('x:version', '1.0'), ('x:build', '1'),
    ('x:changelog', firChangeLog))
apkFile = {'file': open(
    userHomePath + '/easy-ci-workspace/' + commonParameter1_flowId + '/' +
    commonParameter2_repoName + '/app/build/outputs/apk/app-debug.apk', 'rb')}
r = requests.post('https://upload.qbox.me', data=payload, files=apkFile)

temp = json.loads(r.text)
download_url = temp['download_url']

print('preview_url : ' + preview_url + '\n' + 'download_url : ' + download_url + '\n0')

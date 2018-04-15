# -*- coding: UTF-8 -*-

import subprocess
import sys

# 公有参数列表
commonParameter1_flowId = sys.argv[1]
commonParameter1_taskId = sys.argv[2]
commonParameter2_repoName = sys.argv[3]
commonParameter3_platform = sys.argv[4]

# 私有参数列表
cloneUrl = sys.argv[5]
triggerBranch = sys.argv[6]

# 待执行命令列表
cmd1 = 'rm -rf ${HOME}/easy-ci-workspace/' + commonParameter1_flowId + '/' + commonParameter1_taskId
cmd2 = 'git clone -b ' + triggerBranch + ' ' + cloneUrl + ' ${HOME}/easy-ci-workspace/' + \
       commonParameter1_flowId + '/' + commonParameter1_taskId + '/' + commonParameter2_repoName
cmd3 = 'du -sh'

# 依次执行上述命令
subprocess.call(cmd1, shell=True)
subprocess.call(cmd2, shell=True)
log = subprocess.call(cmd3, shell=True)

print(log)

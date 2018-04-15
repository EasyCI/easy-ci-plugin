# -*- coding: UTF-8 -*-

import subprocess
import sys

# 公有参数列表
commonParameter1_flowId = sys.argv[1]
commonParameter1_taskId = sys.argv[2]
commonParameter2_repoName = sys.argv[3]
commonParameter3_platform = sys.argv[4]

# 待执行命令列表
cmd1 = 'gradle --warning-mode=none -p ${HOME}/easy-ci-workspace/' + \
       commonParameter1_flowId + '/' + commonParameter1_taskId + '/' + commonParameter2_repoName + ' assembleDebug'

# 依次执行上述命令
log = subprocess.call(cmd1, shell=True)

print(log)

# -*- coding: UTF-8 -*-

import subprocess
import sys

# 公有参数列表
commonParameter1_flowId = sys.argv[1]

# 待执行命令列表
cmd1 = 'rm -rf ${HOME}/easy-ci-workspace/' + commonParameter1_flowId

# 依次执行上述命令
log = subprocess.call(cmd1, shell=True)

print(log)

import subprocess
import sys

# 公有参数列表
commonParameter1_flowId = sys.argv[1]
commonParameter2_repoName = sys.argv[2]
commonParameter3_platform = sys.argv[3]

# 待执行命令列表
cmd1 = 'gradle -v'
cmd2 = 'gradle -p ${HOME}/easy-ci-workspace/' + commonParameter1_flowId + '/' + commonParameter2_repoName + ' clean'

# 依次执行上述命令
subprocess.call(cmd1, shell=True)
log = subprocess.call(cmd2, shell=True)

print(log)

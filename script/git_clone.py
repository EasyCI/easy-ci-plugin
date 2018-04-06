import subprocess
import sys

# 公有参数列表
commonParameter1_flowId = sys.argv[1]
commonParameter2_repoName = sys.argv[2]
commonParameter3_platform = sys.argv[3]

# 私有参数列表
cloneUrl = sys.argv[4]
triggerBranch = sys.argv[5]

# 待执行命令列表
cmd1 = 'rm -rf ${HOME}/easy-ci-workspace/' + commonParameter1_flowId
cmd2 = 'git clone -b ' + triggerBranch + ' ' + cloneUrl + ' ${HOME}/easy-ci-workspace/' + commonParameter1_flowId + '/' + commonParameter2_repoName

# 依次执行上述命令
subprocess.call(cmd1, shell=True)
log = subprocess.call(cmd2, shell=True)

print(log)

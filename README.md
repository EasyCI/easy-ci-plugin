# EasyCI 插件系统

> EasyCI 是一个简易的持续集成服务，帮助软件开发人员快速的实施持续集成，实现编译、测试、打包、发布全流程自动化。

以下为 EasyCI 插件系统部署流程，更多帮助内容请参阅 **[EasyCI 帮助文档](https://github.com/EasyCI/easy-ci-doc/blob/master/README.md)**

## （一）准备

### 运行环境

- Python 3.5+

### 工具

- Git
- pip

## （二）配置

### 配置运行环境

保证系统中安装的 Python 版本为 3.5+，并安装 pip 工具，可以从这里查看 [pip 安装](http://docs.python-guide.org/en/latest/starting/installation/) 方法。

运行以下命令通过 pip 安装 Python 第三方库

```
pip install requests
pip install email
pip install secure-smtplib
```

### 获取插件脚本

通过以下命令，获取源代码

```
git clone -b master https://github.com/EasyCI/easy-ci-plugin.git
```

将获取的源码下 script/ 文件夹内容拷贝到 EasyCI 后端服务部署的同一台主机中，并按照 **[后端服务配置](./install_back_end.md)** 的 `custum.pluginScriptPath` 参数指定的插件路径下。

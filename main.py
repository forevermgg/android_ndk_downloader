# 这是一个示例 Python 脚本。
import hashlib
import os
import platform
import sys
import requests


# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


class AndroidNDKUrlInfo:
    # 下面定义了2个类变量
    system = ""
    url = ""
    size = 0
    sha1 = ""

    def __init__(self, system, url, size, sha1):
        # 下面定义 2 个实例变量
        self.system = system
        self.url = url
        self.size = size
        self.sha1 = sha1
        print(system, "url：", url)


download_android_r21e_linux_info = \
    AndroidNDKUrlInfo("linux",
                      "https://dl.google.com/android/repository/android-ndk-r21e-linux-x86_64.zip",
                      1190670072,
                      "c3ebc83c96a4d7f539bd72c241b2be9dcd29bda9")
download_android_r21e_macos_info = \
    AndroidNDKUrlInfo("macos",
                      "https://dl.google.com/android/repository/android-ndk-r21e-darwin-x86_64.zip",
                      1042617180,
                      "3f15c23a1c247ad17c7c271806848dbd40434738")
download_android_r21e_windows_info = \
    AndroidNDKUrlInfo("windows",
                      "https://dl.google.com/android/repository/android-ndk-r21e-windows-x86_64.zip",
                      1109665123,
                      "fc44fea8bb3f5a6789821f40f41dce2d2cd5dc30"
                      )


def download(androidNDKUrlInfo):
    with open(os.path.basename(androidNDKUrlInfo.url), 'wb') as f:
        response = requests.get(androidNDKUrlInfo.url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50 - done)))
                sys.stdout.flush()
    sys.stdout.write('\n')


def JMSHA1(path):
    sha1get = hashlib.sha1()
    try:
        a = open(fr'{path}', 'rb')
    except FileNotFoundError:
        print('文件路径有误，请输入正确路径！')
    while True:
        b = a.read(128000)  # 这里就是每次读文件放进内存的大小，小心溢出！
        sha1get.update(b)
        if not b:
            break
    a.close()
    jiamijieguo = sha1get.hexdigest()
    return jiamijieguo


def check_download_is_exists(androidNDKUrlInfo):
    if os.path.exists(os.path.basename(androidNDKUrlInfo.url)):
        file_size = os.path.getsize(os.path.basename(androidNDKUrlInfo.url))
        if file_size == androidNDKUrlInfo.size:
            return True
        else:
            return False
    else:
        return False


def showinfo(tip, info):
    print("{}:{}".format(tip, info))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    showinfo("操作系统及版本信息", platform.platform())
    showinfo('获取系统版本号', platform.version())
    showinfo('获取系统名称', platform.system())
    showinfo('系统位数', platform.architecture())
    showinfo('计算机类型', platform.machine())
    showinfo('计算机名称', platform.node())
    showinfo('处理器类型', platform.processor())
    showinfo('计算机相关信息', platform.uname())

    if check_download_is_exists(download_android_r21e_macos_info):
        print(os.path.basename(download_android_r21e_macos_info.url) + " is exists")
        print(JMSHA1(os.path.basename(download_android_r21e_macos_info.url)) + " is exists")
    else:
        download(download_android_r21e_macos_info)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
# https://github.com/android/ndk/wiki/Unsupported-Downloads

# 一个简单的服务器端口通断检测接口

## 使用教程

### Python

1. 下载 `check.py` 与 `requirements.txt`

2. 安装环境

    `pip install -r requirements.txt`

3. 运行脚本

    `python3 check.py`

### PHP

1. 下载 `check.php` 上传到 PHP 环境服务器中

## API

### 接口说明

### 请求方式

`GET`

### 请求地址

`http://yourserver:yourport/check`

### 请求参数

| 参数名  | 是否必须  | 数据类型  | 参数说明  |
| ------------ | ------------ | ------------ | ------------ |
| server  | 是  | string  | 服务器的地址  |
| port  | 是  | int  | 要检测的端口  |

### 响应参数

| 参数名  | 数据类型  | 参数说明  |
| ------------ | ------------ | ------------ |
| http状态码  | int  | 响应状态码，200为正常，400、500为错误  |
| 返回内容  | string  | 端口通断情况，True为通，False为不通，Error为错误  |

### 响应示例

#### 请求

`GET http://yourserver:yourport/check?server=127.0.0.1&port=80`

#### 响应

`http状态码：200`

`返回内容：True`

#### 错误码说明

| 响应代码  | 错误码说明  |
| ------------ | ------------ |
| 400  | 无效参数。请检查主机和端口的值。  |
| 500  | 检查端口状态时出错。  |
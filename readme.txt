#CQS管道数据导入工具 (C)

##使用前环境要求：
1.windows或者Mac 不过mac 批处理脚本无法用，只能自己到python IDE手敲
2.python3.x 版本 带path安装，即有python3.x环境
3.通过以下cmd命令安装依赖的库
  pip install openpyxl
  pip install cx_Oracle
  注意，其中的cx_Oracle有可能在你pip install 的时候报错,这时候请去官网下载exe
  或者网上有专门的教程，http://www.cnblogs.com/restran/p/4787609.html 按照步骤
  来就好

##功能：
批量导入管道等级表和索引表里的相应内容导入数据库

##使用方法：
1.将需要导入的索引表和等级表复制到本文件夹下
2.点开start.bat脚本开始处理

##注意事项：
1.excel文件的命名：索引表一定要包含"索引表"三个字，等级表同理，其他随便命名
  示范：xxxx001索引表.xlsx
2.excel 文件的格式：
  要导入的excel格式要和范本文件夹下的示范excel一致，这样基本不会出错
3.不要将无关紧要的excel放置到本目录谢谢

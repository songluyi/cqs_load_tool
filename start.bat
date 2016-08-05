@ECHO OFF&PUSHD %~DP0 &TITLE 管道等级表+索引表批量导入工具
mode con cols=70 lines=30
color A
Rd "%WinDir%\system32\test_permissions" >NUL 2>NUL
Md "%WinDir%\System32\test_permissions" 2>NUL||(Echo 请使用右键管理员身份运行！&&Pause >nul&&Exit)
Rd "%WinDir%\System32\test_permissions" 2>NUL
SetLocal EnableDelayedExpansion
cd bin
:Menu
Cls
@ echo.　
@ echo.            ##    ## ######## ########  #### ##    ## 
@ echo.            ###   ## ##       ##     ##  ##  ###   ## 
@ echo.            ####  ## ##       ##     ##  ##  ####  ## 
@ echo.            ## ## ## ######   ########   ##  ## ## ## 
@ echo.            ##  #### ##       ##   ##    ##  ##  #### 
@ echo.            ##   ### ##       ##    ##   ##  ##   ### 
@ echo.            ##    ## ######## ##     ## #### ##    ## 
@ echo.                                              ---NIMS
@ echo.
@ echo.　　　　　           菜 单 选 项
@ echo.
@ echo.   A.       导入excel格式检测（请务必检查）→ 请输入1
@ echo.
@ echo.   B.       导入全部目录下excel数据→ 请输入2
@ echo.
@ echo.   C.       续传全部目录下excel数据→ 请输入3
@ echo. 
@ echo.   D.       恢复数据库中历史版本的数据→ 请输入4
@ echo. 
@ echo.   E.       删除数据库中历史版本的数据→ 请输入5
@ echo.  
@ echo.            PS:目录下生成相应的excel文件。当导入发生问题时，可备用。
@ echo.
set /p xj=     输入数字按回车：
if /i "%xj%"=="1" Goto Check
if /i "%xj%"=="2" Goto All
if /i "%xj%"=="3" Goto ContinueAll
if /i "%xj%"=="4" Goto Recover 
if /i "%xj%"=="5" Goto Delete

:All
@ echo.
ECHO 　　　warning:并行运行python脚本..当六个框均运行结束退出后方可退出..
ECHO 　　　执行索引表插入..请稍等..
start python "/bin/cqs_index.py"
@ echo.
ECHO 　　　执行元件表插入..请稍等..
start python "cqs_items.py"
@ echo.
ECHO 　　　执行壁厚表插入..请稍等..
start python "cqs_pipe_thickness.py"
@ echo.
ECHO 　　　执行压力温度表插入..请稍等..
start python "cqs_pt_rating.py"
@ echo.
ECHO 　　　执行注释表插入..请稍等..
start python "cqs_note.py"
@ echo.
ECHO 　　　执行支管连接表插入 数据会达到上万行 ..请耐心等待..
python "cqs_branch_connect.py"
@ echo.
ECHO 　　　正在上传至FTP，上传完后会仍旧保留目录下的excel..请稍等..
python "about_ftp.py"

ping -n 5 127.1>nul 
goto menu

:ContinueAll
@ echo.
ECHO 　　　执行索引表插入..请稍等..
start python "cqs_index.py"
@ echo.
ECHO 　　　执行元件表插入..请稍等..
start python "cqs_items.py"
@ echo.
ECHO 　　　执行壁厚表插入..请稍等..
start python "cqs_pipe_thickness.py"
@ echo.
ECHO 　　　执行压力温度表插入..请稍等..
start python "cqs_pt_rating.py"
@ echo.
ECHO 　　　执行注释表插入..请稍等..
start python "cqs_note.py"
@ echo.
ECHO 　　　执行支管连接表插入 数据量较多..请耐心等待..
python "cqs_branch_connect.py"
ECHO 　　  warning：并行运行python脚本..当六个框均运行结束退出后方可退出..
ping -n 5 127.1>nul
@ echo.
ECHO 　　　执行进行续传的数据修改..请稍等..
python "continue_load.py"
@ echo.
ECHO 　　　正在上传至FTP..请稍等..
python "about_ftp.py"
goto menu

:Recover
@ echo.
ECHO 　　　正在执行中..请稍等..
python recover_db.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:Delete
@ echo.
ECHO 　　　正在执行中..请稍等..
python delete_db.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:Check
@ echo.
ECHO 　　　正在执行中..请稍等..
python check_legal.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

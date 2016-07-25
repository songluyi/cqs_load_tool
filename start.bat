@ECHO OFF&PUSHD %~DP0 &TITLE 管道等级表+索引表批量导入工具
mode con cols=70 lines=30
color A
Rd "%WinDir%\system32\test_permissions" >NUL 2>NUL
Md "%WinDir%\System32\test_permissions" 2>NUL||(Echo 请使用右键管理员身份运行！&&Pause >nul&&Exit)
Rd "%WinDir%\System32\test_permissions" 2>NUL
SetLocal EnableDelayedExpansion

:Menu
Cls
@ echo.            ##    ## ######## ########  #### ##    ## 
@ echo.            ###   ## ##       ##     ##  ##  ###   ## 
@ echo.            ####  ## ##       ##     ##  ##  ####  ## 
@ echo.            ## ## ## ######   ########   ##  ## ## ## 
@ echo.            ##  #### ##       ##   ##    ##  ##  #### 
@ echo.            ##   ### ##       ##    ##   ##  ##   ### 
@ echo.            ##    ## ######## ##     ## #### ##    ## 
@ echo.
@ echo.　　　　　         菜 单 选 项
@ echo.
@ echo.   A.       导入索引表 → 请输入1
@ echo.
@ echo.   B.       导入等级表的元件表 → 请输入2
@ echo.
@ echo.            导入等级表的管道壁厚表→ 请输入3
@ echo. 
@ echo.            导入等级表的管道温度压力额定表 → 请输入4
@ echo.
@ echo.            导入等级表的支管连接表 → 请输入5
@ echo. 
@ echo.   C.       导入全部目录下excel数据→ 请输入9
@ echo.  
@ echo.            PS:目录下生成相应的excel文件当导入发生问题时，可备用。
set /p xj=     输入数字按回车：
if /i "%xj%"=="1" Goto Index
if /i "%xj%"=="2" Goto Item
if /i "%xj%"=="3" Goto Thickness
if /i "%xj%"=="4" Goto Rating
if /i "%xj%"=="5" Goto Connect
if /i "%xj%"=="9" Goto All

@ echo.
echo      选择无效，请重新输入
ping -n 2 127.1>nul 
goto menu
:Index
@ echo.
ECHO 　　　正在执行中..请稍等..
python cqs_index.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:Item
@ echo.
ECHO 　　　正在执行中..请稍等..
python cqs_items.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:Thickness
@ echo.
ECHO 　　　正在执行中..请稍等..
python cqs_pipe_thickness.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:Rating
@ echo.
ECHO 　　　正在执行中..请稍等..
python cqs_pt_rating.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:Connect
@ echo.
ECHO 　　　正在执行中..请稍等..
python cqs_branch_connect.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu

:All
@ echo.
ECHO 　　　执行索引表插入..请稍等..
python cqs_index.py
@ echo.
ECHO 　　　执行元件表插入..请稍等..
python cqs_items.py
@ echo.
ECHO 　　　执行壁厚表插入..请稍等..
python cqs_pipe_thickness.py
@ echo.
ECHO 　　　执行压力温度表插入..请稍等..
python cqs_pt_rating.py
@ echo.
ECHO 　　　执行支管连接表插入 数据会达到上万行 ..请耐心等待..
python cqs_branch_connect.py
ECHO 　　　已经执行完成正在返回菜单..请稍等..
ping -n 3 127.1>nul 
goto menu
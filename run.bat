@echo off
chcp 65001
set PYTHONIOENCODING=utf-8


echo %~dp0output\

echo 读取输出文件...

python %~dp0/excelParseMgr.py %~dp0/source %~dp0/output

echo 完成！

pause
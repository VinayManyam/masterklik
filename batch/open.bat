@echo off
setlocal enabledelayedexpansion
SETLOCAL

TYPE NUL >adoms
TYPE NUL >asis
rem notepad adoms

:runName
Set "names="
set /p names=
if not defined names goto :main
if /I "%names%" Equ "end" goto :main
(
echo %names% >>adoms
)
goto :runName

goto :main



:openlink
set cid=%~1
#start chrome --incognito %cid%
start %cid%
timeout 1 > NUL 
goto :eof

:main
echo "o started"
for /F "delims=" %%a in (adoms) do (
   call :openlink  %%a
 )
  goto :eof

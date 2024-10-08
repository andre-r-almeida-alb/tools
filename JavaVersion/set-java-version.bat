@echo off
setlocal enabledelayedexpansion

set "java_version=%1"
set "java_home="

for /d %%D in ("C:\Program Files\Java\jdk*%java_version%*") do (
    set "java_home=%%D"
)

if not defined java_home (
    echo Could not find Java version %java_version%
) else (
    set "JAVA_HOME=!java_home!"
    set "PATH=!java_home!\bin;%PATH%"
    echo Activated Java version %java_version% (!java_home!)
)

endlocal & set "JAVA_HOME=%JAVA_HOME%" & set "PATH=%PATH%"
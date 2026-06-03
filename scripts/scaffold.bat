@echo off
setlocal
if "%~2"=="" (
  echo Usage: scaffold.bat ^<brief.yaml^> ^<target-directory^>
  exit /b 1
)
set "STARTER_ROOT=%~dp0.."
python -m scaffold --brief "%~1" --target "%~2"
exit /b %ERRORLEVEL%

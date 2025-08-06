@echo off
echo === Windows Shell Switching Demonstration ===
echo Current Command Interpreter: %COMSPEC%
echo Process ID: %RANDOM%

echo.
echo To switch command interpreters, you can use:
echo cmd         - Command Prompt (DOS-style)
echo powershell  - Windows PowerShell
echo pwsh        - PowerShell Core (if installed)
echo exit        - Return to previous interpreter

echo.
echo Example session:
echo ^> powershell
echo PS^> Write-Host "Now in PowerShell"
echo PS^> cmd  
echo ^> echo Now back in Command Prompt
echo ^> exit
echo PS^> exit
echo Back to original interpreter

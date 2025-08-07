@echo off
REM Custom aliases for Lacrosse Shoe Customizer (Windows)
doskey ll=dir /A
doskey shoe_orders=cd orders ^& dir
doskey backup_orders=xcopy orders\* backups\ /Y 2^>nul ^|^| echo No orders to backup
doskey clean_temp=del temp\* /Q 2^>nul ^& echo Temp directory cleaned
doskey shoe_status=echo Shoe Customizer Status: Active

echo Custom aliases loaded for Windows!
echo Available commands:
echo   ll - detailed file listing
echo   shoe_orders - navigate to orders directory  
echo   backup_orders - backup all orders
echo   clean_temp - clean temporary files
echo   shoe_status - show application status


14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ mkdir test_project

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ echo "sample text"> file1.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ cp file1.txt file2.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ less file2.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ mv file2.txt renamed_file.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ rm rename_file.txt
rm: cannot remove 'rename_file.txt': No such file or directory

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ rm renamed_file.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ echo "another file" > file3.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ mkdir backup_folder

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ cp file1.txt. file3.txt backup_folder/
cp: cannot stat 'file1.txt.': No such file or directory

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ cp file1.txt file3.txt backup_folder

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ ls -1 backup_folder
file1.txt
file3.txt

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ echo $0
/usr/bin/bash

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ sh
sh: __git_ps1: command not found

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2
$ exit
exit

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ nano ~/.bashrc

14752@LAPTOP-7B26NLN9 MINGW64 ~/OneDrive/desktop/Incident-Response-Analysts-/python_2 (main)
$ source ~/.bashrc
[14752@LAPTOP-7B26NLN9 CustomPrompt python_2]$
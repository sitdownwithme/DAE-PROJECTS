# Root Cause Analysis (RCA)

**Incident Title:**  
PowerShell Navigation Errors and Missing `.gitignore` in Project Setup  

**Date of Incident:**  
September 2025  

**Author:**  
Jordan Fields  

---

## 1. Incident Description
While setting up the Scout-Connect project, repeated errors occurred in PowerShell when attempting to change directories and check project files. Specific issues included:  
- `cd 6 month` failed due to unquoted folder names with spaces.  
- `cd C:\Projects\Scout-Connect` failed because the path did not exist.  
- `dir /b` failed because PowerShell interprets `/b` as a path, not a valid flag.  
- `.gitignore` file was missing when attempting to check it with `type .gitignore`.  

---

## 2. Impact
- Blocked progress on Days 1–2 of the project plan.  
- Lost time troubleshooting navigation errors.  
- Confusion around correct project directory (`DAE-PROJECTS` vs `Scout-Connect`).  
- Missing `.gitignore` could have allowed unnecessary files (e.g., `venv/`, `.env`) to be pushed to GitHub.  

---

## 3. Root Cause
- **Incorrect path usage:** Tried to `cd` into folders that did not exist (e.g., `C:\Projects\Scout-Connect`).  
- **Spaces in folder names:** Did not wrap `"6 month"` in quotes when using `cd`.  
- **Wrong command syntax:** Used `dir /b` (CMD syntax) in PowerShell instead of `dir -Name`.  
- **File not created:** `.gitignore` had not been created yet, but verification commands were run as if it existed.  

---

## 4. Contributing Factors
- Switching between Windows Command Prompt syntax and PowerShell syntax.  
- Misalignment between planned folder structure (`Scout-Connect`) and actual repository folder (`DAE-PROJECTS`).  
- Lack of initial check that required files (`.gitignore`) were actually created.  

---

## 5. Corrective Actions
- Standardize project directory naming to avoid spaces (`Scout-Connect`, not `6 month`).  
- Always use quotes for folders with spaces when navigation is required.  
- Use PowerShell-native commands (`dir -Name`, `ls`, `Get-ChildItem`) instead of CMD switches.  
- Create `.gitignore` immediately after initializing the repo to prevent confusion and protect sensitive files.  

---

## 6. Preventive Actions
- Document a one-time **setup checklist** for new projects:  
  - Verify correct folder exists before `cd`.  
  - Create `.gitignore` and `.env.example` on Day 1.  
  - Confirm paths with `pwd` or `Get-Location`.  
- Standardize naming convention: all new projects go into `C:\Users\<User>\Projects\Scout-Connect` (no spaces, consistent case).  
- Train on differences between **PowerShell vs CMD** commands.  

---

## 7. Verification
- Verified navigation works with:  
  ```powershell
  cd "C:\Users\14752\OneDrive\Desktop\DAE-PROJECTS"
  dir -Name
  ```
- Verified `.gitignore` created with:  
  ```powershell
  New-Item .gitignore
  ```
- Verified correct repo linked with:  
  ```powershell
  git remote -v
  ```  

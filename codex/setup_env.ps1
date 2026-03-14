param(
    [string]$PythonExe = "python",
    [string]$VenvDir = ".venv"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
Set-Location $PSScriptRoot

& $PythonExe -m venv $VenvDir

$VenvPython = Join-Path $PSScriptRoot "$VenvDir\Scripts\python.exe"

& $VenvPython -m pip install --upgrade pip
& $VenvPython -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")

Write-Host "Environment ready at $VenvDir"
Write-Host "Next: powershell -ExecutionPolicy Bypass -File .\run_notebook.ps1"

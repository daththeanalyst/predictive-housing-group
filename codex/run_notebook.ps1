param(
    [string]$PythonExe = ".\.venv\Scripts\python.exe",
    [string]$Notebook = "london_price_analysis.ipynb",
    [string]$OutputDir = ".\outputs",
    [switch]$InPlace
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest
Set-Location $PSScriptRoot

if (-not (Test-Path $PythonExe)) {
    $PythonExe = "python"
}

$NotebookPath = Join-Path $PSScriptRoot $Notebook
if (-not (Test-Path $NotebookPath)) {
    throw "Notebook not found: $NotebookPath"
}

if ($InPlace) {
    & $PythonExe -m jupyter nbconvert `
        --to notebook `
        --execute `
        --inplace `
        --ExecutePreprocessor.timeout=0 `
        $NotebookPath
    Write-Host "Executed notebook in place: $Notebook"
    exit 0
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$OutputNotebook = Join-Path $OutputDir ("london_price_analysis_executed_{0}.ipynb" -f $timestamp)

& $PythonExe -m jupyter nbconvert `
    --to notebook `
    --execute `
    --output $OutputNotebook `
    --ExecutePreprocessor.timeout=0 `
    $NotebookPath

Write-Host "Executed notebook written to: $OutputNotebook"

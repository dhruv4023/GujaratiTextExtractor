# Set the project directory and virtual environment name
$venvName = "venv"

# Check if the virtual environment folder exists
$venvExists = Test-Path ($venvName)
New-Item -ItemType Directory -Path ".\temp"
New-Item -ItemType Directory -Path ".\outputs"
if (-not $venvExists) {
    # Create virtual environment if it doesn't exist
    Write-Host "Creating virtual environment..."
    python -m venv $venvName
}
Write-Host "Activate venv"
& venv\Scripts\Activate.ps1
Write-Host "Installing dependencies..."
python -m pip install -r "requirements.txt"
param(
    [string] $environmentName
)


function main()
{
    Write-Host "Setting up virtualenv"
    SetupVirtualenv
}

function SetupVirtualenv()
{
    if (-not (Test-Path env))
    {
        Write-Host "Creating virtualenv in .\env"
        python -m venv env
    }

    try
    {
        . env\scripts\activate.ps1
        python -m pip install --upgrade pip
        Write-Host "Installing dependencies"
        pip install -r requirements.txt
        python -m pytest $testsuitePath
    }
    finally
    {
        deactivate
    }
}


main

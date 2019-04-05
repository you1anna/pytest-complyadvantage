param
(
	[string]$testsuitePath = "tests"
)

try
{
    Write-Host "Running tests"
    . env\scripts\activate.ps1
	python -m pytest $testsuitePath
    # py.test -v $testsuitePath -n auto
}
finally
{
    deactivate
}

pytest --cov=app --cov-fail-under=90
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
behave

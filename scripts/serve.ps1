# Starts the real Jekyll dev server with all the local-machine env vars this
# setup needed:
#   - PATH rebuilt from the registry (Ruby's install added to User PATH,
#     which processes spawned before that change won't inherit)
#   - SSL_CERT_FILE pointed at a CA bundle patched with this network's
#     Zscaler TLS-inspection root CA (see README for how that was derived)
#   - RUBYOPT loading ruby_compat_shim.rb, working around Liquid 4.0.3
#     calling the Object#tainted? API Ruby 3.2+ removed
#
# Always wipes _site/, .jekyll-cache/, and .jekyll-metadata before starting.
# A restart against leftover build artifacts has, more than once, served a
# totally different (and wrong) stylesheet - some leftover cache/metadata
# state occasionally causes Jekyll to serve stale/incorrect output; a fully
# clean build has been reliable every time it's been tested. A full build
# takes the same ~150s either way since --incremental isn't used, so there's
# no speed cost to always starting clean - only a correctness gain.
#
# Run from anywhere: powershell -File scripts\serve.ps1

$RepoRoot = Split-Path -Parent $PSScriptRoot

Remove-Item -Recurse -Force (Join-Path $RepoRoot "_site") -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force (Join-Path $RepoRoot ".jekyll-cache") -ErrorAction SilentlyContinue
Remove-Item -Force (Join-Path $RepoRoot ".jekyll-metadata") -ErrorAction SilentlyContinue

$env:PATH = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")
$env:SSL_CERT_FILE = "C:\Ruby40-x64\cacert.pem"
$env:RUBYOPT = "-r$($RepoRoot -replace '\\','/')/ruby_compat_shim.rb"

Set-Location $RepoRoot
bundle exec jekyll serve --port 4000

# ============================================================
#  ALEK - Instalador automatico
#  Uso: iex (iwr "https://raw.githubusercontent.com/SEU_USUARIO/alek/main/install.ps1").Content
# ============================================================

$ErrorActionPreference = "Stop"

$REPO_USER   = "Alekcode-ui"          # <- troca pelo seu usuario do GitHub
$REPO_NAME   = "alek"
$RAW_BASE    = "https://raw.githubusercontent.com/$REPO_USER/$REPO_NAME/main"
$INSTALL_DIR = "$env:USERPROFILE\.alek"
$MENU_FILE   = "$INSTALL_DIR\menu.py"
$BAT_FILE    = "$INSTALL_DIR\alek.bat"
$PATH_TARGET = "$INSTALL_DIR"

Write-Host ""
Write-Host "  ============================================" -ForegroundColor DarkYellow
Write-Host "    ALEK - Instalador" -ForegroundColor Yellow
Write-Host "  ============================================" -ForegroundColor DarkYellow
Write-Host ""

# ── 1. Verifica Python ──────────────────────────────────────
Write-Host "  [1/4] Verificando Python..." -ForegroundColor Yellow

$pythonCmd = $null
foreach ($cmd in @("python", "python3", "py")) {
    try {
        $ver = & $cmd --version 2>&1
        if ($ver -match "Python 3") {
            $pythonCmd = $cmd
            break
        }
    } catch {}
}

if (-not $pythonCmd) {
    Write-Host "  Python nao encontrado. Instalando..." -ForegroundColor DarkYellow
    $installerUrl = "https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe"
    $installerPath = "$env:TEMP\python_installer.exe"
    Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath
    Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1" -Wait
    Remove-Item $installerPath
    $pythonCmd = "python"
    Write-Host "  Python instalado com sucesso!" -ForegroundColor Green
} else {
    Write-Host "  Python encontrado: $($ver)" -ForegroundColor Green
}

# ── 2. Cria pasta de instalacao ─────────────────────────────
Write-Host ""
Write-Host "  [2/4] Criando pasta de instalacao..." -ForegroundColor Yellow

if (-not (Test-Path $INSTALL_DIR)) {
    New-Item -ItemType Directory -Path $INSTALL_DIR | Out-Null
}
Write-Host "  Pasta: $INSTALL_DIR" -ForegroundColor Green

# ── 3. Baixa o menu.py ──────────────────────────────────────
Write-Host ""
Write-Host "  [3/4] Baixando menu.py..." -ForegroundColor Yellow

Invoke-WebRequest -Uri "$RAW_BASE/menu.py" -OutFile $MENU_FILE
Write-Host "  menu.py baixado com sucesso!" -ForegroundColor Green

# ── 4. Cria comando "alek" no terminal ──────────────────────
Write-Host ""
Write-Host "  [4/4] Criando comando 'alek'..." -ForegroundColor Yellow

# Cria um .bat que chama o menu.py
@"
@echo off
$pythonCmd "$MENU_FILE" %*
"@ | Set-Content -Path $BAT_FILE -Encoding ASCII

# Adiciona ao PATH do usuario (persistente)
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($currentPath -notlike "*$PATH_TARGET*") {
    [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$PATH_TARGET", "User")
    Write-Host "  Adicionado ao PATH!" -ForegroundColor Green
} else {
    Write-Host "  Ja estava no PATH." -ForegroundColor Green
}

# Atualiza PATH da sessao atual
$env:PATH += ";$PATH_TARGET"

# ── Concluido ────────────────────────────────────────────────
Write-Host ""
Write-Host "  ============================================" -ForegroundColor DarkYellow
Write-Host "  Instalacao concluida!" -ForegroundColor Yellow
Write-Host "  Digite 'alek' em qualquer terminal." -ForegroundColor Green
Write-Host "  ============================================" -ForegroundColor DarkYellow
Write-Host ""

# Ja abre o programa
& $pythonCmd $MENU_FILE

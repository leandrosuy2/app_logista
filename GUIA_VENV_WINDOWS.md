# Guia do Ambiente Virtual Windows (venv_windows)

## ✅ Ambiente Virtual Criado com Sucesso!

Foi criado um novo ambiente virtual específico para Windows chamado `venv_windows`, sem modificar o ambiente virtual original (`venv`).

## 📦 Dependências Instaladas

Todas as dependências necessárias foram instaladas:
- Django 4.2.16
- mysqlclient 2.2.7
- bcrypt
- python-dateutil
- WeasyPrint
- reportlab
- pandas
- openpyxl
- requests
- beautifulsoup4

## 🚀 Como Usar o Novo Ambiente Virtual

### Opção 1: Ativar o ambiente virtual (recomendado)

No PowerShell:
```powershell
.\venv_windows\Scripts\Activate.ps1
```

Se houver erro de política de execução:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois execute normalmente:
```powershell
python manage.py runserver
```

### Opção 2: Usar diretamente sem ativar (mais simples)

No PowerShell, execute diretamente:
```powershell
venv_windows\Scripts\python.exe manage.py runserver
```

Outros comandos:
```powershell
# Aplicar migrações
venv_windows\Scripts\python.exe manage.py migrate

# Criar superusuário
venv_windows\Scripts\python.exe manage.py createsuperuser

# Verificar configurações
venv_windows\Scripts\python.exe manage.py check

# Coletar arquivos estáticos
venv_windows\Scripts\python.exe manage.py collectstatic
```

## 📝 Instalar Dependências Adicionais

Se precisar instalar mais pacotes:
```powershell
venv_windows\Scripts\python.exe -m pip install nome_do_pacote
```

Ou instalar todas do requirements.txt:
```powershell
venv_windows\Scripts\python.exe -m pip install -r requirements.txt
```

## 🔍 Verificar Dependências Instaladas

```powershell
venv_windows\Scripts\python.exe -m pip list
```

## 📂 Estrutura

- **venv_windows/** - Novo ambiente virtual para Windows
- **venv/** - Ambiente virtual original (não modificado)

## ⚠️ Notas Importantes

1. O ambiente virtual `venv_windows` é independente do `venv` original
2. Use sempre o Python do `venv_windows` para garantir que está usando as dependências corretas
3. O arquivo `requirements.txt` foi atualizado com todas as dependências necessárias

## 🎯 Comandos Rápidos

```powershell
# Rodar servidor
venv_windows\Scripts\python.exe manage.py runserver

# Rodar servidor em porta específica
venv_windows\Scripts\python.exe manage.py runserver 8001

# Aplicar migrações
venv_windows\Scripts\python.exe manage.py migrate

# Shell do Django
venv_windows\Scripts\python.exe manage.py shell
```

## ✅ Tudo Pronto!

O projeto está configurado e pronto para rodar. Basta executar:

```powershell
venv_windows\Scripts\python.exe manage.py runserver
```

E acessar: **http://127.0.0.1:8000/**


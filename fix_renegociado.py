#!/usr/bin/env python
"""Script para corrigir o campo renegociado na tabela titulo
   IMPORTANTE: Este script NÃO altera dados existentes!
   - Apenas define um valor padrão (DEFAULT 0) para novos registros
   - Atualiza apenas registros que têm NULL (vazio) para 0
   - Preserva todos os valores que já existem (1, 2, etc.)
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from django.db import connection

with connection.cursor() as cursor:
    try:
        # Verificar se o campo existe
        cursor.execute("SHOW COLUMNS FROM titulo LIKE 'renegociado'")
        campo_existe = cursor.fetchone()
        
        if campo_existe:
            print("Campo 'renegociado' já existe.")
            
            # Verificar quantos registros têm NULL
            cursor.execute("SELECT COUNT(*) FROM titulo WHERE renegociado IS NULL")
            count_null = cursor.fetchone()[0]
            print(f"Registros com NULL: {count_null}")
            
            # Verificar quantos registros já têm valores
            cursor.execute("SELECT COUNT(*) FROM titulo WHERE renegociado IS NOT NULL")
            count_com_valor = cursor.fetchone()[0]
            print(f"Registros com valores existentes: {count_com_valor}")
            print("✓ Dados existentes serão preservados!")
            
            # Adicionar DEFAULT 0 (não altera dados existentes)
            print("\nAdicionando DEFAULT 0 ao campo (não altera dados existentes)...")
            cursor.execute("ALTER TABLE titulo MODIFY COLUMN renegociado INT DEFAULT 0")
            
            # Atualizar APENAS registros NULL para 0 (preserva todos os outros valores)
            if count_null > 0:
                print(f"Atualizando {count_null} registros NULL para 0...")
                cursor.execute("UPDATE titulo SET renegociado = 0 WHERE renegociado IS NULL")
                print("✓ Registros NULL atualizados para 0")
            else:
                print("✓ Nenhum registro NULL encontrado")
            
            print("\n✓ Campo 'renegociado' configurado com sucesso!")
            print("✓ Todos os dados existentes foram preservados!")
        else:
            print("Campo 'renegociado' não existe. Adicionando com DEFAULT 0...")
            cursor.execute("ALTER TABLE titulo ADD COLUMN renegociado INT DEFAULT 0")
            print("✓ Campo 'renegociado' adicionado com sucesso!")
            print("✓ Todos os registros existentes receberão 0 automaticamente")
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()

print("\n✅ Concluído! Dados existentes estão intactos.")


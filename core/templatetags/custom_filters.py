from django import template
import re
import datetime
from core.utils import valor_por_extenso 

register = template.Library()

@register.filter
def get_value(dictionary, key):
    """Retorna o valor de um dicionário para uma chave específica."""
    return dictionary.get(key, "")
    
    
@register.filter
def replace(value, args):
    """
    Substitui partes de uma string. Uso: {{ value|replace:"old,new" }}
    """
    old, new = args.split(',')
    return value.replace(old, new)    
    
    
@register.filter
def coalesce(value1, value2):
    """Retorna o primeiro valor não nulo."""
    return value1 or value2
    
@register.filter
def clean_phone_number(value):
    """Remove caracteres não numéricos de um número de telefone."""
    if value:
        return re.sub(r'[^0-9]', '', value)
    return value    

@register.filter
def traduz_permissao(name):
    if name.lower().startswith("can add"):
        return "Pode adicionar"
    elif name.lower().startswith("can change"):
        return "Pode editar"
    elif name.lower().startswith("can delete"):
        return "Pode excluir"
    elif name.lower().startswith("can view"):
        return "Pode visualizar"
    return name
    
@register.filter
def data_por_extenso(value):
    if isinstance(value, datetime.date):
        meses = [
            "janeiro", "fevereiro", "março", "abril", "maio", "junho",
            "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
        ]
        return f"{value.day} de {meses[value.month - 1]} de {value.year}"
    return value  


@register.filter(name='valor_por_extenso')
def valor_por_extenso_filter(valor):
    return valor_por_extenso(valor) 


@register.filter
def get_dict_value(dictionary, key):
    """
    Retorna o valor de um dicionário para uma chave específica.
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key, "Não informado")
    return "Não informado"    
    
@register.filter
def get_value(obj, field_name):
    return getattr(obj, field_name, '')
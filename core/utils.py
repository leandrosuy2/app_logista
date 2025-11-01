import requests
from bs4 import BeautifulSoup


def consultar_cnpj_via_scraping(cnpj):
    url = f"https://cnpj.biz/{cnpj}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Levanta exceção para erros HTTP

        soup = BeautifulSoup(response.text, 'html.parser')
        dados = {
            "razao_social": soup.find('th', text='Razão Social').find_next('td').text.strip() if soup.find('th', text='Razão Social') else None,
            # Outros campos aqui...
        }
        return dados

    except requests.exceptions.RequestException as e:
        return {"erro": f"Erro ao consultar o CNPJ: {e}"}


def valor_por_extenso(valor):
    # Sua implementação de valor_por_extenso
    unidades = [
        '', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove'
    ]
    dezenas = [
        '', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa'
    ]
    centenas = [
        '', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos'
    ]
    especiais = {
        10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze',
        15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove'
    }

    def numero_por_extenso(n):
        if n == 0:
            return 'zero'
        elif n < 10:
            return unidades[n]
        elif n < 20:
            return especiais[n]
        elif n < 100:
            dezena, unidade = divmod(n, 10)
            return dezenas[dezena] + (f' e {unidades[unidade]}' if unidade else '')
        elif n < 1000:
            centena, resto = divmod(n, 100)
            if n == 100:
                return 'cem'
            return centenas[centena] + (f' e {numero_por_extenso(resto)}' if resto else '')
        else:
            milhar, resto = divmod(n, 1000)
            milhar_extenso = f'{numero_por_extenso(milhar)} mil' if milhar > 1 else 'mil'
            return milhar_extenso + (f' e {numero_por_extenso(resto)}' if resto else '')

    reais, centavos = divmod(round(valor * 100), 100)
    reais_extenso = f'{numero_por_extenso(reais)} real{"s" if reais > 1 else ""}' if reais else ''
    centavos_extenso = f'{numero_por_extenso(centavos)} centavo{"s" if centavos > 1 else ""}' if centavos else ''

    if reais and centavos:
        return f'{reais_extenso} e {centavos_extenso}'
    return reais_extenso or centavos_extenso
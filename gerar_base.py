import pandas as pd
import numpy as np

np.random.seed(42)

ufs_regioes = {
    'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte',
    'BA': 'Nordeste', 'CE': 'Nordeste', 'DF': 'Centro-Oeste', 'ES': 'Sudeste',
    'GO': 'Centro-Oeste', 'MA': 'Nordeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'MG': 'Sudeste', 'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul',
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RJ': 'Sudeste', 'RN': 'Nordeste',
    'RS': 'Sul', 'RO': 'Norte', 'RR': 'Norte', 'SC': 'Sul',
    'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
}

base_desocupacao = {
    'BA': 15.8, 'PE': 14.9, 'AL': 13.8, 'SE': 13.5, 'AP': 13.2,
    'RJ': 12.6, 'RN': 12.4, 'AM': 12.1, 'PB': 11.8, 'MA': 11.5,
    'PI': 11.2, 'CE': 10.9, 'PA': 10.6, 'DF': 10.4, 'SP': 9.8,
    'AC': 9.5, 'MG': 8.9, 'RR': 8.7, 'TO': 8.5, 'ES': 8.2,
    'GO': 7.6, 'RS': 6.9, 'PR': 6.4, 'MS': 6.1, 'RO': 5.8,
    'MT': 4.9, 'SC': 4.1
}

base_informalidade = {
    'PA': 58.2, 'MA': 57.5, 'AM': 55.8, 'PI': 54.9, 'BA': 53.4,
    'CE': 52.1, 'AL': 51.8, 'PB': 51.2, 'PE': 50.4, 'AC': 49.8,
    'RN': 48.9, 'SE': 48.5, 'AP': 47.6, 'RO': 46.2, 'TO': 45.8,
    'RR': 44.5, 'MT': 39.4, 'GO': 38.7, 'MG': 37.9, 'ES': 37.2,
    'MS': 36.5, 'RJ': 35.8, 'RS': 32.4, 'PR': 31.8, 'SP': 30.2,
    'DF': 28.9, 'SC': 26.4
}

anos = [2012, 2014, 2016, 2018, 2020, 2022]
fator_ano = {2012: 0.78, 2014: 0.72, 2016: 1.15, 2018: 1.22, 2020: 1.38, 2022: 0.95}

sexos = ['Masculino', 'Feminino']
fator_sexo = {'Masculino': 0.88, 'Feminino': 1.14}

faixas = ['18 a 24 anos', '25 a 39 anos', '40 a 59 anos', '60 anos ou mais']
fator_faixa = {'18 a 24 anos': 1.65, '25 a 39 anos': 0.95, '40 a 59 anos': 0.68, '60 anos ou mais': 0.45}

registros = []

for ano in anos:
    for uf, regiao in ufs_regioes.items():
        for sexo in sexos:
            for faixa in faixas:
                ruido_d = np.random.normal(0, 0.35)
                ruido_i = np.random.normal(0, 0.80)
                
                desoc = round(max(1.8, base_desocupacao[uf] * fator_ano[ano] * fator_sexo[sexo] * fator_faixa[faixa] + ruido_d), 2)
                inform = round(min(78.0, max(15.0, base_informalidade[uf] * (0.95 + (ano - 2012)*0.008) * (1.03 if sexo == 'Feminino' else 0.97) + ruido_i)), 2)
                
                registros.append({
                    'Ano': ano,
                    'Regiao': regiao,
                    'UF': uf,
                    'Sexo': sexo,
                    'Faixa_Etaria': faixa,
                    'Taxa_Desocupacao': desoc,
                    'Taxa_Informalidade': inform
                })

df = pd.DataFrame(registros)
df.to_csv('dados_trabalho_ibge.csv', index=False, encoding='utf-8-sig')
print("Arquivo 'dados_trabalho_ibge.csv' gerado com sucesso! Total de linhas:", len(df))

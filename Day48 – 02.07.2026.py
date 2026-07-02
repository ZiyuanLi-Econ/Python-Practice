import pandas as pd
df = pd.read_csv(r'C:\Users\17964\Desktop\hormuz_energy_project\data_raw\Statistical Review of World Energy Narrow format.csv')
countires = ['US', 'China', 'Germany', 'Total EU', 'Japan', 'India']
vars_prefer = ['oilprod_kbd', 'oilcons_kbd']
table_prefer = df[
    (df['Country'].isin(countires))&
    (df['Var'].isin(vars_prefer))&
    (df['Year']==2024)
]
table_prefer

rows = []
for country in countires:
    country_data = table_prefer[table_prefer['Country'] == country]
    oilprod = country_data[country_data['Var'] =='oilprod_kbd']['Value']
    oilcons = country_data[country_data['Var'] =='oilcons_kbd']['Value']

    if len(oilprod)==0:
        oilprod = 0
    else:
        oilprod = oilprod.iloc[0]
    oilcons = oilcons.iloc[0]
    
    supply_balance = oilprod - oilcons
    import_need = max(-supply_balance, 0)
    Ratio_of_Dependenceon_Import = import_need / oilcons *100
    rows.append({
        'Country':country,
        'oilprod_kbd': oilprod,
        'oilcons_kbd': oilcons,
        'supply_balance': supply_balance,
        'import_need': import_need,
        'Ratio_of_Dependenceon_Import':  Ratio_of_Dependenceon_Import 
    })
gap_table = pd.DataFrame(rows)
gap_table


imports = pd.read_csv(
    r'C:\Users\17964\Desktop\hormuz_energy_project\data_raw\TradeData.csv',
    encoding='latin1',
    index_col=False
)

imports_simple = imports[
    ['refYear', 'reporterDesc', 'partnerDesc', 'cmdCode', 'flowDesc', 'netWgt', 'primaryValue']
]
imports_clean = imports_simple[imports_simple['partnerDesc'] != 'World'].copy()
imports_clean['total_weight_by_country'] = (
    imports_clean.groupby('reporterDesc')['netWgt'].transform('sum')
)

imports_clean['source_share_pct'] = (
    imports_clean['netWgt'] / imports_clean['total_weight_by_country'] * 100
)

imports_clean = imports_clean.sort_values(by='source_share_pct', ascending=False)
imports_clean['reporterDesc'].unique()

country_colu = []
countries = ['USA', 'China', 'India', 'European Union', 'Japan', 'Rep. of Korea', 'Germany']
for country in countries:
    country_data = imports_clean[imports_clean['reporterDesc']==country]
    country_data = country_data.sort_values(
        by='source_share_pct',
        ascending=False
    )
    for index,row in country_data.iterrows():
        country_colu.append({ 
        'country_name':country,
        'partner_share':row['source_share_pct'],
        'partner_name':row['partnerDesc'],
        'netWgt':row['netWgt']
    })

country_colu = pd.DataFrame(country_colu)
country_colu

middle_east = [
    'Saudi Arabia',
    'Iraq',
    'United Arab Emirates',
    'Kuwait',
    'Qatar',
    'Iran',
    'Oman',
    'Bahrain'
]

country_table = country_colu[country_colu['partner_name'].isin(middle_east)]
me = (country_table.groupby('country_name')['partner_share'].sum().reset_index())
me


hormuz_countries = [
    'Saudi Arabia',
    'Iraq',
    'United Arab Emirates',
    'Kuwait',
    'Qatar',
    'Iran',
    'Bahrain'
]

country_colu['is_hormuz_related'] = country_colu['partner_name'].isin(hormuz_countries)

hormuz_share = (
    country_colu[country_colu['is_hormuz_related']]
    .groupby('country_name')['partner_share']
    .sum()
    .reset_index()
)
hormuz_share = hormuz_share.rename(
    columns={'partner_share': 'hormuz_related_share_pct'}
)
hormuz_share
me = me.rename(columns={'partner_share': 'middle_east_share_pct'})
risk_table = gap_table.merge(
    me,
    left_on='Country',
    right_on='country_name',
    how='left'
)
risk_table = risk_table.merge(
    hormuz_share,
    left_on='Country',
    right_on='country_name',
    how='left'
)

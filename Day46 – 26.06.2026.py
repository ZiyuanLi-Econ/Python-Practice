import pandas as pd
df = pd.read_csv(r"C:\Users\17964\Desktop\Hormuz Energy Project\Data Raw\Statistical Review of World Energy Narrow format.csv")

#Q2
##Q2.1 Production
oilprod_relevant = df[
    (df['Year']==2024)&
    (df['Var']=='oilprod_kbd')
    ]

oilprod_relevant_clean = oilprod_relevant[
    ['Country', 'Region', 'SubRegion', 'Var', 'Value']
    ]

oilprod_relevant_rank = oilprod_relevant_clean.sort_values(by='Value', ascending=False)
is_total = oilprod_relevant_rank['Country'].str.startswith(('Total','Other'))
oilprod_relevant_rank_clean = oilprod_relevant_rank[~is_total]
oilprod_relevant_rank_clean = oilprod_relevant_rank_clean.reset_index(drop=True)
oilprod_relevant_rank_clean


##Q2.2 Consumption
oilcons = df[
    (df['Year']==2024)&
    (df['Var']=='oilcons_kbd')
]

oilcons_relevant = oilcons[[
    'Country', 'Region', 'SubRegion', 'Var', 'Value'
]]
is2_total = oilcons_relevant['Country'].str.startswith(('Total','Other'))
oilcons_relevant_clean = oilcons_relevant[~is2_total]
oilcons_relevant_clean2 = oilcons_relevant_clean.sort_values(by='Value', ascending=False)
oilcons_relevant_clean3 = oilcons_relevant_clean2.reset_index(drop=True)
oilcons_relevant_clean3

##
oilcons_relevant_clean3['oilcons_kbd_value']=oilcons_relevant_clean3['Value']
oilcons_relevant_clean3.drop(['Var','Value'], axis=1, inplace=True)
oilcons_relevant_clean3

oilprod_relevant_rank_clean['oilprod_kbd_value']=oilprod_relevant_rank_clean['Value']
oilprod_relevant_rank_clean.drop(['Var','Value'], axis=1, inplace=True)
oilprod_relevant_rank_clean

#
combination = pd.merge(
    oilprod_relevant_rank_clean,
    oilcons_relevant_clean3,
    on = 'Country',
    how = 'inner'
)

combination = combination[['Country', 'Region_x', 'SubRegion_x', 'oilprod_kbd_value', 'oilcons_kbd_value']]
combination['difference'] = combination['oilprod_kbd_value'] - combination['oilcons_kbd_value']
combination = combination.sort_values(by='difference', ascending=True)
combination = combination.reset_index(drop=True)
print(combination)

#
oilprod_top10 = oilprod_relevant_rank_clean.head(10)
oilcons_top10 = oilcons_relevant_clean3.head(10)
prod_countries = set(oilprod_top10['Country'])
cons_countries = set(oilcons_top10['Country'])
overlap = prod_countries & cons_countries
print(overlap)


#Q2.5
oilcons_relevant_clean3['share'] = oilcons_relevant_clean3['oilcons_kbd_value'] / oilcons_relevant_clean3['oilcons_kbd_value'].sum()
oilcons_relevant_clean3
oilprod_relevant_rank_clean['share'] = oilprod_relevant_rank_clean['oilprod_kbd_value'] /  oilprod_relevant_rank_clean['oilprod_kbd_value'].sum()
oilprod_relevant_rank_clean




#Q2.4
oilcons_relevant_clean3 = oilcons_relevant_clean3.groupby('SubRegion')['oilcons_kbd_value'].sum()
group_con  = oilcons_relevant_clean3.sort_values(ascending=False)
group_con = group_con.reset_index()
group_con['share'] = group_con['oilcons_kbd_value'] / group_con['oilcons_kbd_value'].sum()
group_con

oilprod_relevant_rank_clean = oilprod_relevant_rank_clean.groupby('SubRegion')['oilprod_kbd_value'].sum()
group_prod = oilprod_relevant_rank_clean.sort_values(ascending=False)
group_prod = group_prod.reset_index()
group_prod['share'] = group_prod['oilprod_kbd_value'] / group_prod['oilprod_kbd_value'].sum()
group_prod


combined_group = pd.merge(group_con,group_prod, on='SubRegion')
combined_group



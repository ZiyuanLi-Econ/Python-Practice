import pandas as pd

# Source: EIA, World Oil Transit Chokepoints, Table 1
# Unit: million barrels per day (mbd)

eia_chokepoint_table = pd.DataFrame({
    'location': [
        'Strait of Malacca',
        'Strait of Hormuz',
        'Suez Canal and SUMED Pipeline',
        'Bab el-Mandeb',
        'Danish Straits',
        'Turkish Straits (Dardanelles)',
        'Panama Canal',
        'Cape of Good Hope',
        'World maritime oil trade',
        'World total oil supply'
    ],
    2020: [22.8, 19.2, 5.4, 5.7, 3.1, 3.2, 1.7, 7.9, 74.1, 94.1],
    2021: [22.1, 19.7, 5.2, 6.0, 3.1, 3.3, 1.8, 7.2, 75.9, 95.8],
    2022: [23.0, 21.9, 7.3, 8.0, 4.2, 3.2, 2.2, 6.1, 78.6, 100.6],
    2023: [24.0, 21.8, 8.8, 9.3, 5.0, 3.5, 2.2, 6.2, 80.2, 102.6],
    2024: [22.5, 20.7, 4.8, 4.1, 4.9, 3.6, 2.0, 9.3, 79.7, 103.3],
    '1H25': [23.2, 20.9, 4.9, 4.2, 4.9, 3.7, 2.3, 9.1, 79.8, 104.4]
})

print(eia_chokepoint_table)

eia = (eia_chokepoint_table.set_index('location').T)
eia['hormuz_share_pct'] = (
    eia['Strait of Hormuz']
    / eia['World maritime oil trade']
    * 100
).round(1)

eia[['Strait of Hormuz', 'World maritime oil trade', 'hormuz_share_pct']]



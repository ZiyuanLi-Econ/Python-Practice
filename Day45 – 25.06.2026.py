import pandas as pd
import matplotlib.pyplot as plt

#Q1
##Q1.1
df = pd.read_csv(r"C:\Users\17964\Desktop\Hormuz Energy Project\Data Raw\Statistical Review of World Energy Narrow format.csv")
df.head()
total_energy = df[
    (df['Country'] =='Total World') &
    (df['Year']==2024) &
    (df['Var']=='tes_ej')
]
total_energy_value = total_energy['Value'].iloc[0]
total_energy_value

##Q1.2
df['Var'].unique()
world_2024 = df[
    (df['Country']=='Total World')&
    (df['Year']==2024)
]

world_2024[
    world_2024['Var'].str.endswith('_ej', na=False)
    ]['Var'].unique()

energy_Var = ['coalcons_ej', 'gascons_ej', 'nuclear_ej', 'renewables_ej', 'oilcons_ej']
consumption = {}
for Var in energy_Var:
    Var_name = Var
    Var_value = world_2024[world_2024['Var']==Var]['Value'].iloc[0]
    consumption[Var_name] = Var_value


energy_Var_proportion={}
for k,v in consumption.items():
    energy_Var_proportion[k] = v / total_energy_value *100
energy_Var_proportion

rows=[]
for i in energy_Var:
    name = i
    econsumption = consumption[i]
    eproportion = energy_Var_proportion[i]
    rows.append ({
    'Var':name,
    'Var_ej':econsumption,
    'share':eproportion
    })

dff = pd.DataFrame(data = rows)
dff

plt.bar( dff['Var'],  dff['share'])
plt.show()

plt.pie(dff['share'],labels=dff['Var'])
plt.show()
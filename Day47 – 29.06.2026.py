from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# Q3: Country energy structure, 2024

project_folder = Path(r"C:\Users\17964\Desktop\Hormuz Energy Project\Q3. Structure")
data_file = Path(r"C:\Users\17964\Desktop\Hormuz Energy Project\Data Raw\Statistical Review of World Energy Narrow format.csv")

tables_folder = project_folder / "tables"
figures_folder = project_folder / "figures"
tables_folder.mkdir(exist_ok=True)
figures_folder.mkdir(exist_ok=True)

df = pd.read_csv(data_file)

countries = [
    "China",
    "US",
    "India",
    "Japan",
    "South Korea",
    "Germany",
    "Total EU",
]

energy_vars = [
    "tes_ej",
    "oilcons_ej",
    "gascons_ej",
    "coalcons_ej",
    "nuclear_ej",
    "renewables_ej",
]

source_vars = [
    "oilcons_ej",
    "gascons_ej",
    "coalcons_ej",
    "nuclear_ej",
    "renewables_ej",
]


# 1. Select 2024 data for target countries and target variables
selected_table = df[
    (df["Country"].isin(countries))
    & (df["Year"] == 2024)
    & (df["Var"].isin(energy_vars))
]

selected_table = selected_table[["Country", "Year", "Var", "Value"]]

print("\nSelected long table:")
print(selected_table)


# 2. Convert long table to wide table
wide_table = selected_table.pivot(index="Country", columns="Var", values="Value")
wide_table = wide_table.reindex(countries)

print("\nEnergy amount table, EJ:")
print(wide_table)

wide_table.to_csv(tables_folder / "q3_country_energy_amount_2024.csv")


# 3. Calculate energy shares
share_table = wide_table[source_vars].div(wide_table["tes_ej"], axis=0) * 100
share_table["share_sum"] = share_table.sum(axis=1)

print("\nEnergy share table, %:")
print(share_table)

share_table.to_csv(tables_folder / "q3_country_energy_share_2024.csv")


# 4. Rank oil share and find the largest energy source for each country
oil_share_rank = share_table["oilcons_ej"].sort_values(ascending=False)

print("\nOil share ranking, %:")
print(oil_share_rank)

main_energy_source = share_table[source_vars].idxmax(axis=1)
main_energy_share = share_table[source_vars].max(axis=1)

main_energy_table = pd.DataFrame(
    {
        "main_energy_source": main_energy_source,
        "main_energy_share": main_energy_share,
    }
)

print("\nMain energy source by country:")
print(main_energy_table)

main_energy_table.to_csv(tables_folder / "q3_main_energy_source_2024.csv")


# 5. Figure: total energy supply
wide_table["tes_ej"].plot(kind="bar", color="steelblue")
plt.title("Total Energy Supply by Country, 2024")
plt.xlabel("Country")
plt.ylabel("Total energy supply (EJ)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(figures_folder / "q3_total_energy_supply_2024.png", dpi=300)
plt.show()


# 6. Figure: energy consumption by source
wide_table[source_vars].plot(kind="bar", stacked=True)
plt.title("Energy Consumption by Source, 2024")
plt.xlabel("Country")
plt.ylabel("Energy consumption (EJ)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Energy Type", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig(figures_folder / "q3_energy_amount_by_source_2024.png", dpi=300)
plt.show()


# 7. Figure: energy mix share
share_table[source_vars].plot(kind="bar", stacked=True)
plt.title("Energy Mix Share by Country, 2024")
plt.xlabel("Country")
plt.ylabel("Share of total energy supply (%)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Energy Type", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig(figures_folder / "q3_energy_mix_share_2024.png", dpi=300)
plt.show()

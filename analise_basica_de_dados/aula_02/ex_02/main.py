import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('analise_basica_de_dados/aula_02/ex_02/Ecommerce_Consumer_Behavior_Analysis_Data.csv')

dados['Purchase_Amount'] = dados['Purchase_Amount'].str.replace('$', '').astype(float)

sns.set_theme(style="darkgrid", palette="pastel")

# sns.histplot(data=dados, x="Age", kde=True)
# plt.title('Distruibuição de Idade dos Clientes')
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio1_histplot.png')
# plt.close()

# sns.countplot(data=dados, x="Gender", palette='pastel', stat='percent')
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio2_countplot.png')
# plt.close()
 

# sns.boxplot(data=dados, x='Income_Level', y='Purchase_Amount')
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio3_boxplot.png')
# plt.close()


# sns.histplot(data=dados, x='Customer_Satisfaction', hue='Gender')
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio4_histograma.png')
# plt.close()


# ax = sns.scatterplot(data=dados, x='Product_Rating', y='Time_Spent_on_Product_Research(hours)', hue='Purchase_Category')
# sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
# plt.xticks(range(1, 6, 1))
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio5_scatterplot.png')
# plt.close()


# sns.regplot(data=dados, x='Product_Rating', y='Time_Spent_on_Product_Research(hours)')
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio5.1_regplot.png')
# plt.close()


# ax = sns.violinplot(data=dados, x='Purchase_Channel', y='Brand_Loyalty', hue='Discount_Used', split=True)
# sns.move_legend(ax, "upper right", bbox_to_anchor = (1,1))
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio6_violinplot.png')
# plt.close()



# sns.barplot(data=dados, x='Customer_Loyalty_Program_Member', y='Frequency_of_Purchase', estimator='mean', errorbar=None)
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio7_barplot.png')
# plt.close()


# heatmap_data = pd.crosstab(dados['Payment_Method'], dados['Device_Used_for_Shopping'])
# sns.heatmap(heatmap_data)
# plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio8_heatmap.png')
# plt.close()


grid = sns.FacetGrid(dados, col='Location', col_wrap=3, height=4)
grid.map_dataframe(sns.scatterplot, x='Purchase_Amount', y='Age')
plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio9_facetgrid.png')
plt.close()


dados['Month'] = dados['Time_of_Purchase'].dt.to_period('M').astype(str)
media_mensal = dados.groupby('Month')['Purchase_Amount'].mean().reset_index()

sns.lineplot(data=media_mensal, x='Month', y='Purchase_Amount')
plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio10_lineplot.png')
plt.close()

sns.pairplot(dados, hue="Purchase_Amount")
plt.savefig('analise_basica_de_dados/aula_02/ex_02/exercicio11_pairplot.png')
plt.close()
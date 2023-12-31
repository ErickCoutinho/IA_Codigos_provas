
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
#MELHOR ACERTO: Usando as colunas com maior variancia
#COLUNAS COM MAIOR VARIANCIA
derma = pd.read_csv('norma_novo.csv')
samples = derma.drop(['class'],axis=1)
class_values = derma['class'].values
colunas_var = derma[['erythema', 'scaling', 'definite_borders', 'itching', 'koebner_phenomenon', 'polygonal_papules']]

#DESEMPENHO
pca = PCA(n_components=2)
X_pca = pca.fit_transform(colunas_var)
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(colunas_var)
# Dividir os dados reduzidos em treinamento e teste
X_pca_train, X_pca_test, y_train, y_test = train_test_split(X_pca, class_values, test_size=0.2, random_state=42)
X_tsne_train, X_tsne_test, y_train, y_test = train_test_split(X_tsne, class_values, test_size=0.2, random_state=42)
# Criar classificadores k-NN para PCA e t-SNE
knn_pca = KNeighborsClassifier(n_neighbors=3)
knn_tsne = KNeighborsClassifier(n_neighbors=3)
# Treinar os classificadores usando os dados de treinamento
knn_pca.fit(X_pca_train, y_train)
knn_tsne.fit(X_tsne_train, y_train)
# Fazer previsões sobre os dados de teste
y_pred_pca = knn_pca.predict(X_pca_test)
y_pred_tsne = knn_tsne.predict(X_tsne_test)
# Calcular métricas de avaliação para PCA
print("Métricas de avaliação para PCA:")
print(classification_report(y_test, y_pred_pca))
print("Matriz de confusão para PCA:")
print(confusion_matrix(y_test, y_pred_pca))
print(" \nAcuracia PCA: 0.64")

print('\n___________________________________________________________________________________')

# Calcular métricas de avaliação para t-SNE
print(" Métricas de avaliação para t-SNE:")
print(classification_report(y_test, y_pred_tsne))
print("Matriz de confusão para t-SNE:")
print(confusion_matrix(y_test, y_pred_tsne))
print(" \nAcuracia T-SNE: 0.67")
print('\n___________________________________________________________________________________')


#USANDO OUTRO CLASSIFICADOR (Regressão Logistica)
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
print('\nCLASSIFICADOR: REGRESSÃO LOGISTICA')

X_train, X_test, y_train, y_test = train_test_split(colunas_var, class_values, test_size=0.2, random_state=42)
# Criar uma instância do classificador de Regressão Logística
logreg = LogisticRegression()
# Treinar o classificador com os dados de treinamento
logreg.fit(X_train, y_train)
# Fazer previsões usando o conjunto de teste
y_pred = logreg.predict(X_test)
# Criar a matriz de confusão
confusion_matrix = confusion_matrix(y_test, y_pred)
print('\nMatriz de confusão:')
print(confusion_matrix)

# Gerar o relatório de classificação
report = classification_report(y_test, y_pred)
print('\nClassification Report:')
print(report)
# Calcular a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print("\nAcurácia da Regressão Logística: {:.2f}".format(accuracy))





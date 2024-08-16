#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n, m, c, contador = 1;
    cin >> n >> m >> c;

    vector<vector<int>> matriz;

    for(int i = 0; i < n; i++){
        vector <int> aux;

        for(int j = 0; j < m; j++){
            aux.push_back(contador);
            contador++;
        }
        matriz.push_back(aux);
    }

    for(int i = 0; i < c; i++){
        char comando;
        int a, b;
        cin >> comando >> a >> b;
        a = a-1;
        b = b-1;

        if(comando == 'L'){
            vector<int> aux;
            aux = matriz[a];
            matriz[a] = matriz[b];
            matriz[b] = aux;
        }else{
            for(int i = 0; i < n; i++){
                int aux = 0;
                aux = matriz[i][a];
                matriz[i][a] = matriz[i][b];
                matriz[i][b] = aux;
            }
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j ++){
            if(j == (m-1)){
                cout << matriz[i][j] << endl;
            }else{
                cout << matriz[i][j] << " ";
            }
        }
    }
}
/* 
Temos dois comandos:
L = troca a linha A pela linha B
C = troca a coluna A pela coluna B
*/

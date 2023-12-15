#include <iostream>

int main() {
    int x = 1, y = 1, n, Mat[51][51], cont = 2;
    std::cin >> n;
    char resp;
    Mat[x][y] = 1;
    do
    {
    while (cont <= n * n)
    {
        x++;
        Mat[x][y]=cont;
        cont++;
        while(x > 1 && y < n)
        {
            x--;
            y++;
            Mat[x][y]=cont;
            cont++;
        }
        y++;
        Mat[x][y]=cont;
        cont++;
        while(y > 1 && x < n)
        {
            x++;
            y--;
            Mat[x][y]=cont;
            cont++;
        }
        if (x == n && y == 1)
        {
            while(cont <= n*n)
            {
                y++;
                Mat[x][y]=cont;
                cont++;
                while(y > 1 && x < n)
                {
                    x--;
                    y++;
                    Mat[x][y]=cont;
                    cont++;
                }
                x++;
                Mat[x][y]=cont;
                cont++;
                while(x > 1 && y < n)
                {
                    x++;
                    y--;
                    Mat[x][y]=cont;
                    cont++;
                }
            }
        }
    }

    for (x = 1; x <= n; x++)
    {
        for (y = 1; y <= n; y++)
        {
            if (Mat[x][y] < 10)
                std::cout << " ";
            if (Mat[x][y] < 100)
                std::cout << " ";
            std::cout << Mat[x][y] << " ";
        }
        std::cout << std::endl;
    }
    std::cin >> resp;
    }while (resp == 's');
    return 0;
}
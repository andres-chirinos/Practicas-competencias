#include <iostream>
#include <cmath>

using namespace std;

int main() {
  int x, y;
  cin >> x >> y;

  // Calculate the number of digits in the product using logarithms
  int n_digits = floor(log10(pow(2, x)*pow(5, y)))+1;

  cout << n_digits << endl;

  return 0;
}

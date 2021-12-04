#include <iostream>
#include <fstream>
#include "vector"
using namespace std;

int main() {
    string data;
    fstream inFileStr("input.txt", ios::in);
    vector<string> lines;
    vector<string> ox;
    vector<string> co;

    string gamma;
    string epsilon;
    int count;

    // part 1
    for (int i = 0; i < 1000; i++) {
        inFileStr >> data;
        lines.push_back(data);
        ox.push_back(data);
        co.push_back(data);
    }

    for (int i = 0; i < 12; i++){
        for (auto & line : lines) {
            count += static_cast<char>((line[i] == '1'))? 1: -1;
        }
        gamma += static_cast<char>((count > 0))? '1': '0';
        epsilon += static_cast<char>((count > 0))? '0': '1';
        count = 0;
    }

    int int_gamma = stoi(gamma, nullptr, 2);
    int int_epsilon = stoi(epsilon, nullptr, 2);
    cout << int_gamma * int_epsilon << endl;

    // part 2
    int co_ = 0;
    int ox_ = 0;
    for (int i = 0; i < 12; i++){
        for (auto & x : ox) {
            ox_ += static_cast<char>((x[i] == '1'))? 1: -1;
        }
        for (auto & x : co) {
            co_ += static_cast<char>((x[i] == '1'))? 1: -1;
        }
        for (int j=0; j<ox.size(); j++) {
            if (ox[j][i] != (static_cast<char>((ox_ >= 0)) ? '1' : '0')){
                ox.erase(ox.begin() + j);
                j--;
            }
        }
        for (int j=0; j<co.size(); j++) {
            if (!((co[j][i] == (static_cast<char>((co_ < 0 ))? '1': '0')) || (co.size() < 2))){
                co.erase(co.begin() + j);
                j--;
            }
        }
        co_ = 0;
        ox_ = 0;
    }
    int int_co = stoi(co[0], nullptr, 2);
    int int_ox = stoi(ox[0], nullptr, 2);
    cout << int_co * int_ox << endl;
    return 0;
}
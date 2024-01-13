#include <iostream>
#include <cwchar> // std::wcin, std::wstring, std::iswdigit
#include <cmath> // std::sqrt
#include <sstream> // std::ostringstream

// std::any_of
#if __cplusplus >= 202002L // C++20 or later
    #include <ranges>
#else // C++17 or earlier
    #include <algorithm>
#endif


/* TODO:
#include <thread>
*/

//#include <limits>
//size_t LONGSIZE = CHAR_BIT * sizeof(long);
//size_t LLONGSIZE = CHAR_BIT * sizeof(long long);


bool is_prime(unsigned long long n)
{
    if (n < 2)
        return false;

    for (unsigned long long i = 2; i <= std::sqrt(n); i++)
    {
        if (n % i == 0)
            return false;
    }
    
    return true;
}


unsigned long long sum_of_proper_divisors(unsigned long long n)
{
    unsigned long long sum = 0;
    
    for (unsigned long long i = 1; i < n; i++)
    {
        if (n % i == 0)
            sum += i;
    }
    return sum;
}


std::string evaluate_digit(unsigned long long n)
{
    std::ostringstream oss ;
    oss << n;
    std::string n_str = oss.str();
    
   
    std::string answer = "You entered " + n_str + " which is a";
    
    bool prime = is_prime(n);
    unsigned long long sopd;
    
    if (prime)
        sopd = 0;
    else
        sopd = sum_of_proper_divisors(n);
        
    if (sopd == n)
        answer += " PERFECT";
    else if (sopd > n)
        answer += " ABUNDANT";
    else
        answer += " DEFICIENT";
        
    if (prime)
        answer += " PRIME";
    else
        answer += " COMPOSITE";
        
    return answer + " number.\n\n";
}


int main(void)
{  
    std::cout << "Enter a positive integer digit below and I'll describe its characteristics:\n\n";
    
    while (true)
    {
        std::wstring input;
        std::getline(std::wcin, input);
        
        if (std::any_of(input.begin(), input.end(), [](wchar_t& c){ return not std::iswdigit(c); }))
        {
            std::cout << "Bad input\n\n";
            continue;
        }

        std::cout << evaluate_digit(std::stoull(input));
    }
    
    return 0;
}



#include<iostream>
#include<string.h>

/*class list will be used to store list-like files*/
class list
{
    public:
    std::string string_to_convert;

    int count()
    {
        int words;
        for (size_t count = 0; count < string_to_convert.length(); count++)
        {
            if(string_to_convert.at(count)==' '){words++;}
        }
        return words+1;
    }
    


};
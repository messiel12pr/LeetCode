/*****************************************************
 *
 *  844. Backspace String Compare solution c++
 *
 *  Using Stack 
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

bool backspaceCompare(string s, string t)
{
    stack<int> myStack1, myStack2;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '#' && myStack1.size() == 0)
            continue;

        else if (s[i] == '#')
            myStack1.pop();

        else
            myStack1.push(s[i]);
    }

    for (int i = 0; i < t.length(); i++)
    {
        if (t[i] == '#' && myStack2.size() == 0)
            continue;

        else if (t[i] == '#')
            myStack2.pop();

        else
            myStack2.push(t[i]);
    }

    if (myStack1.size() != myStack2.size())
        return false;

    while (myStack1.size() != 0 && myStack2.size() != 0)
    {
        if (myStack1.top() != myStack2.top())
            return false;

        myStack1.pop();
        myStack2.pop();
    }

    return true;
}

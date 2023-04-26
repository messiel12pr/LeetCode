/****************************************************************
 *
 *  1047. Remove All Adjacent Duplicates In String solution c++
 *
 *  Using Stack 
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/***************************************************************

string removeDuplicates(string s)
{
    stack<char> myStack;
    string ans;

    for (int i = 0; i < s.length(); i++)
    {
        if (myStack.size() != 0 && s[i] == myStack.top())
            myStack.pop();

        else
            myStack.push(s[i]);
    }

    while (myStack.size() != 0)
    {
        ans += myStack.top();
        myStack.pop();
    }

    reverse(ans.begin(), ans.end());

    return ans;
}

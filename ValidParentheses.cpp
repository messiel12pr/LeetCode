/*****************************************************
 *
 *  20. Valid Parentheses solution c++
 *
 *  Using Stack 
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************************

bool isValid(string s)
{
    stack<char> myStack;

    if (s.length() % 2 != 0)
        return false;

    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            myStack.push(s[i]);

        else
        {
            if (myStack.size() == 0)
                return false;

            if (s[i] == ')' && myStack.top() == '(')
                myStack.pop();

            else if (s[i] == '}' && myStack.top() == '{')
                myStack.pop();

            else if (s[i] == ']' && myStack.top() == '[')
                myStack.pop();

            else
                return false;
        }
    }

    if (myStack.size() == 0)
        return true;

    else
        return false;
}

/*****************************************
 *                    
 *  682. Baseball Game solution c++
 *
 *  Using Stack 
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/****************************************

int calPoints(vector<string> &operations)
{
    stack<int> scores;
    int sum = 0;

    for (int i = 0; i < operations.size(); i++)
    {
        if (operations[i] == "+")
        {
            int temp = scores.top();
            scores.pop();
            int temp2 = scores.top();
            scores.push(temp);
            scores.push(temp + temp2);
        }

        else if (operations[i] == "D")
        {
            scores.push(scores.top() * 2);
        }

        else if (operations[i] == "C")
        {
            scores.pop();
        }

        else
        {
            stringstream s(operations[i]);
            int n = 0;
            s >> n;

            scores.push(n);
        }
    }

    while (scores.size() != 0)
    {
        sum += scores.top();
        scores.pop();
    }

    return sum;
}

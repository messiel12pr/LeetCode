/*******************************************************************
 *
 *  2108. Find First Palindromic String in the Array solution c++
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/******************************************************************

string firstPalindrome(vector<string> &words)
{
	int r, l;

	for (int i = 0; i < words.size(); i++)
	{
		l = 0;
		r = words[i].size() - 1;
		while (l < r)
		{
			if (words[i][l] != words[i][r])
				break;

			l++;
			r--;
		}

		if (l >= r)
			return words[i];
	}

	return "";
}

/******************************************************
 *
 *  LeetCode Problem 13: Roman to integet solution c++
 *  
 *  Using Hash Map
 *
 *  Joel M. Gonzalez Rodriguez
 *
*/*****************************************************

int romanToInt(string s) 
{
  unordered_map<char, int> subInst;
        
  subInst['I'] = 1;
  subInst['V'] = 5;
  subInst['X'] = 10;
  subInst['L'] = 50;
  subInst['C'] = 100;
  subInst['D'] = 500;
  subInst['M'] = 1000;
        
  int result = 0;
        
  for(int i=0; i<s.size(); i++)
  {
        if(s[i] == 'I' && s[i+1] == 'V')
        {
            result += 4;
            i++;
        }
            
            
        else if(s[i] == 'I' && s[i+1] == 'X')
        {   
            result += 9;
            i++;
        }

        else if(s[i] == 'X' && s[i+1] == 'L')
        {
            result += 40;
            i++;
        } 
            
        else if(s[i] == 'X' && s[i+1] == 'C')
        {
            result += 90;
            i++;
        } 
            
        else if(s[i] == 'C' && s[i+1] == 'D')
        {
            result += 400;
            i++;
        }
              
        else if(s[i] == 'C' && s[i+1] == 'M')
        {
            result += 900;
            i++;
        }  
            
         else
            result += subInst[s[i]];
    }
    
        return result;
 }

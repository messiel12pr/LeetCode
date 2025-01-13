'''

    929. Unique Email Addresses

'''

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split('@')

            if '+' in local:
                local = local[:local.index('+')]
                
            new_local = []
            for c in local:
                if c != '.':
                    new_local.append(c)

            unique.add(f"{''.join(new_local)}@{domain}")
        
        return len(unique)
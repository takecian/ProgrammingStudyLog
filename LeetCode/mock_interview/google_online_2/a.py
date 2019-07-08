class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local = email[:email.index('@')]
            domain = email[email.index('@'):]
            local = local.replace('.', '')
            if local.find('+') != -1:
                local = local[:local.index('+')]
            ans.add(local+domain)
        return len(ans)


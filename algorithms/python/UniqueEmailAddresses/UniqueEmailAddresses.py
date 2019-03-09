from typing import List
import re

# Regex
class Solution1:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            if email.count('+'):
                localName = re.search("[^\+]+", email).group(0)
            else:
                localName = re.search("[^@]+", email).group(0)
            localName = localName.replace('.', '')
            domainName = re.search("@(.+)", email).group(1)
            uniqueEmails.add(localName+'@'+domainName)
        return len(uniqueEmails)

# String manipulation
class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            uniqueEmails.add(local+'@'+domain)
        return len(uniqueEmails)

print(Solution1().numUniqueEmails([
    "ted.st.a2+2@tde.st.com",
    "ted.st.a2+2@tdest.com",
    "ted.st.a2+2@tde.st.com"
]))
# expected: 2
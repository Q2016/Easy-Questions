Question:
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Solution: Python Replace command

    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    def defangIPaddr(self, address: str) -> str:
        return '[.]'.join(address.split('.'))
    def defangIPaddr(self, address: str) -> str:
        return re.sub('\.', '[.]', address)
    def defangIPaddr(self, address: str) -> str:
        return ''.join('[.]' if c == '.' else c for c in address)

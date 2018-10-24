class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_counter = {}

        for cpdomain in cpdomains:
            counter, domain = cpdomain.split()

            counter = int(counter)
            domain_part = domain.split('.')
            if domain in domain_counter:
                domain_counter[domain] += counter
            else:
                domain_counter[domain] = counter

            for i in range(len(domain_part) - 1):
                domain = domain.replace(domain_part[i] + '.', '')
                if domain in domain_counter:
                    domain_counter[domain] += counter
                else:
                    domain_counter[domain] = counter

        results = []
        for domain, counter in domain_counter.iteritems():
            results.append("{} {}".format(str(counter), domain))

        return results

solution = Solution()

print(solution.subdomainVisits(["9001 discuss.leetcode.com"]))
print(solution.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

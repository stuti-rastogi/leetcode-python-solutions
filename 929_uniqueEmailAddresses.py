class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0

        unique_emails = set()
        count_unique_emails = 0

        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.replace('.', '')
            local_name = local_name.split('+')[0]
            parsed_email = local_name + '@' + domain_name
            if parsed_email not in unique_emails:
                count_unique_emails += 1
                unique_emails.add(parsed_email)


        return count_unique_emails
 
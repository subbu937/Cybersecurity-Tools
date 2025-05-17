import dns.resolver
import sys
import pyfiglet

Title= pyfiglet.figlet_format("DNS ENUMERATION TOOL")
print(Title)

try:
    target_domain = sys.argv[1]

except IndexError:
    print(r"Syntax Error - puthon3 .\dns_enum.py <domainname>")
    print(r"     example - python3 .\dns_enum.py youtube.com")
    quit()

records_type = ['A','AAAA','NS','PTR','CNAME','MX','TXT','SOA']

resolver= dns.resolver.Resolver()
for record_type in records_type:
    try:
        answer= resolver.resolve(target_domain, record_type)
        sub_title=f'\n{record_type} record for {target_domain}'
        print(sub_title)
        print('-'*len(sub_title))
        for data in answer:
            print(f'{data}')
    except dns.resolver.NXDOMAIN:
        print(f'{target_domain} domain does not exist')
        quit()
    except dns.resolver.NoAnswer:
        continue
    except KeyboardInterrupt:
        print()
        msg="you stop the task by pressing ctl+c"
        print('-'*len(msg))
        print(f'{msg}')
        print('-'*len(msg))
        print()
        quit()
print()

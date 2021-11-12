import tableauserverclient as TSC
import constants as const


tableau_auth = TSC.PersonalAccessTokenAuth(token_name=const.TOKEN_NAME, personal_access_token=const.TOKEN, site_id=const.SITE_NAME)
server = TSC.Server(const.SERVER_URL, use_server_version=True)
server.auth.sign_in(tableau_auth)

all_sites, pagination_item = server.sites.get()

# print all the site names and ids
for site in all_sites:
    print('site-id:', site.id, 'site-name:', site.name, 'site-content_url:', site.content_url, 'site-state:', site.state)


file_path = server.workbooks.download(const.WORKBOOK_ID)
print("\nDownloaded the file to {0}.".format(file_path))

with server.auth.sign_in(tableau_auth):
    all_workbooks_items, pagination_item = server.workbooks.get()
    # print names of first 100 workbooks
    print([workbook.name for workbook in all_workbooks_items])

    print([workbook.id for workbook in all_workbooks_items])
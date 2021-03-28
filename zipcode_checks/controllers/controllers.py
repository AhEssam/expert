# -*- coding: utf-8 -*-
# import os
#
# from smartystreets_python_sdk import StaticCredentials, exceptions, Batch, ClientBuilder
# from smartystreets_python_sdk.us_zipcode import Lookup as ZIPCodeLookup
#
# from odoo import http
# from odoo.http import request
# from odoo.addons.website_sale.controllers.main import  WebsiteSale
#
#
# class WebsiteSale(WebsiteSale):
#     @http.route(['/shop/address'], type='http', methods=['GET', 'POST'],csrf=False, auth="public", website=True, sitemap=False)
#     def address(self, **kw):
#         print('>>>>>>>>>666>>>>>>>>')
#
#         city = ''
#         zip = ''
#         for key, value in kw.items():
#             if key == 'city':
#                 city = value
#             if key == 'zip':
#                 zip = value
#
#
#
#             print ("%s == %s" %(key, value))
#         print('>>>>>><<<<<<<',city)
#         # self.run(zip)
#
#         # auth_id = "14037cde-229c-0b16-73b7-71560bd9deed"
#         # auth_token = "h7FrqrhPbffgiz3SEiu4"
#         #
#         # # We recommend storing your secret keys in environment variables instead---it's safer!
#         # # auth_id = os.environ['SMARTY_AUTH_ID']
#         # # auth_token = os.environ['SMARTY_AUTH_TOKEN']
#         #
#         # credentials = StaticCredentials(auth_id, auth_token)
#         #
#         # # client = ClientBuilder(credentials).build_us_zipcode_api_client()
#         # client = ClientBuilder(credentials).build_us_zipcode_api_client()
#         # batch = Batch()
#         self.run('12345')
#
    # def run(self,zip):
    #     auth_id = "14037cde-229c-0b16-73b7-71560bd9deed"
    #     auth_token = "h7FrqrhPbffgiz3SEiu4"
    #
    #     # We recommend storing your secret keys in environment variables instead---it's safer!
    #     # auth_id = os.environ['SMARTY_AUTH_ID']
    #     # auth_token = os.environ['SMARTY_AUTH_TOKEN']
    #
    #     credentials = StaticCredentials(auth_id, auth_token)
    #
    #     client = ClientBuilder(credentials).build_us_zipcode_api_client()
    #
    #     # Documentation for input fields can be found at:
    #     # https://smartystreet.com/docs/us-zipcode-api#input-fields
    #
    #     lookup = ZIPCodeLookup()
    #     # lookup.input_id = "dfc33cb6-829e-4fea-aa1b-b6d6580f0817"  # Optional ID from your system
    #     # lookup.city = "Mountain View"
    #     # lookup.state = "California"
    #     lookup.zipcode = zip
    #
    #     try:
    #         client.send_lookup(lookup)
    #     except exceptions.SmartyException as err:
    #         print(err)
    #         return
    #
    #     result = lookup.result
    #     zipcodes = result.zipcodes
    #     cities = result.cities
    #
    #     for city in cities:
    #         print("\nCity: " + city.city)
    #         print("State: " + city.state)
    #         print("Mailable City: {}".format(city.mailable_city))
    #
    #         print('>>>>>>>>>>zip',result.cities)
    #     cities = result.cities
    #




odoo.define('zipcode_checks.zipcode_checks', function (require) {
    "use strict";
    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var _t = core._t;
// const SmartyStreetsSDK = require("smartystreets-javascript-sdk");
    var SmartyStreetsCore = SmartyStreetsSDK.core;
    var Lookup = SmartyStreetsSDK.usZipcode.Lookup;

// for Server-to-server requests, use this code:
    var authId = '14037cde-229c-0b16-73b7-71560bd9deed';
    var authToken = 'h7FrqrhPbffgiz3SEiu4';
// var authId = process.env.SMARTY_AUTH_ID;
// var authToken = process.env.SMARTY_AUTH_TOKEN;

    var credentials = new SmartyStreetsCore.StaticCredentials(authId, authToken);

// for client-side requests (browser/mobile), use this code:
// var key = process.env.SMARTY_WEBSITE_KEY;
// const  credentials = new SmartyStreetsCore.SharedCredentials(key);

    var client = SmartyStreetsCore.buildClient.usZipcode(credentials);

// Documentation for input fields can be found at:
// https://smartystreets.com/docs/us-zipcode-api#input-fields

    // var lookup1 = new Lookup();
    // lookup1.inputId = "01189998819991197253"; // Optional ID from your system
    var zip = $("input[name='zip']").val();
    var city = $("input[name='city']").val();
    console.log('>>>>>>>>>>>>>>>>>>MMMMMMMMMM>>>>>>>>>>>>>>>>>>>>',zip,'<<<<<<<<<<<<<<<<<<<<<<<BB',city)
    // lookup1.zipCode = zip;

    var lookup2 = new Lookup();
    lookup2.inputId = "dfc33cb6-829e-4fea-aa1b-b6d6580f0817";
    // lookup2.city = "Provo";
    // lookup2.state = "UT";
    lookup2.zipCode = zip;

    // var lookup3 = new Lookup();
    // lookup3.city = "Phoenix";
    // lookup3.state = "AZ";

    var batch = new SmartyStreetsCore.Batch();
    // batch.add(lookup1);
    batch.add(lookup2);
    // batch.add(lookup3);
    console.log('>>>>>>>>>>>>1234154645646>>>>>>>M')

        client.send(batch)

            .then(viewResults)
            .catch(console.log);

   var cit = new Array();
   var c;

    function viewResults(response) {

        response.lookups.map(lookup => lookup.result.map(candidate => {
            candidate.cities.map(city =>  cit.push(city.city) );
                  console.log('>>>>>>>>>>>>>>?????????????/',response);


        }

        )
        );

    }



    core.action_registry.add('zipcode_checks', ZipCode);
    //
    return ZipCode;
});
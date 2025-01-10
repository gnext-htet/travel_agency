{
    "name":"Travelling",
    'depends': [ 'mail'],
    "data":[
        #security
        "security/ir.model.access.csv",

        #data
        'data/sequence.xml',
        
        #views
        "views/township.xml",
        "views/travel_gate.xml",
        "views/travel_agency.xml",
        "views/travel_car.xml",
        "views/travel_driver_history.xml",
        "views/transportation_route.xml",
        #widzard
        "wizard/change_driver_wizard.xml",

        #menu
        "views/menu.xml"

    ]
}
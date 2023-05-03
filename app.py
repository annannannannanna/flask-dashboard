from flask import Flask
from flask import render_template
 
app = Flask(__name__)

@app.route("/")


def web_app():


    table_row = [{'NO':'1','ID': '#12594','Date':'Dec 01, 2021', 'Customer Name':'Frank Murlo','Location': '312 S Wilmette Ave', 'Amount':'$847.69', 'Status Order':"New Order", 'Action':"fa-ellipsis-h"},
         {'NO':'2','ID': '#12490','Date':'Nov 15, 2021', 'Customer Name':'Thomas Bleir','Location':'Lathrop Ave, Harvey', 'Amount':'$477,14', 'Status Order':'New Order', 'Action':"fa-ellipsis-h"},
         {'NO':'3','ID': '#12306','Date':'Nov 02, 2021', 'Customer Name':'Bill Norton','Location':'5685 Bruce Ave, Portage', 'Amount':'$477,14', 'Status Order':'New Order', 'Action':" fa-ellipsis-h"}]

    
    table_head = [ {'Name':'NO',"Arrow":'none;'},
                   {'Name': 'ID',"Arrow":'flex'},
                   {'Name':'Date',"Arrow":'none;'},
                   {'Name':'Customer Name',"Arrow":'flex'},
                   {'Name':'Location',"Arrow":'none;'},
                   {'Name': 'Amount',"Arrow":'flex'},
                   {'Name': 'Status Order',"Arrow":'flex'},
                   {'Name': 'Action',"Arrow":'none;'}]

    card_box = [{"text_main":"89,935","text_body":"Total users","icon": "fa-users", "arrow":"fa-arrow-up", "arrow-text":10.2, "text_bottom_text_1": "+", "text_bottom_int":1.01, "text_bottom_text_2": "% this week", "divider":"flex"},
               {"text_main":"23,283.5","text_body":"Total products","icon": "fa-briefcase", "arrow":"fa-arrow-up", "arrow-text":3.1, "text_bottom_text_1": "+", "text_bottom_int":2.56, "text_bottom_text_2": "% this week","divider":"flex"},
               {"text_main":"46,827","text_body":"Total users","icon": "fa-check-square-o", "arrow":"fa-arrow-up", "arrow-text":2.56, "text_bottom_text_1": "-", "text_bottom_int":0.91, "text_bottom_text_2": "% this week","divider":"flex"},
               {"text_main":"124,854","text_body":"Refunded","icon": "fa fa-share-square-o", "arrow":"fa-arrow-up", "arrow-text":7.2, "text_bottom_text_1": "+", "text_bottom_int":1.51, "text_bottom_text_2": "% this week","divider":"none"}]
    left_top_menu = [
        {"name" : "Overview", "arrow" : "fa-chevron-down", 'icon':'fa-bar-chart-o'},
        {"name" : "Product", "arrow" : "fa-chevron-down", 'icon':' fa-briefcase'},
        {"name" : "Orders", "arrow" : "fa-chevron-down", 'icon':'fa-user'},
        {"name" : "Checkout", "arrow" : "fa-chevron-down", 'icon':'fa-list'},
        {"name" : "Settings", "arrow" : "fa-chevron-down", 'icon':'fa-gear'}]

    left_bottom_menu = [
        {"name" : "Help Center", "icon" : "fa fa-question-circle-o", },
        {"name" : "Contact us", "icon" : "fa fa-commenting-o"},
        {"name" : "Log Out", "icon" : "fa fa-repeat",'color':"red"}]

    return render_template('index.html'
    ,left_top_menu = left_top_menu 
    ,left_bottom_menu = left_bottom_menu
    ,table_row = table_row
    ,table_head = table_head
    ,card_box = card_box
    )

app.run(debug= True)